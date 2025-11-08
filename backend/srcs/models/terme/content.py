from imports.services import *

class Content(Model):
    id = db.Column(db.Integer, primary_key=True)

    order = db.Column(db.Integer())
    contenu = db.Column(db.String())
    type = db.Column(db.String(), default="definitions")

    terme = db.relationship('Terme', backref=db.backref('contents', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)