#!/usr/bin/env python3
"""Builds every page of Amanda Hanssen's portfolio from the content below.

Run it from the repository folder:  python3 scripts/build.py
It writes index.html, about.html, personal.html, 404.html and work/*.html.
To change words or images, edit the content in this file and run it again.
A project with "hidden": True is left off the site (no page, no link).
"""
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://amhanssen.github.io"
EMAIL = "amandahanssen04@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/amanda-hanssen-8711a0237/"
INSTAGRAM = "https://www.instagram.com/reidlinmae/"
RESUME = "files/Amanda-Hanssen-Resume.pdf"
GUEST_SITE = "https://amhanssen.github.io/Intertwine/?invite=demo-rosa"


def img(src, alt, fit=False, bg=None, ratio=None, cap=None):
    return {"src": src, "alt": alt, "fit": fit, "bg": bg, "ratio": ratio, "cap": cap}


# ---------------------------------------------------------------- projects
# Order here is the order on the Home page and the "Next project" chain.
PROJECTS = [
  {
    "slug": "intertwine", "title": "Intertwine", "year": "2026", "layout": "intertwine", "featured": True,
    "tags": "iOS app · Website · Brand",
    "summary": "One wedding, in one place: an iPhone app where couples plan events, guests and a registry, and a website where every guest RSVPs with a personal link. Designed and built from research to working code.",
    "cover_phones": ["images/intertwine/o7-home.jpg", "images/intertwine/gh1-guesthome.jpg"],
    "eyebrow": "Case study · iOS app & website · 2026",
    "intro": "One wedding, in one place. An iPhone app where couples plan events, guests and a registry, and a website where each guest opens a personal invite link: no app or account needed.",
    "facts": [("My role", "Research, UX/UI, brand, and building the app and website"), ("Timeline", "Fall 2026"),
              ("Course", "Everyday Enhancements, Module 3 · MassArt"), ("Tools", "Figma, SwiftUI, HTML/CSS/JS, Supabase")],
  },
  {
    "slug": "dreamcast", "title": "DreamCast", "year": "2025",
    "tags": "App concept · UX/UI · Motion",
    "summary": "A Headspace feature that helps you fall asleep and remember your dreams. Personas, journey maps, storyboards, the interface and a motion video, made over seven weeks.",
    "cover": img("images/dreamcast/cover.jpg", "DreamCast on an iPhone lock screen", fit=True, bg="ink"),
    "eyebrow": "Case study · App concept · 2025",
    "intro": "A Headspace feature that helps people fall asleep, remember their dreams and explore their subconscious in a mindful way.",
    "facts": [("My role", "Personas, user stories, wireframes, journey map, storyboards, interface and video"),
              ("Timeline", "7 weeks · Fall 2025"), ("Course", "Information Architecture, with Martha Rettig"),
              ("Tools", "Figma, After Effects, Google Suite")],
    "hero": [img("images/dreamcast/cover.jpg", "DreamCast notification on an iPhone", fit=True, bg="ink", ratio="1280/620")],
    "idea": ("The idea", "What if your sleep app helped you remember your dreams, too?",
             "Headspace already helps people wind down. DreamCast adds a bedtime story that eases you to sleep and a gentle morning log, so you can capture a dream before it fades and get suggestions based on what you remember."),
    "feature": {"title": "Two personas, one happy path", "label": "Who it's for", "cards": [
        {"k": "College student", "t": "Flora", "d": "Balancing school stress and sleep. Wants to fall asleep faster and remember her dreams.", "hi": True},
        {"k": "Fairy guardian of the Dream Portal", "t": "Maya", "d": "The playful guide who greets Flora each night and carries her into the story."}]},
    "process": {"title": "Seven weeks, from a dream to a video.", "steps": [
        ("Weeks 2–3", "Concept", "Settled on dreams and wrote the personas."),
        ("Week 4", "Journey map", "Mapped the happy path and cut features down to Flora's needs."),
        ("Week 5", "Storyboards", "Script, storyboards and a second interface draft that fits Headspace."),
        ("Week 6", "First video", "Bedtime flow: notification, story, dreaming, morning log."),
        ("Week 7", "Polish", "Pacing, color and readability, checked against Flora's goals.")]},
    "outcome": {"quote": "“Refining ideas through research and iteration made something more focused and meaningful.”",
                "body": "The final pieces were a polished interface and a video of the full bedtime flow. The biggest lesson: balancing creativity with simplicity, on a deadline.",
                "video": {"src": "videos/dreamcast.mp4", "poster": "images/dreamcast/video-poster.jpg", "caption": "The final DreamCast video: the full bedtime flow, from notification to morning log. 1 min 12 s."}},
  },
  {
    "slug": "droplet", "title": "Droplet", "year": "", "hidden": True,
    "tags": "", "summary": "", "cover": None,
  },
  {
    "slug": "vows", "title": "VOWS", "year": "2026",
    "tags": "Editorial · Typography · Web",
    "summary": "A magazine about nontraditional weddings, later turned into an interactive website.",
    "cover": img("images/vows/cover.jpg", "VOWS wordmark"),
    "eyebrow": "Case study · Editorial design · 2026",
    "intro": "A magazine about modern, nontraditional weddings for Gen Z and women in their 20s and 30s, later rebuilt as an interactive website.",
    "facts": [("My role", "Editorial design, typography, layout and web design"), ("Timeline", "10 weeks · Spring 2026"),
              ("Course", "Typography III & Information Architecture, with Katherine Hughes & Rita Ferreira"),
              ("Tools", "Figma, InDesign, Illustrator, Photoshop")],
    "hero": [img("images/vows/front-cover.jpg", "VOWS front cover", fit=True, bg="paper", ratio="628/620"),
             img("images/vows/back-cover.jpg", "VOWS back cover", fit=True, bg="paper", ratio="628/620")],
    "idea": ("The idea", "Bridal magazines sell one idea of a perfect wedding. VOWS shows the rest.",
             "Five keywords guided every choice: nontraditional, editorial, bold, playful and expressive. Instead of luxury and perfection, the stories cover real couples, real budgets and real-life celebrations."),
    "feature": {"title": "Print first, then screen", "label": "Two formats", "ratio": "628/460", "cards": [
        {"k": "Print", "t": "An 8 × 9.5 in magazine", "d": "Cover, spine, front matter, features, an interview, a visual essay and departments, printed and bound by hand.",
         "img": img("images/vows/spread.jpg", "Rainy Days Aren't Bad Luck spread", fit=True, bg="paper")},
        {"k": "Web", "t": "An interactive website", "d": "Seven pages with scroll-paced storytelling, full-bleed images, oversized pull quotes and a lace motif.",
         "img": img("images/vows/web/home.jpg", "VOWS website home page", bg="paper")}]},
    "gallery": {"title": "Inside the website", "label": "Web pages", "images": [
        img("images/vows/web/issue.jpg", "VOWS issue landing page", ratio="410/560"),
        img("images/vows/web/feature.jpg", "VOWS feature article page", ratio="410/560"),
        img("images/vows/web/visual-essay.jpg", "VOWS visual essay page", ratio="410/560")]},
    "process": {"title": "Ten weeks, two formats.", "steps": [
        ("Week 1", "Direction", "Theme, audience, keywords and a flexible grid."),
        ("Week 2", "Type", "Type galleys comparing headlines, body text and captions."),
        ("Week 3", "Resize", "Critique moved the format from 10 × 13 to a more intimate 8 × 9.5 in."),
        ("Weeks 4–5", "Production", "Full text, front matter, cover and spine; printed, bound and trimmed."),
        ("Weeks 6–10", "Website", "Sitemap, wireframes, then scroll-based storytelling.")],
        "images": [img("images/vows/type.jpg", "Type exploration", fit=True, bg="apricot", ratio="628/460"),
                   img("images/vows/early-spread.jpg", "Early spread", fit=True, bg="apricot", ratio="628/460")]},
    "outcome": {"quote": "Smaller felt more intimate and personal. The format changes how a story reads.",
                "body": "VOWS became one complete system instead of separate layouts. Moving it to the screen meant rethinking pacing, scale and readability for long stories.",
                "images": [img("images/vows/editors-letter.jpg", "Editor's letter spread", fit=True, bg="paper", ratio="628/440"),
                           img("images/vows/feature.jpg", "Are You Drowning in Love? spread", fit=True, bg="paper", ratio="628/440")]},
  },
  {
    "slug": "the-bench", "title": "The Bench Film Festival", "year": "2025",
    "tags": "Brand identity · Print",
    "summary": "Identity, a 24-page program and a poster for a festival of true crime and documentary film.",
    "cover": img("images/bench/cover.jpg", "The Bench festival program, tickets and envelope"),
    "eyebrow": "Case study · Brand identity · 2025",
    "intro": "An identity for a new film festival of true crime, documentary and psychological drama, designed as a study of judgment and truth.",
    "facts": [("My role", "Concept, naming, identity, 24-page program, poster and digital applications"), ("Timeline", "6 weeks · Fall 2025"),
              ("Course", "Graphic Design 2: Making Meaning, with Joe Quackenbush"), ("Tools", "Illustrator, InDesign, Photoshop, Figma")],
    "hero": [img("images/bench/applications.jpg", "The Bench brand applications title card", fit=True, bg="ink", ratio="1280/620")],
    "story": [
      {"type": "split", "label": "The brief", "heading": "Invent a film festival, then give it a voice.",
       "body": ["Graphic Design 2 asked us to create a festival from scratch: a name, a mission, a lineup, a visual identity and a printed program. I chose the space where true crime, documentary and psychological drama meet.",
                "My mission statement: to show how true stories can be cinematic, emotional and thoughtful, beyond just headlines. The audience: film fans, true-crime fans, justice-minded viewers and curious people who want more than the sensational version."]},
      {"type": "images", "title": "Research", "label": "Week 1", "cols": 3,
       "intro": "I looked at three existing festivals (the UK’s True Crime Film Festival, True Crime Fest in Europe and the Toronto True Crime Film Festival), curated a 15-film lineup, and made three moodboards to test different moods.",
       "images": [img("images/bench/moodboard-1.jpg", "Moodboard 1", ratio="16/9", cap="Moodboard I: crime-scene evidence, case files and a red-and-black thriller mood."),
                  img("images/bench/moodboard-2.jpg", "Moodboard 2", ratio="16/9", cap="Moodboard II: bold editorial illustration with a bit of satire."),
                  img("images/bench/moodboard-3.jpg", "Moodboard 3", ratio="16/9", cap="Moodboard III: the courtroom, with gavels, scales and Lady Justice. This one became the final direction.")]},
      {"type": "images", "cols": 1,
       "images": [img("images/bench/lineup.jpg", "Proposed film lineup", ratio="16/9", cap="The proposed lineup, from Boston Strangler and Girl in the Basement to The Alabama Solution and The Truth vs. Alex Jones.")]},
      {"type": "beforeafter", "title": "From The Evidence Room to The Bench", "label": "Weeks 1–5",
       "intro": "My first concept, The Evidence Room, leaned on crime-scene clichés: black, red, police tape and case files. After critique, I reset the whole idea around the courtroom. The festival became less about the crime and more about judgment.",
       "before": img("images/bench/evidence-room.jpg", "The Evidence Room title slide", ratio="16/9", cap="Week 1: The Evidence Room, a stark white sans on black with a forensic red line."),
       "after": img("images/bench/final-cover.jpg", "The Bench final program cover", fit=True, bg="paper", ratio="16/9", cap="Week 6: The Bench, with navy, aged cream and a hand-drawn scale."),
       "notes": ["The name moved from the crime to the verdict. The bench is where a judge sits, and where the audience sits to watch.",
                 "Red went from blood to a single accent. Navy and cream took over to feel institutional and trustworthy.",
                 "The scale replaced crime-scene imagery and doubles as the wordmark, with “The” and “Bench” resting in its two pans."]},
      {"type": "images", "title": "Finding the mark", "label": "Weeks 2–3", "cols": 2,
       "intro": "I drew 100 wordmark variations, exploring redacted and forensic letterforms, then refined three directions in Illustrator so they’d hold up from a ticket stub to a poster.",
       "images": [img("images/bench/draft-logo.jpg", "Early hand-drawn wordmark", fit=True, bg="paper", ratio="4/3", cap="An early hand-drawn wordmark: playful, but too light for the subject."),
                  img("images/bench/logo-colors.jpg", "Final scale mark in four colors", fit=True, bg="paper", ratio="4/3", cap="The final scale mark, tested in the brand colors.")]},
      {"type": "system", "title": "The system", "label": "Design decisions",
       "intro": "Every choice points back to one idea, a formal judicial dossier: authoritative colors, document-like paper and type that reads like a court transcript.",
       "colors": [("Pantone 533 C", "#263854", "Primary: authority"), ("Pantone 468 C", "#E7DDCD", "Aged document cream"),
                  ("Pantone 3546 C", "#C63430", "Accent: tension, used sparingly"), ("Pantone 4975 C", "#4D3D3D", "Deep shadow"), ("Pantone 7544 C", "#ABB0BB", "Secondary type")],
       "type_faces": [("Display", "Social Gothic", "Condensed, slightly rough capitals that feel stamped and urgent, for titles and the wordmark."),
                      ("Text", "Paralucent", "A clean, geometric sans for synopses, schedules and credits, like a court transcript.")],
       "images": [img("images/bench/colors.jpg", "Scale mark in the five Pantone colors", fit=True, bg="paper", ratio="4/3", cap="The scale mark in all five Pantone colors."),
                  img("images/bench/patterns.jpg", "Gavel and column patterns", ratio="4/3", cap="Gavel and column patterns, used as borders across every piece.")]},
      {"type": "beforeafter", "title": "Reworking the program", "label": "Weeks 3–6",
       "intro": "The program had to hold a lot: 15 films, three days, synopses, ratings, quotes and showtimes. My first drafts were loud; the final version is calmer, so the information can do the work.",
       "before": img("images/bench/draft-program.jpg", "First program draft", fit=True, bg="paper", ratio="16/10", cap="First draft: red, white and blue film pages with heavy headers."),
       "after": img("images/bench/spread-day2.jpg", "Final program spread", fit=True, bg="paper", ratio="16/10", cap="Final spread: cream pages, gavel borders and a steady grid."),
       "notes": ["Moved from loud patriotic colors to the courtroom palette.",
                 "Built one grid so stills, synopses, ratings and showtimes sit in the same place on every page.",
                 "Added the gavel border so every page reads as part of one dossier."]},
      {"type": "images", "title": "The 24-page program", "label": "Final", "cols": 3,
       "images": [img("images/bench/spread-mission.jpg", "Mission and schedule spread", fit=True, bg="paper", ratio="16/10", cap="The mission and the three-day schedule."),
                  img("images/bench/spread-venue.jpg", "Opening day spread with venue map", fit=True, bg="paper", ratio="16/10", cap="Opening day, with a map of the venue."),
                  img("images/bench/spread-day3.jpg", "Day 3 film spread", fit=True, bg="paper", ratio="16/10", cap="Day 3: each spread pairs two films with stills, quotes and details.")]},
      {"type": "steps", "heading": "Six weeks, one verdict.", "steps": [
        ("Week 1", "Discovery", "Mission, visual thesis, 15-film lineup and three moodboards."),
        ("Week 2", "Identity", "100 wordmarks exploring redacted and forensic letterforms."),
        ("Weeks 3–4", "Refine", "Three logo directions refined and 10 program sketches."),
        ("Week 5", "Reset", "A new concept built around judgment and the courtroom."),
        ("Week 6", "Synthesis", "Grid, gavel borders and the scale icon across every touchpoint.")]},
      {"type": "images", "title": "Brand applications", "label": "Print & digital", "cols": 3,
       "images": [img("images/bench/newspaper-layout.jpg", "Newspaper ad layout", ratio="4/3", cap="A newspaper ad: “Take your seat at the bench.”"),
                  img("images/bench/bus-shelter.jpg", "Posters in a bus shelter", ratio="4/3", cap="Posters in a bus shelter."),
                  img("images/bench/posters.jpg", "Poster series", ratio="4/3", cap="A poster series pairing film stills with the festival’s lines."),
                  img("images/bench/web.jpg", "Website screens", ratio="4/3", cap="Website screens for tickets and the lineup."),
                  img("images/bench/notebook.jpg", "Notebook with gavel pattern", ratio="4/3", cap="A notebook wrapped in the gavel pattern."),
                  img("images/bench/tickets.jpg", "Festival tickets", ratio="4/3", cap="Tickets for each festival day.")]},
      {"type": "video", "title": "Breathe in", "label": "Motion",
       "src": "videos/bench-breathing.mp4", "poster": "images/bench/breathing-poster.jpg",
       "cap": "A calming motion piece built from the gavel pattern, for screens between films. 1 min."},
      {"type": "images", "title": "Printed and assembled", "label": "Physical deliverables", "cols": 3,
       "images": [img("images/bench/photo-envelope.jpg", "Printed program, envelope and tickets", ratio="4/3", cap="The printed program, envelope and tickets."),
                  img("images/bench/photo-spread.jpg", "Inside the printed program", ratio="4/3", cap="Inside the printed program."),
                  img("images/bench/photo-newspaper.jpg", "Printed newspaper ad", ratio="4/3", cap="The printed newspaper ad.")]},
      {"type": "reflection", "quote": "“Beyond the headlines, just seeking truth through cinema.”", "points": [
        ("What worked", "Resetting the concept in week 5 was scary, but it gave every piece one clear idea, judgment, and after that each decision got easier."),
        ("What I learned", "A strong metaphor does more than a strong image. The scale, the bench and the gavel all point back to the same question."),
        ("Next time", "I’d test my concept on people earlier, before spending weeks on a direction, and push the website further.")]},
    ],
  },
  {
    "slug": "paws-pastries", "title": "Paws & Pastries", "year": "2025",
    "tags": "Brand identity · Print",
    "summary": "A warm, playful identity for a dog-friendly café: logo, menus and a 24 × 36 in poster.",
    "cover": img("images/paws/cover.jpg", "Paws & Pastries bone-shaped logo"),
    "eyebrow": "Case study · Brand identity · 2025",
    "intro": "A brand for a dog-friendly café with treats for people and pups: name, logo, menus and a 24 × 36 in poster.",
    "facts": [("My role", "Brand strategy, logo, type system, menus and poster"), ("Timeline", "7 weeks · Fall 2025"),
              ("Course", "Graphic Design 2: Making Meaning, with Joe Quackenbush"), ("Tools", "Figma, Illustrator, Adobe Suite")],
    "hero": [img("images/paws/mark.jpg", "Paws & Pastries brand mark", ratio="1280/620")],
    "idea": ("The idea", "Start with food memories, end with a bone.",
             "Mind maps around food memories led to a brand trueline, customer and employee personas and two moodboards. From there, the name and a warm, playful direction took shape."),
    "feature": {"title": "From 100 marks to one", "label": "Logo process", "ratio": "410/340", "cards": [
        {"k": "Weeks 2–3", "t": "100 sketches, 10 refined", "d": "From 100 quick marks to the ten strongest, redrawn in Illustrator.", "img": img("images/paws/refined-logos.gif", "Animation cycling through the ten refined Paws & Pastries logos", fit=True, bg="paper")},
        {"k": "Week 4", "t": "Dual lockup", "d": "One final mark in horizontal and stacked versions, tested in positive and negative.", "img": img("images/paws/lockup.jpg", "Round logo lockup", fit=True, bg="paper")},
        {"k": "Week 5", "t": "Two menus", "d": "A type system and patterns drawn from the logo's shapes, set in black and white first.", "img": img("images/paws/menu.jpg", "Pup treats menu", fit=True, bg="paper")}]},
    "process": {"title": "Seven weeks, from memory to menu.", "steps": [
        ("Week 1", "Strategy", "Mind maps, trueline, personas and two moodboards."),
        ("Week 2", "Explore", "100 logo marks and a type run of the name."),
        ("Week 3", "Refine", "Ten marks drawn in Illustrator and tested at every size."),
        ("Weeks 4–5", "System", "Lockups, menus, patterns and graphic elements."),
        ("Weeks 6–7", "Make", "A 24 × 36 in poster and physical menus.")],
        "images": [img("images/paws/poster.jpg", "Brand system poster", fit=True, bg="apricot", ratio="628/560"),
                   img("images/paws/menus-photo.jpg", "Printed bone-shaped menus", ratio="628/560")]},
    "outcome": {"quote": "“Move past first-thought solutions.”",
                "body": "A complete brand system, from the first mind map to menus you can hold, presented as one visual story."},
  },
  {
    "slug": "splash-zone", "title": "Splash Zone", "year": "2026",
    "tags": "Typography · Installation",
    "summary": "Vinyl lettering that turns a campus bathroom into a playful, slightly uncomfortable experience.",
    "cover": img("images/splash/cover.jpg", "Blue vinyl lettering on bathroom tiles"),
    "eyebrow": "Case study · Typography installation · 2026",
    "intro": "Vinyl type in a campus bathroom that turns an everyday room into a playful, slightly uncomfortable experience.",
    "facts": [("My role", "Team project: concept, mockups and installation"), ("Timeline", "4 weeks · Spring 2026"),
              ("Course", "Typography III, with Katherine Hughes"), ("Tools", "Figma, Illustrator, Photoshop, Procreate")],
    "hero": [img("images/splash/install.jpg", "Splash Zone installation", ratio="1280/620")],
    "idea": ("The idea", "What happens to type when you can walk into it?",
             "Our team walked around campus looking for places with a strong mood or an interesting way people use them. The bathroom won: an everyday, private space where letters splashing across the tiles feel funny and a little too close."),
    "feature": {"title": "Three concepts, one pick", "label": "Week 1", "cards": [
        {"k": "Chosen", "t": "Splash Zone", "d": "Water-drop letters spreading across a bathroom's walls.", "hi": True},
        {"k": "Concept 2", "t": "Don't Spiral", "d": "A circular window piece about anxiety."},
        {"k": "Concept 3", "t": "Sunshine", "d": "A warmer installation for a student lounge."}]},
    "process": {"title": "From mood board to tile wall.", "steps": [
        ("Week 1", "Research", "Scouting spaces, three concepts, mood boards and mockups."),
        ("Week 2", "Test", "Full-scale mockups to test placement, scale and vinyl."),
        ("Week 4", "Install", "The final vinyl installation in the bathroom.")],
        "images": [img("images/splash/mockup.jpg", "Splash Zone wall mockup", fit=True, bg="apricot", ratio="628/520"),
                   img("images/splash/tests.jpg", "Placement tests", fit=True, bg="apricot", ratio="628/520")]},
    "outcome": {"quote": "“It really shifted how I think about type.”",
                "body": "Type became something to experience, not just read. Splash Zone was chosen for its playful tone, its tie to the space and the way it surrounds you.",
                "images": [img("images/splash/team.jpg", "The team in the finished installation", ratio="410/460"),
                           img("images/splash/wall.jpg", "Mockup on the wall", ratio="410/460"),
                           img("images/splash/installed.jpg", "Installed lettering", ratio="410/460")]},
  },
  {
    "slug": "gator-graphix", "title": "Gator Graphix", "year": "2024–2025",
    "tags": "Client work · Signs · Boat graphics",
    "summary": "Boat lettering, signs and banners for clients around Lake Winnipesaukee, designed and installed over two summers.",
    "cover": img("images/gator/lake.jpg", "Carved Lake Winnipesaukee sign"),
    "eyebrow": "Case study · Client work · 2024–2025",
    "intro": "Two summers as graphic designer and manager at a sign shop in Laconia, New Hampshire, making custom boat graphics, signs and banners for local businesses and boat owners.",
    "facts": [("My role", "Graphic designer & manager"), ("Timeline", "Summers 2024–2025"),
              ("Where", "Gator Graphix · Laconia, NH"), ("Tools", "Adobe Illustrator, print and vinyl equipment")],
    "hero": [img("images/gator/install2.jpg", "Twin Engines boat lettering", ratio="628/620"),
             img("images/gator/install3.jpg", "Gracie-Mae transom graphics", ratio="628/620")],
    "idea": ("The job", "Real clients, real boats, real deadlines.",
             "Every job started with a conversation. I met one on one with customers to turn their ideas into designs, then produced and installed them, from boat names to business signs and banners."),
    "feature": {"title": "Boat graphics", "label": "On the water", "ratio": "410/440", "cards": [
        {"k": "Names", "t": "Transom lettering", "d": "Custom names sized and spaced to read from the dock.", "img": img("images/gator/install1.jpg", "Weak Moment transom lettering")},
        {"k": "Decks", "t": "Deck graphics", "d": "Script names cut in vinyl and laid onto the deck.", "img": img("images/gator/install5.jpg", "Hang On Stoopy deck graphic")},
        {"k": "Hulls", "t": "Hull graphics", "d": "Large graphics designed to fit the curve of the hull.", "img": img("images/gator/install6.jpg", "Blue boat with hull graphics")}]},
    "process": {"title": "From conversation to install.", "steps": [
        ("Step 1", "Meet", "Talk through the idea, size and budget with the client."),
        ("Step 2", "Design", "Draft options in Illustrator and refine them together."),
        ("Step 3", "Produce", "Print or cut the vinyl and prep the materials."),
        ("Step 4", "Install", "Apply the graphics on site, from boats to trailers.")],
        "images": [img("images/gator/pool.jpg", "Pool closed sign", ratio="410/560"),
                   img("images/gator/signage.jpg", "Lady Liberty's shop signage", ratio="410/560"),
                   img("images/gator/trailer.jpg", "Landscaping trailer graphics", ratio="410/560")]},
    "outcome": {"quote": "Designing for a real customer means listening first.",
                "body": "Beyond boats: signs for the Long Bay Garden Club and Rourke Fine Home Building, a Lake Winnipesaukee sign, plus shirts and banners.",
                "images": [img("images/gator/lake.jpg", "Lake Winnipesaukee sign", ratio="410/380"),
                           img("images/gator/garden.jpg", "Long Bay Garden Club sign", fit=True, bg="paper", ratio="410/380"),
                           img("images/gator/sign.jpg", "Rourke Fine Home Building sign", ratio="410/380")]},
  },
  {
    "slug": "music-box", "title": "Music Box", "year": "", "hidden": True,
    "tags": "", "summary": "", "cover": None,
  },
]

VISIBLE = [p for p in PROJECTS if not p.get("hidden")]


# ---------------------------------------------------------------- layout
def head(title, desc, r, image="images/share.jpg", path=""):
    full = "Amanda Hanssen" if title == "Home" else f"{title} · Amanda Hanssen"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(full)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{SITE_URL}/{image}">
<meta property="og:url" content="{SITE_URL}/{path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{r}images/monogram.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/style.css">
<script src="{r}js/site.js" defer></script>
</head>
<body>
"""


def nav(r, current=""):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{r}{href}"{cur}>{label}</a></li>'
    return f"""<header class="wrap nav">
  <a class="brand" href="{r}index.html" aria-label="Amanda Hanssen, home"><span class="monogram" aria-hidden="true"></span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
  <ul class="nav-links" id="menu">
    {a("index.html#work", "Work", "work")}
    {a("personal.html", "Personal", "personal")}
    {a("about.html", "About", "about")}
    <li><a href="{r}{RESUME}" target="_blank" rel="noopener">Resume</a></li>
    <li><a class="btn" href="mailto:{EMAIL}">Get in touch</a></li>
  </ul>
</header>
"""


def footer(r):
    return f"""<footer>
  <div class="wrap">
    <div class="foot-top">
      <p class="display-xl">Let's make something <em>together.</em></p>
      <ul class="foot-links">
        <li><a href="mailto:{EMAIL}">{EMAIL}&nbsp; ↗</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn&nbsp; ↗</a></li>
        <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram&nbsp; ↗</a></li>
        <li><a href="{r}{RESUME}" target="_blank" rel="noopener">Resume (PDF)&nbsp; ↗</a></li>
      </ul>
    </div>
    <div class="foot-bottom body-s"><span>© 2026 Amanda Hanssen</span><a href="#top">Back to top&nbsp; ↑</a></div>
  </div>
</footer>
</body>
</html>
"""


def figure(i, r, extra=""):
    cls = " ".join(c for c in ["fit" if i["fit"] else "", f"on-{i['bg']}" if i["bg"] else "", extra] if c)
    style = f' style="aspect-ratio:{i["ratio"]}"' if i.get("ratio") else ""
    bg = ' style="background:var(--apricot)"' if i.get("bg") == "apricot" else ""
    if bg and style:
        style = style[:-1] + ';background:var(--apricot)"'
    elif bg:
        style = bg
    return f'<figure class="{cls}"{style}><img src="{r}{i["src"]}" alt="{escape(i["alt"])}" loading="lazy"></figure>'


def cover(p, r):
    if p.get("cover_phones"):
        phones = "".join(f'<div class="phone"><img src="{r}{s}" alt="" loading="lazy"></div>' for s in p["cover_phones"])
        return f'<div class="cover phones" role="img" aria-label="Intertwine app screens">{phones}</div>'
    c = p["cover"]
    cls = "cover" + (" fit" if c["fit"] else "") + (f" on-{c['bg']}" if c["bg"] else "")
    return f'<div class="{cls}"><img src="{r}{c["src"]}" alt="{escape(c["alt"])}" loading="lazy"></div>'


# ---------------------------------------------------------------- pages
def page_home():
    r = ""
    feat = next(p for p in VISIBLE if p.get("featured"))
    rows = [p for p in VISIBLE if not p.get("featured")]
    html = head("Home", "Amanda Hanssen is a Communication Design student at MassArt designing brands, apps and spaces.", r)
    html += f'<div class="sky" id="top">{nav(r)}'
    html += f"""<section class="wrap hero">
  <p class="label muted eyebrow">Communication design · MassArt, Boston</p>
  <h1 class="display-xl">Designing everyday things that feel <em class="accent">personal.</em></h1>
  <div class="hero-row">
    <p class="body-l">I'm Amanda, a design student at MassArt. I make brands, apps and spaces, from a café identity to a wedding app for couples and their guests.</p>
    <div class="latest"><p class="label muted">Currently</p><p>Looking for design and marketing internships for summer 2027.</p></div>
  </div>
</section></div>
<section class="wrap">
  <a class="featured" href="work/{feat['slug']}.html" style="text-decoration:none">
    {cover(feat, r).replace('class="cover', 'style="aspect-ratio:760/480" class="cover', 1)}
    <div class="text">
      <span class="badge label">Featured case study</span>
      <h2 class="display-l">{feat['title']}</h2>
      <p>{escape(feat['summary'])}</p>
      <p class="body-s muted">{feat['tags']} · {feat['year']}</p>
      <span class="link">View case study&nbsp; →</span>
    </div>
  </a>
</section>
<section class="wrap" id="work">
  <div class="section-head"><h2 class="heading-m">More work</h2><span class="label muted">2024–2026</span></div>
  <div class="project-list">
"""
    for n, p in enumerate(rows, 1):
        html += f"""    <a class="row" href="work/{p['slug']}.html">
      {cover(p, r)}
      <div class="row-text">
        <p class="label"><span class="accent">{n:02d}</span>&nbsp;&nbsp;<span class="muted">{p['tags']} · {p['year']}</span></p>
        <h3 class="heading-m">{escape(p['title'])}</h3>
        <p class="row-summary">{escape(p['summary'])}</p>
      </div>
      <span class="row-arrow" aria-hidden="true">→</span>
    </a>
"""
    html += f"""  </div>
  <a class="text-row" href="personal.html"><span class="heading-s">Personal work</span><span class="muted" style="font-weight:500">Posters, sneakers and illustrations&nbsp; →</span></a>
</section>
<section class="wrap">
  <a class="about-strip" href="about.html">
    <div class="photo"><img src="images/me.jpg" alt="Amanda Hanssen" loading="lazy"></div>
    <div><h2 class="heading-m">Hi, I'm Amanda.</h2><p class="muted">Communication Design student at MassArt, between Boston and Laconia, NH.</p></div>
    <span class="link">More about me&nbsp; →</span>
  </a>
</section>
"""
    return html + footer(r)


CAPS = """<div class="dark-head"><p class="display-l" style="max-width:860px">I like projects where a brand, a screen and a real place all tell the same story.</p><p class="label light">What I do</p></div>
    <div class="caps">
      <div><span class="label light">01</span><h3 class="heading-s">Brand identity</h3><p class="body-s">Logos, type systems and print, like Paws &amp; Pastries and The Bench.</p></div>
      <div><span class="label light">02</span><h3 class="heading-s">Editorial &amp; type</h3><p class="body-s">Magazines, layouts and type you can walk into, like VOWS and Splash Zone.</p></div>
      <div><span class="label light">03</span><h3 class="heading-s">UX/UI &amp; apps</h3><p class="body-s">Research, flows and working apps, like DreamCast and Intertwine.</p></div>
      <div><span class="label light">04</span><h3 class="heading-s">Print &amp; production</h3><p class="body-s">Signs, vinyl and printed pieces, like Gator Graphix and VOWS.</p></div>
    </div>"""


def facts_html(facts):
    return '<div class="wrap facts">' + "".join(
        f'<div><p class="label muted">{escape(k)}</p><p>{escape(v)}</p></div>' for k, v in facts) + "</div>"


def next_html(p, r):
    i = VISIBLE.index(p)
    n = VISIBLE[(i + 1) % len(VISIBLE)]
    return f"""<a class="wrap next" href="{n['slug']}.html">
  <div><p class="label muted">Next project</p><p class="display-l">{escape(n['title'])}&nbsp; →</p></div>
  {cover(n, r)}
</a>
"""


def case_top(p, r):
    html = head(p["title"], p["intro"], r, image=(p["cover"]["src"] if p.get("cover") else "images/intertwine/site-desktop.jpg"), path=f"work/{p['slug']}.html")
    html += f'<div class="sky" id="top">{nav(r, "work")}'
    html += f"""<section class="wrap cs-hero">
  <a class="back" href="{r}index.html#work">←&nbsp; All work</a>
  <p class="label accent">{p['eyebrow']}</p>
  <h1 class="display-xl">{escape(p['title'])}</h1>
  <p class="body-l measure">{escape(p['intro'])}</p>
</section></div>
"""
    return html + facts_html(p["facts"])


def page_case(p):
    r = "../"
    if p.get("layout") == "intertwine":
        return page_intertwine(p)
    if p.get("story"):
        return page_story(p)
    html = case_top(p, r)
    html += '<section class="wrap"><div class="media">' + "".join(figure(i, r) for i in p["hero"]) + "</div></section>\n"
    lab, title, body = p["idea"]
    html += f"""<section class="wrap split">
  <p class="label muted">{lab}</p>
  <div class="stack"><h2 class="heading-m">{escape(title)}</h2><p class="body-l">{escape(body)}</p></div>
</section>
"""
    f = p["feature"]
    html += f'<section class="wrap"><div class="section-head"><h2 class="heading-m">{escape(f["title"])}</h2><span class="label muted">{escape(f["label"])}</span></div><div class="cards">'
    for c in f["cards"]:
        if c.get("img"):
            im = dict(c["img"], ratio=f.get("ratio", "410/360"))
            html += f'<div class="card">{figure(im, r, "top" if "/web/" in im["src"] else "")}<p class="label accent">{escape(c["k"])}</p><h3 class="heading-s">{escape(c["t"])}</h3><p class="muted">{escape(c["d"])}</p></div>'
        else:
            html += f'<div class="card text{" hi" if c.get("hi") else ""}"><p class="label accent">{escape(c["k"])}</p><h3 class="heading-s">{escape(c["t"])}</h3><p class="muted">{escape(c["d"])}</p></div>'
    html += "</div></section>\n"
    g = p.get("gallery")
    if g:
        html += f'<section class="wrap"><div class="section-head"><h2 class="heading-m">{escape(g["title"])}</h2><span class="label muted">{escape(g["label"])}</span></div><div class="media">'
        html += "".join(figure(i, r, "top") for i in g["images"]) + "</div></section>\n"
    pr = p["process"]
    html += f'<section class="process"><div class="wrap"><p class="label muted">Process</p><h2 class="display-l">{escape(pr["title"])}</h2><div class="steps">'
    html += "".join(f'<div><p class="label accent">{w}</p><h3 class="heading-s">{escape(t)}</h3><p class="body-s muted">{escape(d)}</p></div>' for w, t, d in pr["steps"])
    html += "</div>"
    if pr.get("images"):
        html += '<div class="media">' + "".join(figure(i, r) for i in pr["images"]) + "</div>"
    html += "</div></section>\n"
    o = p["outcome"]
    html += f'<section class="outcome"><div class="wrap"><p class="label muted">Outcome</p><p class="display-l quote">{escape(o["quote"])}</p><p class="body-l measure">{escape(o["body"])}</p>'
    if o.get("video"):
        v = o["video"]
        html += f'<figure class="video"><video controls playsinline preload="none" poster="{r}{v["poster"]}"><source src="{r}{v["src"]}" type="video/mp4">Your browser can’t play this video.</video>'
        html += f'<figcaption class="body-s muted">{escape(v["caption"])}</figcaption></figure>'
    if o.get("images"):
        html += '<div class="media">' + "".join(figure(i, r) for i in o["images"]) + "</div>"
    html += "</div></section>\n"
    return html + next_html(p, r) + footer(r)



# ---------------------------------------------------------------- detailed case study ("story")
def cap_figure(i, r, extra=""):
    """An image with an optional caption underneath."""
    f = figure(i, r, extra)
    if i.get("cap"):
        return f'<div class="capfig">{f}<p class="body-s muted caption">{escape(i["cap"])}</p></div>'
    return f


def block_html(b, r):
    t = b["type"]
    head = ""
    if b.get("title"):
        head = f'<div class="section-head"><h2 class="heading-m">{escape(b["title"])}</h2><span class="label muted">{escape(b.get("label", ""))}</span></div>'
    intro = f'<p class="body-l measure story-intro">{escape(b["intro"])}</p>' if b.get("intro") else ""
    if t == "split":
        paras = "".join(f'<p class="body-l">{escape(x)}</p>' for x in b["body"])
        return f'<section class="wrap split"><p class="label muted">{escape(b["label"])}</p><div class="stack"><h2 class="heading-m">{escape(b["heading"])}</h2>{paras}</div></section>\n'
    if t == "images":
        cols = b.get("cols", len(b["images"]))
        figs = "".join(cap_figure(i, r) for i in b["images"])
        return f'<section class="wrap">{head}{intro}<div class="grid cols-{cols}">{figs}</div></section>\n'
    if t == "beforeafter":
        bef, aft = b["before"], b["after"]
        notes = "".join(f"<li>{escape(n)}</li>" for n in b.get("notes", []))
        return f'''<section class="wrap">{head}{intro}<div class="ba">
  <div><p class="label muted">Before</p>{cap_figure(bef, r)}</div>
  <div><p class="label accent">After</p>{cap_figure(aft, r)}</div>
</div>{f'<ul class="changes">{notes}</ul>' if notes else ""}</section>\n'''
    if t == "system":
        sw = "".join(f'<div class="swatch"><span style="background:{h}"></span><p class="body-s"><strong>{escape(n)}</strong><br><span class="muted">{escape(role)}</span></p></div>' for n, h, role in b["colors"])
        ty = "".join(f'<div class="typecard"><p class="label muted">{escape(role)}</p><p class="heading-s">{escape(name)}</p><p class="body-s muted">{escape(why)}</p></div>' for role, name, why in b["type_faces"])
        figs = "".join(cap_figure(i, r) for i in b.get("images", []))
        return f'''<section class="system"><div class="wrap">{head}{intro}
  <div class="system-row"><div><p class="label muted">Color</p><div class="swatches">{sw}</div></div>
  <div><p class="label muted">Type</p><div class="typecards">{ty}</div></div></div>
  {f'<div class="grid cols-{len(b["images"])}">{figs}</div>' if figs else ""}
</div></section>\n'''
    if t == "steps":
        st = "".join(f'<div><p class="label accent">{w}</p><h3 class="heading-s">{escape(h)}</h3><p class="body-s muted">{escape(d)}</p></div>' for w, h, d in b["steps"])
        return f'<section class="process"><div class="wrap"><p class="label muted">{escape(b.get("label","Process"))}</p><h2 class="display-l">{escape(b["heading"])}</h2><div class="steps">{st}</div></div></section>\n'
    if t == "video":
        v = b
        return f'''<section class="wrap">{head}<figure class="video"><video controls playsinline preload="none" poster="{r}{v["poster"]}"><source src="{r}{v["src"]}" type="video/mp4">Your browser can’t play this video.</video><figcaption class="body-s muted">{escape(v["cap"])}</figcaption></figure></section>\n'''
    if t == "reflection":
        items = "".join(f'<div><p class="label light">{escape(k)}</p><p class="body-l">{escape(v)}</p></div>' for k, v in b["points"])
        return f'''<section class="dark reflection"><div class="wrap">
  <p class="label light">{escape(b.get("label","Reflection"))}</p>
  <p class="display-l quote hang">{escape(b["quote"])}</p>
  <div class="reflect-grid">{items}</div>
</div></section>\n'''
    raise ValueError("unknown block " + t)


def page_story(p):
    r = "../"
    html = case_top(p, r)
    html += '<section class="wrap"><div class="media">' + "".join(figure(i, r) for i in p["hero"]) + "</div></section>\n"
    for b in p["story"]:
        html += block_html(b, r)
    return html + next_html(p, r) + footer(r)


def page_intertwine(p):
    r = "../"
    I = r + "images/intertwine/"
    def ph(name, alt, cls=""):
        return f'<div class="phone {cls}"><img src="{I}{name}" alt="{escape(alt)}" loading="lazy"></div>'
    def cap(name, alt, text):
        return f'<figure>{ph(name, alt)}<figcaption class="body-s muted">{escape(text)}</figcaption></figure>'
    html = case_top(p, r)
    html += f"""<section class="wrap"><div class="phones-panel">
  {ph("o1-welcome.jpg", "Intertwine welcome screen")}{ph("o7-home.jpg", "Couple home screen", "big")}{ph("gh1-guesthome.jpg", "Guest home screen")}
</div></section>
<section class="wrap split">
  <p class="label muted">The problem</p>
  <div class="stack"><h2 class="heading-m">Wedding details live everywhere: texts, spreadsheets, websites and registries.</h2>
  <p class="body-l">Couples answer the same guest questions over and over, and guests dig through group chats for times and dress codes. Intertwine gives the couple one place to plan, and gives every guest one link with everything they need.</p></div>
</section>
<section class="wrap">
  <div class="section-head"><h2 class="heading-m">For the couple</h2><span class="label muted">iPhone app</span></div>
  <div class="phone-row">
    {cap("o54-preview.jpg", "Guest preview screen", "Preview what guests will see")}
    {cap("cg2-rsvp.jpg", "RSVP tracking screen", "Track RSVPs in real time")}
    {cap("cr1-registry.jpg", "Registry screen", "Build a registry and funds")}
    {cap("o7-home-dark.jpg", "Home screen in dark mode", "Light and dark mode")}
  </div>
</section>
<section class="guests"><div class="wrap">
  <div class="section-head"><h2 class="heading-m">For guests</h2><span class="label muted">Website · personal invite link</span></div>
  <div class="site-row">
    <div class="shot"><img src="{I}site-desktop.jpg" alt="Guest website on desktop" loading="lazy"></div>
    {ph("site-mobile.jpg", "Guest website on a phone")}
  </div>
  <div class="phone-row">
    {cap("gs1-schedule.jpg", "Schedule screen", "The schedule, event by event")}
    {cap("gw1-wear.jpg", "What to wear screen", "What to wear, with outfit ideas")}
    {cap("gd2-registry.jpg", "Guest registry screen", "“I'll get this” on the registry")}
    {cap("gh1-guesthome.jpg", "Guest home screen", "RSVP in one tap")}
  </div>
</div></section>
<section class="wrap" style="display:grid;gap:48px">
  <p class="label muted">Process</p>
  <h2 class="display-l">From site map to a working app.</h2>
  <div class="steps">
    <div><p class="label accent">Step 1</p><h3 class="heading-s">Research</h3><p class="body-s muted">How couples and guests share wedding info today.</p></div>
    <div><p class="label accent">Step 2</p><h3 class="heading-s">Site map</h3><p class="body-s muted">Every screen for both the couple and the guest.</p></div>
    <div><p class="label accent">Step 3</p><h3 class="heading-s">Brand pass</h3><p class="body-s muted">A script monogram, warm neutrals and Alegreya Sans headings.</p></div>
    <div><p class="label accent">Step 4</p><h3 class="heading-s">Build</h3><p class="body-s muted">A SwiftUI iPhone app and a guest website, connected by Supabase.</p></div>
    <div><p class="label accent">Step 5</p><h3 class="heading-s">Test</h3><p class="body-s muted">A real wedding, real invites and RSVPs, then fix what broke.</p></div>
  </div>
</section>
<section class="outcome dark" style="margin-bottom:0"><div class="wrap">
  <p class="label light">Outcome</p>
  <p class="display-xl quote">One wedding, in one place.</p>
  <p class="body-l measure">The app and website are live and connected. Guests RSVP, ask questions and claim gifts on the website, and it all shows up in the couple's app.</p>
  <a class="link" style="color:var(--periwinkle);justify-self:start" href="{GUEST_SITE}" target="_blank" rel="noopener">See the live guest site&nbsp; ↗</a>
</div></section>
"""
    return html + next_html(p, r) + footer(r)


def page_personal():
    r = ""
    P = "images/personal/"
    def piece(name, title, sub="", cls=""):
        s = f'<p class="body-s muted">{sub}</p>' if sub else ""
        return f'<figure class="{cls}"><img src="{P}{name}" alt="{escape(title)}" loading="lazy"><figcaption class="heading-s">{escape(title)}</figcaption>{s}</figure>'
    html = head("Personal work", "Posters, hand-painted sneakers and handmade characters by Amanda Hanssen.", r, path="personal.html")
    html += f'<div class="sky" id="top">{nav(r, "personal")}'
    html += """<section class="wrap hero">
  <p class="label accent">Personal work</p>
  <h1 class="display-xl">Things I make for <em class="accent">fun.</em></h1>
  <p class="body-l" style="max-width:720px">Posters, hand-painted sneakers and characters, made outside of (and sometimes for) class.</p>
</section></div>
<section class="wrap">
  <div class="section-head"><h2 class="heading-m">Posters</h2><span class="label muted">Print</span></div>
  <div class="gallery">
""" + "".join([
        piece("givinghope.jpg", "Giving Hope"), piece("humans.jpg", "Humans Are Plants"), piece("skin.jpg", "Skin Blindness"),
        piece("flower.jpg", "Flower to Flower"), piece("jeg.jpg", "Jeg elsker ham mer enn meg selv"), piece("angels.jpg", "Protected by Angels, Kissed by Roses"),
        piece("calendar.jpg", "Freight type calendar", "Typography 1 · Fall 2024"), piece("keeptalking.jpg", "Please Keep Talking", cls="wide")]) + """
  </div>
</section>
<section class="dark" style="margin-bottom:0"><div class="wrap">
  <div class="section-head" style="border-top-color:rgba(255,255,255,.3)"><h2 class="heading-m">Custom sneakers</h2><span class="label light">Hand-painted</span></div>
  <div class="sneakers">
    <img src="images/personal/uzi1.jpg" alt="Painted sneaker, side view" loading="lazy">
    <img src="images/personal/uzi2.jpg" alt="Painted sneaker detail" loading="lazy">
    <img src="images/personal/uzi3.jpg" alt="Pair of painted sneakers" loading="lazy">
  </div>
  <p class="body-l" style="max-width:760px;margin-top:40px">Lil Uzi Vert Pink Tour sneakers: hand-painted Air Force 1s inspired by the tour's pink-and-black look.</p>
</div></section>
<section class="wrap" style="padding-top:clamp(56px,9vw,120px)">
  <div class="section-head"><h2 class="heading-m">Characters</h2><span class="label muted">Handmade</span></div>
  <div class="chars">
    <figure style="margin:0;display:grid;gap:10px"><img src="images/personal/bunny.jpg" alt="Strawberry Bunny" loading="lazy"><figcaption class="heading-s">Strawberry Bunny</figcaption></figure>
    <figure style="margin:0;display:grid;gap:10px"><img src="images/personal/chopper.jpg" alt="Tony Tony Chopper" loading="lazy"><figcaption class="heading-s">Tony Tony Chopper</figcaption></figure>
  </div>
</section>
"""
    return html + footer(r)


def page_about():
    r = ""
    html = head("About", "Amanda Hanssen is a Communication Design student at MassArt with a minor in the Business of Creative Industries.", r, path="about.html")
    html += f'<div class="sky" id="top">{nav(r, "about")}'
    html += f"""<section class="wrap about-intro">
  <div class="photo"><img src="images/me.jpg" alt="Amanda Hanssen"></div>
  <div class="stack" style="gap:28px">
    <p class="label muted">About</p>
    <h1 class="display-xl">Hi, I'm Amanda.</h1>
    <p class="body-l">I'm a Communication Design student at MassArt, with a minor in the Business of Creative Industries. I split my time between Boston and Laconia, New Hampshire.</p>
    <p>I love taking a project from first sketch to the finished, printed thing. Over two summers at Gator Graphix I designed boat graphics, signs and banners, working one on one with clients to get every detail right.</p>
    <div class="btns"><a class="btn" href="{RESUME}" target="_blank" rel="noopener">Download resume</a><a class="btn outline" href="mailto:{EMAIL}">Get in touch</a></div>
  </div>
</section></div>
<section class="wrap details">
  <div><h2 class="label muted">Education</h2><ul>
    <li><span class="heading-s">Massachusetts College of Art and Design</span><span class="body-s muted">BFA, Communication Design · 2023–2027</span></li>
    <li><span class="heading-s">Minor</span><span class="body-s muted">Business of Creative Industries</span></li>
  </ul></div>
  <div><h2 class="label muted">Courses</h2><ul>
    <li><span class="heading-s">Graphic Design 2: Making Meaning</span><span class="body-s muted">Fall 2025 · Paws &amp; Pastries, The Bench</span></li>
    <li><span class="heading-s">Information Architecture</span><span class="body-s muted">DreamCast</span></li>
    <li><span class="heading-s">Typography III</span><span class="body-s muted">Spring 2026 · VOWS, Splash Zone</span></li>
    <li><span class="heading-s">Everyday Enhancements</span><span class="body-s muted">Fall 2026 · Intertwine</span></li>
  </ul></div>
  <div><h2 class="label muted">Experience</h2><ul>
    <li><span class="heading-s">Graphic Designer &amp; Manager</span><span class="body-s muted">Gator Graphix · Laconia, NH · 2024–2025. Custom boat graphics, signs and banners for a wide range of clients.</span></li>
    <li><span class="heading-s">Marketing &amp; Social Media Intern</span><span class="body-s muted">Lakes Region Mental Health Center · Laconia, NH · Feb–Jun 2023. Social media content, an illustrated infographic series and campaign visuals.</span></li>
    <li><span class="heading-s">Lab Monitor</span><span class="body-s muted">MassArt Academic Technology Services · Boston · 2023–now. One-on-one support and equipment troubleshooting.</span></li>
    <li><span class="heading-s">Bank Services Representative</span><span class="body-s muted">Bank of New Hampshire · Laconia, NH · Summer 2026</span></li>
  </ul></div>
</section>
<section class="dark" style="margin-bottom:0"><div class="wrap">
  """ + CAPS + """
  <p class="label light" style="margin-top:64px">Skills &amp; tools</p>
  <ul class="chips">""" + "".join(f"<li>{escape(s)}</li>" for s in [
        "Brand identity", "Editorial layout", "Typography", "UX/UI", "Wireframing", "User research", "Personas & journey maps",
        "Storyboarding", "Motion", "AR concepts", "Figma", "Illustrator", "InDesign", "Photoshop", "After Effects", "Procreate",
        "Print production", "Vinyl & large format", "Equipment operation"]) + """</ul>
</div></section>
"""
    return html + footer(r)


def page_404():
    r = "/"
    html = head("Page not found", "This page doesn't exist.", r)
    html += f'<div class="sky" id="top">{nav(r)}<section class="wrap hero"><h1 class="display-xl">This page wandered off.</h1><p class="body-l">Try the <a href="/index.html#work">work</a> or the <a href="/about.html">about page</a>.</p></section></div>'
    return html + footer(r)



def typeset(html):
    """Typographer's quotes, single spaces, and hung opening quotes (see the Beautiful Type Checklist)."""
    html = re.sub(r"(?<=[A-Za-z])(?:'|&#x27;)(?=[A-Za-z])", "\u2019", html)   # I'm -> I’m
    html = html.replace("&nbsp;&nbsp;", " ").replace("&nbsp; ", " ")          # no double spaces
    html = re.sub(r'class="display-l quote">(“|&quot;)', 'class="display-l quote hang">“', html)
    html = re.sub(r'class="display-xl quote">(“)', 'class="display-xl quote hang">“', html)
    return html


def main():
    out = {"index.html": page_home(), "about.html": page_about(), "personal.html": page_personal(), "404.html": page_404()}
    for p in VISIBLE:
        out[f"work/{p['slug']}.html"] = page_case(p)
    # remove pages for projects that are now hidden
    for p in PROJECTS:
        if p.get("hidden"):
            (ROOT / "work" / f"{p['slug']}.html").unlink(missing_ok=True)
    for path, html in out.items():
        html = typeset(html)
        f = ROOT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8")
    print("Built", len(out), "pages:", ", ".join(out))


if __name__ == "__main__":
    main()
