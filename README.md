# EcoNode

EcoNode is a University of Waterloo team project developing computer-vision guidance for apple-tree pruning. The intended MVP gives orchard workers guidance through off-the-shelf augmented-reality glasses and runs inference locally so workers can use it where connectivity is unreliable. The worker makes the pruning decision.

Velocity named EcoNode one of four winners of the March 2026 Agri-Food Innovation Challenge and credited Sheldon Mbuh, Harkamal Bhamra, and Gursimran Chadha. [Velocity announcement](https://www.velocityincubator.com/news/farming-for-canadian-grown-agri-food-innovation)

## Public engineering record

| Resource | What it covers |
| --- | --- |
| [Architecture](docs/architecture.md) | Capture, branch perception, expert review, offline inference, and the wearable MVP |
| [Model development](docs/model-development.md) | Candidate labeling, training, evaluation, and on-device benchmarking tools |
| [Roadmap](docs/roadmap.md) | Evidence required to advance from a model baseline to field evaluation |
| [Browser demonstration](https://sheldonmbuh.github.io/econode/demo/) | A synthetic walkthrough of when a wearable could present or withhold guidance |

The challenge result is public. Model accuracy, sustained offline inference, AR integration, and field effectiveness are development milestones. The browser demonstration evaluates fixed synthetic inputs with illustrative thresholds. It uses no camera, trained model, or orchard data.

EcoNode is a collaborative project. Publication of team software, datasets, annotations, images, model weights, and research artifacts requires the relevant team and data-owner approvals.
