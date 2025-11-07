
<script lang="ts">
    import { goto } from "$app/navigation";


</script>

<ul>
  <li><a on:click={()=>goto("/")}>Main</a></li>
  <li><a on:click={()=>goto("/create")}>Create</a></li>
</ul>

<slot></slot>

<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333333;
}

ul li {
  float: left;
}

ul li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

ul li a:hover {
  background-color: #111111;
}
</style>