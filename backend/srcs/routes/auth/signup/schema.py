from imports.extern import *
    
class CreateUser(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
