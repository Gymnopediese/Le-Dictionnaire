from imports.services import *
from models.terme.terme import *

class Dictionnaire(Model):

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String())
    visibility = db.Column(db.String(10), nullable=False, default="public")
    suggestions = db.Column(db.Boolean, nullable=False, default=True)

    def get_allowed(self, current_user_id):
        for ownership in self.ownerships:
            if ownership.user_id == current_user_id:
                return ownership.rights
            if ownership.rights == "blocked":
                raise Exception(405, "User cannot access this dictionnary")
        if self.visibility == "public":
            return "view"
        raise Exception(405, "User cannot access this dictionnary")

    def put_allowed(self, current_user_id):
        for owner in self.ownerships:
            if owner.id == current_user_id:
                return
        raise Exception(405, "User not allowed")

    def delete_allowed(self, current_user_id):
        return self.put_allowed(current_user_id)
    # ownerships
    # termes
    
    
