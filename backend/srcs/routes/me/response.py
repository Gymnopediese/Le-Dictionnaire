from imports.extern import *

class MeDictionnaireResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    
    
class MeOwnershipResponse(Schema):
    _final = "dictionnaire"
    dictionnaire = fields.Nested("MeDictionnaireResponse")
    rights = fields.String()

class MeTermeResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()

class MeAuthorResponse(Schema):
    _final = "terme"
    terme  = fields.Nested("MeDictionnaireResponse")

class MeResponse(Schema):
    username = fields.String()
    dictionnaires = fields.List(fields.Nested("MeOwnershipResponse"))
    termes = fields.List(fields.Nested("MeAuthorResponse"))
    
    # contents = fields.List(fields.Str(required=True))