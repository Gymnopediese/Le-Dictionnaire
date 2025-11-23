
<script lang="ts">
    import Dictionnaires from "$lib/components/Dictionnaires/Dictionnaires.svelte";
import { del, put } from "$lib/services/api";
    import { user } from "$lib/services/global";
    import { fade } from "svelte/transition";



    // var visibility = $props<{}>();;
    let { terme = $bindable(), visibility = $bindable() } = $props<{}>();

    var changed = $state(false)

</script>

    {#if visibility}
        
    <div in:fade={{duration: 500}} class="popup {visibility ? "show" : "hide"}">



        {#key changed}
             <Dictionnaires mode="add_to_terme" bind:terme>
                
             </Dictionnaires>
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
        background-color: rgb(228, 228, 228);
    }
</style>