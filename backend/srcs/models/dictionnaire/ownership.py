from imports.services import *
from imports.enums import *

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

    @staticmethod
    def get_rights(user_id, dictionnaire_id, number=False):
        owner = Ownership.query.filter_by(user_id=user_id, dictionnaire_id=dictionnaire_id).first()
        rights = "view" if not owner else owner.rights
        if number:
            return rights_level[rights]
        return rights
    
    
    @staticmethod
    def set_rights(user_id, dictionnaire_id, rights):
        owner = Ownership.query.filter_by(user_id=user_id, dictionnaire_id=dictionnaire_id).first()
        if not owner:
            if rights == "view":
                return
            owner = Ownership(user_id=user_id, dictionnaire_id=dictionnaire_id, rights=rights)
            db.session.add(owner)
        elif rights == "view":
            db.session.delete(owner)
        else:
            owner.rights = rights
        db.session.commit()