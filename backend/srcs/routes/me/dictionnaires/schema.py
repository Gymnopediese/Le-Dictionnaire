from imports.extern import *

class MeDictionnairesGet(Schema):
    rights_less_than = fields.String()
    rights_higher_than = fields.String()
    rights_in = fields.List(fields.String())

    
    
    
    # contents = fields.List(fields.Str(required=True))