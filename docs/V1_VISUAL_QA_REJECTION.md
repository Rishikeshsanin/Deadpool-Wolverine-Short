# V1 Visual QA — REJECTED (2026-10-19)

**Reviewed actual submitted file:** `deadpool_wolverine_nuke_1080x1920.mp4`, duration 32.50 seconds, H.264/AAC, 1080x1920 30 fps. Compared time-sampled frames against the user's supplied 26.62-second HYSTAKES reference. **Technical MP4 compliance passed; visual/animation acceptance FAILED.** User explicitly rejected the quality and wants a genuinely finished cinematic result, not an MVP.

## Defects observed in actual movie

| Time | Issue | Required change |
| --- | --- | --- |
| 0:00–0:03 | Both characters are stiff, arms-out and nearly motionless; dark skyline and flat purple floor; opening frame lacks an action hook. | Start with expressive full-body character acting and motivated camera movement; clear attractive background. |
| 0:04–0:08 | A huge flat white circle and arcs replace a believable nuclear detonation; character reaction is weak or absent. | Stage actual flash, fireball/mushroom cloud, heat, shockwave/debris with physically motivated timing and strong bracing/reactions. |
| 0:08–0:17 | Wolverine is close-up but continues arms-out/rest-pose; orange-gray body instead of requested iconic yellow/blue design; white swirls/hexagons do not convey adamantium or healing. | Correct recognizable costume design if permitted by available asset, deliberate rig keyframes, claws, animated stylized anatomical cutaway and clear regenerating-tissue visual. |
| 0:18–0:23 | Mostly empty purple space and scattered white polygon sprites; Deadpool rises into static frame, lacking actual regenerative transformation. | Show a non-graphic coherent Deadpool recovery sequence with staged visual change, not moving simple particles over a static model. |
| 0:24–0:27 | Nearly unchanged two-character shot. Pair sample frames at 24.4 and 26.4s show only ~0.7% pixels change beyond a modest difference threshold on 270x480 sampled images. | Replace with a real action beat plus payoff. |
| 0:28–0:32 | Punchline shot features stiff zooming characters and truncated figure instead of convincing performance. | Animate gestures, eye/head/shoulder responses, facial masking and Wolverine's distinct annoyed reaction; crisp comedic timing. |

Other observations: exaggerated, smooth egg-like Deadpool head; framing crops bodies awkwardly; huge unused areas of background; title and science are communicated primarily by text rather than visual action. Camera zooming over still characters is not a substitute for character animation. Audio metrics alone do not prove audio performance quality.

## Revised production direction

Treat V1 as a **discarded technical pipeline prototype**. Retain working assets and scripts only where useful: licensed meshes, editable environment, captions/audio plumbing, CLI render QA. Rebuild **blocking, character motion, action choreography, lighting, VFX and staging** rather than enhancing the existing static shots with more glow.

1. Check model rig bones/weights and apply genuine animated actions (idle, point, turn, shield, fall/bracing, recovery, walk-away). If provided rig cannot deform well, fix rigging or replace it with permission; don't freeze the model.
2. Make a **3–5 second true moving-character proof**. Characters visibly change pose at minimum every reaction beat, with feet/center of mass plausible and no joint tears. Visually inspect it before any full render.
3. Make an **independent nuclear blast VFX proof**: expanding bright flash, voluminous cloud, pressure-wave timing and reaction. No flat white disk masquerading as a nuke.
4. Render **3 distinct storytelling science visuals**: blast/heat effect, Wolverine adamantium skeletal cutaway, and Deadpool healing with on-screen visible transformation. Non-graphic visual approach.
5. Improve set lighting and contrast for legible, attractive hero design; no dark empty skyline or flat purple backdrop. Wolverine should read unmistakably as yellow/blue, with claws, as brief specifies.
6. Build detailed V2 8-shot animatic with no 2-second frozen stretches, clear action every 1–3 seconds and safe-area captions. Use original narration/dialogue, avoid copying reference.
7. Render representative full-detail frames and one moving clip with final materials/lighting. No 975-frame full export until actual visuals have passed review.
8. Export new MP4, validate full decode **and** conduct human visual review of actual action; label any unresolved issues. Do not mark project production-complete based solely on metadata.

## Acceptance gates

- 0 visible T/A/rest poses in finished film except if narratively intentional and convincingly animated.
- Both recognizable characters demonstrably animated on actual rigs, not two still models moved by a camera.
- Strong visible nuclear blast, reactions, and three physically distinct narrative visual beats.
- No entire long narrated segment represented only by static character + particles/text.
- Effective silhouette, lighting and framing at phone size, no weird head proportions or unintentional crops.
- Original clear audio, readable and correctly timed captions.
- Final deliverable remains the *real finished* 28–35 second video with genuine visual QA, not another technical completion announcement.

Preserve license/rights constraints. No new paid assets or services without user authorization. Do not publish publicly where character-use rights aren't resolved.