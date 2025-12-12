from imports.services import *
from models.dictionnaire.dictionnaire_termes import *
from models.dictionnaire.dictionnaire import *
from imports.enums import *
from models.user.user import User
from imports.responses import *
from copy import deepcopy

class Terme(Model):
    
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text())
    metadatas = db.Column(JSONB)
    visibility = db.Column(db.String(100), default="public")


    @classmethod
    def update(cls):
        objects = cls.query.filter_by(visibility=None).all()
        for object in objects:
            object.visibility = "public"
        db.session.commit()

    # contenus
    # reactions
    # links_in
    # links_outs
    # dictionnaires
    # suggestions
    def put_allowed(self, current_user_id):
        return
        # if "dictionnaires" in args:
        #     for id in args["dictionnaires"]:
        #         dictionnaire = Dictionnaire.query.get(id)
        #         if not dictionnaire:
        #             raise Exception(404, "invalide ressource")
        #         dictionnaire.put_allowed(current_user_id)
        return super().put_allowed(current_user_id)



    @staticmethod
    def join_paragraphs(paragraphs):
        content = ""
        for paragraph in paragraphs:
            content += f"{paragraph['name']}$@@@$"
            for c in paragraph['contents']:
                content += f"{c}$@$"
            content += "$@$"
            
        return content

    def split_paragraphs(self):

        paragraphs = []

        if self.content == None or "$@$$@$" not in self.content:
            self.content = "Description$@@@$comment ?$@$$@$"

        for paragraphe in self.content.split("$@$$@$"):
            if paragraphe == "":
                continue
            name, cts = paragraphe.split("$@@@$")
            contents = []
            for content in cts.split("$@$"):
                if content == "":
                    continue
                contents.append(content)
            paragraphs.append(
                {
                    "name": name,
                    "contents": contents
                }
            )
        return paragraphs
    

    def serialize(self, schema: Schema, user_id=""):
        res = super().serialize(schema)
        if "paragraphs" in schema._declared_fields:
            res["paragraphs"] = self.split_paragraphs()
            
        
        if "description" in schema._declared_fields:
            res["description"] = self.split_paragraphs()[0]["contents"][0]
        # traceback.print_stack()
        if "metadatas" in schema._declared_fields and user_id:
            res["metadatas"] = self.serialize_metadatas(user_id)
            if "metadata_types" in schema._declared_fields:
                metadatas = res["metadatas"]
                for key, val in allowed_metadata_types.items():
                    if key in metadatas:
                        metadatas[key]["name"] = val["name"]
                        metadatas[key]["allowed"] = val["allowed"]
                        metadatas[key]["type"] = val["type"]
                        metadatas[key]["used"] = True
                        continue
                    metadatas[key] = deepcopy(val)
                    metadatas[key]["used"] = False
                res["metadatas"] = metadatas
        
        return res

    
    # Allow to view the word if : it is in a public dictionnary, is in a dictionnary owned by the user or was made by the user.
    def get_allowed(self, current_user_id):
        for dictionnaire in self.dictionnaires:
            if dictionnaire.dictionnaire.visibility == "public":
                return
            for owner in self.ownerships:
                if owner.user_id == current_user_id:
                    return
        for author in self.authors:
            if author.user_id == current_user_id:
                return
        raise Exception(405, "not allowed to access ressource")

    def delete_allowed(self, current_user_id):
        for author in self.authors:
            if author.user_id == current_user_id:
                return
        raise Exception(405, "not allowed to delete ressource links")
    
    def delete_metadata(self, metatype, value):

        if value["type"] != "list":
            self.metadatas.pop(metatype)
            db.session.commit()
            return
        
        for i, val in enumerate(value["data"]):
            if val["type"] == value["type"] and  val["data"] == value["data"]:
                self.metadatas[metatype].pop(i)
                return
                
        
    
    def serialize_metadata(self, metatype, value, user_id, terme_serialize=DictionnaireTermeResponse, user_serialize=UserResponse):

        data_type = value["type"]
        data = value["data"]

        if data_type == "terme":
            data=int(data)
            link = Terme.query.get(data)
            try:
                link.get_allowed(user_id)
            except:
                self.delete_metadata(metatype, value)
            value["data"] = link.serialize(terme_serialize)  
        elif data_type == "user":
            data=int(data)
            link = User.query.get(data)
            try:
                link.get_allowed(user_id)
            except:
                self.delete_metadata(metatype, value)
            value["data"] =  link.serialize(user_serialize)
        return value
    
    
    def serialize_metadatas(self, user_id, terme_serialize=DictionnaireTermeResponse, user_serialize=UserResponse):
        if self.metadatas is None:
            return {
                
            }
        res = {}
        for metatype, value in self.metadatas.items():
            if value["type"] != "list":
                res[metatype] = self.serialize_metadata(metatype, value, user_id, terme_serialize, user_serialize)
                continue
            res[metatype] = deepcopy(value)
            res[metatype]["data"] = []
            for val in value["data"]:
                res[metatype]["data"].append(self.serialize_metadata(metatype, val, user_id, terme_serialize, user_serialize))
                
        return res

    @staticmethod
    def metadata_allowed(metatype, value, user_id):
        
        data_type = value["type"]
        data = value["data"]
        if data_type not in allowed_metadata_types[metatype]["allowed"]:
            raise Exception(422, "Unprocessable antity")
        if data_type == "terme":
            data=int(data)
            link = Terme.query.get(data)
            if not link:
                raise Exception(404, "Not a valid terme")
            link.get_allowed(user_id)
    
        if data_type == "user":
            data=int(data)
            link = User.query.get(data)
            if not link:
                raise Exception(404, "Not a valid terme")
            link.get_allowed(user_id)

    @staticmethod
    def metadatas_allowed(metadatas, user_id):
        
        for metatype, value in metadatas.items():
            
            if len(value) != 2:
                raise Exception(422, f"Invalid metadata keys for {metatype}")
            
            if "type" not in value or "data" not in value:
                raise Exception(422, f"Missing type or data key in metadata {metatype}")
            
            if value["type"] != allowed_metadata_types[metatype]["type"]:
                raise Exception(422, f"Not valid type for metadata {metatype}")
            
            if value["type"] != "list":
                Terme.metadata_allowed(metatype, value, user_id)
                continue
            
            for val in value["data"]:
                Terme.metadata_allowed(metatype, val, user_id)
                
            