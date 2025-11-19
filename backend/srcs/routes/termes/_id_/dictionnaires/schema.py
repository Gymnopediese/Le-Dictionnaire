from imports.enums import *

class TermeDictionnaireCreate(Schema):
    dictionnaires = fields.List(fields.Int(),required=True)