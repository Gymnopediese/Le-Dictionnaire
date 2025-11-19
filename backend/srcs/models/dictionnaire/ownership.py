from imports.services import *

class Ownership(Model):

    rights = db.Column(db.String())

    dictionnaire = db.relationship('Dictionnaire', backref=db.backref('ownerships', cascade='all, delete-orphan'))
    dictionnaire_id = db.Column(db.Integer, db.ForeignKey('dictionnaire.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('dictionnaires', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def serialize(self, depth=-1):
        if depth == "full":
            res = self.dictionnaire.serialize()
            res["rights"] = self.rights
            return res
        return super().serialize(depth)

class OwnerShipRights(enum.Enum):
    all = "all"
    
    read_only = "read_only"
    none = "none"