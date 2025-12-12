<script>
    import TermeView from "$lib/components/TermeView.svelte";
    import { allowed_metadata_types } from "$lib/services/global";




</script>

<TermeView terme_object={{
    metadatas:allowed_metadata_types
    }} ></TermeView>