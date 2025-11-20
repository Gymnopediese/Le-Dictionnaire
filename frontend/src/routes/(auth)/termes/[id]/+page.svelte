<script lang="ts">
    import { get } from "$lib/api";
    import TermeView from "$lib/components/TermeView.svelte";

    export let data;
    let terme;
    async function try_get_terme()
    {
        terme = await get("/termes/" + data.id);
        console.log("j'ai les termes", terme)
        return terme;
    }

</script>


    <!-- <link rel="stylesheet" href="https://unpkg.com/98.css@0.1.4/build/98.css" /> -->

{#await try_get_terme()}
    loading data
{:then terme} 
    <TermeView terme_object={terme} ></TermeView>

{/await}