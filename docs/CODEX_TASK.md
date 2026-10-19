# Codex task — make the actual finished video

## Objective
Create and deliver **one cinematic animated 28–35-second YouTube Short**, `deliverables/deadpool_wolverine_nuke_1080x1920.mp4`, inspired in production ambition (not copied footage) by https://www.youtube.com/shorts/7vkUQI-zUgw.

The users asked specifically for ACTUAL recognizable Deadpool and Wolverine; no original substitutes, toy models or more character concept images. They want 3D animated action better than the existing 26.6-second video, with scientific explanation, smart humor, original narration, effects and readable captions. Fully rendered MP4 is the only completion criterion.

## Candidate actual rigged meshes
- Deadpool facial-rig model: https://sketchfab.com/3d-models/deadpool-fully-rigged-with-facial-rig-bb4be48749df43f0a6899aeabec1cbdd
- Wolverine rigged model: https://sketchfab.com/3d-models/wolverine-rigged-af65afa536854dfebf93e8f342501c5c

These are candidates only. Obtain downloads through authorized channels and validate use permissions, actual meshes, rig hierarchies, textures and quality. Download may require the user's Sketchfab login. Stop and request the files if access fails. Do not claim the models have been acquired or tested.

## Preflight
- Inspect repository, reference docs, available tools and runtime hardware.
- Blender 4.x or compatible, Python, ffmpeg/ffprobe; GPU or practical Eevee rendering path.
- Confirm correct geometry and Blender import from actual model files; ensure materials, textures and skeletons work; render a proof frame of each character and inspect.
- Check Marvel character use/rights and model creator license attribution; do not redistribute third-party model binaries publicly without permission.

## Build
1. Stage a rooftop overlooking an abandoned city at dusk: rich lighting, silhouetted skyline, credible building geometry, atmospheric haze.
2. Animate precise superhero character acting: Deadpool expressive and wisecracking, Wolverine muscular, grounded and annoyed. Natural eyelines, cloth or suit shading, properly attached claws/swords, correct posing.
3. Follow `docs/SHOTLIST.csv`: hero two-shot, intense distant flash, approach of shockwave, science cutaways illustrating adamantium, regeneration and conditional survivability, smoky aftermath and sarcastic dialogue.
4. No graphic body destruction. The science framing must distinguish intense heat, blast and radiation, and qualify comic-based survival and complete vaporization.
5. Use original voiceover text from `docs/SCRIPT.md`, with distinct synthesized or recorded voices that do not mimic real actors.
6. Layer original or licensed effects: siren, flash whoosh, impact/rumble, metallic sting, healing shimmer, wind and record scratch. Add suitable original/licensed music. Mix narration over ambience.
7. Burn in bold, precisely timed captions with restrained yellow emphasis; keep within YouTube Shorts safe area. Do not render captions into scene plates.
8. Do a 3–5s animation proof at reduced resolution first, then produce full 1080x1920 30fps H.264/AAC final, target 28–35s.
9. Generate `deliverables/contact_sheet.png`, keep editable Blender file and reproducible build scripts. Save large MP4 as release asset or Actions artifact when repository blob limits make direct commit impractical.
10. Verify codecs/duration/resolution/audio with `python production/verify_final.py <path>` and inspect actual playback plus transitions. Report honest findings.

## Timeline / decision gates
- Gate 1: Model assets present, licensing documented and rig import confirmed. If not, request specific files and continue asset-independent work.
- Gate 2: Real 3–5s render proof with satisfactory 3D meshes and animation (not a still slideshow).
- Gate 3: 8 shots animated; VO and captions aligned.
- Gate 4: Finished MP4 validated and accessible to user. Only this marks complete.

## Do not
- Copy HYSTAKES footage, voice, captions or transcript.
- Scrape Sketchfab assets or claim fan-mesh license is Marvel IP clearance.
- Replace approved characters with generic equivalents.
- Purchase or subscribe to AI products, spend Google Flow/PixVerse credits or modify another repository.
- Report final delivery if no verified downloadable video exists.

## Expected response
Return exact MP4 download URL, preview/contact-sheet URL, changed files, render evidence, verification metrics, credits/licenses used, and remaining rights concerns. If asset acquisition blocks, state this immediately and ask only for the exact model downloads.