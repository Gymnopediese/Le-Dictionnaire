from imports.enums import *

class ParagraphCreate(Schema):
    name = fields.Str(required=True)
    contents = fields.List(fields.Str(required=True))

class TermeCreate(Schema):
    name = fields.Str(required=True)
    type = fields.Enum(TermeTypes)
    context = fields.Enum(TermeContext)
    language = fields.Str(required=True)
    paragraphs = fields.List(fields.Nested("ParagraphCreate"),required=True)
    
class TermeResponse(Schema):
    name = fields.Str(required=True)
    type = fields.Enum(TermeTypes,required=True)
    contents = fields.List(fields.Str(),required=True)
    language = fields.Str(required=True)
    