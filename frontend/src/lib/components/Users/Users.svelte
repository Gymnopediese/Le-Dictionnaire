<script lang="ts">
    import { goto } from "$app/navigation";
    import { get_users } from "$lib/services/cache";
    import { fade } from "svelte/transition";

    let { users = [],
        buttons= [],
        user_id="me",
        args="",
        filter = ()=> true
     } = $props();

    let query: string = $state("");


    function filter_user(username: string): boolean {
        return username.toLowerCase().includes(query.toLowerCase());
    }
</script>
{#await get_users(user_id, args)}

{:then users} 
    
<div in:fade class="user_list_page">
    <input class="search_bar" bind:value={query} placeholder="Rechercher…" type="text">

    <div class="user_list">
        {#each users as f}
            {#if filter_user(f.username) && filter(f)}
            <!-- on:click={() => goto(`/profiles/${f.id}`)} -->
                <div class="user_item" >
                    <div class="user_name">{f.username}</div>

                    {#each buttons as button}
                        <button on:click={()=> button[1](f)}>{button[0]} </button>
                    {/each}
                </div>
            {/if}

        {/each}
    </div>


</div>
{/await}
<style>
    .user_list_page {
        display: flex;
        flex-direction: column;
        gap: 20px;
        width: 98%;
        padding: 1%;
        font-family: "Source Serif Pro", serif;
        color: #5c544b;
    }

    .search_bar {
        all: unset;
        width: 98%;
        padding: 1%;
        font-size: 18px;
        border: 2px solid #b8a898;
        border-radius: 6px;
        background: #efe7da;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
        color: #5c544b;
    }

    .user_list {
        display: flex;
        flex-direction: column;
        width: 100%;
        gap: 12px;
    }

    .user_item {
        background: #e8dfd3;
        border: 2px solid #b8a898;
        border-radius: 6px;
        padding: 14px;
        box-shadow: 3px 3px 0 #b8a898;
        font-size: 22px;
        cursor: pointer;
        transition: transform 0.08s ease, box-shadow 0.08s ease;
    }

    .user_item:hover {
        transform: translate(2px,2px);
        box-shadow: 1px 1px 0 #b8a898;
    }

    .user_name {
        color: #4d453d;
        font-weight: bold;
    }
</style>
