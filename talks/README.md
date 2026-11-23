# Adding a talk

Talks are self-contained [reveal.js](https://revealjs.com/) decks served as static
HTML. The shared theme files live in `reveal-themes/`.

## Steps

1. **Make a folder:** `talks/<slug>/` (e.g. `talks/civic-recommenders/`).
2. **Author the deck** as `talks/<slug>/<slug>.html`. Skeleton below — it loads the
   markdown, highlight, and notes plugins, so you can write slides in Markdown, get
   syntax-highlighted code, and press **S** for speaker view with your notes.

   ```html
   <!doctype html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>My talk</title>
     <!-- reveal.js core, pinned, from CDN -->
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
     <!-- code-highlighting colours for the highlight plugin -->
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/monokai.css">
     <!-- your theme: External Brain (lavender) or CGT (indigo) -->
     <link rel="stylesheet" href="../reveal-themes/external-brain.css" id="theme">
   </head>
   <body>
     <div class="reveal"><div class="slides">

       <!-- Write slides in Markdown. '---' = new slide, 'Note:' = speaker notes. -->
       <section data-markdown>
         <textarea data-template>
           ## Title slide

           A point in **Markdown**.

           Note: Only you see this in speaker view (press S).

           ---

           ## Code slide

           ```python
           print("syntax-highlighted")
           ```
         </textarea>
       </section>

     </div></div>

     <!-- core + the three plugins, all from the same pinned CDN version -->
     <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/markdown/markdown.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/highlight.js"></script>
     <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
     <script>
       Reveal.initialize({
         hash: true,
         plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
       });
     </script>
   </body>
   </html>
   ```

   Swap `external-brain.css` for `cgt-talk.css` to use the CGT (indigo) theme.
   `reveal-themes/index.html` is a live preview of both themes.

3. **Link it** from `../talks.html` — add one `<li>` inside the list.

## Writing in Markdown

- `data-markdown` + the `<textarea data-template>` lets you write the whole deck in
  Markdown inline. `---` starts a new slide, `--` a vertical sub-slide, and a line
  beginning `Note:` becomes speaker notes for that slide.
- Prefer a separate `.md` file? Point at it instead and keep the HTML tiny:

  ```html
  <section data-markdown="slides.md"
           data-separator="^\n---\n"
           data-separator-vertical="^\n--\n"
           data-separator-notes="^Note:"></section>
  ```

## Notes

- **Speaker view:** press **S** in the deck — opens a second window with your notes,
  next slide, and a timer. Needs the notes plugin (included above).
- Theme fonts (IBM Plex Mono) are bundled in `reveal-themes/fonts/`, so decks render
  the same offline and online.
- Everything loads from the CDN at a single pinned version — no npm, nothing to build.
- **Export to PDF:** open the deck with `?print-pdf` appended, then Print → Save as PDF.
