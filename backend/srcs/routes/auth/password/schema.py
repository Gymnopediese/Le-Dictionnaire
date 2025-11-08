from marshmallow import Schema, fields

    
class PasswordForgoten(Schema):
    email = fields.Str(required=True)

class ChangePassword(Schema):
    password = fields.Str(required=True)
