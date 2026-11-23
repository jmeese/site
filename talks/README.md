# Adding a talk

Talks are self-contained [reveal.js](https://revealjs.com/) decks served as static
HTML. The shared theme files live in `reveal-themes/`.

## Steps

1. **Make a folder:** `talks/<slug>/` (e.g. `talks/civic-recommenders/`).
2. **Author the deck** as `talks/<slug>/index.html` — naming it `index.html` gives a
   clean URL (`/talks/<slug>/`). The skeleton loads the markdown, highlight, and notes
   plugins, so you can write slides in Markdown, get highlighted code, and press **S**
   for speaker view with your notes.

   (The outer block below is fenced with four backticks so the inner ```python example
   displays correctly on GitHub.)

   ````html
   <!doctype html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>My talk</title>
     <!-- reveal.js: reset browser defaults, then core, then code-highlight colours -->
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css">
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/monokai.css">
     <!-- your theme: External Brain (lavender) or CGT (indigo) -->
     <link rel="stylesheet" href="../reveal-themes/external-brain.css" id="theme">
   </head>
   <body>
     <div class="reveal"><div class="slides">

       <!-- Write slides in Markdown. '---' = new slide, 'Note:' = speaker notes.
            Keep every line indented the SAME amount (reveal strips the first line's
            indentation from all lines; mismatched indentation parses wrongly). -->
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
   ````

   Swap `external-brain.css` for `cgt-talk.css` to use the CGT (indigo) theme.
   `reveal-themes/index.html` is a live preview of both themes.

3. **Link it** from `../talks.html` — add one `<li>` inside the list, pointing at the
   folder: `<a href="talks/<slug>/">Talk title</a> — Venue, Year`.

## Writing in Markdown

- The inline `<textarea data-template>` splits horizontal slides on `---` and reads a
  `Note:` line as speaker notes. **Vertical sub-slides (`--`) are off by default** —
  the inline block above does not enable them. To use them, either add
  `data-separator-vertical="^\r?\n--\r?\n"` to the `<section data-markdown>` tag, or
  use the external-file form below (recommended for real talks — it also sidesteps the
  indentation gotcha entirely):

  ```html
  <section data-markdown="slides.md"
           data-separator="^\r?\n---\r?\n"
           data-separator-vertical="^\r?\n--\r?\n"
           data-separator-notes="^Note:"></section>
  ```

  (The `\r?\n` in each pattern matches both Unix and Windows line endings.)

## Notes

- **Speaker view:** press **S** in the deck — a second window with your notes, the next
  slide, and a timer. Needs the notes plugin (included above).
- **Needs internet.** reveal.js and its plugins load from the CDN, so a deck will not
  render offline — only the theme fonts are bundled locally. For a venue, either
  self-host reveal (drop its `dist/` + `plugin/` files into the repo) or keep a **PDF
  backup**.
- **Export to PDF:** open the deck with `?print-pdf` appended, then Print → Save as PDF.
