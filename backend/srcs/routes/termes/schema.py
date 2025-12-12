from imports.enums import *

class ParagraphCreate(Schema):
    name = fields.Str(required=True)
    contents = fields.List(fields.Str(required=True))

class TermeCreate(Schema):
    name = fields.Str(required=True)
    paragraphs = fields.List(fields.Nested("ParagraphCreate"),required=True)
    metadatas = fields.Raw()
    
    