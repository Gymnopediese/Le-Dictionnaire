<script>
    import { get } from "$lib/api";
    import { user } from "$lib/global";
    import InputChoice from "$lib/components/InputChoice.svelte";
    import { goto } from "$app/navigation";



</script>

<div class="dictionnaires">
    {#each $user.dictionnaires as dictionnaire}
        <div class="dictionnaire">
            <p class="name">
                {dictionnaire.name}
            </p>
            <p class="description">
                {dictionnaire.description}
            </p>

            <button class="button" on:click={()=>goto("dictionnaires/" + dictionnaire.id)} >view</button>
            <br>
        </div>
    {/each}

    <button on:click={() => goto('/dictionnaires/new')}>new</button>

</div>



<style>

    .dictionnaires {
        display: grid;
        grid-row: auto;
    }

    .dictionnaire {
        display: flex;
        flex-direction: column;
        padding: 1%;
        margin: 1%;
        border: #cdcdcd solid 2px;
        background-color: #FAF8F3;
        background-image: 
            linear-gradient(#e4e4e4 2px, transparent 2px),
            linear-gradient(90deg, #e4e4e4 2px, transparent 2px),
            linear-gradient(#e4e4e4 1px, transparent 1px),
            linear-gradient(90deg, #e4e4e4 1px, #faf8f3 1px);
        background-size: 100px 100px, 100px 100px, 20px  20px, 20px 20px;
        background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px; 
        /* background-color: rgba(250, 248, 243, 1);
        background-image: 
            linear-gradient(#cdcdcd 2px, transparent 2px),
            linear-gradient(#e4e3e1 1px, transparent 1px),
            linear-gradient(90deg, #e1c9c9 2px, transparent 2px);
        background-size: 100px 100px, 20px  20px, 5000px,  5000px;
        background-position: -2px -62px, -1px -1px, -4950px, -2px; */
    }

    .name {
        margin-left: 2px;
    }

</style>