import { del, post, put } from "$lib/services/api";
import { get_writable, toggle_view_mode, view_mode } from "$lib/services/global";
import { json } from "@sveltejs/kit";
import { writable, type Writable } from "svelte/store";

export class Paragraph
{
    name            : HTMLInputElement = null;
    name_value      : string = "";
    content         : HTMLInputElement = null;
    content_value   : string = "";

    constructor(name="", content="")
    {
        this.name_value = name;
        this.content_value = content
    }

    refresh_input()
    {
        var content = this.content;
        content.addEventListener('input', () => {

            content.value = content.value.trimLeft()
            if (content.value.trim() == "")
                content.value = ""
            while (content.value.length - content.value.trimRight().length > 2)
                content.value = content.value.substring(0, content.value.length - 1)
            
            content.style.height = 'auto';
            var count = (content.value.match(/\n/g)|| []).length + 1
            content.style.height = count * 40 + 'px';
            content.style.height = content.scrollHeight + 'px';
        });
        content.style.height = 'auto';
        content.style.height = content.scrollHeight + 'px';
        var count = (content.value.match(/\n/g)|| []).length + 1
        content.style.height = count * 40 + 'px';
        content.style.height = content.scrollHeight + 'px';
        // console.log(content.scrollHeight)
    }
}

export default class Terme
{
    terme;
    id                  : number = -1;
    name                : HTMLInputElement | null = null;
    name_value          : string = "";     
    inputs              : [HTMLInputElement];
    inputs_value        : [string];

    type                : HTMLInputElement | null = null;
    type_value          : string = "";     
    // genre               : HTMLInputElement | null = null;
    // genre_value         : string = "";     
    context             : HTMLInputElement | null = null;
    context_value       : string = "";     
    langue              : HTMLInputElement | null = null;
    langue_value        : string = "";     
    dictionnaire        : HTMLInputElement | null = null;
    dictionnaire_value  : string = "";     
    reactive            : Writable<boolean> = writable(false);


    paragraphs      : [Paragraph] = [];

    next_x          : number = -1;
    next_y          : number = -1;
    next_start      : number = 0;

    current_input   : number = 0;
    new             : boolean = false;
    remove          : boolean = false
    error           : Writable<string> = writable("");
    draft_id        : string = "";
    
    constructor(terme)
    {
        this.init(terme);
    }

    init(terme)
    {
        if (terme == undefined)
        {
            this.paragraphs.push(new Paragraph())
            this.set_inputs();
            this.new = true;
            return
        }
        this.terme = terme;
        console.log(terme)
        this.id = terme.id ?? -1;
        this.draft_id = terme.draft_id ?? "";
        this.name_value = terme.name;
        this.type_value = terme.type;
        this.context_value = terme.context;
        this.langue_value = terme.language;
        for (let paragraph of terme.paragraphs)
        {
            this.paragraphs.push(new Paragraph(paragraph.name, paragraph.contents[0]))
        }

        this.set_inputs();
    }
    payload()
    {

        for (let input of this.inputs)
        {
            if (input.value === "")
            {
                throw (`Cannot save empty fieds, ${input}`)
            }
        }
        console.log("saving")
        return { terme : {
            name: this.name.value,
            // genre: this.genre.value,
            type: this.type.value,
            context: this.context.value,
            language: this.langue.value,
            paragraphs: this.paragraphs.map(element => {
                return {
                    "name": element.name_value,
                    "contents": [element.content_value]
                }
            })
        }
    }
    }
    async post()
    {
        try {

            var payload = this.payload()
            var terme = await post("/termes/", payload["terme"]);
            this.id = terme.id;
            // await put(`/termes/${this.id}/dictionnaires`, payload["dictionnaires"]);
        
        }
        catch (e){
            this.error.update(()=>e);
            return false;
        }
        return true
    }

    draft()
    {
        if (this.draft_id == "")
            this.draft_id = "draft_" + String(Math.round(Math.random() * 100000000000))
        var payload = this.payload()
        localStorage.setItem(this.draft_id, JSON.stringify(payload.terme))
    }

    load_draft()
    {
        if (this.draft_id == "")
            return;
        var terme = localStorage.getItem(this.draft_id)
        this.init(terme);
    }

    del_draft()
    {
        localStorage.removeItem(this.draft_id);
    }


    async put()
    {
        if (this.id == -1)
            return this.draft()
        this.del_draft()
        try {
            var payload = this.payload()
            await put(`/termes/${this.id}`, payload["terme"]);
            // await put(`/termes/${this.id}/dictionnaires`, payload["dictionnaires"]);
        } catch (e: any){
            this.error.update(()=>e);
            console.log(e)
            return false
        }
        return true;
    }
    
    async delete()
    {
        await del(`/termes/${this.id}`)
    }

    set_inputs()
    {
        this.inputs = [
            this.name,
            this.type,
            this.context,
            this.langue,
        ]

        this.inputs_value = [
            this.name_value,
            this.type_value,
            this.context_value,
            this.langue_value,
        ]

        var i = 0
        for (let x of Array(this.paragraphs.length).keys())
        {
            if (i != 0)
                this.inputs.push(this.paragraphs[x].name);
            this.inputs.push(this.paragraphs[x].content);


            if (i != 0)
                this.inputs_value.push(this.paragraphs[x]);
            this.inputs_value.push(this.paragraphs[x]);
            i +=1 
        }
        console.log(this.inputs)
    }

    focus(index, shift)
    {
        if (index + shift < 0)
            index += this.inputs.length
        if (index + shift >= this.inputs.length)
            index -= this.inputs.length
        this.inputs[index + shift].focus()
    }

    focus_at(x, y)
    {  
        if (x < 0 || x >= this.paragraphs.length)
            return false
        var paragraph = this.paragraphs[x]
        if (y == -1 && x != 0)
        {
            paragraph.name.focus()
        }
        else
        {
            paragraph.content.focus();
        }
        return true;
    }


    set_focus()
    {
        if (this.new)
        {
            this.name?.focus()
            this.new = false
            return
        }
        this.focus_at(this.next_x, this.next_y)
        this.next_x = -1;
    }

    change_paragraph_amount(x, num)
    {
        if (num < 0 && this.paragraphs.length == 1)
            return

        if (num > 0)
        {
            if (x == -1)
                x = this.paragraphs.length - 1;
            this.next_x = x + 1;
            this.next_y = -1;
            this.paragraphs.splice(x + 1, 0, new Paragraph())
            this.set_inputs();
            this.reactive.update((v)=>!v)
            console.log("new paragraphe !")
            return;
        }

        this.next_x = x - 1;
        if (this.next_x == -1)
            this.next_x = 0
        this.next_y = -1;
        this.paragraphs.splice(x, 1);
        this.set_inputs();
        this.reactive.update((v)=>!v)
        console.log("new paragraphe !")
    }

    refresh_paragraphs()
    {
        for (let paragraph of this.paragraphs)
            paragraph.refresh_input()
    }

    get_paragraphe_x(paragraph)
    {
        for (let x of Array(this.paragraphs.length).keys())
            if (this.paragraphs[x].name == paragraph)
                return x
        return -1;
    }


    get_content_x(content)
    {
        for (let x of Array(this.paragraphs.length).keys())
            if (this.paragraphs[x].content == content)
                return x
        return -1;
    }

    async toggle_button()
    {
        if (get_writable(view_mode) == "edit" && !(await this.put()))
            return
        toggle_view_mode()
    }
}