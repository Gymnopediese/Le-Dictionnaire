from imports.extern import *

class MeGetTermesTermeResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    type = fields.String()
    context = fields.String()
    language = fields.String()
    
    
class MeGetTermesAuthorResponse(Schema):
    _final = "terme"
    terme = fields.Nested("MeGetTermesTermeResponse")

class MeGetTermesResponse(Schema):
    termes = fields.List(fields.Nested("MeGetTermesAuthorResponse"))
    
    
    # contents = fields.List(fields.Str(required=True))