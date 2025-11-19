<script>
    import { goto } from "$app/navigation";
    import { get } from "$lib/api";
    import { langues, types } from "$lib/enums.js";

    export let data;
    let dico;
    async function try_get_terme()
    {
        dico = await get("/dictionnaires/" + data.id + "");
        console.log(dico.termes[0])
        return dico;
    }

</script>


{#await try_get_terme()}
    loading data
{:then dictionnaire} 

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
            <button on:click={()=>goto("/termes/" + terme.id)} >remove</button> <br>
            <hr>
        </div>
            <br>
    {/each}

{/await}

<style>

    .terme {
        padding: 1%;
        box-shadow: 10px;
        border: 10px ridge rgba(211, 220, 50, 0.6);
    }

    .terme_name {
        margin: 0;
        padding: 2%;
        padding-left: 2%;
        border: 10px ridge rgba(211, 220, 50, 0.6);

    }

</style>