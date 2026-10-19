# AGENTS.md — Codex production contract

## Non-negotiable goal
Produce a **genuinely animated** 28–35 second film at `deliverables/deadpool_wolverine_nuke_1080x1920.mp4`. Characters are Deadpool and Wolverine themselves, not renamed substitutes. The final MP4 must contain coherent 3D action, original narration and dialogue, edited effects, music, synchronized burnt-in captions and a humorous ending.

## Start
Read `docs/CODEX_TASK.md`, `docs/SCRIPT.md`, `docs/SHOTLIST.csv`, and `docs/ATTRIBUTIONS.md` in full. Inspect the repository and dependencies; verify `blender`, `ffmpeg`, and a working render device. Detect real original model assets before committing to a render.

## Required implementation
1. Obtain or request legitimately downloadable, high-detail rigged meshes for both superheroes. Model creators' rights and copyright ownership must be checked. Do not download through scraping, obfuscated endpoints or viewer extraction.
2. Put permitted imported assets in `assets/models/` locally or in a permitted asset store; do not publish third-party binaries or the user's reference Short into public GitHub by default.
3. In Blender, verify material texture paths, bones, facial or body posing, and geometry; render model turnaround/preview frames. Do NOT use primitive geometry or static-card montages as the final film.
4. Build coherent rooftop scene, skyline, flash, wave, controlled debris, science cutaways, non-graphic regeneration visualization and an original comedy finish.
5. Render at reduced resolution for one 3–5-second proof first. Show a truthful preview status. For final render use 1080x1920 at 30fps; output original animation with no AI-baked text.
6. Mix new narration with distinct original character voices (do not clone actors); sound effects, basic music, carefully timed and readable captions. Follow `docs/SCRIPT.md` but retime naturally to 28–35 seconds if needed.
7. Final export H.264 yuv420p + AAC audio in MP4; run `production/verify_final.py` and visually inspect frame samples, all cuts and the audio. Supply verified MP4, contact sheet, editable Blender project, source scripts and attributions.

## Integrity and scope
- User explicitly rejected low-poly procedurally generated prototypes; quality matters more than a fake 'done'.
- Never claim model compatibility, rigging correctness, actual rendered frames, or final quality unless tested.
- If models cannot legally be downloaded or work cannot actually render in the environment, stop with precise blocker and asset request; do not substitute AI placeholder video.
- The HYSTAKES Short is reference-only, no copying its footage/audio/captions/transcript.
- Credit Marvel as appropriate. CC BY on a fan-uploaded mesh does NOT establish rights to Marvel-owned characters for distribution.
- No changing other repositories, external credit charges or purchases.
- Git history should contain sources/scripts/docs; store substantial output videos in release assets or workflow artifacts if repository size is a concern.

## Output contract
Report: playable video download URL, screenshot contact sheet, model licenses and file sources, duration, fps, codec, size, verification results, and any unresolved publishing/rights issues. If incomplete, state it explicitly.