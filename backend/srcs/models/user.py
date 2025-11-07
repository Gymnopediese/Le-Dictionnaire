from imports.main import *

from hashlib import sha256

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }
    
    @staticmethod
    def exists(username=None, password=None):
        if username:
            return User.query.filter_by(username=username).first() != None
        else:
            return User.query.filter_by(password=password).first() != None
    
    @staticmethod
    def hash(password):
        return sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.password == sha256(password.encode()).hexdigest()
    
    def generate_token(self):
        return create_access_token({"id": self.id, "username": self.username})
