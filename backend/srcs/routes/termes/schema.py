
from marshmallow import Schema, fields
import enum
from flask_smorest.fields import Upload

    

    


class UpdatePublicationImage(Schema):
    image = Upload()
    
class UpdatePublication(Schema):
    title = fields.Str()
    description = fields.Str()



    
class PublicationResponse(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    url = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    
    user = fields.Nested("UserSchema")
    likes = fields.Int()
    comments = fields.Int()

class UserListResponse(Schema):
    publications = fields.List(fields.Nested(PublicationResponse))
    

class TypeEnum(enum.Enum):
    nom_commun = "nom_commun"
    nom_propre = "nom_propre"
    groupe_de_mot = "groupe_de_mot"
    adjectif = "adjectif"
    verbe = "verbe"
    adverbe = "adverbe"
    maxime = "maxime"
    poesie = "poesie"
    nouvelle = "nouvelle"
    roman = "roman"
    discution = "discution"
    
    
    
class GenreEnum(enum.Enum):
    masculin = "masculin"
    feminin = "feminin"
    invariable = "invariable"
    

# class PublicationListQuery(Schema):
    
#     order_by = fields.Enum(PublicationOrderByEnum)
#     order = fields.Enum(PublicationOrderEnum)
#     start = fields.Int()
#     limit = fields.Int()

class ContenuTypeEnum(enum.Enum):
    definitions = "definitions"
    exemples = "exemples"
    note = "note"
    origine = "origine"

class CreateContenu(Schema):
    contenu = fields.Str(required=True)
    type = fields.Str(required=True)

class CreateTerme(Schema):
    name = fields.Str(required=True)
    genre = fields.Enum(GenreEnum)
    type = fields.Enum(TypeEnum)
    contenus = fields.List(fields.Nested("CreateContenu"),required=True)
    
class ResponseTermes(Schema):
    name = fields.Str(required=True)
    type = fields.Enum(TypeEnum,required=True)
    genre = fields.Enum(GenreEnum,required=True)
    contenus = fields.List(fields.Str(),required=True)