import type Terme from "../classes/terme.ts";

var terme           : Terme;
var current_input   : any;
var input           : any;
var input_type      : any;
var args            : any;


function getKey(e: KeyboardEvent) {
    return (e.shiftKey ? "Shift+" : "") + (e.metaKey ? "Meta+" : "") + e.key;
}

const handlers: Record<string, (e: KeyboardEvent) => void> = {

    "Meta+e" : e => {
        stop(e);
        terme.toggle_button()
    },

    "Meta+d" : e => {
        stop(e);
        args.show_dict_popup()
    },

    "Meta+s" : e => {
        stop(e);
        terme.put()
    },

    "Tab": e => {
        stop(e);
        terme.focus(current_input, 1);
    },

    "Shift+Enter": e => {
        stop(e);
        let p = terme.get_paragraphe_x(input);
        if (p !== -1) return terme.change_paragraph_amount(p, 1);
        let c = terme.get_content_x(input);
        if (c !== -1) return terme.change_paragraph_amount(c, 1);
    },

    "Shift+Backspace": e => {
        stop(e);
        let p = terme.get_paragraphe_x(input);
        if (p !== -1) terme.change_paragraph_amount(p, -1);
    },

    "Backspace": e => {
        let p = terme.get_paragraphe_x(input);
        let c = terme.get_content_x(input);
        if ((p !== -1 || c !== -1) &&
            terme.inputs_value[current_input].name_value === "" &&
            terme.inputs_value[current_input].content_value === "") {
            stop(e);
            terme.change_paragraph_amount(p, -1);
        }
        else if (input.selectionStart == 0 && input.selectionEnd == 0) {
            stop(e);
            terme.focus(current_input, -1);
        }
    },

    "Enter": e => {
        if (input_type !== "textarea") {
            stop(e);
            terme.focus(current_input, 1);
        }
    },

    "ArrowDown": e => {
        if (input_type !== "textarea") {
            stop(e);
            terme.focus(current_input, 1);
            return;
        }
        if (input.selectionStart > input.value.lastIndexOf("\n")) {
            stop(e);
            terme.focus(current_input, 1);
        }
    },

    "ArrowUp": e => {
        if (input_type !== "textarea") {
            stop(e);
            terme.focus(current_input, -1);
            return;
        }
        const idx = input.value.indexOf("\n");
        if (input.selectionStart <= idx || idx === -1) {
            stop(e);
            terme.focus(current_input, -1);
        }
    }
};

function stop(e: KeyboardEvent) {
    e.preventDefault();
    e.stopPropagation();
}

export function edit_view_event_manage(e: KeyboardEvent, t: Terme, a: any) {
    terme = t;
    input = document.activeElement;
    input_type = input.tagName.toLowerCase();
    current_input = terme.inputs.indexOf(input);
    args = a;

    const key = getKey(e);
    const h = handlers[key];
    if (h) h(e);
}