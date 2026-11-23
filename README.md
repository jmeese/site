# jmeese/site

Personal academic site — plain static HTML, no Jekyll, no build framework.
Served by GitHub Pages at <https://jmeese.github.io/site/>.

## Files

- `index.html` — home / bio. Hand-edit.
- `talks.html` — talks index. Hand-edit; see `talks/README.md` to add a deck.
- `publications.html` — **generated**, do not hand-edit (it gets overwritten).
- `style.css` — the one stylesheet for every page.
- `data/papers.bib` — source of truth for publications.
- `build_publications.py` — regenerates `publications.html` from the `.bib`.
- `talks/reveal-themes/` — reveal.js themes (External Brain + CGT) for future talks.

## Editing

- **Any page except publications:** open the `.html`, change it, commit, push.
- **Publications:** edit `data/papers.bib`, then:

  ```bash
  python3 build_publications.py
  ```

  Commit both the `.bib` and the regenerated `publications.html`.

## Deploy

GitHub Pages serves the `main` branch root directly (Settings → Pages → Source:
"Deploy from a branch", `main` / `/root`). `.nojekyll` keeps Pages from running
Jekyll over the files. Push to `main` and the live site updates.
