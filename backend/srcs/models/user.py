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
    
    def check_password(self, password):
        return self.password == sha256(password.encode()).hexdigest()
    
    def generate_token(self):
        return create_access_token({"id": self.id, "username": self.username})
