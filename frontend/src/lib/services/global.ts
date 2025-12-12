import Terme from "$lib/classes/terme";
import { writable, type Writable } from "svelte/store";

export var user = writable({});
export var popup = writable("");
export var metadatas = writable({});

export var terme : Writable<Terme> = writable(new Terme(undefined))

export var focus_input_function = writable(null);

export var view_mode = writable("edit");


export function toggle_view_mode(){
    view_mode.update((val) => {
        if (val == "edit")
            return "read"
        else
            return "edit"
    })
}

export function get_writable(writable: Writable<any>) {

    var r;
    writable.update((val)=>
    {
        r = val;
        return val;
    }
    )
    return r;
}

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
        
    ]
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
    "allowed": ["dictionnaire"]
  },
  "users": {
    "name": "dictionnaires",
    "type": "list",
    "allowed": ["user"]
  },

}
