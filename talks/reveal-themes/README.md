# reveal.js themes

Two custom reveal.js themes, each matching an existing James design system.

- **`external-brain.css`** — External Brain look. Catppuccin Latte, lavender accent, all IBM Plex Mono (self-hosted in `fonts/`, renders offline). Sentence-case headings, teal `_` after `h2`.
- **`cgt-talk.css`** — CGT-site "standard talk blue". White ground, ink text, indigo `#2626e6` accent, Fraunces display headings + Schibsted Grotesk body (via Google Fonts — needs network first load).

## Two ways to use these

**A — Built CSS, no build step (`.css`).** Fits a no-npm setup. Copy `external-brain.css` / `cgt-talk.css` into `dist/theme/` of your reveal checkout (and the `fonts/` folder next to `external-brain.css`), then link one. These already contain the compiled template rules.

**B — Sass source, the README way (`.scss`).** Needs the reveal.js dev environment. Copy `external-brain.scss` / `cgt-talk.scss` into `css/theme/`, run `npm run build:styles` → compiles to `dist/theme/*.css`. The `.scss` use Google Fonts (incl. IBM Plex Mono); self-host the woff2 for offline. NOT compile-tested here — structure mirrors reveal's own `white.scss`.

## Use in a deck
Load reveal core, then one theme:
```html
<link rel="stylesheet" href="dist/reveal.css">
<link rel="stylesheet" href="external-brain.css" id="theme">   <!-- or cgt-talk.css -->
```
Standalone: each file sets the `--r-*` variables **and** the rules that consume them, so no built-in base theme is needed.

## Preview
Open `index.html` in a browser (loads reveal 5.1.0 from CDN). Top-right buttons switch between the two themes.

## Theme-specific markup
- **CGT kicker** (uppercase mono label above a title): `<p class="kicker">...</p>`
- **CGT accent word** (indigo inside a heading): `<h1>The <span class="accent">public</span></h1>`

## Notes / deferred
- CGT fonts load from Google Fonts. For a guaranteed-offline deck, self-host the Fraunces + Schibsted Grotesk woff2 and swap the `@import` in `cgt-talk.css` for `@font-face` rules (as External Brain already does).
- "The blue" was read as the CGT site indigo `#2626e6`. If you meant a different blue (e.g. Outlook `#0072C6`), change `--cgt-indigo`.
