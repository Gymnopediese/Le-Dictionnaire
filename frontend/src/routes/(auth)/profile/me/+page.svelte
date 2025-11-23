<script>
    import { goto } from "$app/navigation";
    import { get } from "$lib/services/api"; 
    import { user } from "$lib/services/global.js";

</script>


{$user.username}
<button on:click={()=> goto("/profile/me/termes")}>
    termes
</button>
<button on:click={()=> goto("/profile/me/drafts")}>
    drafts
</button>