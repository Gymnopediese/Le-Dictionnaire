from imports.services import *

class Ip(Model):
    ip = db.Column(db.String(100), nullable=False, unique=True)
    user = db.relationship('User', backref='ips')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)