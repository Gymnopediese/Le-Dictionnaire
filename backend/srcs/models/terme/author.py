from imports.services import *

class Author(Model):
    terme = db.relationship('Terme', backref=db.backref('authors', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('termes', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)