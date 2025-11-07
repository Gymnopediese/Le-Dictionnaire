from imports.main import *

from hashlib import sha256

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user = db.relationship('User',  backref=db.backref('publications', cascade='all, delete-orphan'))
    terme = db.relationship('Terme', backref=db.backref('authors', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('authors', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }