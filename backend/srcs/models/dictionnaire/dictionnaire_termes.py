from imports.services import *

class DictionnaireTerme(Model):

    dictionnaire = db.relationship('Dictionnaire', backref=db.backref('termes', cascade='all, delete-orphan'))
    dictionnaire_id = db.Column(db.Integer, db.ForeignKey('dictionnaire.id'), nullable=False)
    
    terme = db.relationship('Terme', backref=db.backref('dictionnaires', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)