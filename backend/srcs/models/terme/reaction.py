from imports.services import *

class Reaction(Model):
    
    note = db.Column(db.String())
    type = db.Column(db.String())

    terme = db.relationship('Terme', backref=db.backref('reactions', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('reactions', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    