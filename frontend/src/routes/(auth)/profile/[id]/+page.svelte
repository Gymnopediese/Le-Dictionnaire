<script>
    import { get } from "$lib/api";
    import Terme from "$lib/components/Terme.svelte";

    export let data;
    let user;
    async function try_get_terme()
    {
        user = await get("/users/" + data.id);
        console.log(user)
        return user;
    }

</script>


{#await try_get_terme()}
    loading data
{:then user} 
    {user.username}
{/await}