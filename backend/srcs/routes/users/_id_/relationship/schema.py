from imports.enums import *

class RelationshipCreate(Schema):
    type = fields.Enum(RelationshipTypes)
    