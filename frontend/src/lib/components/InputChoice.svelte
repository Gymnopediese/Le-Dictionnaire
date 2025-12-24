<script lang="ts">
    import { scroll_div, view_mode } from "$lib/services/global";
    import { onMount } from "svelte";


    export var label        : string = "";
    export var options      : any = [];
    export var placeholder  : string = "";
    export let input        : HTMLElement | null = null;
    export let class_name   : string = "";
    export let value        : string = "";
    export let on_focus              = null;
    var id                  : string = String(Math.random() * 100000)


    function on_mount_input(event){
        var child = event.target
        var new_pos = child.offsetTop - $scroll_div.clientHeight * 1 / 4
        requestAnimationFrame(() => {
            $scroll_div.scrollTop = new_pos
        })
    }

    onMount(() => {
        on_mount_input({target: input})
    })
</script>
<div >


{#if $view_mode == "edit"}
<!-- style="float: {align}; width:{width};font-size:{font_size}; height:{height};" -->
<input on:focus={on_focus} on:click={on_focus} on:keydown={focus_input_function} bind:value class="{class_name}" bind:this={input}  placeholder="{placeholder}" list="{id}" type="text"> <br>
<datalist id="{id}">
    {#each options as option}
        <option value="{option}"> </option>
    {/each}
</datalist>
{:else}
    <!-- style="float: {align}; width:{width};font-size:{font_size}; height:{height};" -->
    <label class="{class_name}" bind:this={input}  placeholder="{placeholder}" type="text">{value}</label><br>
{/if}
</div>
<style>


input, input:focus, label, div {
    all: unset;
}

div {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
}

/* label {
    width: 10%;
} */
label, input:focus, input, datalist {

    white-space: break-spaces;
    outline: none;
    border: none;
    /* font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; */
}

* {
    padding: 0;
    margin: 0;
}



/* hr {
  border: none;
  border-top: 3px double #333;
  color: #333;
  overflow: visible;
  text-align: center;
  height: 5px;
}

hr::after {
  background: #fff;
  content: "§";
  padding: 0 4px;
  position: relative;
  top: -13px;
} */
</style>