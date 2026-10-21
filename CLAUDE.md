# Portfolio site: notes for Claude

Amanda Hanssen's portfolio (MassArt Communication Design student). She designs in Figma and is new to code; explain in short, plain steps. She publishes with **GitHub Desktop → Push origin** (the terminal isn't signed in to GitHub). Ask before pushing or publishing.

- Design source: Figma file `RTCuHNsYRQknTtg1j0gi1X` ("Portfolio"). Removed projects live on its "Archive (removed projects)" page.
- Site: plain HTML/CSS. All content is in `scripts/build.py`; edit there, then run `python3 scripts/build.py`. Don't hand-edit the generated `.html` files.
- Colors: apricot #FFEDD5 (bg), crimson #470B24, periwinkle #B5BEDD, ink #2B0616. Fonts: Instrument Serif + DM Sans (Google Fonts).
- Droplet and Music Box are `"hidden": True` until she sends images and text.
- The Intertwine guest site is a separate repo published at /Intertwine/.
- Preview: `python3 -m http.server 4200`, then http://localhost:4200.
