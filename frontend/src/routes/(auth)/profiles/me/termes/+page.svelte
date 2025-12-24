<script>
    import Dictionnaire from "$lib/components/Dictionnaire/Dictionnaire.svelte";
    import { goto } from "$app/navigation";
    import { get } from "$lib/services/api";
    import { langues, types } from "$lib/services/enums.js";

    export let data;
    let dictionnaire;
    async function try_get_terme()
    {
        dictionnaire = await get("/me/termes");
        return dictionnaire;
    }

</script>


{#await try_get_terme()}
    loading data
{:then dictionnaire} 
    <Dictionnaire dictionnaire= {
        {
            name: "all my termes",
            description: "all the termes I ever wrote",
            termes: dictionnaire.termes,
        }
    }>
    </Dictionnaire>
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