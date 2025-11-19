from imports.services import *

class User(Model):

    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    
    @staticmethod
    def hash(password):
        return sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.password == sha256(password.encode()).hexdigest()
    
    def generate_token(self):
        return create_access_token({"id": self.id, "username": self.username})
