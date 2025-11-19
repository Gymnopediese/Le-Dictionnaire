from imports.services import *

class Relationship(Model):
    

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('followings', cascade='all, delete-orphan'))
    target = db.relationship('User', foreign_keys=[target_id], backref=db.backref('followers', cascade='all, delete-orphan'))
    