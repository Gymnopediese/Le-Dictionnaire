from imports.services import *
from models.terme.terme import *

class Dictionnaire(Model):

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String())
    visibility = db.Column(db.String(10), nullable=False)
    suggestions = db.Column(db.Boolean, nullable=False, default=True)

    def get_allowed(self, current_user_id):
        for ownership in self.ownerships:
            if ownership.user_id != current_user_id:
                continue
            if ownership.rights == "none":
                break
            return
        raise Exception(405, "User cannot access this dictionnary")

    def put_allowed(self, current_user_id):
        for owner in self.ownerships:
            print(owner.id, current_user_id)
            if owner.id == current_user_id:
                return
        raise Exception(405, "User not allowed")

    def delete_allowed(self, current_user_id):
        return self.put_allowed(current_user_id)
    # ownerships
    # termes
    
    
