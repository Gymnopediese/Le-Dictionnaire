<script>
    import { get } from "$lib/api";
    import Terme from "$lib/components/Terme.svelte";

    export let data;
    let terme;
    async function try_get_terme()
    {
        terme = await get("/me");
        console.log(terme)
        return terme;
    }

</script>


{#await try_get_terme()}
    loading data
{:then terme} 
    <Terme terme={terme}> </Terme>
{/await}