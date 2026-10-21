# Amanda Hanssen — portfolio

Live at **https://amhanssen.github.io** (once published with GitHub Pages).
Designed in the Figma file *Portfolio*.

## How it's built
- Plain HTML and CSS, no build tools needed to view it.
- `scripts/build.py` holds all the words and image lists. It writes `index.html`, `about.html`, `personal.html`, `404.html` and the pages in `work/`.
- `css/style.css` has the colors, fonts and layout. `js/site.js` opens the phone menu.
- Images are in `images/`, the resume is in `files/`.

## Making changes
1. Edit the content in `scripts/build.py` (or ask Claude to).
2. Run `python3 scripts/build.py` in this folder.
3. In GitHub Desktop, commit and click **Push origin**. The site updates in a minute or two.

## Hidden projects
Droplet and Music Box are in `scripts/build.py` with `"hidden": True`. Fill in their content and remove that line to put them on the site.

## Preview on your computer
`python3 -m http.server 4200` in this folder, then open http://localhost:4200
