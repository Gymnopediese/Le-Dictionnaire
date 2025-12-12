<script lang="ts">
    import { goto } from "$app/navigation";
    import DictAddTermePopup from "$lib/popups/DictAddTermePopup.svelte";
    import { del, get, put } from "$lib/services/api.js";
    import { follow_dictionnaire, get_dictionnaire, unfollow_dictionnaire, unwrite_dictionnaire } from "$lib/services/cache";
    import { langues, types } from "$lib/services/enums.js";
    import TermeFilter from "../TermeFilter.svelte";

    export let data = {};
    export let popup = false;
    export let dictionnaire: any = null;

    async function try_get_terme() {
        if (dictionnaire != null) return dictionnaire;
        dictionnaire = await  get_dictionnaire(data.id);
        console.log(dictionnaire)
        return dictionnaire
        // dictionnaire = await get("/dictionnaires/" + data.id);
        // dictionnaire.termes = await get("/dictionnaires/" + data.id + "/termes?sort_by=ctime");
        // return dictionnaire;
    }

    async function add_dict(terme) {
        await put("/dictionnaires/" + data.id + "/termes/" + terme.id, {});
        dictionnaire.termes.push(terme);
    }

    async function remove_terme(terme) {
        await del("/dictionnaires/" + data.id + "/termes/" + terme.id);
        dictionnaire.termes = dictionnaire.termes.filter(t => t.id !== terme.id);
    }

    var letter = ""
    function is_new_letter(word: string)
    {
        return false
        if (word == "")
        return
        if (word[0].toLowerCase() != letter)
        {
            letter = word[0].toLowerCase()
            return true
        }
        return false;
    }

</script>

{#if popup}
<DictAddTermePopup bind:dictionnaire onAdd={add_dict} />
{/if}

{#await try_get_terme()}
    <div class="loading">Loading dictionary...</div>
{:then _} 

<div class="dictionnaire_page">
    <h1>{dictionnaire.name}</h1>
    <h3>{dictionnaire.description}</h3>
    <h5>{dictionnaire.termes.length} words</h5>
    {#if dictionnaire.rights == "view"}
        <button on:click={()=> follow_dictionnaire(dictionnaire)}  >follow</button>
    {:else if dictionnaire.rights == "read"}
        <button on:click={()=> unfollow_dictionnaire(dictionnaire)} >unfollow</button>
    {:else if dictionnaire.rights == "write"}
        <button on:click={()=> unwrite_dictionnaire(dictionnaire)} >givup write acess</button>
    {/if}
    <!-- <TermeFilter></TermeFilter> -->
    {#each dictionnaire.termes as terme}
        {#if is_new_letter(terme.name)}
            <div class="terme">
                <div class="terme_header">
                <h3 class="terme_name">{terme.name[0].toUpperCase()}</h3>
            </div>
            </div>
        {/if}
        <div class="terme">
            <div class="terme_header">
                <h3 class="terme_name">{terme.name}</h3>
                <div class="terme_buttons">
                    <button on:click={() => goto("/termes/" + terme.id)}>view</button>
                    <button on:click={() => remove_terme(terme)}>remove</button>
                </div>
            </div>
            <div class="terme_meta">
                {types[terme.type]} - {terme.context} - {langues[terme.language]}
            </div>
            <p class="terme_desc">{terme.description}</p>
        </div>
    {/each}
</div>

{/await}

<style>
/* Page background and vibe */
.dictionnaire_page {
    font-family: "Source Serif Pro", serif;
    color: #5c544b;
    padding: 30px;
    background-color: transparent;
    min-height: 100vh;

        display: flex;
        flex-direction: column;
        /* padding: 1%; */
        /* margin: 1%; */

        /* background-color: rgba(250, 248, 243, 1);
        background-image: 
            linear-gradient(#cdcdcd 2px, transparent 2px),
            linear-gradient(#e4e3e1 1px, transparent 1px),
            linear-gradient(90deg, #e1c9c9 2px, transparent 2px);
        background-size: 100px 100px, 20px  20px, 5000px,  5000px;
        background-position: -2px -62px, -1px -1px, -4950px, -2px; */
    }


/* Terme cards with paper/drawn effect */
.terme {
    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    border-radius: 6px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 4px 4px 0px #b8a898;
}

.terme_header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.terme_name {
    margin: 0;
    font-size: 32px;
    color: #4d453d;
}

.terme_buttons button {
    all: unset;
    cursor: pointer;
    padding: 6px 14px;
    margin-left: 10px;
    font-size: 22px;
    color: #5c544b;
    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    border-radius: 4px;
    box-shadow: 2px 2px 0px #b8a898;
    transition: transform 0.08s ease, box-shadow 0.08s ease;
}

.terme_buttons button:hover {
    color: #4d453d;
}

.terme_buttons button:active {
    transform: translate(2px,2px);
    box-shadow: 1px 1px 0px #b8a898;
}

.terme_meta {
    font-size: 20px;
    margin: 10px 0;
    color: #7a7065;
}

.terme_desc {
    font-size: 22px;
    line-height: 1.4;
}

.loading {
    font-size: 28px;
    color: #5c544b;
    text-align: center;
    margin-top: 50px;
}
</style>

<!-- <script lang="ts">
    import { goto } from "$app/navigation";
    import DictAddTermePopup from "$lib/popups/DictAddTermePopup.svelte";
    import { del, get, put } from "$lib/services/api.js";
    import { langues, types } from "$lib/services/enums.js";

    export let data = {};
    export let popup = false;
    export let dictionnaire: any = null;
    async function try_get_terme()
    {
        if (dictionnaire != null)
        {
            console.log(dictionnaire)
            return dictionnaire
        }
        dictionnaire = await get("/dictionnaires/" + data.id + "");
        return dictionnaire;
    }

    async function add_dict(terme)
    {
        await put("/dictionnaires/" + data.id + "/termes/" + terme.id, {});
        dictionnaire.termes.push(terme)
    }
    async function remove_terme(terme) {
        await del("/dictionnaires/" + data.id + "/termes/" + terme.id)
        dictionnaire.remove(terme)
    }


</script>

{#if popup}
<DictAddTermePopup bind:dictionnaire onAdd={add_dict}>

</DictAddTermePopup>
{/if}

{#await try_get_terme()}
    loading data
{:then _} 

<script>
</script>


    <h1>
        {dictionnaire.name}
    </h1>
    <h3>
        {dictionnaire.description}
    </h3>
    <h5>
        {dictionnaire.termes.length} words
    </h5>

    {#each dictionnaire.termes as terme}
        <div class="terme">
            <h3 class="terme_name">
                {terme.name}
            </h3>
            <hr>
            {types[terme.type]} - {terme.context} - {langues[terme.language]} <br>
            <p>
                {terme.description}
            </p>
            <button on:click={()=>goto("/termes/" + terme.id)} >view</button>
            <button on:click={()=>remove_terme(terme)} >remove</button> <br>
            <hr>
        </div>
            <br>
    {/each}

{/await}

<style>

    .terme {
        padding: 1%;
        box-shadow: 10px;
        border: 10px solid rgba(211, 220, 50, 0.6);
    }

    .terme_name {
        margin: 0;
        padding: 2%;
        padding-left: 2%;
        border: 10px solid rgba(211, 220, 50, 0.6);

    }

</style> -->