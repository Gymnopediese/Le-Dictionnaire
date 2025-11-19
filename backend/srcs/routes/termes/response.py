from imports.extern import *
from imports.enums import *


class TermeParagraphResponse(Schema):
    name = fields.Str(required=True)
    contents = fields.List(fields.Str(required=True))

class TermeDictionnaireTrueResponse(Schema):
    id = fields.Integer()
    name = fields.Str()
    
class TermeDictionnaireResponse(Schema):
    _final = "dictionnaire"
    dictionnaire = fields.Nested("TermeDictionnaireTrueResponse")

class TermeResponse(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    genre = fields.Enum(TermeGenre)
    language = fields.Str()
    type = fields.Enum(TermeTypes)
    context = fields.Enum(TermeContext)
    paragraphs = fields.List(fields.Nested("TermeParagraphResponse"),required=True)
    dictionnaires = fields.List(fields.Nested("TermeDictionnaireResponse"),required=True)