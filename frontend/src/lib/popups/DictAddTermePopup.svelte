
<script lang="ts">

    import { fade } from "svelte/transition";



    // var visibility = $props<{}>();;
    let { terme = $bindable(), visibility = $bindable(), dictionnaire = $bindable(), onAdd} = $props<{}>();

    var changed = $state(false)
    // var visibility = $state(false)
    window.onkeydown = (e) => {
        if (!!e.metaKey && e.key == "d")
        {
            e.preventDefault();
            e.stopPropagation();
            visibility = !visibility;
        }
    }


</script>

    {#if visibility}
        
    <div in:fade={{duration: 500}} class="popup {visibility ? "show" : "hide"}">

        <slot></slot>

    </div>
    {/if}
    

<style>

    .show {
        opacity: 1;
    }

    .hide {
        opacity: 0;
    }

.popup {
    position: absolute;
    left: 10%;
    top: 10%;
    width: 80%;
    height: 80%;
    overflow: scroll;

    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    border-radius: 6px;

    box-shadow: 6px 6px 0px #b8a898;
    font-family: "Source Serif Pro", serif;
    color: #5c544b;
}
    
    .chooser {
    display: flex;
    width: 100%;
    height: 100%;
}

.sidebar {
    width: 25%;
    overflow-y: auto;
    border-right: 2px solid #b8a898;
    background-color: #f3ede4;
    padding: 10px 0;
}

.dict_item {
    padding: 16px 20px;
    font-size: 28px;
    font-family: "Source Serif Pro", serif;
    cursor: pointer;
    color: #5c544b;

    border-bottom: 2px solid #e0d6cb;
}

.dict_item:hover {
    background-color: #e8dfd3;
}

.dict_item.active {
    background-color: #e0d6cb;
    font-weight: bold;
}

.content {
    width: 75%;
    padding: 20px;
    overflow-y: auto;
}

.word_card {
    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    margin-bottom: 25px;
    padding: 20px;
    border-radius: 4px;

    box-shadow: 3px 3px 0px #b8a898;
}

.word {
    font-size: 40px;
    color: #4d453d;
    font-family: "Source Serif Pro", serif;
}

.type {
    font-size: 28px;
    color: #7a7065;
    margin-top: 6px;
}

.desc {
    font-size: 26px;
    margin-top: 12px;
    color: #5c544b;
}

.add_btn {
    all: unset;
    cursor: pointer;

    margin-top: 20px;
    padding: 10px 24px;
    font-size: 28px;
    font-family: "Source Serif Pro", serif;
    color: #5c544b;

    background-color: #e8dfd3;
    border: 2px solid #b8a898;
    border-radius: 4px;

    box-shadow: 3px 3px 0px #b8a898,
        inset 0 0 0 2px rgba(255,255,255,0.4);

    transition: transform 0.08s ease, box-shadow 0.08s ease;
}

.add_btn:active {
    transform: translate(2px, 2px);
    box-shadow:
        1px 1px 0px #b8a898,
        inset 0 0 0 2px rgba(255,255,255,0.4);
}
</style>