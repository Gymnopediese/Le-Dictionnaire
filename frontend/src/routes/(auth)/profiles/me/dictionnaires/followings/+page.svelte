<script>
    import Dictionnaires from "$lib/components/Dictionnaires/Dictionnaires.svelte";
    import { get_dictionnaires } from "$lib/services/cache";


    

</script>

<Dictionnaires user_id="me" args={`rights_in=${["read"]}`} mode="voila" >


</Dictionnaires>