from marshmallow import Schema, fields

class LoginUser(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    
class LoginResponse(Schema):
    token = fields.Str()

    