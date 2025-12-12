<script lang="ts">
    import { get } from "$lib/services/api.js";
    import TermeView from "$lib/components/TermeView.svelte";
    import { goto } from "$app/navigation";

    export let data;
    let terme;
    async function try_get_terme()
    {
        terme = localStorage.getItem(data.id)
        if (terme == null)
        {
            goto("/")
            return;
        }
        terme = JSON.parse(terme)
        terme.draft_id = data.id;
        return terme;
    }

</script>


    <!-- <link rel="stylesheet" href="https://unpkg.com/98.css@0.1.4/build/98.css" /> -->

{#await try_get_terme()}
    loading data
{:then terme} 
    <TermeView terme_object={terme} ></TermeView>

{/await}