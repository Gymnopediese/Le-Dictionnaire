from imports.extern import *

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
    

allowed_metadata_types = {
  "type": {
    "name": "type",
    "type": "string",
    "allowed": ["string"]
  },
  "domaine": {
    "name": "domaine",
    "type": "string",
    "allowed": ["string"]
  },
  "context": {
    "name": "context",
    "type": "string",
    "allowed": ["string"]
  },
  "genre": {
    "name": "genre",
    "type": "string",
    "allowed": ["string"]
  },
  "date": {
    "name": "date",
    "type": "date",
    "allowed": ["date"]
  },
  "language": {
    "name": "language",
    "type": "string",
    "allowed": ["string"]
  },
  "aka": {
    "name": "aka",
    "type": "list",
    "allowed": ["string", "terme"]
  },
  "synonyme": {
    "name": "synonyme",
    "type": "list",
    "allowed": ["string", "terme"]
  },
  "friend": {
    "name": "friend",
    "type": "list",
    "allowed": ["string", "terme"]
  },
  "anthonyme": {
    "name": "anthonyme",
    "type": "list",
    "allowed": ["string", "terme"]
  }
}
