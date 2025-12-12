

from imports.extern import *

class DictionnaireResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
