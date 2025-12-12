<script>
    import Profile from "$lib/components/Profile/Profile.svelte";

    export let data;
</script>

<Profile id={data.id}></Profile>