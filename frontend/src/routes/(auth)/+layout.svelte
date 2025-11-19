
<script lang="ts">
    import { goto } from "$app/navigation";
    import { user } from "$lib/global"

</script>

<link rel="stylesheet" href="https://fonts.bunny.net/css?family=source-serif-pro:400,600,700" />


<main class="container">

    <section class="meta">
        <!-- Vos items WRITING / READING / WATCHING… -->
    

<div class="navbar">
    <button on:click={()=>goto("/")}>Main</button>
    <button on:click={()=>goto("/dictionnaires")}>Dictionnaires</button>
    <button on:click={()=>goto("/")}>Users</button>
    <button on:click={()=>goto("/create")}>Create</button>
</div>
</section>
</main>

<div class="content">
    <slot></slot>
</div>
<style>

    .content {
        overflow: scroll;
        width: 100%;
        height:85vh;
        padding: 0;
        margin:0;
        border: #e4e4e4 solid 2px;
        background-color: rgba(250, 248, 243, 0.8);

        
        /* background-image: 
            linear-gradient(#e4e4e4 2px, transparent 2px),
            linear-gradient(90deg, #e4e4e4 2px, transparent 2px),
            linear-gradient(#e4e4e4 1px, transparent 1px),
            linear-gradient(90deg, #e4e4e4 1px, #faf8f3 1px);
        background-size: 100px 100px, 100px 100px, 20px  20px, 20px 20px;
        background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px; */

        /* margin-top: 50px;
        height: 2px;
        background: linear-gradient(to right, transparent 50%, #223049 50%), linear-gradient(to right, #00b9ff, #59d941);
        background-size: 16px 2px, 100% 2px; */
    }

    button {
        all: unset;
    }


.navbar {
    width: 96%;
    display: flex;
    align-items: center;
    gap: 20px;
    list-style-type: none;
    overflow: hidden;
    margin: 2%; 
    align-items: center;
     justify-content: center;
    color: rgb(212, 196, 176);
    font-size: 16px;
  /* background-color: #333333; */
}

    button:hover {
        color: rgb(143, 136, 128);
    }

.navbar li {
  float: left;
}

.navbar li button {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.navbar li a:hover {
  /* background-color: #111111; */
}
</style>