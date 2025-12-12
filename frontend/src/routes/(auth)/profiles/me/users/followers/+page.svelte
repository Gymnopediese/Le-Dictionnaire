<script>
    import Dictionnaires from "$lib/components/Dictionnaires/Dictionnaires.svelte";
    import Users from "$lib/components/Users/Users.svelte";
    import { get_dictionnaires, get_users } from "$lib/services/cache";


    

</script>

<Users user_id="me" args={`relationship_types=${["follower_only"]}`}>

</Users>
