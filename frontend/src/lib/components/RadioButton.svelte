<script lang="ts">
    import { view_mode } from "$lib/services/global";

    export let search = "";
    export let input;
    export let options: string[] = [
        "nom commun",
        "nom propre",
        "adjectif",
        "verbe",
        "adverbe",
        "pronom",
        "préposition"
    ];

    let open = false;
    let lastValid = "";   // mémorise la dernière entrée valide

    $: filtered = options.filter(o =>
        o.toLowerCase().includes(search.toLowerCase())
    );

    function select(opt: string) {
        search = opt;
        lastValid = opt;
        open = false;
    }

    function onInputKey(e: KeyboardEvent) {
        var t = options.filter(o =>
                    o.toLowerCase().includes(search.toLowerCase())
                )
        if (t.length == 0)
        {
            search = lastValid
            return
        }
        lastValid = search
        if (e.key == "Tab" && t.length > 1)
        {
            e.preventDefault();
            e.stopPropagation();
            select(filtered[0]);
            return;
        }
        if (e.key === "Backspace" && t.length < 2) {
            // retour à l’ancienne recherche
            // if (!options.includes(search)) search = lastValid;
            while (filtered.length < 2)
            {
                search = search.substring(0, search.length - 1)
                filtered= options.filter(o =>
                    o.toLowerCase().includes(search.toLowerCase())
                )

            }
            open = true
            e.preventDefault();
            e.stopPropagation();
            return;
        }

        if (filtered.length === 1) {
            // auto-lock sur l'unique résultat
            select(filtered[0]);
            return;
        }


        open = true;
    }
    function focusOut(){
        setTimeout(() => {
            open = false
        }, 150);
        //  requestAnimationFrame(() => {
        //     open = false
        //  })
    }
</script>

<div class="select_box">

    {#if $view_mode == "edit"}
    <input
        class="select_input"
        bind:value={search}
        bind:this={input}
        on:focus={() => (open = true)}
        on:keydown={onInputKey}
        on:input={onInputKey}
        on:focusout={focusOut}
        placeholder="choisir…"
        type="text"
    />
    {:else}
        <span>{search}</span>
    {/if}

    {#if open}
        <div class="select_popup">
            {#each filtered as opt}
                <div class="select_opt" on:click={() => select(opt)}>
                    {opt}
                </div>
            {/each}
        </div>
    {/if}
</div>

<style>
    .select_box {
        position: relative;
        width: 90%;
    }

    .select_input {
        all: unset;
        border: 1px solid #b8a898;
        padding: 6px 10px;
        font-size: 20px;
        width: 100%;
        background: transparent;
        color: #6e6a63;
        cursor: text;
    }

    .select_popup {
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        background: #fdfcf8;
        border: 1px solid #b8a898;
        display: flex;
        flex-direction: column;
        max-height: 40dvh;
        overflow-y: auto;
        z-index: 20;
    }

    .select_opt {
        padding: 6px 10px;
        font-size: 26px;
        border-bottom: 1px solid #e6ded5;
        cursor: pointer;
    }

    .select_opt:last-child {
        border-bottom: none;
    }

    .select_opt:hover {
        background: #f2ece5;
    }
</style>
