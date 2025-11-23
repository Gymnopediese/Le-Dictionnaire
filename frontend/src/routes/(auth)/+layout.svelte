
<script lang="ts">
    import { goto } from "$app/navigation";
    import { popup, user } from "$lib/services/global"

    var visibility = $state(true);

</script>

<link rel="stylesheet" href="https://fonts.bunny.net/css?family=source-serif-pro:400,600,700" />


<main class="container">
    <!-- {#key visibility} -->
        
    <section class="meta">
        <div class="navbar {visibility ? "" : "hide"}">

            <button class="{visibility ? "show_button" : ""}" on:click={()=>visibility = !visibility}>Hide</button>

            <button class="{visibility ? "" : "hide_button"}" on:click={()=>visibility = !visibility}>Hide</button>
            <button class="{visibility ? "" : "hide_button"}" on:click={()=>goto("/")}>Main</button>
            <button class="{visibility ? "" : "hide_button"}" on:click={()=>goto("/profile/me")}>Me</button>
            <button class="{visibility ? "" : "hide_button"}" on:click={()=>goto("/dictionnaires")}>Dictionnaires</button>
            <button class="{visibility ? "" : "hide_button"}" on:click={()=>goto("/")}>Users</button>
            <button class="{visibility ? "" : "hide_button"}" on:click={()=>goto("/create")}>Create</button>
        </div>



        <div class="content">
            <slot></slot>
        </div>
    </section>
    <!-- {/key} -->



</main>
<style>

    .popup {
        position: absolute;
        left: 10%;
        top: 10%;
        width: 80%;
        height: 80%;
        border: rgb(65, 65, 65) solid 2px;
        border-radius: 2%;
        background-color: rgb(213, 214, 209);
    }

    @keyframes slidein {
        from {
            width: 10%;
            /* margin: 1%;  */
            padding: 1%; 
        }

        to {
            width: 1%;
            margin: 0;
            padding: 0;
        }
    }

    @keyframes hide {
        from {
            opacity: 1;
            /* margin: 1%;  */
            /* padding: 1%;  */
        }

        to {
            opacity: 0;
        }
    }



    .content {
        overflow: scroll;
        width: 98%;
        height:96vh;
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

section {

    display: flex;
}



.navbar {
    width: 10%;
    display: flex;
    align-items: center;
    flex-direction: column;
    position: relative;
    gap: 20px;
    list-style-type: none;
    overflow: hidden;
    /* margin: 1%;  */
    padding: 1%;
    align-items: center;
     justify-content: center;
    color: rgb(212, 196, 176);
    font-size: 16px;
  /* background-color: #333333; */
}

.hide_button {
    animation-duration: 0.5s;
    animation-name: hide;
    opacity: 0;
}

.hide {
    animation-duration: 1s;
    animation-name: slidein;
    width: 1%;
    margin: 0;
    padding: 0;
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


</style>