<script lang="ts">
    import { del, get, put } from "$lib/services/api";
    import { user } from "$lib/services/global";
    import InputChoice from "$lib/components/InputChoice.svelte";
    import { goto } from "$app/navigation";
    import { fade } from "svelte/transition";


    let { 
        dictionnaires = $user.dictionnaires,
        mode = "view",
        terme = $bindable()
    } = $props();

    let changed : boolean = $state(false)
    var query   : string = $state("");

    function query_filter(word: string) : boolean
    {
        // Naive filter
        return (word.toLowerCase().startsWith(query.toLowerCase()));
    }
    
    function remove_dict(id: number)
    {
        del(`/termes/${terme.id}/dictionnaires`, {
            dictionnaires: [id]
        })
        terme.terme.dictionnaires = terme.terme.dictionnaires.filter((d) => {
            return d.id != id;
        })
        changed = !changed
    }

    function add_dict(id: number)
    {
        put(`/termes/${terme.id}/dictionnaires`, {
            dictionnaires: [id]
        })
        terme.terme.dictionnaires.push({id})
        changed = !changed
    }

</script>

<input class="search_bar" bind:value={query} placeholder="search..." type="text">

<div class="dictionnaires">
    {#each dictionnaires as dictionnaire}
    {#if query_filter(dictionnaire.name)}

        <div class="dictionnaire">
            <p class="name">
                {dictionnaire.name}
            </p>
            <p class="description">
                {dictionnaire.description}
            </p>

            <slot></slot>
            {#if mode == "view"}
            <button class="button drawn_button" on:click={()=>goto("dictionnaires/" + dictionnaire.id)} >view</button>
            {:else if mode == "add_to_terme"}
                {#key changed}
                    
                    {#if terme.terme.dictionnaires.find((d)=> d.id == dictionnaire.id)}
                        <button on:click={()=>remove_dict(dictionnaire.id)}>remove</button>
                    {:else}
                        <button on:click={()=>add_dict(dictionnaire.id)}>add</button>
                    {/if}
                {/key}
            {/if}
            <br>
        </div>




        {/if}
    {/each}
        {#if mode == "view"}
            <button on:click={() => goto('/dictionnaires/new')}>new</button>
        {/if}
</div>



<style>

    .search_bar {
        all: unset;
        width: 100%;
        padding: 1%;
        font-size: 20px;
    }

    .dictionnaires {
        display: grid;
        grid-template-columns: repeat(3, 33%);
        /* grid-row: auto; */
    }

    .dictionnaire {
        display: flex;
        flex-direction: column;
        padding: 1%;
        margin: 1%;
        border: #cdcdcd solid 2px;
        background-color: #FAF8F3;
        background-image: 
            linear-gradient(#e4e4e4 2px, transparent 2px),
            linear-gradient(90deg, #e4e4e4 2px, transparent 2px),
            linear-gradient(#e4e4e4 1px, transparent 1px),
            linear-gradient(90deg, #e4e4e4 1px, #faf8f3 1px);
        background-size: 100px 100px, 100px 100px, 20px  20px, 20px 20px;
        background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px; 
        /* background-color: rgba(250, 248, 243, 1);
        background-image: 
            linear-gradient(#cdcdcd 2px, transparent 2px),
            linear-gradient(#e4e3e1 1px, transparent 1px),
            linear-gradient(90deg, #e1c9c9 2px, transparent 2px);
        background-size: 100px 100px, 20px  20px, 5000px,  5000px;
        background-position: -2px -62px, -1px -1px, -4950px, -2px; */
    }

    .name {
        margin-left: 2px;
    }
    

</style>