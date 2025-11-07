<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
    import { cookies, load_cookies, remove_cookie, set_cookie } from '$lib/cookies';
    import { goto } from '$app/navigation';
    import { get, ping } from '$lib/api';
    import { onMount } from 'svelte';
	
	let { children } = $props();
    let decisionmade = false;


    if (!load_cookies())
    {
        console.log(cookies);
        // onMount(async () => {
        // //    console.log("ping ",  await get("/ping"))
        //     var user = await get("/me");
        //     console.log(user);
        // })
        if (cookies.token)
        {
            decisionmade = true;
        }
        else
        {
            console.log("mais")
            decisionmade = true;
            goto('/login');
        }


    }
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<!-- {#if decision_made} -->
{@render children()}
<!-- {/if} -->
<!-- TODO : add loading icon whatever. -->