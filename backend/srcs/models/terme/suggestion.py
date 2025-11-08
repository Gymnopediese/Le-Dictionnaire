from imports.services import *

class Suggestion(Model):
    
    name = db.Column(db.String())
    
    note = db.Column(db.String())

    type = db.Column(db.String())
    
    state = db.Column(db.String())
    
    terme = db.relationship('Terme', backref=db.backref('suggestions', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    target = db.relationship('Terme', backref=db.backref('termes_suggestion', cascade='all, delete-orphan'))
    target_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('authors', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    