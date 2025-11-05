<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
    import { cookies, load_cookies, set_cookie } from '$lib/cookies';
    import { goto } from '$app/navigation';
    import { ping } from '$lib/api';
    import { onMount } from 'svelte';
	
	let { children } = $props();

    load_cookies()
    set_cookie("token", "salut");
    onMount(async () => {
        console.log(await ping());
    })
    if (cookies.token)
    {
        goto('menu');
    }
    else
    {
        goto('login');
    }


</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
