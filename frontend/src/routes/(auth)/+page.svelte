<script lang="ts">
    import { goto } from "$app/navigation";

</script>

<div class="intro">
    <div class="panel">
        <h1>Bienvenue dans le dictionnaire</h1>
        <p>Un espace pour organiser, explorer et enrichir vos mots.</p>
        <button on:click={() => goto("/profiles/me")}>Profile</button>
        <button on:click={() => goto("/create")}>Creer</button>
    </div>
</div>

<style>



.panel h1 {
    margin: 0;
    font-size: 2.4rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid #c4b7a3;
    padding-bottom: 0.5rem;
    background-color: transparent;
}

.panel p {
    margin: 0 0 2rem 0;
    font-size: 1.2rem;
}

button {
    padding: 0.6rem 1.2rem;
    background: #e3d6c8;
    border: 1px solid #9b8c7c;
    border-radius: 4px;
    font-size: 1rem;
}

.panel {
    width: 100%;
    height: 100%;
    margin: 3%;
    margin-top: 3%;
}
</style>
