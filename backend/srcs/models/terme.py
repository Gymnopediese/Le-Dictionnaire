from imports.main import *

from hashlib import sha256

class Terme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    genre = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    

    
    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "genre": self.genre,
            "type": self.type,
            "definitions": [cont.serialize() for cont in self.contenus if cont.type == "definitions"],
            "exemples": [cont.serialize() for cont in self.contenus if cont.type == "exemples"],
            "origines": [cont.serialize() for cont in self.contenus if cont.type == "origines"],
            "notes": [cont.serialize() for cont in self.contenus if cont.type == "notes"]
        }

    @staticmethod
    def exists(username=None, password=None):
        if username:
            return User.query.filter_by(username=username).first() != None
        else:
            return User.query.filter_by(password=password).first() != None
    
    def check_password(self, password):
        return self.password == sha256(password.encode()).hexdigest()
    
    def generate_token(self):
        return create_access_token({"id": self.id, "username": self.username})
