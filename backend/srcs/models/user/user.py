from imports.services import *

class User(Model):

    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    visibility = db.Column(db.String(100), default="public")
    
    @staticmethod
    def hash(password):
        return sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.password == sha256(password.encode()).hexdigest()
    
    def generate_token(self):
        return create_access_token({"id": self.id, "username": self.username})

    def get_allowed(self, current_user_id):
        return 
    
    @classmethod
    def update(cls):
        objects = cls.query.filter_by(visibility=None).all()
        for object in objects:
            object.visibility = "public"
        db.session.commit()
    
    @classmethod
    def new(cls, **kwargs):
        kwargs["password"] = User.hash(kwargs["password"])
        return super().new(**kwargs)
    
    @classmethod
    def get_or_create(cls, **kwargs):
        kwargs["password"] = User.hash(kwargs["password"])
        print(kwargs)
        return super().get_or_create(**kwargs)
    