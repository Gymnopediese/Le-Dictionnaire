from imports.services import *

class Link(Model):
    
    name = db.Column(db.String())
    note = db.Column(db.String())
    type = db.Column(db.String())
    
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)


    terme = db.relationship('Terme', foreign_keys=[terme_id], backref=db.backref('links_out', cascade='all, delete-orphan'))
    target = db.relationship('Terme', foreign_keys=[target_id], backref=db.backref('links_in', cascade='all, delete-orphan'))
    
    user = db.relationship('User', backref=db.backref('links_made', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    