from imports.services import *

class Suggestion(Model):
    
    name = db.Column(db.String())
    
    note = db.Column(db.String())

    type = db.Column(db.String())
    
    state = db.Column(db.String())
    
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    target_id = db.Column(db.Integer,  db.ForeignKey('terme.id'), nullable=False)
    
    target = db.relationship('Terme',  foreign_keys=[target_id], backref=db.backref('termes_suggestion', cascade='all, delete-orphan'))
    terme = db.relationship('Terme', foreign_keys=[terme_id], backref=db.backref('suggestions', cascade='all, delete-orphan'))
    
    user = db.relationship('User', backref=db.backref('authors', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    