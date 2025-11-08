
from marshmallow import Schema, fields
import enum


class UpdateUser(Schema):
    password = fields.Str()
    
class UserResponse(Schema):
    id = fields.Int()
    username = fields.Str()

class UsersResponse(Schema):
    users = fields.List(fields.Nested(UserResponse))
    
class UserOrderByEnum(enum.Enum):
    username = "username"
    email = "email"

class OrderEnum(enum.Enum):
    asc = "asc"
    desc = "desc"

class UserListQuery(Schema):
    order_by = fields.Enum(UserOrderByEnum)
    order = fields.Enum(OrderEnum)
    start = fields.Int()
    limit = fields.Int()
