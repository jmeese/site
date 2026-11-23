# Adding a talk

Talks are self-contained [reveal.js](https://revealjs.com/) decks served as static
HTML. The shared theme files live in `reveal-themes/`.

## Steps

1. **Make a folder:** `talks/<slug>/` (e.g. `talks/civic-recommenders/`).
2. **Author the deck** as `talks/<slug>/<slug>.html`. Minimal skeleton:

   ```html
   <!doctype html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>My talk</title>
     <!-- reveal.js core, pinned, from CDN -->
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
     <!-- your theme: External Brain (lavender) or CGT (indigo) -->
     <link rel="stylesheet" href="../reveal-themes/external-brain.css" id="theme">
   </head>
   <body>
     <div class="reveal"><div class="slides">
       <section><h1>Title slide</h1></section>
       <section><h2>Next slide</h2></section>
     </div></div>
     <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
     <script>Reveal.initialize({ hash: true });</script>
   </body>
   </html>
   ```

   Swap `external-brain.css` for `cgt-talk.css` to use the CGT (indigo) theme.
   `reveal-themes/index.html` is a live preview of both themes.

3. **Link it** from `../talks.html` — add one `<li>` inside the list.

## Notes

- Theme fonts (IBM Plex Mono) are bundled in `reveal-themes/fonts/`, so decks render
  the same offline and online.
- reveal.js core is loaded from the CDN at a pinned version — no npm, nothing to build.
- Export to PDF: open the deck with `?print-pdf` appended and use the browser's
  Print → Save as PDF.
