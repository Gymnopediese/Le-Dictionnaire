from imports.services import *

class Relationship(Model):
    
    user = db.relationship('User', backref=db.backref('followings', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    target = db.relationship('User', backref=db.backref('followers', cascade='all, delete-orphan'))
    target_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    