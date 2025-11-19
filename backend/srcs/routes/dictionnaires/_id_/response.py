from imports.extern import *



class DictionnaireTermeResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    type = fields.String()
    language = fields.String()
    context = fields.String()
    genre = fields.String()

class DictionnairePasserelTermeResponse(Schema):
    _final = "terme"
    terme = fields.Nested("DictionnaireTermeResponse")

class DictionnaireResponse(Schema):
    name = fields.String()
    description = fields.String()
    termes = fields.List(fields.Nested("DictionnairePasserelTermeResponse"))
    
class DictionnaireFinalResponse(Schema):
    name = fields.String()
    description = fields.String()
    termes = fields.List(fields.Nested("DictionnaireTermeResponse"))
    
    
    # contents = fields.List(fields.Str(required=True))