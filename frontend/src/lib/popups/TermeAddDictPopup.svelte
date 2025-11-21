
<script lang="ts">
    import { del, put } from "$lib/services/api";
    import { user } from "$lib/services/global";
    import { fade } from "svelte/transition";



    // var visibility = $props<{}>();;
    let { terme, visibility } = $props<{}>();

    var changed = $state(false)

    function remove_dict(id)
    {
        del(`/termes/${terme.id}/dictionnaires`, {
            dictionnaires: [id]
        })
        terme.terme.dictionnaires = terme.terme.dictionnaires.filter((d) => {
            return d.id != id;
        })
        changed = !changed
    }

    function add_dict(id)
    {
        put(`/termes/${terme.id}/dictionnaires`, {
            dictionnaires: [id]
        })
        terme.terme.dictionnaires.push({id})
        changed = !changed
    }

</script>

    {#if visibility}
        
    <div in:fade={{duration: 500}} class="popup {visibility ? "show" : "hide"}">
        {#key changed}
            
        {#each $user.dictionnaires as dict}
            {dict.name}
            {#if terme.terme.dictionnaires.find((d)=> d.id == dict.id)}
                <button on:click={()=>remove_dict(dict.id)}>remove</button>
            {:else}
                <button on:click={()=>add_dict(dict.id)}>add</button>
            {/if}
            <br>
        {/each}
        {/key}

    </div>
    {/if}

<style>

    .show {
        opacity: 1;
    }

    .hide {
        opacity: 0;
    }

    .popup {
        position: absolute;
        left: 10%;
        top: 10%;
        width: 80%;
        height: 80%;
        border: rgb(65, 65, 65) solid 2px;
        border-radius: 2%;
        background-color: rgb(213, 214, 209);
    }
</style>