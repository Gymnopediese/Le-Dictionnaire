from imports.extern import *
    
class PasswordForgoten(Schema):
    email = fields.Str(required=True)

class ChangePassword(Schema):
    password = fields.Str(required=True)
