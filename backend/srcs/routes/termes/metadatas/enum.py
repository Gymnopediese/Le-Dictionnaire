from imports.services import *
from services.ts import load_ts_var
class MetadataTypes(enum.Enum):
    # le type du texte
    type="type"
    # le domaine dans lequelle sinscrit le text, litterature, philosophie, Science, Math etx...
    domaine="domaine"
    # le context du texte : familier, insulte, etc
    context="context"
    # le genre du text
    genre="genre"
    # date d'ecriture
    date="date"
    # la langue du texte
    language="language"
    # autres noms pour la meme chose
    aka="aka"
    # synonymes
    synonyme="synonyme"
    # same idea, not same meaning
    friens="friend"
    # les antonymes du mot
    anthonyme="anthonyme"
    
    

class MetadataDataTypes(enum.Enum):
    string="string"
    date="date"
    terme="terme"
    user="user"
    
allowed_metadata_types = load_ts_var("./shared/metadatas.ts")
