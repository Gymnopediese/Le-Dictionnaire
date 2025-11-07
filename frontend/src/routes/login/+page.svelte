<script lang="ts">
    import { signin, signup } from "$lib/login";



    var username_signin : String = "";
    var password_signin : String = "";
    var error_signin    : String = "";

    var username_signup : String = "";
    var password_signup : String = "";
    var reapeat_signup  : String = "";
    var error_signup    : String = "";

    async function try_signin() : Promise<void>
    {
        error_signin = ""
        error_signup = ""
        try {
            await signin(username_signin, password_signin)
        }
        catch (error) {
            error_signin = error;
        }
        
    }
    
    async function try_signup() : Promise<void>
    {
        error_signin = ""
        error_signup = ""
        try {
            await signup(username_signup, password_signup, reapeat_signup)
        }
        catch (error) {
            error_signup = error;
        }
    }
    

</script>

<div>
    hello, signe toi mon pote !
    <br>
    <input bind:value={username_signin} type="text" name="username" placeholder="username" id="">
    <br>
    <input bind:value={password_signin} type="password" name="password" placeholder="password" id="">
    <br>
    <button on:click={try_signin}>valider</button>
    <br>
    {#if error_signin}
        <p class="error">{error_signin}</p>
    {/if}

</div>

<br>
<div>
    ta pas de compte ? creer un mon pote !
    <br>
    <input bind:value={username_signup} type="text" placeholder="username" id="">
    <br>
    <input bind:value={password_signup} type="password" placeholder="password" id="">
    <br>
    <input bind:value={reapeat_signup} type="password" placeholder="repeat..." id="">
    <br>
    <button on:click={try_signup}>valider</button>
    {#if error_signup}
        <p class="error">{error_signup}</p>
    {/if}
    <br>
</div>

<style>

    .error {
        color: #ff6060;
    }

</style>

