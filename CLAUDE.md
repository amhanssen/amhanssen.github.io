# Portfolio site: notes for Claude

Read this first. It sums up everything done so far, so a new chat can pick up without redoing work.

## About Amanda
- Communication Design student at MassArt (BFA 2023–2027, minor in Business of Creative Industries). Lives between Boston and Laconia, NH.
- Designs in Figma; new to code and Git. Explain in short, plain steps with exact button names.
- Publishes with **GitHub Desktop → Push origin** (the terminal is not signed in to GitHub). Ask before pushing or publishing. Check "Current Repository" says **amhanssen.github.io** first (she also has an Intertwine repo).
- Wants to save credits: keep answers short, batch changes, avoid extra screenshots and re-checks unless something looks off.

## Where things live
- **Live site:** https://amhanssen.github.io (GitHub Pages, public repo `amhanssen/amhanssen.github.io`, branch `main`). Pages can sit in GitHub's queue a few minutes after a push.
- **Site folder:** `~/Documents/GitHub/amhanssen.github.io`
- **Figma:** file `RTCuHNsYRQknTtg1j0gi1X` ("Portfolio"). Page "Portfolio" has Home, About, Personal, all case studies (desktop + phone), the resume frame ("Resume — Letter"), share card, and components (Nav, Footer, Monogram). Page "Archive (removed projects)" has Through Monet, LRMHC and Recipe cards. Figma case studies are the *older, shorter* versions; the website has the detailed ones.
- **Source files:** `~/Desktop/Classes` (class work, ~19 GB), `~/Documents/Portfoilo` (Gator, personal work, photos), old site https://amhanssen.myportfolio.com (week-by-week write-ups).
- **Resume:** `files/resume.html` is the source. Print it to PDF with headless Chrome and copy to `files/Amanda-Hanssen-Resume.pdf` and `~/Documents/Amanda Hanssen Resume.pdf`. Must stay one page with no widows/orphans. Summary is upright DM Sans (she found italic hard to read).

## How the site is built
- Plain HTML/CSS. **All content is in `scripts/build.py`** (PROJECTS list + page functions). Edit there, then run `python3 scripts/build.py`. Never hand-edit the generated `.html` files.
- Case studies use the `"story"` format: a list of blocks (`split`, `images`, `beforeafter`, `system`, `phones`, `phonepanel`, `site`, `steps`, `video`, `reflection`). Images use `img(src, alt, fit, bg, ratio, cap)`; `cap` is the caption.
- `css/style.css` (colors, layout), `js/site.js` (phone menu), `scripts/share-card.html` (renders `images/share.jpg`).
- Preview: `python3 -m http.server 4200` in the folder, then http://localhost:4200. Headless Chrome caches, so use a fresh `--user-data-dir` for screenshots.
- Check before committing: broken links/images, no sideways scroll at 390px wide.

## Design system
- Colors: apricot `#FFEDD5` (bg), paper `#FFF6EA`, ink `#2B0616`, crimson `#470B24`, periwinkle `#B5BEDD`, periwinkle-deep `#4F5B9A`. Headers fade periwinkle → apricot.
- Fonts: Instrument Serif (headings), DM Sans (text). Monogram = crimson "AH" mark, no circle, no name text next to it in the nav.
- Follows her "Beautiful Type Checklist": curly apostrophes, single spaces, no tracking on mixed case, no widows/orphans, en-dashes in ranges.

## Projects (Home order)
Featured: **Intertwine** (marked *In progress*). Then DreamCast, VOWS, The Bench Film Festival, Paws & Pastries, Splash Zone, Gator Graphix. Plus a Personal page (posters, sneakers, characters).
- **Hidden** (`"hidden": True` in build.py): **Droplet** and **Music Box**. Waiting for her images and text. Figma has fill-in pages for both.
- Verified facts: Bench fonts Social Gothic + Paralucent, Pantones 533/468/3546/4975/7544 C. VOWS fonts Elido (sans, wordmark/headlines) + Odile (serif), palette wine/butter/cream/gold/plum, 8 × 9.5 in. Paws fonts Decoy + Almarai. Intertwine fonts Elido (headings) + SF Pro (UI); the guest website uses Alegreya Sans only as a stand-in.

## Still open (ask her)
- Splash Zone: her specific role, Week 3, and "Next time" are still [brackets].
- Reflections on every case study were drafted from her notes; she may want to reword them.
- An unused dark VOWS cover scan: alternate cover or draft?
- 100-logo GIFs (13–15 MB) were left out; she could export them as MP4.
- Custom domain: amandahanssen.com was available (Porkbun suggested); she decided to wait.
- Job search: MVSB said to email mvsbmarketing@mvsb.com about summer 2027 (draft email was written in chat).
