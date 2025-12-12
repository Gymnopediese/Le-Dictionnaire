from imports.extern import *

class UserResponse(Schema):
    id = fields.Int()
    username = fields.Str()
    relationship = fields.Str()