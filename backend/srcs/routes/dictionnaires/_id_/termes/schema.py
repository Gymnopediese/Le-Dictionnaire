from imports.extern import *

class DictionnaireTermesGet(Schema):
    starts_with = fields.String()
    sort_by = fields.String()
    amount = fields.Integer()