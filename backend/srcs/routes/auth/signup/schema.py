from marshmallow import Schema, fields

class CreateUser(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
