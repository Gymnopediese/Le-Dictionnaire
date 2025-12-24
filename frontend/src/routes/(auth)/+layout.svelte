
<script lang="ts">
    import { goto } from "$app/navigation";
    import Error from "$lib/components/Error/Error.svelte";
    import { popup, user, scroll_div } from "$lib/services/global"
    import { onMount } from "svelte";

    var visibility = $state(true);

    let scrollDiv = null;

    function handleKeydown(event) {
        return
        if (scrollDiv == null) return
        const input = event.target;
        if (input.selectionStart !== null) {
        // position verticale du curseur par rapport à la page
        const rect = input.getBoundingClientRect();
        const scrollRect = scrollDiv.getBoundingClientRect();
        
        // calcul pour centrer le curseur dans le div scrollable
        const cursorY = rect.top - scrollRect.top + scrollDiv.scrollTop;
        scrollDiv.scrollTop = cursorY - scrollDiv.clientHeight / 2 + rect.height / 2;
        }
    }

    onMount(()=>{
        $scroll_div = scrollDiv;
    })



    

</script>

<link rel="stylesheet" href="https://fonts.bunny.net/css?family=source-serif-pro:400,600,700" />

<Error></Error>
<main class="container">
    <!-- {#key visibility} -->
        
    <section class="meta">
        <div class="navbar {visibility ? "show" : "hide"}">

            <button class="{visibility ? "show_button" : "hide_button"}" on:click={()=>visibility = !visibility}>hide</button>
            <button class="{visibility ? "show_button" : "hide_button"}" on:click={()=>goto("/")}>Main</button>
            <button class="{visibility ? "show_button" : "hide_button"}" on:click={()=>goto("/dictionnaires")}>Dictionnaires</button>
            <button class="{visibility ? "show_button" : "hide_button"}" on:click={()=>goto("/create")}>Create</button>
            <button class="{visibility ? "show_button" : "hide_button"}" on:click={()=>goto("/profiles/me")}>Profile</button>
            <!-- <button class="{visibility ? "" : "hide_button"}" on:click={()=>goto("/")}>Users</button> -->
        </div>

        <div bind:this={scrollDiv} class="carreaux content">
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

    @keyframes slideout {
        from {
            width: 10%;
            /* margin: 1%;  */
            opacity: 1;
            padding: 1%; 
        }

        50% {
            opacity: 0;
        }

        to {
            width: 1%;
            margin: 0;
            padding: 0;
        }
    }

/* 
        @keyframes slidein {
        from {
            width: 1%;
            margin: 1%; 
            padding: 0; 
        }

        to {
            width: 10%;
            margin: 0;

            opacity: 1;
        }
    } */
    

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
        width: 60%;
        background: #efe7da;
        border: 2px solid #b5a391;
        border-radius: 8px;
        padding: 2rem;
        box-shadow: 6px 6px 0 #b5a391;
        color: #5a5146;
        font-family: "Source Serif Pro", serif;
    }

    .content {
        overflow: scroll;
        width: 98%;
        height:96vh;
        padding: 0;
        margin:0;
        border: #e4e4e4 solid 2px;
        background-color: rgba(250, 248, 243, 0.8);

        border: #cdcdcd solid 2px;
        background-color: #FAF8F3;
        background-image: 
            linear-gradient(#e4e4e4 2px, transparent 2px),
            linear-gradient(90deg, #e4e4e4 2px, transparent 2px),
            linear-gradient(#e4e4e4 1px, transparent 1px),
            linear-gradient(90deg, #e4e4e4 1px, #faf8f3 1px);
        background-size: 100px 100px, 100px 100px, 20px  20px, 20px 20px;
        background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px; 
    
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
        animation-name: slideout;
        width: 1%;
        margin: 0;
        padding: 0;
    }


    .show {
        animation-duration: 1s;
        animation-name: slidein;
        animation-direction: reverse;
        width: 10%;
        padding: 1%;
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