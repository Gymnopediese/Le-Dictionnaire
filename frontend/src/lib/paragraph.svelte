<!-- <script>

    
</script>
import { settled } from "svelte";

export class Terme
{
    name        : HTMLInputElement | null = null;

    inputs      : [HTMLInputElement];

    type        : HTMLInputElement | null = null;
    genre       : HTMLInputElement | null = null;
    context     : HTMLInputElement | null = null;
    langue      : HTMLInputElement | null = null;;

    paragraphs  : [Paragraph];

    constructor()
    {
        this.paragraphs = [new Paragraph()]
        this.set_inputs();
    }

    set_inputs()
    {
        this.inputs = [
            this.name,
            this.genre,
            this.type,
            this.context,
            this.langue,
        ]

        for (let x of Array(this.paragraphs).keys())
        {
            this.inputs.push(this.paragraphs[x].name);
            for (let y of Array(this.paragraphs[x].contents).keys())
                this.inputs.push(this.paragraphs[x].contents[y]);
        }      
    }

    change_paragraph_amount(x, num)
    {
        this.set_inputs();
        console.log(this.paragraphs)
        if (num > 0)
        {
            this.paragraphs.push(new Paragraph())
            return;
        }
        this.paragraphs.splice(x, 1);
    }

    change_paragraph_content_amount(x, y, num)
    {
        this.paragraphs[x].change_content_amount(y, num);
        this.set_inputs();
    }

    refresh_paragraphs()
    {
        for (let paragraph of this.paragraphs)
            paragraph.refresh_input()
    }

    get_paragraphe_x(paragraph)
    {
        for (let x of Array(this.paragraphs.length).keys())
        {
            if (this.paragraphs[x] == paragraph)
            {
                return x
            }
        }
        return -1;
    }


    get_conntent_x_y(content)
    {
        for (let x of Array(this.paragraphs.length).keys())
            for (let y of Array(this.paragraphs[x].contents.length).keys())
                if (this.paragraphs[x].contents[y] == content)
                    return [x, y]
        return -1;
    }
}


export class Paragraph
{
    name        : HTMLInputElement | null = null;
    contents    : [HTMLInputElement | null] = [null];

    constructor()
    {

    }

    refresh_input()
    {
        for (let content of this.contents)
            content.addEventListener('input', () => {
                content.style.height = 'auto';
                content.style.height = content.scrollHeight + 'px';
            });
    }


    change_content_amount(y, num)
    {
        if (num > 0)
        {
            this.contents.push(null)
            return;
        }

        console.log(content_fields[x])
        console.log(x, y)
        content_fields[x].splice(y, 1)
        content_fields[x].push("")
        console.log(content_fields[x])
    }

} -->
