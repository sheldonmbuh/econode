# EcoNode architecture

The off-the-shelf glasses MVP is a design under development. A worker sees the live environment directly and remains responsible for whether and where to cut.

1. **Capture.** Acquire permissioned imagery with the candidate camera and record scene conditions. A device must provide suitable camera access, resolution, viewing angle, and exposure outdoors.
2. **Perception.** Preprocess frames and run a compact detector or segmenter to locate branches and features. Evaluate whether boxes preserve enough structure or whether masks, keypoints, depth, or temporal context are needed.
3. **Decision support.** Keep visual detections separate from expert-reviewed pruning criteria. Treat disagreement, occlusion, unsupported tree conditions, and uncertainty as reasons to withhold guidance.
4. **Presentation.** Start with a legible display cue. Evaluate an aligned overlay only after calibrating camera-to-display geometry and measuring drift while a worker moves. Provide an obvious way to dismiss the cue.
5. **Offline runtime.** Package the model and its preprocessing with the application. Compare glasses-only inference with a nearby companion device using a local link. Loss of the local link or a stale frame should suppress guidance.

A phone or laptop can support early review with recorded imagery. Hardware selection for the wearable depends on camera SDK access, local display updates, daylight readability, PPE compatibility, measured latency, battery life, and temperature during sustained use.
