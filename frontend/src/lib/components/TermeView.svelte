
<script lang="ts">
    import { del, post, put } from "$lib/services/api.js";
    import InputChoice from "$lib/components/InputChoice.svelte";
    import { contenu_types, contexts, genres, langues, types } from "$lib/services/enums.js";
    import { popup, toggle_view_mode, user, view_mode } from "$lib/services/global";
    import { onMount } from "svelte";
    import TermeAddDictPopup from "$lib/popups/TermeAddDictPopup.svelte";
    import Terme from "$lib/classes/terme";
    import { edit_view_event_manage } from "./TermeViewInputManager.js";
    
    let { terme_object } = $props<{}>();
    var show_add_dict = $state(false)
    var terme = $state(new Terme(terme_object));
    let { reactive, error } = terme;


    $effect(()=>
    {
        $reactive = $reactive;
        terme.set_inputs();
        terme.set_focus();
        terme.refresh_paragraphs();
    })

    onMount(()=> {
        terme.refresh_paragraphs()
        terme.set_inputs();
    })


    $effect(()=>console.log(reactive))


    document.addEventListener('keydown', (event) => edit_view_event_manage(event, terme, {
        "show_dict_popup": ()=> show_add_dict = !show_add_dict
    } ))

</script>

<TermeAddDictPopup bind:terme bind:visibility={show_add_dict} ></TermeAddDictPopup>

{#if $view_mode == "edit"}
    <div class="toolbar">
        <span>
            {$error}
        </span>
    </div>
{/if}

<main class="{$view_mode == "edit" ? "main_edit" : ""}">
    <div class="content">
{#if $view_mode == "edit"}
    <div class="name_div">
        <input bind:value={terme.name_value} bind:this={terme.name} autoComplete="off"  id="name" type="text" list="browsers" placeholder="Nom..."><br>
    </div>
{:else}
    <div class="name_div">
        <label bind:this={terme.name} autoComplete="off"  id="name" type="text" list="browsers" placeholder="name">{terme.name_value}</label><br>
    </div>
{/if}

<div class="metadata_div">
    <InputChoice class_name="metadata_input" bind:value={terme.type_value} bind:input={terme.type} label={"Type\t\t: "}    align="right" width="93%" placeholder="type..." options={Object.keys(types)} ></InputChoice>
    <InputChoice class_name="metadata_input" bind:value={terme.context_value} bind:input={terme.context} label={"Context\t: "} align="right" width="93%" placeholder="context..." options={Object.keys(contexts)} ></InputChoice>
    <InputChoice class_name="metadata_input" bind:value={terme.langue_value} bind:input={terme.langue} label={"Langue\t: "}  align="right" width="93%" placeholder="langue..." options={Object.keys(langues)} ></InputChoice>
</div>

{#key $reactive}
    {#each Array(terme.paragraphs.length) as _, x}
            {#if x != 0}
                <div class="paragraph_name_div" >
                    <div style="width:95%;">
                    <InputChoice class_name="paragraph_name_input"  placeholder="Paragraphe name..." options={contenu_types} bind:input={terme.paragraphs[x].name} bind:value={terme.paragraphs[x].name_value} > </InputChoice>
                    </div>
                    <button on:click={() => terme.change_paragraph_amount(x, -1)} style="margin:1%;">X</button>
                </div>
            {/if}
            <div class="content_div">
            {#key terme.paragraphs[x].content}
                <textarea class="content_input" bind:value={terme.paragraphs[x].content_value} bind:this={terme.paragraphs[x].content} name="contenu" id="1" placeholder="contenu" ></textarea>
            {/key}
            </div>
    {/each}
{/key}

</div>

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
        margin-top: 30px;
        margin-bottom:38px;
        margin-left: 75px;
        width: auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }


    .toolbar {
        height: 10%;
    }
   main {
    width: 100%;
    min-height: 100%;
    background-color: rgba(250, 248, 243, 1);

    background-image:
        linear-gradient(#cdcdcd 2px, transparent 2px),
        linear-gradient(#e4e3e1 1px, transparent 1px),
        linear-gradient(90deg, #e1c9c9 2px, transparent 2px);

    background-size:
        200px 200px,
        40px 40px,
        200px 10000px;

    background-position:
        0 82px,
        0 2px,
        70px 0;
    background-repeat:
        repeat,      /* grille large */
        repeat,      /* grille fine  */
        no-repeat;   /* la ligne vertical UNIQUE */

}

    .main_edit {
        border-top: #cdcdcd solid 2px;
        min-height: 89%;
    }

    #name, #name:focus {
        margin-left: 75px;
        font-family: "Source Serif Pro", serif;
        background-color: unset;
        width: 100%;
        height: auto;
        font-size: 80px;
        border: none;
        outline: none;
        color: #a7a299;
        /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif */
    }

    .content {
        /* margin-left: 73px; */
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
        margin-left: 75px;
        display:flex;

    }
    .metadata_div :global(.metadata_input) {
        width: 100%;
        margin: 0;
        padding: 0;
        font-size: 34px;
        height: 40px;
        vertical-align: center;
        
    }
    main :global(.paragraph_name_input) {
        width: 90%;
        margin-top: 20px;
        font-size: 56px;
        height: 60px;
    }

    .content_input {

        line-height: 100px;
        all: unset;
        margin-left: 75px;
        margin-bottom: 40px;
        width: 95%;
        height: 40px;
        font-size: 32px;
        border: none;
        outline: none;
        resize: none; /* désactive le redimensionnement utilisateur */
        overflow: hidden; /* cache la scrollbar */
        white-space: pre-wrap;
  white-space: pre-wrap;
  overflow-wrap: break-word;
        /* height: fit-content; */
        /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif */
    }

    .name_label {
        margin-left: 10px;
        margin-top: 10px;
        width: 73px;
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

