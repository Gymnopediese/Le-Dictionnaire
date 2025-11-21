<script lang="ts">
    import { del, get } from "$lib/services/api";
    import TermeView from "$lib/components/TermeView.svelte";


    var termes          : any;

    async function try_get_termes()
    {  
       termes = await get("/termes");
       console.log(termes);
    }
    
    try_get_termes();


</script>
{#each termes as terme}
    <TermeView terme_object={terme}></TermeView>
{/each}