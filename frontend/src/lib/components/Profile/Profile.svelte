

<script>
    import { goto } from "$app/navigation";
    import { follow_user, get_user, unfollow_user } from "$lib/services/cache";
    import { user } from "$lib/services/global.js";
    import { signout } from "$lib/services/login";

    let oldPass = "";
    let newPass = "";
    let newPassConf = "";

    export let id="me";
    

</script>

{#await get_user(id)}
    
{:then profile} 
    

    <div class="profile">
    <div class="card">
        <h1 class="title">Profil</h1>

        <div class="row">
            <span class="label">Utilisateur :</span>
            <span class="value">{profile.username}</span>
        </div>

        <div class="row">
            <span class="label">Relation :</span>
            <span class="value">{profile.relationship}</span>
        </div>

      

        {#if id == "me"}
            
        <h2>Termes</h2>
        <div class="buttons">
            <button on:click={() => goto("/profiles/me/termes")}>Mes termes</button>
            <button on:click={() => goto("/profiles/me/drafts")}>Mes brouillons</button>
        </div>
        <h2>Dictionnaires</h2>
        <div class="buttons">
            <button on:click={() => goto("/profiles/me/dictionnaires")}>Mes dictionnaires</button>
            <button on:click={() => goto("/profiles/me/dictionnaires/shared")}>Partager avec moi</button>
            <button on:click={() => goto("/profiles/me/dictionnaires/followings")}>Dictionnaires suivis</button>
        </div>

                <h2>Users</h2>
        <div class="buttons">
            <button on:click={() => goto("/profiles/me/users/friends")}>Amis</button>
            <button on:click={() => goto("/profiles/me/users/followers")}>Followers</button>
            <button on:click={() => goto("/profiles/me/users/followings")}>Followings</button>
            <button on:click={() => goto("/profiles/me/users/blocked")}>Contes Bloque</button>
        </div>

        <div class="section">
            <h2>Mot de passe</h2>
            <input type="password" placeholder="Ancien mot de passe" bind:value={oldPass} />
            <input type="password" placeholder="Nouveau mot de passe" bind:value={newPass} />
            <input type="password" placeholder="Nouveau mot de passe" bind:value={newPassConf} />
            <button class="action">Mettre à jour</button>
        </div>

         <button on:click={() => signout()}>Se Deconnecter</button>
        {:else}
          <div class="buttons">
            <button on:click={() => goto(`/profiles/${id}/termes`)}>Termes</button>
        </div>

        {#if $user.id != id}
            {#if ["friend", "follow"].includes(profile.relationship)}
                <button on:click={()=> unfollow_user(id)}>
                    unfollow
                </button>
            {:else if ["stranger"].includes(profile.relationship)} 
                <button on:click={()=> follow_user(id)}>
                    follow
                </button>
            {:else if ["following"].includes(profile.relationship)} 
                <button on:click={()=> follow_user(id)}>
                    follow back
                </button>
            {:else if ["blocked"].includes(profile.relationship)} 
                <button on:click={()=> unfollow_user(id)}>
                    unblock
                </button>
            {/if}
        {/if}

        <h2>Dictionnaires</h2>
        <div class="buttons">
            <button on:click={() => goto(`/profiles/${id}/dictionnaires`)}>Dictionnaires</button>
            <button on:click={() => goto(`/profiles/${id}/followings`)}>Suivis</button>
        </div>
        {/if}
    </div>
</div>

<style>
    .profile {
        display: flex;
        justify-content: center;
        padding: 4vh 0;
    }
    .card {
        width: 100%;
        padding: 1%;
        height: 100%;
    }

    .title {
        margin: 0;
        margin-bottom: 1.5rem;
        font-size: 2rem;
        border-bottom: 2px solid #c4b7a3;
        padding-bottom: 0.5rem;
    }

    .row {
        display: flex;
        gap: 1rem;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }

    .label {
        font-weight: bold;
    }

    .section {
        margin-top: 2rem;
        padding: 1rem;
        border: 2px dashed #cbbba8;
        border-radius: 6px;
        background: #f7f3ed;
    }

    input {
        display: block;
        width: 60%;
        margin: 0.5rem 0;
        padding: 0.4rem 0.6rem;
        background: #fcfaf7;
        border: 1px solid #a69786;
        border-radius: 4px;
        font-size: 0.9rem;
    }

    .action {
        margin-top: 0.8rem;
        padding: 0.4rem 0.6rem;
        border: 1px solid #8f8374;
        background: #d4c7b8;
        border-radius: 4px;
        font-size: 0.95rem;
    }

    .buttons {
        margin-top: 2rem;
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .buttons button {
        padding: 0.4rem 0.8rem;
        background: #e3d6c8;
        border: 1px solid #9b8c7c;
        border-radius: 4px;
        font-size: 0.95rem;
    }
</style>


{/await}