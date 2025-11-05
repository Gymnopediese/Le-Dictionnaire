<script lang="ts">


    var username_signin : String;
    var password_signin : String;

    var username_signup : String;
    var password_signup : String;
    var reapeat_signup  : String;
    

</script>

<div>
    hello, signe toi mon pote !
    <br>
    <input bind:value={username_signin} type="text" name="username" placeholder="username" id="">
    <br>
    <input bind:value={password_signin} type="password" name="password" placeholder="password" id="">
    <br>
    <button>valider</button>
    <br>
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
    <button>valider</button>
</div>



