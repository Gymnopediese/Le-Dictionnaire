from imports.extern import *

class MeDictionnaireResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    
class MeOwnershipResponse(Schema):
    _final = "dictionnaire"
    dictionnaire = fields.Nested("MeDictionnaireResponse")
    rights = fields.String()

class MeDictionnairesResponse(Schema):
    dictionnaires = fields.List(fields.Nested("MeOwnershipResponse"))