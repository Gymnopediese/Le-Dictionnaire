<script>
    import { goto } from "$app/navigation";


    export var terme;


    async function try_delete_terme()
    {
        var res = await del("/termes/" + terme.id);
        console.log(res);
    }

</script>

<h3 on:click={() => goto("termes/" + terme.id)} >{terme.name}</h3> <button on:click={try_delete_terme}>X</button>
<h4>{terme.type}</h4>
<h4>{terme.genre}</h4>
    <label for="">Definitions:</label><br>
    <ol>
    {#each terme.definitions as definition}
        <li>{definition.contenu}</li>
    {/each}
    </ol>  
    <label for="">Exemple:</label><br>
    <ol>
    {#each terme.exemples as exemple}
        <li>{exemple.contenu}</li>
    {/each}
     </ol>  
    <label for="">Origine:</label><br>
    <ol>
    {#each terme.origines as origine}
        <li>{origine.contenu}</li>
    {/each}
    </ol>  
    <label for="">Note:</label><br>
    <ol>
    {#each terme.notes as note}
        <li>{note.contenu}</li>
    {/each}
    </ol>  
<br>