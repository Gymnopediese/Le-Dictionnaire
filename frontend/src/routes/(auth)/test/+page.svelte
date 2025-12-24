<script>
  import { onMount } from 'svelte';
  let textarea;
  let caretX = 0;
  let caretY = 0;
  let ghostDiv;

  function updateCaretPosition() {
    const { selectionStart } = textarea;
    const taStyle = getComputedStyle(textarea);

    // Copier le style si le ghostDiv n'a pas encore été configuré
    if (!ghostDiv.style.font) {
      ghostDiv.style.position = 'absolute';
      ghostDiv.style.visibility = 'hidden';
      ghostDiv.style.whiteSpace = 'pre-wrap';
      ghostDiv.style.wordWrap = 'break-word';
      ghostDiv.style.overflow = 'auto';
      ghostDiv.style.top = '0';
      ghostDiv.style.left = '0';
      ghostDiv.style.padding = taStyle.padding;
      ghostDiv.style.border = taStyle.border;
      ghostDiv.style.font = taStyle.font;
      ghostDiv.style.lineHeight = taStyle.lineHeight;
      ghostDiv.style.letterSpacing = taStyle.letterSpacing;
      ghostDiv.style.width = taStyle.width;
    }

    // Texte avant le curseur
    ghostDiv.textContent = textarea.value.slice(0, selectionStart);

    // Ajouter un span pour mesurer
    let span = ghostDiv.querySelector('span');
    if (!span) {
      span = document.createElement('span');
      ghostDiv.appendChild(span);
    }
    span.textContent = textarea.value.slice(selectionStart) || '.';

    const rect = span.getBoundingClientRect();
    const taRect = textarea.getBoundingClientRect();

    caretX = rect.left - taRect.left + textarea.scrollLeft + 98 ;
    caretY = rect.top - taRect.top + textarea.scrollTop + 7;
  }

  onMount(() => {
    ghostDiv = document.createElement('div');
    document.body.appendChild(ghostDiv);

    textarea.addEventListener('keyup', updateCaretPosition);
    textarea.addEventListener('click', updateCaretPosition);
    textarea.addEventListener('input', updateCaretPosition);
  });
</script>

<textarea bind:this={textarea} rows="5" cols="30" placeholder="Tapez ici..."></textarea>
<p>Position du curseur : X = {caretX.toFixed(0)}, Y = {caretY.toFixed(0)}</p>

  <div
    style="
      position: absolute;
      left: {caretX + 100}px;
      top: {caretY + 20}px;
      width: 2px;
      height: 5px;
      background: black;
      pointer-events: none;
    "
  />