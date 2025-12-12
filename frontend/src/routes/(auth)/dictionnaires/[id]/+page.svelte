<script>
    import Dictionnaire from "$lib/components/Dictionnaire/Dictionnaire.svelte";

    import DictAddTermePopup from "$lib/popups/DictAddTermePopup.svelte";

    export let data
</script>



<Dictionnaire bind:data popup={true}>

</Dictionnaire>