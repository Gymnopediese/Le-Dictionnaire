from services.db import db
import inspect
import sqlalchemy
import secrets
from imports import responses
def generate_id():
    # Generates a 16-character random hexadecimal string
    return secrets.token_hex(8).upper()  # 8 bytes = 16 hex chars


class Model(db.Model):
    __abstract__ = True  # n'est pas une table

    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(16), default=generate_id, unique=True)
    ctime = db.Column(db.DateTime, server_default=db.func.now(), default=db.func.now())
    utime = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now(), default=db.func.now())

    @classmethod
    def update_all_secrets(cls):
        total = 0
        for subclass in cls.__subclasses__():
            subclass.update()
        print(f"{total} secrets mis à jour dans toutes les tables.")

    @classmethod
    def update(cls):
        print(cls)
        authors = cls.query.filter_by(secret=None).all()

        for author in authors:
            author.secret = generate_id()
        db.session.commit()

    def put(self, args):
        for key, value in args.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    @classmethod
    def exists(cls, **kwargs):
        return bool(cls.query.filter_by(**kwargs).first())

    def choose(self, i, depth):
        if "models" in str(type(i[1])) and depth > 0:
            return i[1].serialize(depth - 1)
        elif "models" in str(type(i[1])):
            return i[1].id
        elif type(i[1]) == sqlalchemy.orm.collections.InstrumentedList:
            res = []
            for el in i[1]:
                res.append(self.choose([0, el], depth - 1))
            return res
        return i[1]


    def get_allowed(self, current_user_id):
        raise Exception(500, f"'get_allowed' not implemented for object of type {str(type(self))}")
        
    def post_allowed(self, current_user_id):
        raise Exception(500, f"'post_allowed' not implemented for object of type {str(type(self))}")
        
    def put_allowed(self, current_user_id):
        raise Exception(500, f"'put_allowed' not implemented for object of type {str(type(self))}")
    
    def delete_allowed(self, current_user_id):
        raise Exception(500, f"'delete_allowed' not implemented for object of type {str(type(self))}")
    
        

    def serialize(self, schema):
        res = {}
        for name in schema._declared_fields.keys():
            if not hasattr(self, name):
                continue
            attr = getattr(self, name)
            print(type(attr))
            
            if type(attr) == sqlalchemy.orm.collections.InstrumentedList:
                list = attr
                attr = []
                nested_schema = schema._declared_fields[name].inner.nested
                nested_schema = responses.__dict__[nested_schema]
                for elem in list:
                    attr.append(elem.serialize(nested_schema))
            if "Nested" in str(schema._declared_fields[name]):
                nested_schema = responses.__dict__[schema._declared_fields[name].nested]
                attr = attr.serialize(nested_schema)
            res[name] = attr
            print("attr", name, attr)
        
        if "_final" in schema.__dict__.keys():
            print(schema._declared_fields.keys())
            print(hasattr(self, "dictionnaire"))
            print(res)
            print(type(self))
            rt = res
            res = res[schema.__dict__["_final"]]
            for key, pair in rt.items():
                if key != schema.__dict__["_final"]:
                    res[key] = pair
        return res

