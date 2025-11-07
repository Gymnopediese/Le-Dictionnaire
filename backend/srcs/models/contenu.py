from imports.main import *

from hashlib import sha256

class Contenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    order = db.Column(db.Integer())
    contenu = db.Column(db.String())
    type = db.Column(db.String(), default="definitions")

    # user = db.relationship('User',  backref=db.backref('publications', cascade='all, delete-orphan'))
    terme = db.relationship('Terme', backref=db.backref('contenus', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "order": self.order,
            "contenu": self.contenu,
            "type": self.type,
        }