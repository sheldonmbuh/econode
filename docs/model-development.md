# Model development

## Prepare the data

Obtain grower consent and document usage rights before collection. Keep image and label versions together, retain examples of “cannot assess,” and review disagreement with experienced pruners. Group train, validation, and test samples by orchard session or tree so adjacent frames do not leak across splits.

Use Python to check that every annotation has an image, labels use the agreed vocabulary, coordinates are valid, and there are no duplicated images across splits. An approved local annotation editor can export YOLO-format labels. A YOLO-family model such as YOLOv8 is a candidate perception baseline. PyTorch with a versioned configuration supports checking whether boxes, masks, or keypoints work better for the chosen annotation task.

## Train and review

Develop a small reproducible baseline locally before submitting a larger job through an approved Slurm workflow. Record the code revision, environment, dataset version, split definition, random seed, metrics, and model artifact. Compare runs against the same held-out group and review representative misses and false detections by variety, lighting, and occlusion.

Evaluate pruning guidance separately against expert judgments. Report agreement, false guidance, abstention, and conditions where a second view is required. A perception metric alone cannot establish better pruning decisions.

## Profile offline

Export the candidate model to a runtime supported by the hardware. ONNX Runtime is one option to evaluate on a capable edge device. Compare the exported predictions with the training baseline before measuring end-to-end latency, memory, throughput, battery, and thermal behavior with internet connectivity disabled.

Public results require a reproducible test protocol and permission to share the underlying evidence. This repository has no released training runs, datasets, or model artifacts.
