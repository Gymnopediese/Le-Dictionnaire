<script lang="ts">
    import { goto } from "$app/navigation";
    import { post } from "$lib/api";

    
    import InputChoice from "$lib/components/InputChoice.svelte";


    var name        : string = "";
    var visibility  : string = "";
    var suggestions : boolean = true;

    async function create_dictionnaire()
    {
        await post("/dictionnaires/", {
            name, visibility, suggestions
        })
        location.href = '/dictionnaires'
    }
</script>


<input bind:value={name} style="height: 3dvh;" class="input" placeholder="input" type="text">
<InputChoice bind:value={visibility} options={[
    'public', 'link', 'private'
    ]}> 

</InputChoice>

<input bind:checked={suggestions} type="checkbox" name="" id="">

<button on:click={create_dictionnaire}>lets go</button>