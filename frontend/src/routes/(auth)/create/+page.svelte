
<script lang="ts">
    import { post } from "$lib/api";
    import { contenu_types, genres, types } from "$lib/enums";
    import { get_radio_button_checked } from "$lib/radio";
    import { onMount } from "svelte";

    var name            : String = "";
    var genre_buttons   : NodeListOf<HTMLElement>;
    var type_buttons    : NodeListOf<HTMLElement>;

    var contenu_amount  : Number = 1
    var contenu_filds   : any = Array(10);


    var origine_amount  : Number = 0
    var origine_filds   : any = Array(10);

    var exemple_amount  : Number = 0
    var exemple_filds   : any = Array(10);

    var note_amount  : Number = 0
    var note_filds   : any = Array(10);



    onMount(()=> {
        genre_buttons = document.getElementsByName("genre")
        type_buttons = document.getElementsByName("type")

    })

    async function try_post()
    {
        var genre = get_radio_button_checked(genre_buttons)
        var type = get_radio_button_checked(type_buttons)
        var contenus = []
        for (let i of Array(contenu_amount).keys())
            contenus.push({"contenu": contenu_filds[i], "type":contenu_types.definitions})
        for (let i of Array(exemple_amount).keys())
            contenus.push({"contenu": exemple_filds[i], "type":contenu_types.exemples})
        for (let i of Array(origine_amount).keys())
            contenus.push({"contenu": origine_filds[i], "type": contenu_types.origine})
        for (let i of Array(note_amount).keys())
            contenus.push({"contenu": note_filds[i], "type":contenu_types.note})
        try
        {
            console.log(name, genre, type);
            await post("/termes", {name, genre, type, contenus})
        }
        catch (error){
            console.log(error);
        }
    }

    function change_contenu_amount(num)
    {
        if (contenu_amount + num > 0 && contenu_amount + num < 10)
            contenu_amount += num;
    }
    function change_exemple_amount(num)
    {
        if (exemple_amount + num >= 0 && exemple_amount + num < 10)
            exemple_amount += num;
    }
    function change_note_amount(num)
    {
        if (note_amount + num >= 0 && note_amount + num < 10)
            note_amount += num;
    }
    function change_origine_amount(num)
    {
        if (origine_amount + num >= 0 && origine_amount + num < 10)
            origine_amount += num;
    }
</script>

<label for="">name:</label><br>
<input bind:value={name} type="text" placeholder="name"><br>

    
<label for="">Contenu</label><br>
<button on:click={() => change_contenu_amount(-1)} >-</button>
<button on:click={() => change_contenu_amount(1)} >+</button><br>
{#each Array(contenu_amount) as _, index}
<textarea bind:value={contenu_filds[index]} name="contenu" id="1" placeholder="contenu" ></textarea><br>
{/each}

<label for="">Exemple</label><br>
<button on:click={() => change_exemple_amount(-1)} >-</button>
<button on:click={() => change_exemple_amount(1)} >+</button><br>
{#each Array(exemple_amount) as _, index}
<textarea bind:value={exemple_filds[index]} name="contenu" id="1" placeholder="exemple" ></textarea><br>
{/each}

<label for="">Origine</label><br>
<button on:click={() => change_origine_amount(-1)} >-</button>
<button on:click={() => change_origine_amount(1)} >+</button><br>
{#each Array(origine_amount) as _, index}
<textarea bind:value={origine_filds[index]} name="contenu" id="1" placeholder="origine" ></textarea><br>
{/each}

<label for="">Note</label><br>
<button on:click={() => change_note_amount(-1)} >-</button>
<button on:click={() => change_note_amount(1)} >+</button><br>
{#each Array(note_amount) as _, index}
<textarea bind:value={note_filds[index]} name="contenu" id="1" placeholder="note" ></textarea><br>
{/each}
<br>
<!-- <label for="">Genre</label><br>
<br> -->

<h3>Genres</h3>
<div>
    {#each Object.keys(genres) as genre}
        <input type="radio" id="{genre}" name="genre" value="{genre}" checked>
        <label for="{genre}">{genre}</label><br>
    {/each}
</div>
<br>
<h3>Types</h3>
<div>
    {#each Object.keys(types) as type}
        <input type="radio" id="{type}" name="type" value="{type}" checked>
        <label for="{type}">{type}</label><br>
    {/each}
</div>

<button on:click={try_post}>create terme</button>

