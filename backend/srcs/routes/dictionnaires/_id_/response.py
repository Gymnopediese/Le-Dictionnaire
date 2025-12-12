from imports.extern import *


class DictionnaireResponse(Schema):
    id = fields.Int()
    name = fields.String()
    description = fields.String()
    rights= fields.String()
    # termes = fields.List(fields.Nested("DictionnairePasserelTermeResponse"))
    
class DictionnaireFinalResponse(Schema):
    name = fields.String()
    description = fields.String()
    # termes = fields.List(fields.Nested("DictionnaireTermeResponse"))
    
    
    # contents = fields.List(fields.Str(required=True))