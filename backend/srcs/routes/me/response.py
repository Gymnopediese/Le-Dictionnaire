from imports.extern import *

class MeDictionnaireResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    
    
class MeOwnershipResponse(Schema):
    _final = "dictionnaire"
    dictionnaire = fields.Nested("MeDictionnaireResponse")
    rights = fields.String()

class MeResponse(Schema):
    username = fields.String()
    dictionnaires = fields.List(fields.Nested("MeOwnershipResponse"))
    
    
    # contents = fields.List(fields.Str(required=True))