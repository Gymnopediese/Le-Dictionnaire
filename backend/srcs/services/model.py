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
    def update_all(cls):
        for subclass in cls.__subclasses__():
            subclass.update()

    @classmethod
    def update(cls):
        pass

    def put(self, args):
        for key, value in args.items():
            if hasattr(self, key):
                setattr(self, key, value)
                print(key, value)
        db.session.commit()

    @classmethod
    def exists(cls, **kwargs):
        return bool(cls.query.filter_by(**kwargs).first())
    
    
    @classmethod
    def get(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()
    
    
    @classmethod
    def get_all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()
    
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
        
        if "_final" in schema.__dict__.keys():
            rt = res
            res = res[schema.__dict__["_final"]]
            for key, pair in rt.items():
                if key != schema.__dict__["_final"]:
                    res[key] = pair
        return res

    @classmethod
    def new(cls, **kwargs):
        object = cls(**kwargs)
        db.session.add(object)
        db.session.commit()
        return object
    
    @classmethod
    def get_or_create(cls, **kwargs):
        object = cls.get(**kwargs)
        return object if object else cls.new(**kwargs)
    