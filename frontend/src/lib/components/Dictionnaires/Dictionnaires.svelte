<script lang="ts">
    import { del, put } from "$lib/services/api";
    import { user } from "$lib/services/global";
    import { goto } from "$app/navigation";
    import { fade } from "svelte/transition";
    import { get_dictionnaires } from "$lib/services/cache";



    let { 
        dictionnaires = $user.dictionnaires,
        args = "",
        user_id = "",
        mode = "view",
        terme = $bindable(),
        buttons =[],
        filter=()=>true
    } = $props();

    let changed : boolean = $state(false)
    var query : string = $state("");

    function query_filter(word: string) : boolean {
        return word.toLowerCase().startsWith(query.toLowerCase());
    }

    function remove_dict(id: number) {
        del(`/termes/${terme.id}/dictionnaires`, { dictionnaires: [id] });
        terme.terme.dictionnaires = terme.terme.dictionnaires.filter(d => d.id != id);
        changed = !changed;
    }

    function add_dict(id: number) {
        put(`/termes/${terme.id}/dictionnaires`, { dictionnaires: [id] });
        terme.terme.dictionnaires.push({id});
        changed = !changed;
    }
</script>


{#await get_dictionnaires(user_id, args)}

{:then dictionnaires} 

<div in:fade class="dictionary_page">
    <input class="search_bar" bind:value={query} placeholder="Rechercher..." type="text">

    <div class="dictionnaires">
        {#each dictionnaires as dictionnaire}
            {#if query_filter(dictionnaire.name) && filter(dictionnaire)}
                <div class="dictionnaire">
                    <p class="name">{dictionnaire.name}</p>
                    <p class="description">{dictionnaire.description}</p>
                    {#each buttons as button}

                        <button class="drawn_button" on:click={()=> button[1](dictionnaire)}>{button[0]}</button>

                    {/each}
                    {#if mode == "view"}
                        <button class="drawn_button" on:click={()=>goto("/dictionnaires/" + dictionnaire.id)}>Voir</button>
                    {:else if mode == "add_to_terme"}
                    
                        {#key changed}
                            {#if terme.terme.dictionnaires.find(d => d.id == dictionnaire.id)}
                                <button class="drawn_button" on:click={()=>remove_dict(dictionnaire.id)}>Supprimer</button>
                            {:else}
                                <button class="drawn_button" on:click={()=>add_dict(dictionnaire.id)}>Ajouter</button>
                            {/if}
                        {/key}
                    {/if}
                </div>
            {/if}
        {/each}

        {#if mode == "view"}
            <button class="drawn_button add_dict" on:click={() => goto('/dictionnaires/new')}>Nouveau dictionnaire</button>
        {/if}
    </div>
</div>

{/await}
<style>
.dictionary_page {
    font-family: "Source Serif Pro", serif;
    color: #5c544b;
    /* padding: 30px; */
    padding: 1%;
    /* min-height: 100vh; */
    background-color: transparent;
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 98%;
}

.search_bar {
    all: unset;
    width: 98%;
    padding: 1%;
    font-size: 18px;
    border: 2px solid #b8a898;
    border-radius: 6px;
    background: #efe7da;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
    color: #5c544b;
}

.dictionnaires {
    display: grid;
    grid-template-columns: repeat(3, 32.3%);
    gap: 16px;
}

.dictionnaire {
    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    border-radius: 6px;
    padding: 16px;
    box-shadow: 4px 4px 0px #b8a898;
    display: flex;
    flex-direction: column;
    gap: 10px;
    height: 20dvh;
}

.name {
    font-size: 22px;
    font-weight: bold;
    color: #4d453d;
    margin: 0;
}

.description {
    font-size: 18px;
    color: #7a7065;
    margin: 0;
    height: 10dvh;
    overflow: hidden;
}

.drawn_button {
    all: unset;
    cursor: pointer;
    padding: 6px 14px;
    font-size: 16px;
    color: #5c544b;
    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    border-radius: 4px;
    box-shadow: 2px 2px 0px #b8a898;
    text-align: center;
    transition: transform 0.08s ease, box-shadow 0.08s ease;
    
}

.drawn_button:hover {
    color: #4d453d;
}

.add_dict {
    height: 23.3dvh;
}

.drawn_button:active {
    transform: translate(2px,2px);
    box-shadow: 1px 1px 0px #b8a898;
}
</style>
