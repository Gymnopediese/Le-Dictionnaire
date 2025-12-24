
<script lang="ts">

    import InputChoice from "$lib/components/InputChoice.svelte";
    import { contenu_types, contexts, genres, langues, types } from "$lib/services/enums.js";
    import { metadatas, popup, scroll_div, toggle_view_mode, user, view_mode, writing_mode} from "$lib/services/global";
    import { onMount } from "svelte";
    import TermeAddDictPopup from "$lib/popups/TermeAddDictPopup.svelte";
    import Terme from "$lib/classes/terme";
    import { edit_view_event_manage } from "./TermeViewInputManager.js";
    import Metadata from "./Metadata.svelte";
    import TextAreaPosition from "./TextAreaPosition.svelte";
    
    let { terme_object } = $props<{}>();
    var show_add_dict = $state(false)
    var terme = $state(new Terme(terme_object));
    let { reactive, error } = terme;

    $metadatas = terme_object.metadatas
    console.log($metadatas)
    
    $effect(()=>
    {
        $reactive = $reactive;
        terme.set_inputs();
        terme.set_focus();
        terme.refresh_paragraphs();
    })

    onMount(async ()=> {
        terme.refresh_paragraphs()
        terme.set_inputs();
    })

    




    document.addEventListener('keydown', (event) => edit_view_event_manage(event, terme, {
        "show_dict_popup": ()=> show_add_dict = !show_add_dict
    } ))

    var fontSize = $state(8);
    
    $effect(()=>document.documentElement.style.setProperty('--font-size', String(fontSize / 10) + "px"))

    function focus_input_function(event){
        var child = event.target
        var new_pos = child.offsetTop
        if (new_pos - $scroll_div.scrollTop > 600)
            new_pos -= $scroll_div.clientHeight * 5 / 6
        else if (new_pos - $scroll_div.scrollTop < 200)
            new_pos -= $scroll_div.clientHeight * 1 / 4
        else
            return
        requestAnimationFrame(() => {
            $scroll_div.scrollTop = new_pos
        })
    }



    function name_focus(){
        requestAnimationFrame(() => {
        $scroll_div.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        })
    }


</script>

<TermeAddDictPopup bind:terme bind:visibility={show_add_dict} ></TermeAddDictPopup>

{#if $view_mode === "edit"}
<div class="edit_panel">
    <button class="panel_btn" on:click={() => terme.post()}>
        {#if terme.id == -1}
            upload
        {:else}
            save
        {/if}
    </button>

    <div class="panel_group">
        <label>Text size</label>
        <input
            class="size_input"
            type="number"
            min="1"
            max="96"
            bind:value={fontSize}
        />
    </div>

    <div class="panel_group">
        <button class="panel_btn" on:click={()=>terme.change_paragraph_amount(-1, 1)}>+</button>
        <button class="panel_btn" on:click={()=>terme.change_paragraph_amount(-1, -1)}>−</button>
    </div>

    <div class="edit_panel">
    <button class="drawn_button" on:click={() => {$writing_mode = !$writing_mode;}}>
        {$writing_mode === true ? "désactiver mode écriture" : "activer mode écriture"}
    </button>
</div>
</div>
{/if}

<main class="{$view_mode == "edit" ? "main_edit" : ""}">
    <div class="content">
        {#if $view_mode == "edit"}
            <div class="name_div">
                <input on:focus={name_focus} on:input={name_focus} bind:value={terme.name_value} bind:this={terme.name} autoComplete="off"  id="name" type="text" list="browsers" placeholder="Nom..."><br>
            </div>
        {:else}
            <div class="name_div">
                <label bind:this={terme.name} autoComplete="off"  id="name" type="text" list="browsers" placeholder="name">{terme.name_value}</label><br>
            </div>
        {/if}

    <div class="metadata_div">
        <Metadata></Metadata>
        <!-- <InputChoice class_name="metadata_input" bind:value={terme.type_value} bind:input={terme.type} label={"Type\t\t: "}    align="right" width="93%" placeholder="type..." options={Object.keys(types)} ></InputChoice>
        <InputChoice class_name="metadata_input" bind:value={terme.context_value} bind:input={terme.context} label={"Context\t: "} align="right" width="93%" placeholder="context..." options={Object.keys(contexts)} ></InputChoice>
        <InputChoice class_name="metadata_input" bind:value={terme.langue_value} bind:input={terme.langue} label={"Langue\t: "}  align="right" width="93%" placeholder="langue..." options={Object.keys(langues)} ></InputChoice> -->
    </div>

    {#key $reactive}
        {#each Array(terme.paragraphs.length) as _, x}
                {#if x != 0}
                    <div class="paragraph_name_div" >
                        <div style="width:95%;">
                            <InputChoice on_focus={focus_input_function} class_name="paragraph_name_input"  placeholder="Paragraphe name..." options={contenu_types} bind:input={terme.paragraphs[x].name} bind:value={terme.paragraphs[x].name_value} > </InputChoice>
                        </div>
                        <!-- <button on:click={() => terme.change_paragraph_amount(x, -1)} style="margin:1%;">X</button> -->
                    </div>
                {/if}
                <div class="content_div">
                {#key terme.paragraphs[x].content || fontSize || terme.paragraphs[x].content_value}
                    <!-- <textarea  spellcheck="true" class="content_input" bind:value={terme.paragraphs[x].content_value} bind:this={terme.paragraphs[x].content} name="contenu" id="1" placeholder="contenu" ></textarea> -->
                     <TextAreaPosition bind:fontSize={fontSize} bind:value={terme.paragraphs[x].content_value} bind:input={terme.paragraphs[x].content} placeholder="contenu"></TextAreaPosition>
                {/key}
                </div>
        {/each}
    {/key}

    </div>

    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>

    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
</main>
<style>

    .name_div {
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .metadata_div {
        margin-top: calc(30 * var(--font-size));
        margin-bottom:calc(30 * var(--font-size));
        margin-left: calc(75 * var(--font-size));
        width: calc(100% - 75px);
        display: flex;
        flex-direction: column;
        /* justify-content: center; */
        /* align-items: center; */
    }


    .toolbar {
        height: 10%;
    }
   main {
    width: 98.5%;
    min-height: 97.5%;
    margin: 0.5%;

    /* width: 95%; */
    border: 2px solid #b8a898;
    border-radius: 8px;
    /* box-shadow: 12px 12px 24px rgba(185, 185, 185, 0.15), 0 0 0 4px #f4efe7 inset; */
    display: flex;
    flex-direction: column;
    /* gap: 24px; */
    transition: transform 0.2s ease;
    
    background-color: rgba(250, 248, 243, 1);

    background-image:
        linear-gradient(#cdcdcd 2px, transparent 2px),
        linear-gradient(#e4e3e1 1px, transparent 1px),
        linear-gradient(90deg, #e1c9c9 2px, transparent 2px);

    background-size:
        calc(200 * var(--font-size)) calc(200 * var(--font-size)),
        calc(40 * var(--font-size)) calc(40 * var(--font-size)),
        calc(200 * var(--font-size)) 10000px;

    background-position:
        0 calc(80 * var(--font-size)),
        0 0px,
        calc(70 * var(--font-size)) 0;
    background-repeat:
        repeat,      /* grille large */
        repeat,      /* grille fine  */
        no-repeat;   /* la ligne vertical UNIQUE */

}

    .main_edit {
        min-height: 87%;
    }

    #name, #name:focus {
        margin-left: calc(75 * var(--font-size));
        font-family: "Source Serif Pro", serif;
        background-color: unset;
        width: 100%;
        height: auto;
        font-size: calc(80 * var(--font-size));
        border: none;
        outline: none;
        color: #a7a299;
        /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif */
    }


    .content_div
    {
        display:flex;
        width: 100%;
    }

    .left_side {
        width: 95%;
    }

    .paragraph_name_div
    {
        margin-left: calc(75 * var(--font-size));
        display:flex;

    }
    .metadata_div :global(.metadata_input) {
        width: 100%;
        margin: 0;
        padding: 0;
        font-size: calc(34 * var(--font-size));
        height: calc(40 * var(--font-size));
        vertical-align: center;
        
    }
    main :global(.paragraph_name_input) {
        width: 90%;
        margin-top:  calc(20 * var(--font-size));
        font-size:  calc(56 * var(--font-size));
        height:  calc(60 * var(--font-size));
    }


    .edit_panel {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 10px 20px;
        border-bottom: 2px solid #b8a898;
        background: #f4efe7;
    }

    .panel_group {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .panel_btn {
        all: unset;
        cursor: pointer;
        padding: 6px 14px;
        font-size: 18px;
        color: #5c544b;
        background-color: #e8dfd3;
        border: 2px solid #b8a898;
        border-radius: 4px;
        box-shadow: 2px 2px 0px #b8a898;
    }

    .panel_btn:active {
        transform: translate(2px,2px);
        box-shadow: 1px 1px 0px #b8a898;
    }

    .size_input {
        all: unset;
        width: 60px;
        text-align: center;
        font-size: 18px;
        border-bottom: 2px solid #b8a898;
        color: #5c544b;
    }

    .edit_panel {
        position: sticky;
        top: 0;
        z-index: 10;
    }



:root {
    --font-size: 1; /* default scale, can represent px, %, em, etc. */
}

/* Example elements */
#name, #name:focus {
    font-size: calc(80 * var(--font-size));
}

.content_input {
    font-size: calc(32 * var(--font-size));
    line-height: calc(100 * var(--font-size));
}

.metadata_div :global(.metadata_input) {
    font-size: calc(34 * var(--font-size));
    height: calc(40 * var(--font-size));
}

main :global(.paragraph_name_input) {
    font-size: calc(56 * var(--font-size));
    height: calc(60 * var(--font-size));
}
/* 
.panel_btn {
    font-size: calc(18 * var(--font-size));
} */
/* 
.size_input {
    font-size: calc(18 * var(--font-size));
} */

.edit_panel {
    position: sticky;
    top: 0;
    background: #fdfcf8;
    border-bottom: 2px solid #b8a898;
    padding: 8px;
    z-index: 10;
}
</style>



