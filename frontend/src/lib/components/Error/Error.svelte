<script lang="ts">
	import { fade, fly } from "svelte/transition";
    import { errorStore } from "./Error";
</script>

{#if $errorStore}
	<div
		class="error_panel"
		in:fly={{ y: -20, duration: 180 }}
		out:fade={{ duration: 120 }}
	>
		<div class="error_title">Error</div>
		<div class="error_text">
			{$errorStore}
		</div>
	</div>
{/if}

<style>
.error_panel {
	position: fixed;
	top: 20px;
	left: 50%;
	transform: translateX(-50%);
	z-index: 9999;

	min-width: 320px;
	max-width: 520px;

	background: #f8e7e4;
	border: 2px solid #b88c88;
	border-radius: 6px;
	box-shadow: 6px 6px 0px #b88c88;

	padding: 14px 18px;

	font-family: "Source Serif Pro", serif;
	color: #5a2f2f;
}

.error_title {
	font-size: 18px;
	font-weight: bold;
	margin-bottom: 6px;
}

.error_text {
	font-size: 16px;
	line-height: 1.4;
}
</style>
