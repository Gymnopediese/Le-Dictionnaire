from imports.services import *

class Terme(Model):
    
    name = db.Column(db.String(100), nullable=False, unique=True)
    genre = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    context = db.Column(db.String(100), nullable=False)
    # contenus
    # reactions
    # links_in
    # links_outs
    # dictionnaires
    # suggestions
    
    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "genre": self.genre,
            "type": self.type,
            "language": self.language,
            "context": self.context,
            "definitions": [cont.serialize() for cont in self.contenus if cont.type == "definitions"],
            "exemples": [cont.serialize() for cont in self.contenus if cont.type == "exemples"],
            "origines": [cont.serialize() for cont in self.contenus if cont.type == "origines"],
            "notes": [cont.serialize() for cont in self.contenus if cont.type == "notes"]
        }