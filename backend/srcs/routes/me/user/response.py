from imports.extern import *

class MeUserResponse(Schema):
    id = fields.Integer()
    username = fields.String()
    

    
class MeRelationshipResponse(Schema):
    _final = "target"
    target = fields.Nested("MeUserResponse")
    type = fields.String()
    
        
class MeRelationshipReverseResponse(Schema):
    _final = "user"
    user = fields.Nested("MeUserResponse")
    type = fields.String()