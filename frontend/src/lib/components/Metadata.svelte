<script lang="ts">
	import InputChoice from "$lib/components/InputChoice.svelte";
    import DictAddTermePopup from "$lib/popups/DictAddTermePopup.svelte";
    import { onMount } from "svelte";
    import ChooseTerme from "./ChooseTerme.svelte";
    import { goto } from "$app/navigation";
    import { metadatas, view_mode } from "$lib/services/global";
    import RadioButton from "./RadioButton.svelte";
    import Dictionnaires from "./Dictionnaires/Dictionnaires.svelte";
    import Users from "./Users/Users.svelte";
    import { allowed_metadata_types } from "$lib/shared/metadatas";
    import { combineTransactionSteps } from "@tiptap/core";

    

	let metadataPopup   = $state(false);
    var termMode        = $state("text")

	// Chaque entrée = { kind: "context", value: "", ref: HTMLElement/null }

    const listMetadata = ["antonym", "synonym", "example"];
    let addTermPopup = $state(null); // index du champ où on ajoute
    let allowedTermePopup = []
    let newTerm = "";

    function addMetadata(key)
    {
        $metadatas[key].used = true;
        metadataPopup = false;
    }

    function removeMetadata(key)
    {
        $metadatas[key].used = false;
    }

    function AddString()
    {
        if ($metadatas[addTermPopup].data == undefined)
            $metadatas[addTermPopup].data = []
        $metadatas[addTermPopup]["data"] = [{
            "data": newTerm,
            "type": "string"
        },...(metadatas[addTermPopup]["data"] ?? [])]
        addTermPopup = null
        newTerm = ""
    }

    function AddTerme(t)
    {
        if ($metadatas[addTermPopup].data == undefined)
            $metadatas[addTermPopup].data = []
        $metadatas[addTermPopup]["data"] = [{
            "data": t,
            "type": "terme",
        },...($metadatas[addTermPopup]["data"])]
        addTermPopup = null
        newTerm = ""
    }

    function AddDictionnaire(dictinonaire)
    {
        if ($metadatas[addTermPopup].data == undefined)
            $metadatas[addTermPopup].data = []

        $metadatas[addTermPopup]["data"] = [{
            "data": dictinonaire,
            "type": "dictionnaire",
        },...($metadatas[addTermPopup]["data"])]
        addTermPopup = null
        newTerm = ""
    }

    function AddUser(user)
    {
        if ($metadatas[addTermPopup].data == undefined)
            $metadatas[addTermPopup].data = []
    
        $metadatas[addTermPopup]["data"] = [{
            "data": user,
            "type": "user",
        },...($metadatas[addTermPopup]["data"])]
        addTermPopup = null
        newTerm = ""
    }

    document.addEventListener('keydown', (event) => {
        if (event.key == "Escape")
        {
            metadataPopup = false;
            addTermPopup = null
        }
    })
    console.log($metadatas)

    for (let key of Object.keys(allowed_metadata_types))
    {
        if ($metadatas[key])
            continue
        if (!allowed_metadata_types[key].required)
            continue
        console.log("bitch ?")
        $metadatas[key] = allowed_metadata_types[key]
        $metadatas[key]["data"] = allowed_metadata_types[key].default
    }

    console.log($metadatas)


</script>

<div class="metadata_block">

{#each Object.keys(allowed_metadata_types).filter(x => ($metadatas[x])) as key, i}
    {console.log(key)}
	<div class="meta_line">
		<div class="meta_label">{key}</div>
		<!-- CASE: list-based metadata -->
            {#if $metadatas[key].type == "list"}
                <div class="list_box">
                    {#each $metadatas[key].data as item, j}
                        <div class="list_item">
                            {#if item.data}   
                            {#if (item.type) == "string"}
                                <span>{item.data}</span>
                            {:else if (item.type) == "terme"}
                                <button class="terme_link" on:click={()=>{
                                    goto(`/termes/${item.data.id}`);
                                }}><u><i>{item.data.name}</i></u></button>
                            {:else if (item.type) == "user"}
                                {console.log(item)}
                                <button class="terme_link" on:click={()=>{
                                    goto(`/profiles/${item.data.id}`);
                                }}><u><i>{item.data.username}</i></u></button>
                            {:else}
                                <button class="terme_link" on:click={()=>{
                                    goto(`/dictionnaires/${item.data.id}`);
                                }}><u><i>{item.data.name}</i></u></button>
                            {/if}

                            {#if $view_mode == "edit" && !((item.type) == "user" && item.data.rights == "all")}
                                <button class="del_small" on:click={() => {
                                    $metadatas[key].data = $metadatas[key].data.filter((_, x) => x !== j);
                                }}>✕</button>
                            {/if}
                            {/if}
                        </div>
                    {/each}
                    {#if $view_mode == "edit"}
                    <button class="list_add" on:click={() => { 

                            allowedTermePopup = allowed_metadata_types[key].allowed
                            termMode = allowed_metadata_types[key].allowed[0]
                            addTermPopup = key; 
                        }}>
                        + add
                    </button>
                    {/if}
                </div>

            {:else if allowed_metadata_types[key].options && $metadatas[key]}
                <RadioButton options={allowed_metadata_types[key].options} bind:input={$metadatas[key].ref} bind:search={$metadatas[key].data}></RadioButton>

            {:else}
                <!-- DEFAULT INPUTCHOICE -->
                <InputChoice
                    bind:input={$metadatas[key].ref}
                    bind:value={$metadatas[key].data}
                    options={[]}
                    placeholder={key}
                />
            {/if}

		<div class="remove_btn" on:click={() => removeMetadata(key)}>✕</div>
	</div>
{/each}


    {#if $view_mode == "edit"}
	<button class="add_btn" on:click={() => (metadataPopup = true)}>
		+ add metadata
	</button>
    {/if}
</div>


{#if metadataPopup}
	<div class="popup_bg">
		<div class="popup">
			
            <div class="meta_choices">
			{#each Object.keys($metadatas).filter(x => $metadatas[x].used == false || $metadatas[x].used == undefined ) as key}
				<div class="choice" on:click={() => addMetadata(key)}>
                    {key}
				</div>
			{/each}
            </div>
            <button class="close sticky" on:click={() => (metadataPopup = false)}>close</button>

		</div>
	</div>
{/if}
{#if addTermPopup !== null}
	<div class="popup_bg">
		<div class="popup">

			<!-- NAV -->
			<div class="popup_nav">
                {#each allowedTermePopup as allowed, i}
				<div
					class:active={termMode === allowed}
					on:click={() => termMode = allowed}
				>{allowed}</div>
                {/each}

			</div>

			<!-- CONTENT -->
			{#if termMode === "terme"}
				<ChooseTerme onAdd={AddTerme} />
            {:else if termMode === "dictionnaire"}


                <Dictionnaires buttons={
                    [
                        ["add", AddDictionnaire]
                    ]
                } user_id="me" args={`rights_in=write&rights_in=all`} mode="voila"
                filter={(dictionnaire)=> {
                    if ($metadatas[addTermPopup].data == undefined)
                        return true
                    return $metadatas[addTermPopup].data.findIndex((d)=>d.data.name == dictionnaire.name) == -1
                }}
                >


                </Dictionnaires>

            {:else if termMode === "user"}
                <Users user_id="me" args={`relationship_types=${["following"]}`}
                buttons={
                    [
                        ["add", AddUser]
                    ]}
                 filter={(user)=> {
                    if ($metadatas[addTermPopup].data == undefined)
                        return true
                    return $metadatas[addTermPopup].data.findIndex((d)=>d.data.username == user.username) == -1
                }}>

                </Users>
			{:else}
				<input
					class="popup_input"
					bind:value={newTerm}
					placeholder="add…"
					type="text"
				/>

                <div style="display:flex; gap:10px;">
				<button class="close" on:click={() => AddString()}>
					add
				</button>

				<button class="close" on:click={() => {
					newTerm = "";
					addTermPopup = null;
				}}>
					cancel
				</button>
			</div>
			{/if}

			

		</div>
	</div>
{/if}



<!-- {#if addTermPopup !== null}
	<div class="popup_bg">
		<div class="popup">

            <ChooseTerme></ChooseTerme>

			<input
				class="popup_input"
				bind:value={newTerm}
				placeholder="add…"
				type="text"
			/>
			<div style="display:flex; gap:10px;">



				<button class="close" on:click={() => {
					if (newTerm.trim().length > 0) {
						if (!Array.isArray(metadataFields[addTermPopup].value))
							metadataFields[addTermPopup].value = [];

						metadataFields[addTermPopup].value = [
							...metadataFields[addTermPopup].value,
							newTerm.trim()
						];
					}
					newTerm = "";
					addTermPopup = null;
				}}>
					add
				</button>


				<button class="close" on:click={() => {
					newTerm = "";
					addTermPopup = null;
				}}>
					cancel
				</button>
			</div>
		</div>
	</div>
{/if} -->



<style>
	.metadata_block {
		display: flex;
		flex-direction: column;
		gap:0px;
        width: 100%;
        align-items: left;
	}

	.meta_line {
		display: grid;
		grid-template-columns: 20dvh 1fr 36px;
		align-items: center;
	}

	.meta_label {
		font-size:  calc(24 * var(--font-size));;
		color: #a7a299;
	}

	.remove_btn {
		cursor: pointer;
		font-size:  calc(32 * var(--font-size));;
		text-align: center;
	}

	.add_btn {
		font-size:  calc(28 * var(--font-size));;
		border: 1px solid #b8a898;
        background-color: #e3d6c8;
        /* z-index: 100; */
		background: transparent;
		padding:  calc(6 * var(--font-size))  calc(14 * var(--font-size));;
        margin:0;
        margin-right:  calc(10 * var(--font-size));;
		cursor: pointer;
	}

	.popup_bg {
		position: fixed;
		left: 0;
		top: 0;
		width: 100vw;
		height: 100vh;
		background: rgba(0, 0, 0, 0.2);
		display: flex;
		justify-content: center;
		align-items: center;
        z-index: 10;
	}

	.popup {
		background: #fdfcf8;
		border: 2px solid #b8a898;
		padding: 20px;
		width: 80%;
        height: 80%;
		display: flex;
		flex-direction: column;
		gap: 10px;
        z-index: 10;

	}

    .meta_choices {
        overflow: scroll;
        display: flex;
		flex-direction: column;
		gap: 10px;
        z-index: 10;
    }

	.choice {
		padding: 8px;
		border: 1px solid #b8a898;
		cursor: pointer;
	}

	.close {
		margin-top: 10px;
	}
    .sticky {
        position: sticky;
        top: 20px;
    }

.list_box {
    display: flex;
    flex-wrap: wrap;     /* ← makes it horizontal and wrap to next row */
    gap: 6px;
}


.list_item {
	display: inline-flex;
	align-items: center;
	gap: calc(8 * var(--font-size));
	border: 1px solid #b8a898;
	padding: calc(2 * var(--font-size)) calc(8 * var(--font-size));
	border-radius: calc(4 * var(--font-size));
	width: fit-content;
	font-size:  calc(22 * var(--font-size));
	color: #6e6a63;
}

.del_small {
	all: unset;
	cursor: pointer;
	font-size: calc(20 * var(--font-size));
	color: #8b6f6f;
}

.list_add {
	all: unset;
	cursor: pointer;
	font-size: calc(24 * var(--font-size));
	color: #8b6f6f;
	border-bottom: 1px dashed #b8a898;
	width: fit-content;
}

.popup_input {
	all: unset;
	border-bottom: 1px solid #b8a898;
	font-size: 26px;
	margin-bottom: 14px;
}


	.popup_nav {
		display: flex;
		gap: 20px;
		margin-bottom: 16px;
		font-size: 22px;
	}

	.popup_nav div {
		cursor: pointer;
		color: #8b857b;
		border-bottom: 1px solid transparent;
	}

	.popup_nav div.active {
		color: #4a463f;
		border-bottom: 1px solid #b8a898;
	}

    .terme_link {
        all: unset;
        
    }
</style>
