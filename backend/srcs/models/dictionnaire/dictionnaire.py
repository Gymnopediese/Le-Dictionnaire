from imports.services import *

class Dictionnaire(Model):
    
    name = db.Column(db.String(100), nullable=False, unique=True)
    visibility = db.Column(db.String(10), nullable=False)
    suggestions = db.Column(db.Boolean, nullable=False, default=True)
    
    # ownerships
    # termes
    
    
