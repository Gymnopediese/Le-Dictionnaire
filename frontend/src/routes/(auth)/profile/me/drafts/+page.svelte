<script>
    import Dictionnaire from "$lib/components/Dictionnaire/Dictionnaire.svelte";
    import { goto } from "$app/navigation";
    import { get } from "$lib/services/api";
    import { langues, types } from "$lib/services/enums.js";

    export let data;
    let dico = {termes:[]};
    async function try_get_terme()
    {

        var i = 0;
        while (i <  localStorage.length)
        {
            var key = localStorage.key(i);
            var t = JSON.parse(localStorage.getItem(key));
            t.id = "drafts/" + key
            dico.termes.push(t);
            i += 1;
        }
        return dico;
    }

</script>


{#await try_get_terme()}
    loading data
{:then dictionnaire} 
    <Dictionnaire dico= {
        {
            name: "all my ",
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