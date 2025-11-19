<script lang="ts">
    import { view_mode } from "$lib/global";


    export var label        : string = "";
    export var options      : any = [];
    export var placeholder  : string = "";
    export let input        : HTMLElement | null = null;
    export let class_name   : string = "";
    export let value        : string = "";
    var id                  : string = String(Math.random() * 100000)

    console.log(options)
</script>
<div >
{#if label}
    <label for="">{label}</label>
{/if}

{#if $view_mode == "edit"}
<!-- style="float: {align}; width:{width};font-size:{font_size}; height:{height};" -->
<input bind:value class="{class_name}" bind:this={input}  placeholder="{placeholder}" list="{id}" type="text"> <br>
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