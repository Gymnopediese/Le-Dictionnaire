import Terme from "$lib/classes/terme";
import { writable, type Writable } from "svelte/store";

export var user = writable({});
export var popup = writable("");
export var metadatas = writable({});

export var terme : Writable<Terme> = writable(new Terme(undefined))

export var scroll_div : Writable<HTMLDivElement|null> = writable(null);

export var view_mode = writable("edit");

export var writing_mode = writable(false);

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
