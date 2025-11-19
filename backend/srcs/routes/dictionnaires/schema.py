from imports.extern import *

class DictionnaireVisibilityEnum(enum.Enum):
    public = "public"
    link = "link"
    private = "private"

class DictionnaireCreate(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    visibility = fields.Enum(DictionnaireVisibilityEnum, required=True)
    suggestions = fields.Boolean(required=True)

class DictionnaireResponse(Schema):
    name = fields.Str(required=True)
    # visibility = fields.Enum(DictionnaireVisibility, required=True)
    suggestions = fields.Boolean(required=True)
    termes = fields.List(fields.List(fields.Nested("TermeResponse")), required=True)
    owners = []
    
