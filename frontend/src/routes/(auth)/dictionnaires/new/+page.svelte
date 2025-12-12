<script lang="ts">
    import { goto } from "$app/navigation";
    import { post } from "$lib/services/api";
    import InputChoice from "$lib/components/InputChoice.svelte";

    let name = "";
    let description = "";
    let visibility = "";
    let suggestions = true;

    async function create_dictionnaire() {
        await post("/dictionnaires/", { name, visibility, suggestions, description });
        goto('/dictionnaires');
    }
</script>

<link rel="stylesheet" href="https://fonts.bunny.net/css?family=source-serif-pro:400,600,700" />

<div class="paper">
    <div class="field">
        <label>Nom</label>
        <input bind:value={name} class="input" type="text" />
    </div>

    <div class="field">
        <label>Visibilité</label>
        <InputChoice class_name="input" bind:value={visibility} options={['public','link','private']} />
    </div>

    <div class="field">
        <label>Description</label>
        <textarea bind:value={description}></textarea>
    </div>

    <div class="check">
        <input bind:checked={suggestions} type="checkbox" id="sugg" />
        <label for="sugg">Autoriser les commentaires</label>
    </div>

    <button class="create" on:click={create_dictionnaire}>Créer</button>
</div>

<style>
.paper {
    margin: auto;
    /* height: 100%; */
    padding: 2rem;
    border-radius: 8px;
    font-family: "Source Serif Pro", serif;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.field {
    display: flex;
    flex-direction: column;
    gap: .3rem;
    color: #5a5146;
}

.input, textarea, .field :global(.input) {
    width: 100%;
    background: rgba(255,255,255,0.7);
    border: 2px solid #d0c6b9;
    padding: .6rem;
    border-radius: 4px;
    font-size: 1rem;
    color: #4d463e;
}

textarea {
    height: 15vh;
    resize: none;
}

.check {
    display: flex;
    align-items: center;
    gap: .5rem;
    color: #5a5146;
}

.create {
    all: unset;
    cursor: pointer;
    align-self: flex-end;
    background: #efe7da;
    padding: .8rem 1.3rem;
    border: 2px solid #b5a391;
    border-radius: 6px;
    box-shadow: 3px 3px 0 #b5a391;
    transition: 0.1s ease-in-out;
}

.create:hover {
    transform: translate(-2px, -2px);
    box-shadow: 5px 5px 0 #b5a391;
}
</style>
