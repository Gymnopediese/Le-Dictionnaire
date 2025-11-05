from imports.main import *

from hashlib import sha256

class IP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100), nullable=False, unique=True)
    user = db.relationship('User', backref='likes')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.ip,
            "email": self.user,
        }