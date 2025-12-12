from imports.extern import *

class DictionnaireTermeResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    type = fields.String()
    language = fields.String()
    context = fields.String()
    ctime = fields.String()

class DictionnairePasserelTermeResponse(Schema):
    _final = "terme"
    terme = fields.Nested("DictionnaireTermeResponse")