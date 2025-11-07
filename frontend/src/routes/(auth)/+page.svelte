<script lang="ts">
    import { del, get } from "$lib/api";
    import Terme from "$lib/components/Terme.svelte";


    var termes          : any;

    async function try_get_termes()
    {  
       termes = await get("/termes");
       console.log(termes);
    }
    
    try_get_termes();


</script>
{#each termes as terme}
    <Terme terme={terme}></Terme>
{/each}