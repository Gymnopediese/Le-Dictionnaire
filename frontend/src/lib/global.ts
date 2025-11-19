import { writable } from "svelte/store";

export var user = writable({});

export var view_mode = writable("edit");

export function toggle_view_mode(){
    view_mode.update((val) => {
        if (val == "edit")
            return "read"
        else
            return "edit"
    })
}