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
    "slug": "intertwine", "title": "Intertwine", "year": "2026", "featured": True,
    "tags": "iOS app · Website · Brand · In progress",
    "summary": "One wedding, in one place: an iPhone app where couples plan events, guests and a registry, and a website where every guest RSVPs with a personal link. A work in progress, designed and built from research to working code.",
    "cover_phones": ["images/intertwine/o7-home.jpg", "images/intertwine/gh1-guesthome.jpg"],
    "eyebrow": "Case study · In progress · iOS app & website · 2026",
    "intro": "One wedding, in one place. An iPhone app where couples plan events, guests and a registry, and a website where each guest opens a personal invite link: no app or account needed.",
    "facts": [("My role", "Solo: research, UX/UI, brand, and building the app and website"), ("Status", "In progress · Fall 2026"),
              ("Course", "Everyday Enhancements, Module 3 · MassArt"), ("Tools", "Figma, SwiftUI, HTML/CSS/JS, Supabase")],
    "story": [
      {"type": "phonepanel", "images": [img("images/intertwine/o1-welcome.jpg", "Intertwine welcome screen"), img("images/intertwine/o7-home.jpg", "Couple home screen"), img("images/intertwine/gh1-guesthome.jpg", "Guest home screen")]},
      {"type": "split", "label": "The problem", "heading": "Wedding details live everywhere: texts, spreadsheets, websites and registries.",
       "body": ["Couples answer the same guest questions over and over, and guests dig through group chats for times, places and dress codes. Most wedding apps make guests download something or create an account first.",
                "Intertwine splits the job in two: the couple gets an iPhone app to plan, and every guest gets one personal link that just works in their browser."]},
      {"type": "images", "title": "Mapping two journeys", "label": "Site map", "cols": 1,
       "intro": "I mapped every screen for both sides: the couple setting up a wedding and the guest opening an invite. Onboarding alone became a 12-step flow, from choosing a role to publishing the first event.",
       "images": [img("images/intertwine/onboarding-map.jpg", "Onboarding flow, all screens", fit=True, bg="paper", ratio="2400/899", cap="The couple’s first-time setup, in light and dark mode, from welcome to the first published event.")]},
      {"type": "phones", "title": "Setting up a wedding", "label": "Couple · onboarding",
       "images": [img("images/intertwine/o4-wedding.jpg", "Wedding info step", cap="Names, date and place, one short step at a time."),
                  img("images/intertwine/o54-preview.jpg", "Guest preview", cap="Couples see exactly what guests will see before publishing."),
                  img("images/intertwine/o55-ready.jpg", "Ready to publish", cap="A final check, then one tap sends it live."),
                  img("images/intertwine/o7-home.jpg", "Couple home", cap="Home: countdown, next event and RSVP numbers.")]},
      {"type": "phones", "title": "Running it day to day", "label": "Couple · tabs",
       "images": [img("images/intertwine/cg2-rsvp.jpg", "RSVP tracking", cap="RSVPs from the website arrive here in real time."),
                  img("images/intertwine/cg4-questions.jpg", "Guest questions", cap="Questions from guests, answered in one place."),
                  img("images/intertwine/cr1-registry.jpg", "Registry", cap="A registry with gifts and cash funds."),
                  img("images/intertwine/o7-home-dark.jpg", "Dark mode", cap="Every screen works in light and dark mode.")]},
      {"type": "site", "title": "For guests: one link", "label": "Website",
       "intro": "Each guest gets a personal invite link. No app, no account, no password: open it, RSVP, and find everything about the weekend.",
       "desktop": "images/intertwine/site-desktop.jpg", "mobile": "images/intertwine/site-mobile.jpg",
       "cap": "The live guest website on desktop and phone, using the demo invite."},
      {"type": "phones", "title": "What guests can do", "label": "Guest · website",
       "images": [img("images/intertwine/gs1-schedule.jpg", "Schedule", cap="The schedule, event by event, with maps and add-to-calendar."),
                  img("images/intertwine/gw1-wear.jpg", "What to wear", cap="Dress codes with outfit ideas for each event."),
                  img("images/intertwine/gd2-registry.jpg", "Guest registry", cap="“I’ll get this” claims a gift so nobody doubles up."),
                  img("images/intertwine/gh3-sent.jpg", "RSVP sent", cap="RSVP in a tap, with a clear confirmation.")]},
      {"type": "system", "title": "The system", "label": "Brand pass",
       "intro": "Calm, warm and trustworthy: wedding planning is stressful, so the interface stays quiet. Colors and spacing live as tokens shared by Figma, the app and the website, so all three always match.",
       "colors": [("Canvas", "#FCF5E5", "Background"), ("Slate", "#3F5562", "Accent and buttons"), ("Ink", "#202B31", "Text"),
                  ("Sage", "#E3ECE2", "Success: RSVP yes"), ("Clay", "#9E3A3A", "Errors")],
       "type_faces": [("Headings", "Alegreya Sans", "A friendly humanist sans with a little elegance, for titles and the website."),
                      ("Interface", "SF Pro", "Apple’s system font for body text and controls, so the app feels at home on iPhone.")],
       "images": [img("images/intertwine/components.jpg", "Component library", fit=True, bg="paper", ratio="1812/1200", cap="The component library: buttons, fields, badges, cards, tabs and flow parts, each with light and dark versions.")]},
      {"type": "steps", "heading": "From site map to a working app.", "steps": [
        ("Step 1", "Research", "How couples and guests share wedding info today."),
        ("Step 2", "Site map", "Every screen for both the couple and the guest."),
        ("Step 3", "Brand pass", "A script monogram, warm neutrals, tokens and components."),
        ("Step 4", "Build", "A SwiftUI iPhone app and a guest website, connected by Supabase."),
        ("Now", "Test", "Testing with a real wedding, real invites and RSVPs, and fixing what breaks.")]},
      {"type": "reflection", "label": "Where it stands", "quote": "Still in progress: one wedding, in one place.", "points": [
        ("Working so far", "Designing both sides at once. Seeing the couple’s screen next to the guest’s made every feature, like RSVPs and the registry, connect end to end."),
        ("What I’m learning", "Building it myself changes how I design: shared tokens and components save hours and keep Figma and code in sync."),
        ("Next steps", "Finish testing with a real couple, show photos added on other phones, and add push notifications for new RSVPs and questions.")]},
    ],
  },
  {
    "slug": "dreamcast", "title": "DreamCast", "year": "2025",
    "tags": "App concept · UX/UI · Motion",
    "summary": "A Headspace feature that helps you fall asleep and remember your dreams. Personas, journey maps, storyboards, the interface and a motion video, made over seven weeks.",
    "cover": img("images/dreamcast/cover.jpg", "DreamCast on an iPhone lock screen", fit=True, bg="ink"),
    "eyebrow": "Case study · App concept · 2025",
    "intro": "A Headspace feature that helps people fall asleep, remember their dreams and explore their subconscious in a mindful way.",
    "facts": [("My role", "Concept, personas, journey map, wireframes, interface and video (started with a partner, then my own version)"),
              ("Timeline", "7 weeks · Fall 2025"), ("Course", "Information Architecture 1, with Martha Rettig"),
              ("Tools", "Figma, After Effects, Google Suite")],
    "hero": [img("images/dreamcast/cover.jpg", "DreamCast notification on an iPhone", fit=True, bg="ink", ratio="1280/620")],
    "story": [
      {"type": "split", "label": "The brief", "heading": "Design a new feature for an app people already use.",
       "body": ["My partner and I started by exploring apps to build a feature for. We landed on dreams: an app that could help people fall asleep and remember their dreams more easily. I’ve always been fascinated by dreams, and I’ve even practiced lucid dreaming, so I loved the idea right away.",
                "Our first pitch mixed Kindle with dream tracking. I’d never really used Kindle, so I made my own version inside Headspace, which already helps people with mindfulness and sleep. That became DreamCast."]},
      {"type": "images", "title": "Who it’s for", "label": "Week 3", "cols": 2,
       "intro": "Two personas kept me honest: one realistic, one from the dream world. They helped me think about how DreamCast could serve everyday users and still feel imaginative.",
       "images": [img("images/dreamcast/persona-flora.jpg", "Persona: Flora Miller", ratio="16/9", cap="Flora Miller, 21, a college student balancing school stress and sleep. She wants to sleep better and use her dreams as a creative outlet."),
                  img("images/dreamcast/persona-maya.jpg", "Persona: Maya Light", ratio="16/9", cap="Maya Light, guardian of the Dream Portal, who guides people through the dream world. A playful second lens on the experience.")]},
      {"type": "images", "title": "Mapping Flora’s night", "label": "Week 4", "cols": 1,
       "intro": "I had so many feature ideas that the happy path got crowded. Mapping Flora’s goals, actions and feelings, from scrolling in bed to waking up groggy, showed me which moments actually mattered.",
       "images": [img("images/dreamcast/journey-map.jpg", "DreamCast journey map and happy path", fit=True, bg="paper", ratio="2800/762", cap="The journey map and happy path: Flora’s goals, actions, feelings and the opportunities DreamCast could answer.")]},
      {"type": "beforeafter", "title": "From sketch to screen", "label": "Weeks 3–5",
       "intro": "My first wireframes were busy with ideas. Working in Figma, I cut the flow down to Flora’s night and made every screen feel like it belonged in Headspace.",
       "before": img("images/dreamcast/wireframes.jpg", "Hand-drawn wireframes", fit=True, bg="paper", ratio="16/9", cap="Week 3: hand-drawn wireframes for the home, player and dream log."),
       "after": img("images/dreamcast/night-home.jpg", "Final night home screen", fit=True, bg="ink", ratio="16/9", cap="Week 7: the night home screen, with a DreamCast card that offers to help pick a story."),
       "notes": ["Kept Headspace’s tabs, cards and illustration style, so DreamCast feels like a feature, not a separate app.",
                 "Gave Headspace’s assistant, Ebb, the job of guiding Flora at night and checking in about her dream in the morning.",
                 "Made the home screen change with the time of day: a night sky before bed, a sunrise in the morning."]},
      {"type": "phones", "title": "The bedtime flow", "label": "Final interface",
       "intro": "From a gentle reminder to falling asleep to a story.",
       "images": [img("images/dreamcast/notification.jpg", "Bedtime notification", cap="A gentle reminder: tonight’s sleepcast is ready."),
                  img("images/dreamcast/night-home.jpg", "Night home screen", cap="The night home screen offers help picking a story."),
                  img("images/dreamcast/ebb-story.jpg", "Ebb helping pick a story", cap="Ebb asks how Flora feels and suggests a story."),
                  img("images/dreamcast/dreamcasts.jpg", "Dreamcasts collection", cap="The Dreamcasts collection of guided dream stories.")]},
      {"type": "phones", "title": "The morning after", "label": "Final interface",
       "images": [img("images/dreamcast/listening.jpg", "Sleep story player", cap="An eight-hour sleep story with ambience and voice controls."),
                  img("images/dreamcast/morning-home.jpg", "Morning home screen", cap="In the morning, a sunrise and a prompt to log the dream."),
                  img("images/dreamcast/ebb-reflect.jpg", "Ebb dream reflection", cap="Ebb helps Flora reflect and suggests what to listen to next.")]},
      {"type": "steps", "heading": "Seven weeks, from a dream to a video.", "steps": [
        ("Week 2", "Research", "Explored apps with my partner and settled on dreams."),
        ("Week 3", "Personas", "Flora and Maya, user stories and first wireframes."),
        ("Week 4", "Journey map", "Mapped the happy path and cut features down to Flora’s needs."),
        ("Week 5", "Storyboards", "Script, storyboards and a second interface draft that fits Headspace."),
        ("Weeks 6–7", "Video", "Recorded flows, wrote narration, then polished pacing and transitions.")]},
      {"type": "video", "title": "The final video", "label": "Motion",
       "src": "videos/dreamcast.mp4", "poster": "images/dreamcast/video-poster.jpg",
       "cap": "The full bedtime flow as an ad, from notification to morning log. 1 min 12 s."},
      {"type": "reflection", "quote": "“I learned how important it is to balance creativity with simplicity.”", "points": [
        ("What worked", "Focusing on Flora. Once every feature had to support her night, the happy path got simpler and the app felt calmer."),
        ("What I learned", "In motion, pacing is everything. My first video draft needed smoother transitions and a clearer link between visuals and narration."),
        ("Next time", "I’d test the flow with real people who struggle with sleep, and see if the morning reflection actually helps them remember more.")]},
    ],
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
    "intro": "A magazine about modern, nontraditional weddings for Gen Z and women in their 20s and 30s, printed and bound by hand, then rebuilt as an interactive website.",
    "facts": [("My role", "Concept, writing and editing, editorial design, typography, print production and web design"), ("Timeline", "10 weeks · Spring 2026"),
              ("Course", "Typography III & Information Architecture, with Katherine Hughes & Rita Ferreira"),
              ("Tools", "InDesign, Illustrator, Photoshop, Figma")],
    "hero": [img("images/vows/front-cover.jpg", "VOWS front cover", fit=True, bg="paper", ratio="628/620"),
             img("images/vows/back-cover.jpg", "VOWS back cover", fit=True, bg="paper", ratio="628/620")],
    "story": [
      {"type": "split", "label": "The idea", "heading": "Bridal magazines sell one idea of a perfect wedding. VOWS shows the rest.",
       "body": ["Traditional bridal magazines are built on an idealized, luxury look. I wanted a magazine for weddings that look like the people in them: courthouse ceremonies, small budgets, rainy days and couples who do it their own way.",
                "The audience is Gen Z and women in their 20s and 30s who follow fashion, art and social media. Five keywords guided every choice: nontraditional, editorial, bold, playful and expressive."]},
      {"type": "images", "title": "Building the system", "label": "Weeks 1–2", "cols": 2,
       "intro": "Before any spreads, I organized the content into sections and built a flexible grid. Type galleys tested how each typeface pairing handled headlines, body text and captions.",
       "images": [img("images/vows/galley.jpg", "Type galley", fit=True, bg="paper", ratio="4/3", cap="A type galley, comparing typefaces for headings and body text."),
                  img("images/vows/type.jpg", "Type exploration spread", fit=True, bg="paper", ratio="4/3", cap="Testing hierarchy through size, weight and contrast.")]},
      {"type": "images", "title": "Experimental spreads", "label": "Week 3", "cols": 3,
       "intro": "I pushed each layout in a different direction, changing image scale, type emphasis and pacing, to see how far the grid could stretch while still feeling like one magazine.",
       "images": [img("images/vows/early-afford.jpg", "Early spread: Could I afford to get married?", fit=True, bg="paper", ratio="3/4", cap="“Could I afford to get married?”: big type over a full-bleed photo."),
                  img("images/vows/early-drowning.jpg", "Early spread: Are you drowning in love?", fit=True, bg="paper", ratio="3/4", cap="“Are you drowning in love?”: an underwater photo carrying the headline."),
                  img("images/vows/early-lucky.jpg", "Early spread: Lucky days to get married", fit=True, bg="paper", ratio="3/4", cap="“Lucky days to get married”: dates as an illustrated list.")]},
      {"type": "beforeafter", "title": "Smaller, more personal", "label": "Week 3 critique",
       "intro": "In critique I realized my 10 × 13 in format felt too big and too formal. A wedding magazine should feel intimate, so I resized everything to 8 × 9.5 in, and then rethought the color and ornament to match.",
       "before": img("images/vows/early-rainy.jpg", "Early black and white Rainy Days spread", fit=True, bg="paper", ratio="4/3", cap="Week 3: “Rainy Days Aren’t Bad Luck,” black and white at 10 × 13 in."),
       "after": img("images/vows/final-rainy.jpg", "Final Rainy Days spread", fit=True, bg="paper", ratio="4/3", cap="Final: the same idea in wine and cream at 8 × 9.5 in, paired with “Wedding Superstitions.”"),
       "notes": ["Resized from 10 × 13 to 8 × 9.5 in, so it feels like a book you hold, not a poster.",
                 "Replaced black with a deep wine color and cream paper, for a romantic tone without the luxury clichés.",
                 "Turned the flowers and lace into a recurring motif across the magazine and, later, the website."]},
      {"type": "beforeafter", "title": "Reworking a feature", "label": "Weeks 3–5",
       "before": img("images/vows/early-drowning.jpg", "Early drowning spread", fit=True, bg="paper", ratio="4/3", cap="First draft: a single photo with the headline set over it."),
       "after": img("images/vows/final-drowning.jpg", "Final drowning spread", fit=True, bg="paper", ratio="4/3", cap="Final: the photo bleeds across the spread, and the script headline floats in the water."),
       "notes": ["Let the image cross the gutter, so the spread feels like one continuous scene.",
                 "Swapped the bold sans headline for a lighter script, which feels more like the story."]},
      {"type": "system", "title": "The system", "label": "Design decisions",
       "intro": "Romantic but not precious: a wine and cream palette, lace and floral ornaments, and two typefaces with real personality.",
       "colors": [("Wine", "#5E2A3A", "Primary: headlines and ornaments"), ("Cream", "#F4EAD8", "Paper"),
                  ("Blush", "#D9B8B4", "Soft accents"), ("Ink", "#1E1416", "Body text"), ("Sage", "#9AA58A", "Photos and nature")],
       "type_faces": [("Display", "Elido", "An expressive serif with matching ornaments, for headlines and the VOWS wordmark."),
                      ("Text", "Odile", "A warm, readable serif for long articles, with decorative initials and ornaments.")],
       "images": [img("images/vows/contents.jpg", "Table of contents", fit=True, bg="paper", ratio="4/3", cap="The table of contents."),
                  img("images/vows/editors.jpg", "Editor’s letter", fit=True, bg="paper", ratio="4/3", cap="The editor’s letter, with the lace motif down the side.")]},
      {"type": "images", "title": "The finished magazine", "label": "Print · 8 × 9.5 in", "cols": 3,
       "intro": "Cover, spine and back cover, front matter, two features, an interview, a visual essay and departments. I printed every page at full scale in black and white to check alignment, then printed, bound and trimmed the final copy myself.",
       "images": [img("images/vows/dinner.jpg", "Dinner party spread", fit=True, bg="paper", ratio="4/3", cap="Opening spread for a dinner-party wedding story."),
                  img("images/vows/final-lucky.jpg", "Lucky days spread", fit=True, bg="paper", ratio="4/3", cap="“Lucky Days to Get Married,” with the floral ornaments."),
                  img("images/vows/real-people.jpg", "Real people spread", fit=True, bg="paper", ratio="4/3", cap="A real-couple story, with a pull quote.")]},
      {"type": "images", "title": "Visual essay", "label": "Print", "cols": 3,
       "images": [img("images/vows/print-1.jpg", "Visual essay spread 1", fit=True, bg="paper", ratio="4/3", cap="Rings and a letter, shot from above."),
                  img("images/vows/print-2.jpg", "Visual essay spread 2", fit=True, bg="paper", ratio="4/3", cap="Flowers, shoes and small details."),
                  img("images/vows/print-3.jpg", "Visual essay spread 3", fit=True, bg="paper", ratio="4/3", cap="A garden ceremony to close the issue.")]},
      {"type": "images", "title": "Print to screen", "label": "Weeks 6–10", "cols": 2,
       "intro": "The second half of the project turned the magazine into a seven-page website. I mapped a sitemap, made black-and-white wireframes, then rebuilt each section for scrolling: bigger type, narrower columns, full-bleed images and oversized pull quotes.",
       "images": [img("images/vows/web/home.jpg", "VOWS website home page", ratio="1/1", cap="The homepage, introducing the issue."),
                  img("images/vows/web/issue.jpg", "Issue landing page", ratio="1/1", cap="The issue landing page: contents, editor’s letter and contributors.")]},
      {"type": "images", "cols": 2,
       "images": [img("images/vows/web/feature.jpg", "Feature article page", ratio="1/1", cap="The interactive feature, where scrolling sets the pace."),
                  img("images/vows/web/visual-essay.jpg", "Visual essay page", ratio="1/1", cap="The visual essay, adapted for screen.")]},
      {"type": "steps", "heading": "Ten weeks, two formats.", "steps": [
        ("Week 1", "Direction", "Theme, audience, keywords and a flexible grid."),
        ("Week 2", "Type", "Type galleys for headlines, body text and captions."),
        ("Week 3", "Resize", "Critique moved the format from 10 × 13 to 8 × 9.5 in."),
        ("Weeks 4–5", "Production", "Full text, front matter, cover and spine; printed, bound, trimmed."),
        ("Weeks 6–10", "Website", "Sitemap, wireframes, then scroll-based storytelling.")]},
      {"type": "reflection", "quote": "“The project started to come together as a complete system rather than a series of individual layouts.”", "points": [
        ("What worked", "Resizing the magazine. A smaller page made every story feel more personal, and it changed how I designed the rest."),
        ("What I learned", "Print and screen need different pacing. On the website I had to slow readers down with scale, white space and big quotes."),
        ("Next time", "I’d plan the website alongside the magazine, so ideas like the scrolling feature could shape the print version too.")]},
    ],
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
    "intro": "A brand for a dog-friendly café in Carmel-by-the-Sea, with treats for people and pups: name, logo, menus and a 24 × 36 in poster.",
    "facts": [("My role", "Brand strategy, naming, logo, type system, menus and poster"), ("Timeline", "7 weeks · Fall 2025"),
              ("Course", "Graphic Design 2: Making Meaning, with Joe Quackenbush"), ("Tools", "Illustrator, InDesign, Photoshop, Figma")],
    "hero": [img("images/paws/mark.jpg", "Paws & Pastries brand mark", ratio="1280/620")],
    "story": [
      {"type": "split", "label": "The brief", "heading": "Start with food memories, end with a bone.",
       "body": ["Graphic Design 2 asked us to invent a restaurant and build its whole brand. I started with a mind map around food memories, the smells, places and people tied to eating, and kept coming back to slow mornings, pastries and dogs under the table.",
                "That became Paws & Pastries: “Where sweet treats and wagging tails come together.” A café with a shaded patio, water bowls and leash hooks, a dog park out back, weekly events with shelter dogs, and a menu for both people and pups."]},
      {"type": "images", "title": "Research", "label": "Week 1", "cols": 2,
       "intro": "I set the café in Carmel-by-the-Sea, a storybook village on California’s Monterey Peninsula known for being dog friendly. Two moodboards tested the feeling, and two personas kept the brand grounded in real people.",
       "images": [img("images/paws/location.jpg", "Location: Carmel-by-the-Sea", ratio="16/9", cap="The location: Carmel-by-the-Sea, a dog-friendly village on the Monterey Peninsula."),
                  img("images/paws/moodboards.jpg", "Two moodboards", ratio="16/9", cap="Two moodboards: warm pastries, cottage storefronts and dogs at the table, in plum, pink, butter and coral."),
                  img("images/paws/personas.jpg", "Customer and employee personas", ratio="16/9", cap="Personas: Claire, a local who adopted her dog at one of the café’s events, and Rosa, a college student who works the counter."),
                  img("images/paws/features.jpg", "What keeps customers coming back", ratio="16/9", cap="What makes customers come back: the patio, the dog park, the community garden and weekly events.")]},
      {"type": "images", "title": "From 100 marks to one", "label": "Weeks 2–4", "cols": 3,
       "intro": "I sketched 100 marks, literal and metaphoric, then ran the name through hundreds of typefaces. The ten strongest went into Illustrator. The winner was a bone holding the name, simple enough to work at any size.",
       "images": [img("images/paws/sketches.jpg", "Early logo sketch", fit=True, bg="paper", ratio="1/1", cap="An early sketch: a dog and a pastry in one line."),
                  img("images/paws/type-test.jpg", "Type test of the name", fit=True, bg="paper", ratio="1/1", cap="A type run, testing how the name reads in different letterforms."),
                  img("images/paws/refined-logos.gif", "Animation of the ten refined logos", fit=True, bg="paper", ratio="1/1", cap="The ten refined marks, each testing a different idea.")]},
      {"type": "images", "title": "The dual lockup", "label": "Week 4", "cols": 3,
       "intro": "One mark, two shapes: a horizontal bone for signs and the website, and a stacked version for menus and narrow pieces. I tested both in positive and negative, so the weight holds on any background.",
       "images": [img("images/paws/lockup-bone.jpg", "Horizontal bone lockup", fit=True, bg="paper", ratio="1/1", cap="Horizontal lockup, in black."),
                  img("images/paws/lockup-round.jpg", "Round lockup", fit=True, bg="paper", ratio="1/1", cap="A round badge version."),
                  img("images/paws/lockup-negative.jpg", "Negative lockup", fit=True, bg="ink", ratio="1/1", cap="The stacked lockup in negative, white on black.")]},
      {"type": "system", "title": "The system", "label": "Design decisions",
       "intro": "Everything had to feel like a cozy bakery, not a pet store. Deep chocolate keeps it grown-up, pink and butter make it sweet, and patterns built from the logo’s shapes tie every piece together.",
       "colors": [("Chocolate", "#4A1F1F", "Primary: logo and text"), ("Butter", "#F8E7B0", "Background and paper"),
                  ("Pastry pink", "#E9A0AE", "Accent: warmth and play"), ("Berry", "#C4505A", "Highlights and menus"), ("Cream", "#FFF8EC", "Light backgrounds")],
       "type_faces": [("Display", "Decoy", "A soft, rounded serif with a bakery feel, for the logo and headings."),
                      ("Text", "Almarai", "A clean, friendly sans that keeps long menus easy to read.")],
       "images": [img("images/paws/color-brown-pink.jpg", "Logo in chocolate and pink", fit=True, bg="paper", ratio="1/1", cap="Testing the mark in chocolate and pink."),
                  img("images/paws/color-pink.jpg", "Logo in pink", fit=True, bg="paper", ratio="1/1", cap="A lighter, all-pink version.")]},
      {"type": "beforeafter", "title": "Reworking the menu", "label": "Weeks 5–7",
       "intro": "I set both menus in black and white first, to get the type right, then added color. The first color version was sweet but flat. The final one uses a pattern from the logo, so the menu feels like part of the brand.",
       "before": img("images/paws/menu-draft.jpg", "First menu draft", fit=True, bg="paper", ratio="4/5", cap="First color draft: a scalloped border and a single list."),
       "after": img("images/paws/menu-final.jpg", "Final menu", fit=True, bg="paper", ratio="4/5", cap="Final menu: the paw pattern frames three columns, with a sleepy-dog illustration."),
       "notes": ["Moved from one column to three, so breakfast, lunch and pastries are easier to scan.",
                 "Replaced the scalloped border with a paw-print pattern drawn from the logo.",
                 "Gave the pup menu its own bone-shaped card, so it’s fun to hand to customers."]},
      {"type": "beforeafter", "title": "The brand poster", "label": "Week 6",
       "intro": "The 24 × 36 in poster is a snapshot of the whole system: logo variations, the brand equation, typefaces, patterns, color palette, menus and applications.",
       "before": img("images/paws/brand-poster.jpg", "First brand poster", fit=True, bg="paper", ratio="2/3", cap="First version: everything on white, so it felt like a spec sheet."),
       "after": img("images/paws/poster.jpg", "Final brand poster", fit=True, bg="paper", ratio="2/3", cap="Final: the chocolate panels and butter background make the poster feel like the café."),
       "notes": ["Put each part of the system in its own chocolate panel, so the poster reads as one brand, not a list.",
                 "Added real applications, like tote bags, coffee cups and signage, to show the brand in use."]},
      {"type": "steps", "heading": "Seven weeks, from memory to menu.", "steps": [
        ("Week 1", "Strategy", "Mind maps, trueline, personas and two moodboards."),
        ("Week 2", "Explore", "100 logo marks and a type run of the name."),
        ("Week 3", "Refine", "Ten marks drawn in Illustrator and tested at every size."),
        ("Weeks 4–5", "System", "Dual lockup, menus, patterns and graphic elements."),
        ("Weeks 6–7", "Make", "A 24 × 36 in poster and physical menus.")]},
      {"type": "images", "title": "Printed and assembled", "label": "Physical deliverables", "cols": 3,
       "images": [img("images/paws/photo-menu.jpg", "Printed menu", ratio="4/3", cap="The printed main menu."),
                  img("images/paws/bone-menu.jpg", "Bone-shaped pup menu", fit=True, bg="paper", ratio="4/3", cap="The bone-shaped pup menu."),
                  img("images/paws/menus-photo.jpg", "Printed menus together", ratio="4/3", cap="Both menus, cut and printed.")]},
      {"type": "reflection", "quote": "“Move past first-thought solutions.”", "points": [
        ("What worked", "Drawing 100 marks pushed me past the obvious paw print. The bone shape only showed up after the easy ideas ran out."),
        ("What I learned", "Designing in black and white first made the type stronger. Color is easier to add when the layout already works."),
        ("Next time", "I’d design more of the café itself, like signs, cups and the patio, to show the brand in its space.")]},
    ],
  },
  {
    "slug": "splash-zone", "title": "Splash Zone", "year": "2026",
    "tags": "Typography · Installation",
    "summary": "Vinyl lettering that turns a campus bathroom into a playful, slightly uncomfortable experience.",
    "cover": img("images/splash/cover.jpg", "Blue vinyl lettering on bathroom tiles"),
    "eyebrow": "Case study · Typography installation · 2026",
    "intro": "A team installation that splashes vinyl type across a campus bathroom, turning an everyday room into a playful, slightly uncomfortable experience.",
    "facts": [("My role", "Team project: concept, mockups and installation [add your specific part]"), ("Timeline", "4 weeks · Spring 2026"),
              ("Course", "Typography III, with Katherine Hughes"), ("Tools", "Illustrator, Photoshop, Procreate, Figma")],
    "hero": [img("images/splash/install.jpg", "Splash Zone installation", ratio="1280/620")],
    "story": [
      {"type": "split", "label": "The brief", "heading": "What happens to type when you can walk into it?",
       "body": ["Typography III asked us to put type into a real space and see how the space changes its meaning. Our team walked around campus looking for places with a strong mood, or an interesting way people use them.",
                "The project shifted how I think about type: not just something you read, but something you experience with your whole body."]},
      {"type": "images", "title": "Three concepts", "label": "Week 1", "cols": 3,
       "intro": "We pitched three directions, each with its own location, moodboard and mockups.",
       "images": [img("images/splash/proposal-2.jpg", "Splash Zone concept slide", ratio="16/9", cap="Splash Zone: a ground-floor bathroom, a hazard-sign mark and wet, dripping letters."),
                  img("images/splash/proposal-4.jpg", "Don't Spiral concept slide", ratio="16/9", cap="Don’t Spiral: a round window where repeating type mimics anxious thoughts."),
                  img("images/splash/proposal-6.jpg", "Sunshine concept slide", ratio="16/9", cap="Sunshine: a warmer, uplifting piece for a sunny second-floor lounge.")]},
      {"type": "images", "title": "Planning it in phases", "label": "Week 1", "cols": 3,
       "images": [img("images/splash/proposal-3.jpg", "Splash Zone phases", ratio="16/9", cap="Splash Zone, step by step: the sign builds up across the stall doors."),
                  img("images/splash/proposal-5.jpg", "Don't Spiral phases", ratio="16/9", cap="Don’t Spiral, growing more intense the closer you get."),
                  img("images/splash/proposal-7.jpg", "Sunshine phases", ratio="16/9", cap="Sunshine, with type that catches the light through the window.")]},
      {"type": "images", "title": "Choosing Splash Zone", "label": "Week 2", "cols": 2,
       "intro": "After critique, Splash Zone won: the most playful tone, the strongest tie to its space, and the most immersive. We then tested placement, scale and vinyl at full size.",
       "images": [img("images/splash/proposal-8.jpg", "Final options slide", ratio="16/9", cap="The final options side by side."),
                  img("images/splash/mockups.jpg", "Splash Zone mockup on a stall door", fit=True, bg="paper", ratio="16/9", cap="A mockup of the hazard sign on a real stall door.")]},
      {"type": "beforeafter", "title": "From mockup to wall", "label": "Weeks 2–4",
       "intro": "Our first idea was a single hazard sign. Testing it at full size showed it felt like a real sign and got ignored, so we let the letters splash across the whole room instead.",
       "before": img("images/splash/mockup.jpg", "Early wall mockup", fit=True, bg="apricot", ratio="4/3", cap="Week 2: gray paper mockups of the logo and drips on the wall."),
       "after": img("images/splash/installed.jpg", "Installed blue vinyl", ratio="4/3", cap="Week 4: blue vinyl letters spilling across the tiles."),
       "notes": ["Went from one sign to letters scattered around the whole room, so you’re surrounded.",
                 "Switched from gray to a bright blue that reads like water on the tiles.",
                 "Placed the drips around fixtures and corners, so the type seems to react to the space."]},
      {"type": "steps", "heading": "From mood board to tile wall.", "steps": [
        ("Week 1", "Research", "Scouting campus spaces, three concepts, mood boards and mockups."),
        ("Week 2", "Test", "Chose Splash Zone; full-size mockups for placement, scale and vinyl."),
        ("Week 3", "Produce", "[Add what your team did this week, like cutting the vinyl.]"),
        ("Week 4", "Install", "Installed the final vinyl in the bathroom.")]},
      {"type": "images", "title": "The installation", "label": "Final", "cols": 3,
       "images": [img("images/splash/team.jpg", "The team in the installation", ratio="4/5", cap="Our team in the finished room."),
                  img("images/splash/wall.jpg", "Wall view", ratio="4/5", cap="The view from the door."),
                  img("images/splash/tests.jpg", "Placement detail", fit=True, bg="apricot", ratio="4/5", cap="Drips placed around the fixtures.")]},
      {"type": "reflection", "quote": "“It really shifted how I think about type.”", "points": [
        ("What worked", "Testing at full size. Paper mockups on the real wall showed us what a sketch never could."),
        ("What I learned", "Space changes meaning. The same letters feel funny in a bathroom and anxious in a window."),
        ("Next time", "[Add your own thought here, for example what you’d change about the install or the teamwork.]")]},
    ],
  },
  {
    "slug": "gator-graphix", "title": "Gator Graphix", "year": "2024–2025",
    "tags": "Client work · Signs · Boat graphics",
    "summary": "Boat lettering, signs and banners for clients around Lake Winnipesaukee, designed and installed over two summers.",
    "cover": img("images/gator/lake.jpg", "Lake Winnipesaukee lettering on a wooden boat transom"),
    "eyebrow": "Case study · Client work · 2024–2025",
    "intro": "Two summers as graphic designer and manager at a sign shop in Laconia, New Hampshire, making custom boat graphics, signs, apparel and vehicle graphics for local businesses and boat owners.",
    "facts": [("My role", "Graphic designer & manager"), ("Timeline", "Summers 2024–2025"),
              ("Where", "Gator Graphix · Laconia, NH"), ("Tools", "Adobe Illustrator, large-format printers and vinyl cutters")],
    "hero": [img("images/gator/install2.jpg", "Twin Engines boat lettering", ratio="628/620"),
             img("images/gator/install3.jpg", "Gracie-Mae transom graphics", ratio="628/620")],
    "story": [
      {"type": "split", "label": "The job", "heading": "Real clients, real boats, real deadlines.",
       "body": ["Class projects have imaginary clients. At Gator Graphix every job had a real person waiting for it, often with a boat that needed to be on the water by the weekend.",
                "I met with customers one on one, turned their ideas into designs in Illustrator, then printed, cut and installed the work myself. As manager, I also kept jobs moving and the equipment running."]},
      {"type": "steps", "label": "How a job works", "heading": "From conversation to install.", "steps": [
        ("Step 1", "Listen", "Talk through the idea, size, budget and where it will live."),
        ("Step 2", "Design", "Draft options in Illustrator and refine them with the client."),
        ("Step 3", "Produce", "Print or cut the vinyl and prep the surface."),
        ("Step 4", "Install", "Apply on site, from transoms and decks to trailers."),
        ("Step 5", "Check", "Walk the client through it and fix anything before they leave.")]},
      {"type": "images", "title": "Boat graphics", "label": "On the water", "cols": 3,
       "intro": "Boat lettering has to read from the dock, survive sun and spray, and fit curves that are never quite flat.",
       "images": [img("images/gator/install1.jpg", "Weak Moment transom lettering", ratio="3/4", cap="Transom lettering, sized and spaced to read from across the water."),
                  img("images/gator/install5.jpg", "Hang On Stoopy deck graphic", ratio="3/4", cap="A script name cut in vinyl and laid onto the deck."),
                  img("images/gator/install6.jpg", "Blue boat with hull graphics", ratio="3/4", cap="Hull graphics designed to follow the curve of the boat.")]},
      {"type": "images", "title": "One idea, many surfaces", "label": "A client set", "cols": 3,
       "intro": "One customer wanted their dog on everything. I turned a photo into a clean graphic, then adapted it for the boat, the hull script and a dock box, so the set feels like one brand.",
       "images": [img("images/gator/install4.jpg", "Living the Dream script on a boat", ratio="3/4", cap="“Living the Dream!” in script along the hull."),
                  img("images/gator/install7.jpg", "Dog graphic on boat side", ratio="3/4", cap="The dog graphic on the boat."),
                  img("images/gator/chest.jpg", "Dog graphic on a dock box", ratio="3/4", cap="The same graphic on a matching dock box.")]},
      {"type": "images", "title": "Signs, apparel and vehicles", "label": "Beyond boats", "cols": 3,
       "images": [img("images/gator/install-photo.jpg", "Gold lettering on a wooden transom", ratio="4/3", cap="Gold lettering for a classic Century boat: “Lake Winnipesaukee, Alton, NH.”"),
                  img("images/gator/gath.jpg", "Gath Landscaping trailer", ratio="4/3", cap="Trailer graphics for Gath Landscaping."),
                  img("images/gator/shirt.jpg", "Koung Sushi Mart shirt", ratio="4/3", cap="A printed shirt for Koung Sushi Mart in Laconia and Concord."),
                  img("images/gator/pool.jpg", "Pool closed sign", ratio="4/3", cap="A “Pool Closed” sign for a local property."),
                  img("images/gator/signage.jpg", "Lady Liberty's shop signage", ratio="4/3", cap="Window and shop signage."),
                  img("images/gator/garden.jpg", "Long Bay Garden Club sign", fit=True, bg="paper", ratio="4/3", cap="A sign for the Long Bay Garden Club.")]},
      {"type": "reflection", "quote": "Designing for a real customer means listening first.", "points": [
        ("What worked", "Asking lots of questions up front. The fewer surprises at the proof stage, the happier the client and the faster the install."),
        ("What I learned", "Production shapes design. Knowing how vinyl cuts, stretches and weathers changed how thin I drew letters and how I spaced them."),
        ("Next time", "I’d keep a simple brand guide for repeat clients, so their logo and colors stay consistent from one job to the next.")]},
    ],
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
      <span class="badge label">Featured · In progress</span>
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
    if t == "phones":
        figs = "".join(f'<figure><div class="phone"><img src="{r}{i["src"]}" alt="{escape(i["alt"])}" loading="lazy"></div><figcaption class="body-s muted">{escape(i.get("cap") or "")}</figcaption></figure>' for i in b["images"])
        dark = " phones-dark" if b.get("dark") else ""
        return f'<section class="wrap{dark}">{head}{intro}<div class="phone-row cols-{len(b["images"])}">{figs}</div></section>\n'
    if t == "phonepanel":
        ph = "".join(f'<div class="phone{" big" if k == 1 else ""}"><img src="{r}{i["src"]}" alt="{escape(i["alt"])}" loading="lazy"></div>' for k, i in enumerate(b["images"]))
        return f'<section class="wrap"><div class="phones-panel">{ph}</div></section>\n'
    if t == "site":
        return f'''<section class="guests"><div class="wrap">{head}{intro}<div class="site-row"><div class="shot"><img src="{r}{b["desktop"]}" alt="Guest website on desktop" loading="lazy"></div><div class="phone"><img src="{r}{b["mobile"]}" alt="Guest website on a phone" loading="lazy"></div></div><p class="body-s muted caption">{escape(b["cap"])}</p></div></section>\n'''
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
    if p.get("hero"):
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
    <li><span class="heading-s">Everyday Enhancements</span><span class="body-s muted">Fall 2026 · Intertwine (in progress)</span></li>
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
