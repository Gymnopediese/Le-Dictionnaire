<script lang="ts">
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  export let value: string = "";        // text search
  export let selected: string = "";     // selected letter

  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

  // split into 3 rows: 9 / 9 / 8
  const rows: string[][] = [
    letters.slice(0, 9),
    letters.slice(9, 18),
    letters.slice(18, 26)
  ];

  function onInput(e: InputEvent) {
    const v = (e.target as HTMLInputElement).value;
    value = v;
    if (v !== "") selected = "";
    dispatch("input", { value });
  }

  function chooseLetter(l: string) {
    if (selected === l) {
      selected = "";
      dispatch("letter", { letter: null });
    } else {
      selected = l;
      value = "";
      dispatch("letter", { letter: l });
    }
  }
</script>

<div class="filter-panel">
  <input
    class="search"
    placeholder="Rechercher…"
    bind:value
    on:input={onInput}
    aria-label="Recherche"
  />

  <div class="alphabet">
    {#each rows as row}
      <div class="alpha_row">
        {#each row as l}
          <button
            class="letter {selected === l ? 'pressed' : ''}"
            on:click={() => chooseLetter(l)}
            aria-pressed={selected === l}
            title={l}
          >
            {l}
          </button>
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
  :global(:root) {
    --bg: #f4efe7;
    --card: #e8dfd3;
    --border: #b8a898;
    --ink: #4d453d;
    --muted: #7a7065;
    --shadow: #b8a898;
  }

  .filter-panel {
    width: 100%;
    max-width: 760px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    background: linear-gradient(180deg, rgba(255,255,255,0.6), transparent 30%), var(--bg);
    border: 2px solid var(--border);
    border-radius: 10px;
    box-shadow: 6px 6px 0px var(--shadow);
    font-family: "Source Serif Pro", serif;
    color: var(--ink);
  }

  .search {
    all: unset;
    width: 100%;
    padding: 12px 16px;
    font-size: 18px;
    border-radius: 8px;
    border: 2px solid var(--border);
    background: linear-gradient(180deg, #fbf8f4, #f1eadf);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
    color: var(--ink);
  }

  .search::placeholder {
    color: var(--muted);
  }

  .alphabet {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 8px;
    background: transparent;
  }

  .alpha_row {
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    gap: 8px;
  }

  /* last row has 8 letters: center them nicely */
  .alpha_row:nth-child(3) {
    grid-template-columns: repeat(8, 1fr);
    justify-items: center;
  }

  .letter {
    all: unset;
    cursor: pointer;
    user-select: none;

    display: inline-flex;
    justify-content: center;
    align-items: center;

    aspect-ratio: 1 / 1;
    min-width: 44px;
    padding: 8px;

    font-size: 18px;
    line-height: 1;
    color: var(--ink);
    background-color: var(--card);
    border: 2px solid var(--border);
    border-radius: 6px;

    /* drawn / 2D effect */
    box-shadow:
      3px 3px 0px var(--shadow),
      inset 0 1px 0 rgba(255,255,255,0.6);

    transition: transform 0.08s ease, box-shadow 0.08s ease, background-color 0.12s;
  }

  .letter:hover {
    transform: translateY(-2px);
  }

  /* pressed / selected state: looks pushed into the paper */
  .letter.pressed {
    transform: translate(3px, 3px);
    box-shadow:
      0 0 0 rgba(0,0,0,0),
      inset 3px 3px 0 rgba(0,0,0,0.04);
    background: linear-gradient(180deg, #e0d6c8, #ddcfbe);
    border-color: #a99583;
    color: #3f372f;
  }

  /* subtle responsive adjustments */
  @media (max-width: 560px) {
    .alpha_row {
      grid-template-columns: repeat(9, 1fr);
    }
    .alpha_row:nth-child(3) {
      grid-template-columns: repeat(9, 1fr);
    }
    .letter { min-width: 36px; font-size: 16px; }
  }

  @media (max-width: 420px) {
    .filter-panel { padding: 10px; }
    .letter { min-width: 32px; font-size: 14px; }
    .search { padding: 10px 12px; font-size: 16px; }
  }
</style>
