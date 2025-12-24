<script lang="ts">
    import { scroll_div ,writing_mode} from "$lib/services/global";
    import { onMount } from "svelte";

    let  {input = $bindable(), value = $bindable(), x, y, fontSize = $bindable() } = $props<{}>()


    let caretPos = $state({ top: 0, left: 0 });
    let input_div;

  function getCaretCoordinates(element, position) {
    const div = document.createElement("div");
    const style = getComputedStyle(element);

    const props = [
      "direction","boxSizing","width","height","overflowX","overflowY",
      "borderTopWidth","borderRightWidth","borderBottomWidth","borderLeftWidth",
      "paddingTop","paddingRight","paddingBottom","paddingLeft",
      "fontStyle","fontVariant","fontWeight","fontStretch","fontSize",
      "fontSizeAdjust","lineHeight","fontFamily","textAlign","textTransform",
      "textIndent","textDecoration","letterSpacing","wordSpacing"
    ];

    props.forEach(prop => div.style[prop] = style[prop]);

    div.style.position = "absolute";
    div.style.visibility = "hidden";
    div.style.whiteSpace = "pre-wrap";
    div.style.wordWrap = "break-word";

    div.textContent = element.value.substring(0, position);

    const span = document.createElement("span");
    span.textContent = "|";
    div.appendChild(span);

    document.body.appendChild(div);

    const spanRect = span.getBoundingClientRect();
    const divRect = div.getBoundingClientRect();
    
    document.body.removeChild(div);
    return {
      top: spanRect.top - divRect.top + element.scrollTop,
      left: spanRect.left - divRect.left + element.scrollLeft
    };
    x = spanRect.left - divRect.left + element.scrollLeft;
    y = spanRect.top - divRect.top + element.scrollTop;
    // resize_input()
    return {
      top: spanRect.top - divRect.top + element.scrollTop,
      left: spanRect.left - divRect.left + element.scrollLeft
    };
  }

  function updateCaret() {
    if (!input) return;
    caretPos = getCaretCoordinates(input, input.selectionStart);
  }

    function resize_input(){
        var content = input;
        if (!content)
        return
        content.value = content.value.trimLeft()
        if (content.value.trim() == "")
            content.value = ""
        while (content.value.length - content.value.trimRight().length > 2)
            content.value = content.value.substring(0, content.value.length - 1)
        
        content.style.height = "auto";           // reset height
        content.style.height = content.scrollHeight + "px";
    }
    function refresh_input()
    {
        var content = input;
        content.addEventListener('input', () => resize_input());
        resize_input()
        // content.style.height = 'auto';
        // content.style.height = content.scrollHeight + 'px';
        // var count = (content.value.match(/\n/g)|| []).length + 1
        // content.style.height = count * 40 + 'px';
        // content.style.height = content.scrollHeight + 'px';
    }
    onMount(()=>{
        updateCaret()
        refresh_input()
    })

    $effect(()=> {
        if (fontSize) resize_input()
        if (value) resize_input()
    })

    function focus_textarea(){
        if (!$scroll_div)
        return
        var child = input_div;
        var new_pos = child.offsetTop + caretPos.top - $scroll_div.clientHeight / 4;
        $scroll_div.scrollTop = new_pos
        $scroll_div.scrollTo({
                    top: new_pos,
                    behavior: 'smooth'
                });
    }

    function writemode(){
        if (!$scroll_div)
            return
        var child = input_div;
        var new_pos = child.offsetTop + caretPos.top - $scroll_div.clientHeight / 2;
        $scroll_div.scrollTop = new_pos
        $scroll_div.scrollTo({
                    top: new_pos,
                    behavior: 'smooth'
                });
    }

    function in_view(){
        if (!$scroll_div)
        return
        var child = input_div;
        var new_pos = child.offsetTop + caretPos.top;
        if (new_pos - $scroll_div.scrollTop > 600)
            new_pos -= $scroll_div.clientHeight * 5 / 6
        else if (new_pos - $scroll_div.scrollTop < 200)
            new_pos -= $scroll_div.clientHeight * 1 / 4
        else
            return
        // if (new_pos - $scroll_div.scrollTop < 100)
        $scroll_div.scrollTop = new_pos
        // else
        //     $scroll_div.scrollTo({
        //                 top: new_pos,
        //                 behavior: 'smooth'
        //             });
        // $scroll_div.scrollTo({
        //             top: new_pos,
        //             behavior: 'smooth'
        //         });
    }

    function defaultmode(){
        if (!$scroll_div)
        return
        var child = input_div;
        var new_pos = child.offsetTop + caretPos.top - $scroll_div.clientHeight * 3 / 4;
        console.log(new_pos - $scroll_div.scrollTop)
        if (new_pos - $scroll_div.scrollTop < 86)
        {
            return
        }
        if (new_pos - $scroll_div.scrollTop < 100)
            $scroll_div.scrollTop = new_pos
        else
            $scroll_div.scrollTo({
                        top: new_pos,
                        behavior: 'smooth'
                    });
    }

  
    function focus()
    {
         requestAnimationFrame(() => {
                updateCaret()   
                in_view()
                // focus_textarea()
             });
    }

    function key_down(e: Event)
    {
        if (e.key == "Tab")
            return
        requestAnimationFrame(() => {
            updateCaret()
            if ($writing_mode)
                writemode()
            else
                in_view()
        })
    }
</script>

<div bind:this={input_div} style="position: relative; width: 100%;">
  <textarea
    on:focus={focus}
    on:keydown={key_down}

    on:input={updateCaret}
    on:click={focus}
    spellcheck="true"
    class="content_input"
    bind:this={input}
    bind:value={value}
    name="contenu"
    id="1"
    placeholder="contenu"
  ></textarea>
  <div
    style="
      position: absolute;
      left: {caretPos.left}px;
      top: {caretPos.top + 8}px;
      width: 2px;
      height: 5px;
      background: black;
      pointer-events: none;
    "
  />
</div>

<style>
  .content_input {
    line-height: calc(100 * var(--font-size));
    all: unset;
    margin-left: calc(75 * var(--font-size));
    margin-bottom: calc(40 * var(--font-size));
    width: calc(100% - 75 * var(--font-size));
    height: calc(40 * var(--font-size));
    font-size: calc(32 * var(--font-size));
    border: none;
    outline: none;
    resize: none;
    overflow: scroll;
    white-space: pre-wrap;
    overflow-wrap: break-word;
  }
</style>
