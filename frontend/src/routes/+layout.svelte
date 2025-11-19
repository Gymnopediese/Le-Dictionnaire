<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
    import { cookies, load_cookies, remove_cookie, set_cookie } from '$lib/cookies';
    import { goto } from '$app/navigation';
    import { get, ping } from '$lib/api';
    import { onMount } from 'svelte';
    import { user } from '$lib/global';
	
	let { children } = $props();

    async function get_me()
    {
        $user = await get("/me/");
        console.log($user);
    } 

    if (!load_cookies() && !cookies.token)
    {
        goto('/login');
    }
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
{#await get_me()}
    
{:then _} 
    {@render children()}
{/await}


<!-- TODO : add loading icon whatever. -->