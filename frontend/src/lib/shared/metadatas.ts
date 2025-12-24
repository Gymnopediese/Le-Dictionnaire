
export let allowed_metadata_types = {
  "type": {
    "name": "type",
    "type": "string",
    "allowed": ["string"],
    "options": [
        "nom commun",
        "nom propre",
        "adverbe",
        "adjectif",
        "pronom",
        "verbe",
        "livre",
        "roman",
        "poesie"
    ],
    "required": true,
    "default": ""
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
    "allowed": ["string"],
    "options": [
        "feminin",
        "masculin",
        "invariable"
    ]
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
  },
  "dictionnaires": {
    "name": "dictionnaires",
    "type": "list",
    "allowed": ["dictionnaire"],
    "required": true,
    "default": []
  },
  "authors": {
    "name": "authors",
    "type": "list",
    "allowed": ["user"],
    "required": true,
    "default": []
  },
  "visibility": {
    "name": "visibility",
    "type": "string",
    "allowed": ["string"],
    "options": [
        "public",
        "dictionnaire_only",
        "private"
    ],
    "required": true,
    "default": "public"
  }
}
