
<script lang="ts">
    import { del, post, put } from "$lib/api";
    import InputChoice from "$lib/components/InputChoice.svelte";
    import { contenu_types, contexts, genres, langues, types } from "$lib/enums";
    import { toggle_view_mode, user, view_mode } from "$lib/global";
    import { onMount } from "svelte";
    
    let { terme_object } = $props<{}>();
    var dico_name = $user.dictionnaires.map((elem)=> elem.name);

    class Paragraph
    {
        name            : HTMLInputElement = $state(null);
        name_value      : string = $state("");
        contents        : [HTMLInputElement] = $state([null]);
        contents_value  : [string] = $state([""]);

        constructor(name="", contents=[""])
        {
            this.name_value = name;
            this.contents_value = contents
            while (this.contents.length < this.contents_value)
                this.contents.push(null)
        }

        refresh_input()
        {
            for (let content of this.contents)
            {
                content.addEventListener('input', () => {
                    content.style.height = 'auto';
                    content.style.height = content.scrollHeight + 'px';
                });
                content.style.height = 'auto';
                content.style.height = content.scrollHeight + 'px';
            }
        }


        change_content_amount(y, num)
        {
            if (num > 0)
            {
                if (y == -1)
                    y = this.contents.length - 1;
                this.contents.splice(y + 1, 0, null);
                this.contents_value.splice(y + 1, 0, "");
                console.log("new paragraph ?? ? ", this.contents)
                console.log("new paragraph ? ", this.contents_value)
                return;
            }
            this.contents.splice(y, 1)
            this.contents_value.splice(y, 1)
        }

    }
    
    class Terme
    {
        id                  : number = -1;
        name                : HTMLInputElement | null = $state(null);
        name_value          : string = $state("");     
        inputs              : [HTMLInputElement];

        type                : HTMLInputElement | null = $state(null);
        type_value          : string = $state("");     
        genre               : HTMLInputElement | null = $state(null);
        genre_value         : string = $state("");     
        context             : HTMLInputElement | null = $state(null);
        context_value       : string = $state("");     
        langue              : HTMLInputElement | null = $state(null);
        langue_value        : string = $state("");     
        dictionnaire        : HTMLInputElement | null = $state(null);
        dictionnaire_value  : string = $state("");     


        paragraphs      : [Paragraph] = $state([]);;

        next_x          : number = 0;
        next_y          : number = 0;
        next_start      : number = 0;

        current_input   : number = 0;
        new             : boolean = false;
        constructor(terme)
        {
            if (terme == undefined)
            {
                this.paragraphs.push(new Paragraph())
                this.set_inputs();
                this.new = true;
                return
            }

            this.id = terme.id;
            this.name_value = terme.name;
            this.type_value = terme.type;
            this.genre_value = terme.genre;
            this.context_value = terme.context;
            this.langue_value = terme.language;
            this.dictionnaire_value = terme.dictionnaires[0].name;
            console.log(terme.paragraphs)
            for (let paragraph of terme.paragraphs)
            {
                this.paragraphs.push(new Paragraph(paragraph.name, paragraph.contents))
            }

            this.set_inputs();
        }

        payload()
        {
            return { terme : {
                name: this.name.value,
                genre: this.genre.value,
                type: this.type.value,
                context: this.context.value,
                language: this.langue.value,
                paragraphs: this.paragraphs.map(element => {
                    return {
                        "name": element.name_value,
                        "contents": [...element.contents_value]
                    }
                })
            }, dictionnaires: {
                dictionnaires: [$user.dictionnaires.find((elem)=>elem.name == this.dictionnaire.value).id]
            }}
        }
        async post()
        {
            var payload = this.payload()
            var terme = await post("/termes/", payload["terme"]);
            this.id = terme.id;
            await put(`/termes/${this.id}/dictionnaires`, payload["dictionnaires"]);
            return 
        }


        async put()
        {
            if (this.new)
            {
                this.post()
                this.new = false
                return
            }

            var payload = this.payload()
            await put(`/termes/${this.id}`, payload["terme"]);
            await put(`/termes/${this.id}/dictionnaires`, payload["dictionnaires"]);
        }
        
        async delete()
        {
            await del(`/termes/${this.id}`)
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

            for (let x of Array(this.paragraphs.length).keys())
            {
                this.inputs.push(this.paragraphs[x].name);
                for (let y of Array(this.paragraphs[x].contents.length).keys())
                    this.inputs.push(this.paragraphs[x].contents[y]);
            }
        }

        focus(index, shift)
        {
            if (index + shift < 0 || index + shift >= this.inputs.length)
                return        
            this.inputs[index + shift].focus()
        }

        focus_at(x, y)
        {  
            console.log(x, y)
            if (x < 0 || x >= this.paragraphs.length)
                return false
            var paragraph = this.paragraphs[x]
            if (y >= paragraph.contents.length)
                return false;
            if (y == -1)
            {
                paragraph.name.focus()
            }
            else
            {
                paragraph.contents[y].focus();
            }
            return true;
        }


        set_focus()
        {
            this.focus_at(this.next_x, this.next_y)
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
                return;
            }

            this.next_x = x - 1;
            if (this.next_x == -1)
                this.next_x = 0
            this.next_y = -1;
            this.paragraphs.splice(x, 1);
            this.set_inputs();
        }

        change_paragraph_content_amount(x, y, num)
        {
            if (this.paragraphs[x].contents.length == 1 && num < 0)
                return
            if (num > 0)
            {
                this.next_x = x;
                this.next_y = y + 1;
            }
            else
            {
                this.next_x = x;
                this.next_y = y - 1;
                if (this.next_y == -1)
                    this.next_y = 0
            }
            this.paragraphs[x].change_content_amount(y, num);
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


        get_content_x_y(content)
        {
            for (let x of Array(this.paragraphs.length).keys())
            {
                if (this.paragraphs[x].name == content)
                    return [x, -1]
                for (let y of Array(this.paragraphs[x].contents.length).keys())
                {
                    if (this.paragraphs[x].contents[y] == content)
                    {
                        return [x, y]
                    }
                }
            }
            return -1;
        }

        async toggle_button()
        {
            toggle_view_mode()
            if ($view_mode == "edit")
                return;
            console.log(this)
            await this.put();
        }
    }
    console.log(terme_object);
    var terme = $state(new Terme(terme_object));

    $effect(()=>
    {
        terme.set_inputs();
        terme.set_focus();
        terme.refresh_paragraphs();
    })

    onMount(()=> {
        terme.refresh_paragraphs()
        terme.set_inputs();
    })

    document.addEventListener('keydown', function(event) {

        var input = document.activeElement
        var input_type = input.tagName.toLowerCase();
        
        if (!['input', "textarea"].includes(input_type))
        {
            terme.inputs[0].focus();
            return;
        }

        // console.log("Active: ", document.activeElement)
        // console.log("element; ", terme.inputs)
        // console.log('Key pressed:', event.key);
        // console.log('Key code:', event.code);
        // console.log('Which key:', event.which); // Backup for older browsers

        if (event.key == "Tab") {   //tab pressed
            event.preventDefault(); // stops its action
            event.stopPropagation();
        }


        var current_input = terme.inputs.indexOf(input);
        if (!!event.shiftKey && event.key == "Enter")
        {
            event.preventDefault(); // stops its action
            event.stopPropagation();
            var ind: any = terme.get_paragraphe_x(input);
            if (ind != -1)
            {
                terme.change_paragraph_amount(ind, 1);
                console.log("t bete toi");
                return;
            }

            ind = terme.get_content_x_y(input);
            if (ind != -1)
            {
                terme.change_paragraph_content_amount(ind[0], ind[1], 1);
                return;
            }
        }

        if (!!event.shiftKey && event.key == "Backspace")
        {
            event.preventDefault(); // stops its action
            event.stopPropagation();
            var ind: any = terme.get_paragraphe_x(input);
            if (ind != -1)
            {
                terme.change_paragraph_amount(ind, -1);
                console.log("t bete toi");
                return;
            }

            ind = terme.get_content_x_y(input);
            if (ind != -1)
            {
                terme.change_paragraph_content_amount(ind[0], ind[1], -1);
                return;
            }
        }

        if (!!event.shiftKey && event.key == "ArrowUp")
        {
            event.preventDefault(); // stops its action
            event.stopPropagation();
            var ind: any = terme.get_content_x_y(input);
            if (ind != -1)
            {
                if (ind[1] == -1)
                    ind[0] -= 1;
                if (terme.focus_at(ind[0], -1))
                    return;
            }
        }

        if (!!event.shiftKey && event.key == "ArrowDown")
        {
            event.preventDefault(); // stops its action
            event.stopPropagation();
            var ind: any = terme.get_content_x_y(input);
            if (ind != -1)
            {
                if (terme.focus_at(ind[0] + 1, -1))
                return;
            }
        }
        // console.log(event.key)
        // if (!!event.metaKey && event.key == "e")
        // {
        //     toggle_view_mode()
        // }

        if (((event.key == "ArrowDown" || (event.key == "Enter")) && input_type != "textarea") || event.key == "Tab")
        {
            event.preventDefault(); // stops its action
            event.stopPropagation();
            terme.focus(current_input, 1)
        }
        if ((event.key == "ArrowUp" && input_type != "textarea") || (event.key == "Backspace" && input.value == "" ) )
        {           
            event.preventDefault(); // stops its action
            event.stopPropagation();    
            terme.focus(current_input, -1)
        }


        if (input_type == "textarea" && event.key == "ArrowDown")
        {
            if (input.selectionStart > input.value.lastIndexOf("\n"))
            {
                event.preventDefault(); // stops its action
                event.stopPropagation();  
                terme.focus(current_input, 1)
            }
        }
        var index = input.value.indexOf("\n")
        if (input_type == "textarea" && event.key == "ArrowUp")
        {
            if (input.selectionStart <=  index || index == -1)
            {
                event.preventDefault(); // stops its action
                event.stopPropagation();  
                terme.focus(current_input, -1)
            }
        }
    });

    // setInterval(toggle_view_mode, 1000)


</script>

<main>
{#if $view_mode == "edit"}
    <input bind:value={terme.name_value} bind:this={terme.name} autoComplete="off"  id="name" type="text" list="browsers" placeholder="name"><br>
    <button on:click={() => terme.toggle_button()}>save</button>
{:else}
    <label bind:this={terme.name} autoComplete="off"  id="name" type="text" list="browsers" placeholder="name">{terme.name_value}</label><br>
    <button on:click={toggle_view_mode}>edit</button>
{/if}
<hr>
<InputChoice class_name="metadata_input" bind:value={terme.genre_value} bind:input={terme.genre} label={"Genre\t: "}   align="right" width="93%" placeholder="genre..." options={Object.keys(genres)} ></InputChoice>
<hr>
<InputChoice class_name="metadata_input" bind:value={terme.type_value} bind:input={terme.type} label={"Type\t\t: "}    align="right" width="93%" placeholder="type..." options={Object.keys(types)} ></InputChoice>
<hr>
<InputChoice class_name="metadata_input" bind:value={terme.context_value} bind:input={terme.context} label={"Context\t: "} align="right" width="93%" placeholder="context..." options={Object.keys(contexts)} ></InputChoice>
<hr>
<InputChoice class_name="metadata_input" bind:value={terme.langue_value} bind:input={terme.langue} label={"Langue\t: "}  align="right" width="93%" placeholder="langue..." options={Object.keys(langues)} ></InputChoice>
<hr>
<InputChoice class_name="metadata_input" bind:value={terme.dictionnaire_value} bind:input={terme.dictionnaire}  label={"Dico\t\t: "}  align="right" width="93%" placeholder="langue..." options={dico_name} ></InputChoice>
<hr>
{#key terme.paragraphs.length}
{console.log("mmm ", terme.paragraphs.length)}
{#each Array(terme.paragraphs.length) as _, x}
        <div class="paragraph_name_div" >
            <div style="width:95%;">
            <InputChoice class_name="paragraph_name_input"  placeholder="Paragraphe name..." options={contenu_types} bind:input={terme.paragraphs[x].name} bind:value={terme.paragraphs[x].name_value} > </InputChoice>
            <hr>
            </div>
            <button on:click={() => terme.change_paragraph_amount(x, -1)} style="margin:1%;">X</button>
        </div>
        {#key terme.paragraphs[x].contents.length}
            {#each Array(terme.paragraphs[x].contents.length) as _, y}
                <div class="contents_div" >
                    <textarea style="width:95%;" class="content_input" bind:value={terme.paragraphs[x].contents_value[y]} bind:this={terme.paragraphs[x].contents[y]} name="contenu" id="1" placeholder="contenu" ></textarea>
                    <button on:click={() => terme.change_paragraph_content_amount(x, y, -1)} style="margin:1%; max-height:3.3dvh; align:center;">X</button>
                </div>
                <!-- <br> -->
            {/each}
        {/key}
        <!-- <button on:click={() => change_content_amount(x, -1)} >-</button> -->
        <button class="content_plus" on:click={() => terme.change_paragraph_content_amount(x, -1, 1)} >+ Contenu</button><br>

{/each}
    
{/key}
    
<!-- <button on:click={() => change_paragraph_amount(-1)} >-</button> -->
 <br>
<button class="plus" on:click={() => terme.change_paragraph_amount(-1, 1)} >+ Paragraphe</button><br>

<br>
<!-- <label for="">Genre</label><br>
<br> -->

<button on:click={()=>terme.post()}>create terme</button>

</main>
<style>

    #name, #name:focus {
        width: 100%;
        height: auto;
        font-size: 8dvh;
        border: none;
        outline: none;
        /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif */
    }

    .contents_div
    {
        display:flex;
    }

    .left_side {
        width: 95%;
    }

    .paragraph_name_div
    {
        display:flex;

    }
    main :global(.metadata_input) {
        width: 80%;
        font-size: 3dvh;
        height: 5dvh;
        vertical-align: center;
        
    }
     main :global(.paragraph_name_input) {
        width: 90%;
        font-size: 5dvh;
        height: 6dvh;
    }

    .content_input {
        width: 95%;
        font-size: 2.5dvh;
        border: none;
        outline: none;
        resize: none; /* désactive le redimensionnement utilisateur */
        overflow: hidden; /* cache la scrollbar */
        /* height: fit-content; */
        /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif */
    }


    .plus
    {
        width: 100%;
        height: auto;
        font-size: 4dvh;
    }

    .content_plus
    {
        width: 100%;
    }
</style>

