from imports.services import *
from models.dictionnaire.dictionnaire_termes import *
from models.dictionnaire.dictionnaire import *

class Terme(Model):
    
    name = db.Column(db.String(100), nullable=False)
    # genre = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100))
    context = db.Column(db.String(100))
    content = db.Column(db.Text())



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
    

    def serialize(self, schema: Schema):
        res = super().serialize(schema)
        if "paragraphs" in schema._declared_fields:
            res["paragraphs"] = self.split_paragraphs()
        if "description" in schema._declared_fields:
            res["description"] = self.split_paragraphs()[0]["contents"][0]
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