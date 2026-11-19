# Compositional Human Motion & Interaction

**A living paper survey of temporal, spatial, semantic, interaction and skill composition for digital humans.**

从经典动作拼接到生成模型、交互与具身执行，按“组合了什么、依赖哪些条件、验证了什么”组织。

Last audit: **2026-11-19** · **128 unique papers** · **28 method-level / 100 abstract-level records** · No external method reproduced.

[Interactive clickable map](https://yutao-yang.github.io/awesome-compositional-human-motion/) · [All audit cards](notes/papers.md) · [Comparison matrix](notes/comparison.md) · [Benchmarks](notes/benchmarks.md) · [中文阅读指南](notes/reading-guide.zh.md) · [BibTeX](references.bib) · [JSON](papers.json) · [Search & inclusion protocol](SEARCH_PROTOCOL.md) · [Maintenance](CONTRIBUTING.md)

> Breadth-first, evidence-labelled curation; not a claim of exhaustive full-text review. “Method” means targeted method/evaluation reading, not reproduction. Displayed years use the first preprint where known; venue and cited-version bibliography years are separate.

## Research map

The diagram is a visual overview. Every category and paper in the directory below is a normal clickable link; the interactive map also offers search, evidence filters and expandable paper cards.

```mermaid
mindmap
  root((Compositional Human Motion))
    Motion composition
      Classical motion composition
      Temporal composition and long sequences
      Body-part and semantic composition
      Motion editing and in-betweening
      Generative backbones and representations
    Interaction composition
      Human-object and articulated interaction
      Human-scene interaction and planning
      Multi-person and collaborative interaction
    Data and execution
      Datasets and compositional evaluation
      Physics-based character control
      Humanoid transfer and loco-manipulation
    Related fields
      Audio, dance and gesture composition
      Surveys and field maps
      Adjacent: compositional human video
```

## Clickable directory

- [Classical motion composition](#classics) — 4 papers
- [Temporal composition & long sequences](#temporal) — 13 papers
- [Body-part & semantic composition](#spatial) — 10 papers
- [Motion editing & in-betweening](#editing) — 8 papers
- [Generative backbones & representations](#backbones) — 13 papers
- [Human-object & articulated interaction](#objects) — 19 papers
- [Human-scene interaction & planning](#scenes) — 9 papers
- [Multi-person & collaborative interaction](#people) — 7 papers
- [Datasets & compositional evaluation](#datasets) — 17 papers
- [Physics-based character control](#physics) — 11 papers
- [Humanoid transfer & loco-manipulation](#humanoids) — 6 papers
- [Audio, dance & gesture composition](#audio) — 6 papers
- [Surveys & field maps](#surveys) — 4 papers
- [Adjacent: compositional human video](#video) — 1 papers

## How to read the evidence

- **Abstract**: identity and task-level claims checked against a primary source; detailed protocol remains to be audited.
- **Method**: targeted method/conditions/evaluation reading; see the linked source and locator when available.
- **Curator boundary**: limitations distinguish comparison scope from authors’ claims; they do not assert an untested method failure.
- **Official code link**: points to an author-linked repository; availability is not installation, licensing or reproducibility verification.

A long sequence is not automatically compositional generalization. Report unseen source pairings, unseen semantic skill pairings and state-dependent task chains separately.

<a id="classics"></a>
## Classical motion composition

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **parametric-motion-graphs** — Parametric Motion Graphs | 2007 | Connects parameterized motion synthesis with valid dynamically generated blending transitions. | abstract | [Paper](https://graphics.cs.wisc.edu/Papers/2007/HG07/) · [Audit](notes/papers.md#parametric-motion-graphs) |
| **motion-annotations** — Motion Synthesis from Annotations | 2003 | Uses annotated action timelines and multiscale dynamic programming to assemble motion, including overlapping qualitative constraints. | method | [Paper](https://escholarship.org/uc/item/23g204tp) · [Audit](notes/papers.md#motion-annotations) |
| **interactive-motion-examples** — Interactive motion generation from examples | 2002 | Cuts and pastes mocap via randomized hierarchical graph search under constraints at interactive speeds. | abstract | [Paper](https://experts.illinois.edu/en/publications/interactive-motion-generation-from-examples/) · [Audit](notes/papers.md#interactive-motion-examples) |
| **motion-graphs** — Motion Graphs | 2002 | Builds a directed graph of captured clips and synthesized transitions; graph walks satisfy user constraints such as locomotion paths. | abstract | [Paper](https://graphics.cs.wisc.edu/Papers/2002/KGP02/) · [Audit](notes/papers.md#motion-graphs) |

<a id="temporal"></a>
## Temporal composition & long sequences

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **prism** — PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition | 2026 | Kinematic-unit continuous latents, causal VAE and flow matching support prefix continuation, segment chaining and narrative composition. | abstract | [Paper](https://arxiv.org/abs/2603.08590) · [Audit](notes/papers.md#prism) · [Code](https://github.com/ZeyuLing/PRISM) |
| **timelinecontrol** — Streaming Multi-Track Timeline Control for 3D Human Motion Generation | 2026 | TimelineControl combines interval-aware conditioning, causal part representations and part-aware denoising with TimelineMotion annotations. | abstract | [Paper](https://arxiv.org/abs/2610.03873) · [Audit](notes/papers.md#timelinecontrol) |
| **dart** — DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control | 2024 / ICLR 2025 as DartControl | Latent diffusion predicts motion primitives from history and current text; noise optimization or RL provides spatial control. | abstract | [Paper](https://arxiv.org/abs/2410.05260) · [Audit](notes/papers.md#dart) |
| **motion-mamba** — Motion Mamba: Efficient and Long Sequence Motion Generation | 2024 | Hierarchical temporal and bidirectional spatial state-space blocks improve long-motion modeling and efficiency. | abstract | [Paper](https://arxiv.org/abs/2403.07487) · [Audit](notes/papers.md#motion-mamba) · [Code](https://github.com/steve-zeyu-zhang/MotionMamba) |
| **stmc** — Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation | 2024 / CVPR Workshops 2024 | Test-time spatial stitching and temporal score arithmetic operate at every diffusion step. | method | [Paper](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf) · [Audit](notes/papers.md#stmc) |
| **flowmdm** — Seamless Human Motion Composition with Blended Positional Encodings | 2024 | FlowMDM generates temporally composed text-conditioned motion and evaluates transition quality. | method | [Paper](https://arxiv.org/abs/2402.15509) · [Audit](notes/papers.md#flowmdm) · [Code](https://github.com/BarqueroGerman/FlowMDM) |
| **t2lm** — T2LM: Long-Term 3D Human Motion Generation from Multiple Sentences | 2024 | Uses a local 1D-convolutional VQ-VAE decoder to decode a continuous text-predicted latent stream, trained on short clips. | abstract | [Paper](https://arxiv.org/abs/2406.00636) · [Audit](notes/papers.md#t2lm) |
| **amd-autoregressive** — AMD: Autoregressive Motion Diffusion | 2023 | Introduces HumanLong3D and conditions iterative diffusion generation on current text plus previous text and action sequences. | abstract | [Paper](https://arxiv.org/abs/2305.09381) · [Audit](notes/papers.md#amd-autoregressive) |
| **diffcollage** — DiffCollage: Parallel Generation of Large Content with Diffusion Models | 2023 | Factor-graph composition aggregates diffusion outputs over overlapping pieces for large parallel generation, including long text-guided motion. | abstract | [Paper](https://arxiv.org/abs/2303.17076) · [Audit](notes/papers.md#diffcollage) |
| **priormdm** — Human Motion Diffusion as a Generative Prior | 2023 / ICLR 2024 | Introduces DoubleTake sequential composition, ComMDM two-person coordination and DiffusionBlending joint-control model composition. | method | [Paper](https://arxiv.org/abs/2303.01418) · [Audit](notes/papers.md#priormdm) · [Code](https://github.com/priorMDM/priorMDM) |
| **st2m** — Sequential Texts Driven Cohesive Motions Synthesis with Natural Transitions | 2023 / ICCV 2023 | Combines previous/current text semantics with learnable transition tokens and a transition loss. | abstract | [Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.pdf) · [Audit](notes/papers.md#st2m) · [Code](https://github.com/Druthrie/ST2M) |
| **multi-act-2022** — MultiAct: Long-Term 3D Human Motion Generation from Multiple Action Labels | 2022 | Recurrently conditions on prior motion and the next action label to generate transitions and long multi-action sequences. | abstract | [Paper](https://arxiv.org/abs/2212.05897) · [Audit](notes/papers.md#multi-act-2022) · [Code](https://github.com/TaeryungLee/MultiAct_RELEASE) |
| **teach** — TEACH: Temporal Action Composition for 3D Humans | 2022 | Generates ordered action sequences using a hierarchical Transformer: parallel within each action and autoregressive between actions. | abstract | [Paper](https://arxiv.org/abs/2209.04066) · [Audit](notes/papers.md#teach) · [Code](https://github.com/atnikos/teach) |

<a id="spatial"></a>
## Body-part & semantic composition

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **fusion** — FUSION: Full-Body Unified Motion Prior for Body and Hands via Diffusion | 2026 | Unifies body and hand datasets into a full-body motion prior, with optimization-driven object-motion and self-interaction applications. | method | [Paper](https://arxiv.org/abs/2601.03959) · [Audit](notes/papers.md#fusion) |
| **frankenmotion** — FrankenMotion: Part-level Human Motion Generation and Composition | 2026 | Learns hierarchical part/action/sequence-conditioned diffusion instead of test-time pose stitching. | method | [Paper](https://arxiv.org/abs/2601.10909) · [Audit](notes/papers.md#frankenmotion) |
| **mixermdm** — MixerMDM: Learnable Composition of Human Motion Diffusion Models | 2025 | Learns adversarial dynamic mixing of pretrained single-person and interaction diffusion models. | abstract | [Paper](https://arxiv.org/abs/2504.01019) · [Audit](notes/papers.md#mixermdm) |
| **salad** — SALAD: Skeleton-aware Latent Diffusion for Text-driven Motion Generation and Editing | 2025 | Models joint-frame-word relationships and edits generated motion by cross-attention modulation without explicit user masks. | abstract | [Paper](https://arxiv.org/abs/2503.13836) · [Audit](notes/papers.md#salad) |
| **demogen** — Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models | 2025 / CVPR 2026 | Trains compositional scores to reconstruct holistic motion without individual-concept motion targets. | method | [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Towards_Decompositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Models_CVPR_2026_paper.pdf) · [Audit](notes/papers.md#demogen) · [Code](https://github.com/Jiro-zhang/DeMoGen) |
| **coma** — CoMA: Compositional Human Motion Generation with Multi-modal Agents | 2024 / AAAI 2026 | Collaborating language/vision agents control a part-specific masked motion generator and self-correction for detailed long prompts and editing. | abstract | [Paper](https://arxiv.org/abs/2412.07320) · [Audit](notes/papers.md#coma) |
| **energymogen** — EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space | 2024 / CVPR 2025 | Combines latent and text-attention energy formulations for concept conjunction and negation. | method | [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf) · [Audit](notes/papers.md#energymogen) |
| **parco** — ParCo: Part-Coordinating Text-to-Motion Synthesis | 2024 | Separate part tokenizers and lightweight generators communicate through a coordination module. | abstract | [Paper](https://arxiv.org/abs/2403.18512) · [Audit](notes/papers.md#parco) · [Code](https://github.com/qrzou/ParCo) |
| **amd-anatomical** — AMD:Anatomical Motion Diffusion with Interpretable Motion Decomposition and Fusion | 2023 | Parses complex text into anatomical scripts and fuses script and text guidance in diffusion. | abstract | [Paper](https://arxiv.org/abs/2312.12763) · [Audit](notes/papers.md#amd-anatomical) |
| **sinc** — SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation | 2023 / ICCV 2023 | Studies simultaneous actions through body-part motion composition and synthetic training examples. | method | [Paper](https://arxiv.org/abs/2304.10417) · [Audit](notes/papers.md#sinc) |

<a id="editing"></a>
## Motion editing & in-betweening

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **motionlab** — MotionLab: Unified Human Motion Generation and Editing via the Motion-Condition-Motion Paradigm | 2025 | Unifies generation and editing tasks through a motion-condition-motion formulation, including text, trajectory, style and in-between tasks. | abstract | [Paper](https://arxiv.org/abs/2502.02358) · [Audit](notes/papers.md#motionlab) |
| **bamm** — BAMM: Bidirectional Autoregressive Motion Model | 2024 | Bidirectional autoregressive motion-token generation predicts ending and supports completion and long-sequence synthesis. | abstract | [Paper](https://arxiv.org/abs/2403.19435) · [Audit](notes/papers.md#bamm) |
| **infinite-motion** — Infinite Motion: Extended Motion Generation via Long Text Instructions | 2024 | Extends and reassembles text-motion data, using timestamped text for long narrative generation, local editing and independent sequence splicing. | abstract | [Paper](https://arxiv.org/abs/2407.08443) · [Audit](notes/papers.md#infinite-motion) |
| **motionfix** — MotionFix: Text-Driven 3D Human Motion Editing | 2024 | Collects source/target/edit-text triplets and trains TMED conditional diffusion; proposes retrieval-based editing evaluation. | abstract | [Paper](https://arxiv.org/abs/2408.00712) · [Audit](notes/papers.md#motionfix) |
| **motionclr** — Pay Attention and Move Better: Harnessing Attention for Interactive Motion Generation and Training-free Editing | 2024 | MotionCLR explicitly models word-motion correspondence and manipulates attention for interactive generation edits. | abstract | [Paper](https://arxiv.org/abs/2410.18977) · [Audit](notes/papers.md#motionclr) · [Code](https://github.com/IDEA-Research/MotionCLR) |
| **mmm** — MMM: Generative Masked Motion Model | 2023 / CVPR 2024 | Text-conditioned masked motion tokens support in-betweening, body-part changes and long sequence synthesis. | abstract | [Paper](https://arxiv.org/abs/2312.03596) · [Audit](notes/papers.md#mmm) · [Code](https://github.com/exitudio/MMM) |
| **motionclip** — MotionCLIP: Exposing Human Motion Generation to CLIP Space | 2022 | Aligns a motion autoencoder with CLIP text and rendered-image embeddings to support semantic edits and interpolation. | abstract | [Paper](https://arxiv.org/abs/2203.08063) · [Audit](notes/papers.md#motionclip) |
| **holden-deep-motion** — A Deep Learning Framework for Character Motion Synthesis and Editing | 2016 | Convolutional motion manifolds support high-level trajectory generation and optimization for constraints and style transfer. | abstract | [Paper](https://www.research.ed.ac.uk/en/publications/a-deep-learning-framework-for-character-motion-synthesis-and-edit/) · [Audit](notes/papers.md#holden-deep-motion) |

<a id="backbones"></a>
## Generative backbones & representations

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **momask** — MoMask: Generative Masked Modeling of 3D Human Motions | 2023 / CVPR 2024 | Hierarchical residual quantization and masked token generation provide a discrete motion prior with text-guided temporal inpainting. | abstract | [Paper](https://arxiv.org/abs/2312.00063) · [Audit](notes/papers.md#momask) |
| **t2m-gpt** — T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations | 2023 | CNN VQ-VAE with EMA/code reset and a text-conditioned GPT predicts discrete motion tokens. | abstract | [Paper](https://arxiv.org/abs/2301.06052) · [Audit](notes/papers.md#t2m-gpt) |
| **tmr** — TMR: Text-to-Motion Retrieval Using Contrastive 3D Human Motion Synthesis | 2023 / ICCV 2023 | Learns text-motion embeddings using contrastive retrieval and motion synthesis, supplying a retrieval benchmark and evaluator foundation. | abstract | [Paper](https://arxiv.org/abs/2305.00976) · [Audit](notes/papers.md#tmr) · [Code](https://github.com/Mathux/TMR) |
| **mld** — Executing Your Commands via Motion Diffusion in Latent Space | 2022 / CVPR 2023 | MLD compresses motions with a VAE before conditional latent diffusion, substantially reducing denoising cost. | abstract | [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.pdf) · [Audit](notes/papers.md#mld) · [Code](https://github.com/ChenFengYe/motion-latent-diffusion) |
| **mdm** — Human Motion Diffusion Model | 2022 | MDM predicts clean motion samples in diffusion, facilitating geometric losses and text/action conditioning. | abstract | [Paper](https://arxiv.org/abs/2209.14916) · [Audit](notes/papers.md#mdm) |
| **motion-puzzle** — Motion Puzzle: Arbitrary Motion Style Transfer by Body Part | 2022 | Transfers multiple local motion styles to body parts using topology-aware features, AdaIN and attention without style labels or paired motions. | abstract | [Paper](https://arxiv.org/abs/2202.05274) · [Audit](notes/papers.md#motion-puzzle) |
| **motiondiffuse** — MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model | 2022 | Text-conditioned diffusion models human motion and provides a foundation for fine-grained guided synthesis. | abstract | [Paper](https://arxiv.org/abs/2208.15001) · [Audit](notes/papers.md#motiondiffuse) |
| **temos** — TEMOS: Generating diverse human motions from textual descriptions | 2022 | Pairs motion VAE training with a text encoder that predicts compatible latent distributions; generates skeleton or SMPL motion. | abstract | [Paper](https://arxiv.org/abs/2204.14109) · [Audit](notes/papers.md#temos) |
| **actor** — Action-Conditioned 3D Human Motion Synthesis with Transformer VAE | 2021 | ACTOR samples variable-duration SMPL sequences from categorical actions using a Transformer VAE. | abstract | [Paper](https://arxiv.org/abs/2104.05670) · [Audit](notes/papers.md#actor) |
| **skeleton-aware-retarget** — Skeleton-Aware Networks for Deep Motion Retargeting | 2020 | Skeleton-aware convolutions and pooling map homeomorphic skeletons into a common primal-skeleton motion latent space. | abstract | [Paper](https://arxiv.org/abs/2005.05732) · [Audit](notes/papers.md#skeleton-aware-retarget) |
| **unpaired-style** — Unpaired Motion Style Transfer from Video to Animation | 2020 | Separates motion content and style, using AdaIN and shared 2D/3D style embeddings to transfer styles from animations or videos. | abstract | [Paper](https://arxiv.org/abs/2005.05751) · [Audit](notes/papers.md#unpaired-style) |
| **language2pose** — Language2Pose: Natural Language Grounded Pose Forecasting | 2019 | Joint language-to-pose embedding is trained with a short-to-long curriculum for sentence-conditioned animation. | abstract | [Paper](https://arxiv.org/abs/1907.01108) · [Audit](notes/papers.md#language2pose) |
| **plappert-bidirectional** — Learning a bidirectional mapping between human whole-body motion and natural language using deep recurrent neural networks | 2017 | Sequence-to-sequence RNN learns shared continuous language/motion representations without manual motion segmentation. | abstract | [Paper](https://arxiv.org/abs/1705.06400) · [Audit](notes/papers.md#plappert-bidirectional) |

<a id="objects"></a>
## Human-object & articulated interaction

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **cosmi** — COSMI: COmpositional Synthesis of Multi-object Interactions | 2026 | Composes contact-local captured interactions and learns a text-conditioned multi-object diffusion model. | method | [Paper](https://arxiv.org/abs/2610.03252) · [Audit](notes/papers.md#cosmi) |
| **duethoi** — DuetHOI: Language-Guided Bimanual Hand--Object Motion Generation with Articulation Planning and Contact Refinement | 2026 | Contact intent and articulation planning condition structured hand/object generation; proximity refinement fixes objects while correcting hands. | method | [Paper](https://arxiv.org/abs/2603.08390v3) · [Audit](notes/papers.md#duethoi) |
| **trace** — Harnessing Coupled Stream Completion For Human-Object Interaction Modeling | 2026 | TRACE retains body, object and hand latent streams while coupling their updates; decoded geometry constrains contacts and completion supports missing streams. | abstract | [Paper](https://arxiv.org/abs/2609.32551) · [Audit](notes/papers.md#trace) |
| **pami** — PAMI: Part Anchored Motion for Text to Human-Object Interaction Generation | 2026 | Body-part-relative object votes structure a latent interaction model; coarse generation is followed by contact-oriented surface refinement. | abstract | [Paper](https://arxiv.org/abs/2609.38466) · [Audit](notes/papers.md#pami) |
| **sk-hoi** — Surface Keypoint Representation for Multi-Object and Articulated Human-Object Interaction Generation | 2026 | Represents rigid components with surface-keypoint trajectories, predicts spatiotemporal contact-distance fields and synthesizes contact-guided whole-body motion. | method | [Paper](https://arxiv.org/abs/2608.03158) · [Audit](notes/papers.md#sk-hoi) · [Code](https://github.com/neu-vi/SK-HOI) |
| **dechoi** — Decoupled Generative Modeling for Human-Object Interaction Synthesis | 2025 | DecHOI separates goal-conditioned trajectory planning from contact-oriented action generation. | method | [Paper](https://arxiv.org/abs/2512.19049) · [Audit](notes/papers.md#dechoi) |
| **hoifhli** — Human-Object Interaction from Human-Level Instructions | 2025 / ICCV 2025 | Language planning orchestrates contextual full-body manipulation with finger interactions and RL reference tracking. | method | [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_Human-Object_Interaction_from_Human-Level_Instructions_ICCV_2025_paper.pdf) · [Audit](notes/papers.md#hoifhli) |
| **interact** — InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation | 2025 | Consolidates HOI sources, refines artifacts and hands, augments under contact invariance, and benchmarks six generation/completion tasks. | abstract | [Paper](https://arxiv.org/abs/2509.09555) · [Audit](notes/papers.md#interact) · [Code](https://github.com/wzyabcas/InterAct) |
| **interactmove** — InteractMove: Text-Controlled Human-Object Interaction Generation in 3D Scenes with Movable Objects | 2025 | Aligns HOI recordings with scenes containing movable objects and spatial distractors to study text-grounded contextual manipulation. | abstract | [Paper](https://arxiv.org/abs/2509.23612) · [Audit](notes/papers.md#interactmove) |
| **primhoi** — PrimHOI: Compositional Human-Object Interaction via Reusable Primitives | 2025 / ICCV 2025 | Composes relative-geometry interaction primitives spatially and temporally through hierarchical planning, targeting unseen multi-object tasks. | method | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.html) · [Audit](notes/papers.md#primhoi) · [Code](https://github.com/Kairobo/PrimitiveHOI) |
| **himo** — HIMO: A New Benchmark for Full-Body Human Interacting with Multiple Objects | 2024 | Multi-object full-body mocap with text and temporal segments; diffusion branches and autoregressive segments support timeline control. | method | [Paper](https://arxiv.org/abs/2407.12371) · [Audit](notes/papers.md#himo) |
| **cg-hoi** — CG-HOI: Contact-Guided 3D Human-Object Interaction Generation | 2023 | Joint diffusion with cross-attention models human motion, object motion and surface contact; predicted contact guides inference. | abstract | [Paper](https://arxiv.org/abs/2311.16097) · [Audit](notes/papers.md#cg-hoi) |
| **chois** — Controllable Human-Object Interaction Synthesis | 2023 | Joint human/object/contact diffusion combines geometry supervision with contact guidance and connects to planning for extended manipulation. | method | [Paper](https://arxiv.org/abs/2312.03913) · [Audit](notes/papers.md#chois) · [Code](https://github.com/lijiaman/chois_release) |
| **interdiff** — InterDiff: Generating 3D Human-Object Interactions with Physics-Informed Diffusion | 2023 | Interaction diffusion forecasts human/object motion and a physics-informed correction predictor refines denoised interactions. | abstract | [Paper](https://arxiv.org/abs/2308.16905) · [Audit](notes/papers.md#interdiff) |
| **omomo** — Object Motion Guided Human Motion Synthesis | 2023 | Two diffusion stages infer hand positions and full-body manipulation from object motion, with hand contact as an intermediate constraint. | abstract | [Paper](https://arxiv.org/abs/2309.16237) · [Audit](notes/papers.md#omomo) |
| **procigen** — Template Free Reconstruction of Human-object Interaction with Procedural Interaction Generation | 2023 | Procedurally creates varied human-object interaction pairs and trains an image-conditioned reconstruction model for unseen objects. | method | [Paper](https://arxiv.org/abs/2312.07063) · [Audit](notes/papers.md#procigen) |
| **imos** — IMos: Intent-Driven Full-Body Motion Synthesis for Human-Object Interactions | 2022 | Intent-object text encoding and separate variational autoregressors coordinate arms and body for full-body object interaction. | abstract | [Paper](https://arxiv.org/abs/2212.07555) · [Audit](notes/papers.md#imos) · [Code](https://github.com/anindita127/IMoS) |
| **goal** — GOAL: Generating 4D Whole-Body Motion for Hand-Object Grasping | 2021 | GNet predicts a whole-body goal grasp and MNet produces approach motion with coordinated hands, head and body. | abstract | [Paper](https://arxiv.org/abs/2112.11454) · [Audit](notes/papers.md#goal) |
| **saga** — SAGA: Stochastic Whole-Body Grasping with Contact | 2021 | Generates whole-body grasping motions using contact as a coordination signal. | abstract | [Paper](https://arxiv.org/abs/2112.10103) · [Audit](notes/papers.md#saga) |

<a id="scenes"></a>
## Human-scene interaction & planning

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **world2hosi** — World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation | 2026 | Orchestrates navigation, object and scene interaction experts around persistent scene state, reconciling boundaries and updating object effects. | method | [Paper](https://arxiv.org/abs/2610.27725) · [Audit](notes/papers.md#world2hosi) |
| **trumans** — Scaling Up Dynamic Human-Scene Interaction Modeling | 2024 / CVPR 2024 | TRUMANS captures human and part-level dynamic-object interaction across indoor scene configurations; autoregressive diffusion supports extended motion synthesis. | abstract | [Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.pdf) · [Audit](notes/papers.md#trumans) · [Code](https://github.com/hygenie1228/TRUMANS) |
| **circle** — CIRCLE: Capture In Rich Contextual Environments | 2023 | Captures real human movement in perceived virtual scenes and learns scene-conditioned full-body reaching. | abstract | [Paper](https://arxiv.org/abs/2303.17912) · [Audit](notes/papers.md#circle) |
| **scenediffuser** — Diffusion-based Generation, Optimization, and Planning in 3D Scenes | 2023 | SceneDiffuser combines scene-conditioned diffusion with differentiable optimization and goal-oriented planning across human motion, pose, grasp and navigation tasks. | abstract | [Paper](https://arxiv.org/abs/2301.06015) · [Audit](notes/papers.md#scenediffuser) · [Code](https://github.com/scenediffuser/Scene-Diffuser) |
| **occupancy** — Revisit Human-Scene Interaction via Space Occupancy | 2023 | Uses space occupancy to connect locomotion and interaction control; evaluates reaching and extended indoor action sequences. | abstract | [Paper](https://arxiv.org/abs/2312.02700) · [Audit](notes/papers.md#occupancy) |
| **dimos** — Synthesizing Diverse Human Motions in 3D Indoor Scenes | 2023 | DIMOS uses learned motion primitives and scene-aware policies to navigate and perform successive furniture interactions. | method | [Paper](https://arxiv.org/abs/2305.12411) · [Audit](notes/papers.md#dimos) · [Code](https://github.com/zkf1997/DIMOS) |
| **coins** — Compositional Human-Scene Interaction Synthesis with Semantic Control | 2022 | COINS encodes body surface points and objects in a joint latent space, permitting multiple atomic action-object pairs without corresponding composite training examples. | abstract | [Paper](https://arxiv.org/abs/2207.12824) · [Audit](notes/papers.md#coins) · [Code](https://github.com/zkf1997/COINS) |
| **samp** — Stochastic Scene-Aware Motion Prediction | 2021 | Stochastic scene-aware motion generation combines cluttered navigation and diverse target-object interaction styles. | abstract | [Paper](https://arxiv.org/abs/2108.08284) · [Audit](notes/papers.md#samp) |
| **pigraphs** — PiGraphs: Learning Interaction Snapshots from Observations | 2016 | Probabilistic prototype interaction graphs couple body poses, object geometry, contact and visual attention for scene and pose synthesis. | abstract | [Paper](https://graphics.stanford.edu/projects/pigraphs/) · [Audit](notes/papers.md#pigraphs) · [Code](https://github.com/msavva/pigraphs) |

<a id="people"></a>
## Multi-person & collaborative interaction

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **core4d** — CORE4D: A 4D Human-Object-Human Interaction Dataset for Collaborative Object REarrangement | 2025 / CVPR 2025 | Combines real collaborative object rearrangement recordings with collaboration retargeting to additional object shapes. | abstract | [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.pdf) · [Audit](notes/papers.md#core4d) |
| **hhoi-text** — Learning to Generate Human-Human-Object Interactions from Textual Descriptions | 2025 | Integrates individual HOI and HHI diffusion models through a shared sampling framework to synthesize object-mediated multi-human interactions. | abstract | [Paper](https://arxiv.org/abs/2511.20446) · [Audit](notes/papers.md#hhoi-text) |
| **freemotion** — FreeMotion: A Unified Framework for Number-free Text-to-Motion Synthesis | 2024 | Factorizes conditional motion generation into generation and interaction modules to support variable participant counts and spatial controls. | abstract | [Paper](https://arxiv.org/abs/2405.15763) · [Audit](notes/papers.md#freemotion) |
| **intermask** — InterMask: 3D Human Interaction Generation via Collaborative Masked Modeling | 2024 | Collaboratively predicts masked discrete motion tokens for two people and also supports reaction generation. | method | [Paper](https://arxiv.org/abs/2410.10010) · [Audit](notes/papers.md#intermask) |
| **inter-x** — Inter-X: Towards Versatile Human-Human Interaction Analysis | 2023 | Captured full-body interactions with hand gestures and detailed part-level text support perceptual and generative benchmarking. | abstract | [Paper](https://arxiv.org/abs/2312.16051) · [Audit](notes/papers.md#inter-x) · [Code](https://github.com/liangxuy/Inter-X) |
| **intergen** — InterGen: Diffusion-based Multi-human Motion Generation under Complex Interactions | 2023 | Two cooperative weight-sharing denoisers exchange mutual attention to generate coordinated two-person motion from text. | method | [Paper](https://arxiv.org/abs/2304.05684) · [Audit](notes/papers.md#intergen) |
| **remos** — ReMoS: 3D Motion-Conditioned Reaction Synthesis for Two-Person Interactions | 2023 | Spatiotemporal cross-attention generates a second person’s body and hand response to a given actor motion; contributes ReMoCap. | method | [Paper](https://arxiv.org/abs/2311.17057) · [Audit](notes/papers.md#remos) · [Code](https://github.com/anindita127/ReMoS) |

<a id="datasets"></a>
## Datasets & compositional evaluation

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **hiphi** — HiPHI: A Large-Scale Benchmark for High-Precision Human Motion and Object-Interaction | 2026 | Optical whole-body motion and mesh-level object trajectories organized for broad primitive coverage; evaluates diversity, grounding and consistency. | abstract | [Paper](https://arxiv.org/abs/2608.16222) · [Audit](notes/papers.md#hiphi) · [Code](https://github.com/noitom-robotics/hiphi) |
| **robomocap** — RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning | 2026 | Pairs egocentric/wrist observations with optical whole-body capture for locomotion, transport and manipulation; benchmarks reconstruction, foot estimation and retargeting. | abstract | [Paper](https://arxiv.org/abs/2611.10994) · [Audit](notes/papers.md#robomocap) |
| **finemotion** — FineMotion: A Dataset and Benchmark with both Spatial and Temporal Annotation for Fine-grained Motion Generation and Editing | 2025 / ICCV 2025 | Adds aligned body-part descriptions for motion snippets and complete sequences, supporting fine-grained generation and spatial/temporal editing. | abstract | [Paper](https://arxiv.org/abs/2507.19850) · [Audit](notes/papers.md#finemotion) · [Code](https://github.com/CVI-SZU/FineMotion) |
| **motionmillion** — Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data | 2025 / ICCV 2025 | Introduces MotionMillion and MotionMillion-Eval for zero-shot, out-of-domain and complex compositional text-to-motion evaluation with a scalable model. | abstract | [Paper](https://arxiv.org/abs/2507.07095) · [Audit](notes/papers.md#motionmillion) · [Code](https://github.com/VankouF/MotionMillion-Codes) |
| **vimogen-mbench** — The Quest for Generalizable Motion Generation: Data, Model, and Evaluation | 2025 / ICLR 2026 | Combines mocap, web-derived and video-generated motion in ViMoGen-228K; introduces ViMoGen and hierarchical MBench evaluation. | abstract | [Paper](https://arxiv.org/abs/2510.26794) · [Audit](notes/papers.md#vimogen-mbench) · [Code](https://github.com/MotrixLab/ViMoGen) |
| **instructmotion** — Learning Generalizable Human Motion Generator with Reinforcement Learning | 2024 | Uses reinforcement learning and contrastive text-motion rewards on paired data and synthetic text-only prompts to improve generalization. | abstract | [Paper](https://arxiv.org/abs/2405.15541) · [Audit](notes/papers.md#instructmotion) |
| **parahome** — ParaHome: Parameterizing Everyday Home Activities Towards 3D Generative Modeling of Human-Object Interactions | 2024 | Captures full-body, hand, multi-object and articulated-object activity in a home setting, including sequential and concurrent manipulations. | method | [Paper](https://arxiv.org/abs/2401.10232) · [Audit](notes/papers.md#parahome) |
| **motionx** — Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset | 2023 | Provides expressive SMPL-X motion, sequence semantic labels and frame-level descriptions from a scalable video annotation pipeline. | abstract | [Paper](https://arxiv.org/abs/2307.00818) · [Audit](notes/papers.md#motionx) · [Code](https://github.com/IDEA-Research/Motion-X) |
| **best-automated-metric** — What is the Best Automated Metric for Text to Motion Generation? | 2023 / SIGGRAPH Asia 2023 Conference | Studies alignment between automated metrics and human judgments, separating sample-level and average model-level correlation; introduces MoBERT. | abstract | [Paper](https://arxiv.org/abs/2309.10248) · [Audit](notes/papers.md#best-automated-metric) |
| **behave** — BEHAVE: Dataset and Method for Tracking Human Object Interactions | 2022 | Multi-view RGB-D body-object interaction data with body/object fits and contacts across everyday objects and locations. | abstract | [Paper](https://arxiv.org/abs/2204.06950) · [Audit](notes/papers.md#behave) |
| **humanml3d** — Generating Diverse and Natural 3D Human Motions From Text | 2022 / CVPR 2022 | Introduces HumanML3D and a stochastic text-to-motion baseline. | method | [Paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf) · [Audit](notes/papers.md#humanml3d) |
| **intercap** — InterCap: Joint Markerless 3D Tracking of Humans and Objects in Interaction | 2022 | Reconstructs whole-body SMPL-X and known objects from synchronized multi-view RGB-D, using contact cues. | abstract | [Paper](https://arxiv.org/abs/2209.12354) · [Audit](notes/papers.md#intercap) |
| **mocapact** — MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control | 2022 | Provides a multi-task resource for simulated humanoid control and reusable motion-capture skills. | abstract | [Paper](https://arxiv.org/abs/2208.07363) · [Audit](notes/papers.md#mocapact) |
| **babel** — BABEL: Bodies, Action and Behavior with English Labels | 2021 | Adds sequence and temporally localized action language to AMASS, supporting action understanding and temporal composition. | abstract | [Paper](https://arxiv.org/abs/2106.09696) · [Audit](notes/papers.md#babel) |
| **grab** — GRAB: A Dataset of Whole-Body Human Grasping of Objects | 2020 | Marker-based whole-body, articulated hand/face and object trajectories with detailed grasp interaction. | abstract | [Paper](https://arxiv.org/abs/2008.11200) · [Audit](notes/papers.md#grab) · [Code](https://github.com/otaheri/GRAB) |
| **amass** — AMASS: Archive of Motion Capture as Surface Shapes | 2019 | Unifies heterogeneous optical mocap collections through MoSh++ and a common parametric body surface representation. | abstract | [Paper](https://arxiv.org/abs/1904.03278) · [Audit](notes/papers.md#amass) |
| **kitml** — The KIT Motion-Language Dataset | 2016 | Aggregates mocap in a capture-independent representation with crowdsourced natural-language descriptions. | abstract | [Paper](https://arxiv.org/abs/1607.03827) · [Audit](notes/papers.md#kitml) |

<a id="physics"></a>
## Physics-based character control

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **maskadapt** — MaskAdapt: Learning Flexible Motion Adaptation via Mask-Invariant Prior for Physics-Based Characters | 2026 | Mask-invariant base policy plus residual adaptation enables multi-part composition and text-driven partial tracking. | abstract | [Paper](https://arxiv.org/abs/2603.29272) · [Audit](notes/papers.md#maskadapt) |
| **simdiff** — SimDiff: Simulator-constrained Diffusion Model for Physically Plausible Motion Generation | 2025 | Conditions diffusion on environment coefficients and reports unseen combinations of environmental parameters. | abstract | [Paper](https://arxiv.org/abs/2509.20927) · [Audit](notes/papers.md#simdiff) |
| **closd** — CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control | 2024 | Closes a feedback loop between an autoregressive text/target-conditioned diffusion planner and an RL tracker for task sequences. | abstract | [Paper](https://arxiv.org/abs/2410.03441) · [Audit](notes/papers.md#closd) |
| **mhc** — Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots | 2024 | Masked-motion curriculum learns multimodal control and combines joystick locomotion with partial-body mimicry. | abstract | [Paper](https://arxiv.org/abs/2408.07295) · [Audit](notes/papers.md#mhc) |
| **maskedmimic** — MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | 2024 | Unifies masked keyframes, objects, text and mixed descriptions as partial motion constraints for simulated character control. | abstract | [Paper](https://arxiv.org/abs/2409.14393) · [Audit](notes/papers.md#maskedmimic) |
| **diffmimic** — DiffMimic: Efficient Motion Mimicking with Differentiable Physics | 2023 | Uses differentiable physics for efficient reference motion imitation. | abstract | [Paper](https://arxiv.org/abs/2304.03274) · [Audit](notes/papers.md#diffmimic) |
| **phc** — Perpetual Humanoid Control for Real-time Simulated Avatars | 2023 / ICCV 2023 | Scales physics-based imitation with recovery from falls and noisy reference motion. | method | [Paper](https://arxiv.org/abs/2305.06456) · [Audit](notes/papers.md#phc) · [Code](https://github.com/ZhengyiLuo/PHC) |
| **pulse** — Universal Humanoid Motion Representations for Physics-Based Control | 2023 | Distills a broad motion imitator into a variational latent representation with proprioception-conditioned prior for downstream hierarchical RL. | abstract | [Paper](https://arxiv.org/abs/2310.04582) · [Audit](notes/papers.md#pulse) |
| **ase** — ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters | 2022 | Learns reusable latent motor skills from unsegmented motion using adversarial imitation and unsupervised RL. | abstract | [Paper](https://arxiv.org/abs/2205.01906) · [Audit](notes/papers.md#ase) |
| **amp** — AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control | 2021 | Learns motion-style rewards from unstructured clips alongside task rewards; reports emergent skill composition. | abstract | [Paper](https://arxiv.org/abs/2104.02180) · [Audit](notes/papers.md#amp) |
| **deepmimic** — DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills | 2018 | Combines motion imitation and task objectives for simulated skills, recovery and multi-clip agents. | abstract | [Paper](https://arxiv.org/abs/1804.02717) · [Audit](notes/papers.md#deepmimic) |

<a id="humanoids"></a>
## Humanoid transfer & loco-manipulation

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **grail** — GRAIL: Generating Humanoid Loco-Manipulation from World Models | 2026 | Grounds generated videos in known 3D scenes/assets, recovers HOI, retargets and trains trackers and visual policies. | abstract | [Paper](https://arxiv.org/abs/2606.05160) · [Audit](notes/papers.md#grail) |
| **intermimicgen** — InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation | 2026 | Retargets heterogeneous HOI, learns a generalist simulation tracker and iteratively retains task-preserving perturbations that execute successfully. | abstract | [Paper](https://arxiv.org/abs/2610.06850) · [Audit](notes/papers.md#intermimicgen) |
| **weave** — Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions | 2026 | Contact-aware retargeting and approach completion feed a geometry/contact-aware whole-body and finger controller; releases simulated robot-object rollouts. | method | [Paper](https://arxiv.org/abs/2609.16683) · [Audit](notes/papers.md#weave) |
| **beyondmimic** — BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion | 2025 | Combines robust motion tracking with a distilled diffusion policy and test-time cost guidance for navigation and control. | abstract | [Paper](https://arxiv.org/abs/2508.08241) · [Audit](notes/papers.md#beyondmimic) |
| **gmr** — Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking | 2025 | Studies how retargeting quality affects BeyondMimic tracking on LAFAN1 and introduces GMR. | abstract | [Paper](https://arxiv.org/abs/2510.02252) · [Audit](notes/papers.md#gmr) · [Code](https://github.com/YanjieZe/GMR) |
| **exbody** — Expressive Whole-Body Control for Humanoid Robots | 2024 | Tracks upper-body expression while lower-body velocity control enables robust locomotion, with real robot demonstrations. | abstract | [Paper](https://arxiv.org/abs/2402.16796) · [Audit](notes/papers.md#exbody) · [Code](https://github.com/chengxuxin/expressive-humanoid) |

<a id="audio"></a>
## Audio, dance & gesture composition

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **cfgcomposer** — CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction | 2026 | Composes audio and text motion diffusion scores while learning a cross-modal correction for their dependence; relevant to model-level composition beyond text-only actions. | abstract | [Paper](https://arxiv.org/abs/2611.15101) · [Audit](notes/papers.md#cfgcomposer) |
| **moco** — Multi-Modal Controlled Coherent Motion Generation | 2026 / ECCV 2026 | Combines text, speech and trajectory denoisers by body region and recurrently assembles a holistic motion at each diffusion step. | method | [Paper](https://feifeifeiliu.github.io/MOCO/) · [Audit](notes/papers.md#moco) |
| **emage** — EMAGE: Towards Unified Holistic Co-Speech Gesture Generation via Expressive Masked Audio Gesture Modeling | 2024 | Audio and masked gesture hints drive holistic face/body/hand/global motion with compositional quantized priors; introduces BEAT2. | abstract | [Paper](https://arxiv.org/abs/2401.00374) · [Audit](notes/papers.md#emage) |
| **lodge** — Lodge: A Coarse to Fine Diffusion Network for Long Dance Generation Guided by the Characteristic Dance Primitives | 2024 | Global diffusion generates characteristic dance primitives; parallel local diffusion expands them into detailed long sequences, with a foot refinement component. | abstract | [Paper](https://arxiv.org/abs/2403.10518) · [Audit](notes/papers.md#lodge) |
| **edge** — EDGE: Editable Dance Generation From Music | 2022 | Music-conditioned diffusion supports joint-wise constraints and temporal in-betweening, connecting body-part control with long dance editing. | abstract | [Paper](https://arxiv.org/abs/2211.10658) · [Audit](notes/papers.md#edge) |
| **finedance** — FineDance: A Fine-grained Choreography Dataset for 3D Full Body Dance Generation | 2022 | Full-body music-dance dataset with detailed hand motion and dance genres; its retrieval and generation mechanisms provide an adjacent composition setting. | abstract | [Paper](https://arxiv.org/abs/2212.03741) · [Audit](notes/papers.md#finedance) |

<a id="surveys"></a>
## Surveys & field maps

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **interaction-survey** — A Survey on Human Interaction Motion Generation | 2025 | Organizes human-human, human-object and human-scene generation with datasets and evaluation; useful for backward citation chasing across interaction types. | abstract | [Paper](https://arxiv.org/abs/2503.12763) · [Audit](notes/papers.md#interaction-survey) |
| **video-motion-survey** — Human Motion Video Generation: A Survey | 2025 | Adjacent literature: surveys human-motion video generation, including planning, generation and refinement across visual, text and audio conditions. | abstract | [Paper](https://arxiv.org/abs/2509.03883) · [Audit](notes/papers.md#video-motion-survey) · [Code](https://github.com/Winn1y/Awesome-Human-Motion-Video-Generation) |
| **generative-survey** — Motion Generation: A Survey of Generative Approaches and Benchmarks | 2025 | Reviews generative model families, conditioning, datasets and metrics, emphasizing recent motion-generation literature. | abstract | [Paper](https://arxiv.org/abs/2507.05419) · [Audit](notes/papers.md#generative-survey) |
| **text-motion-overview** — Text-driven Motion Generation: Overview, Challenges and Directions | 2025 | Reviews text-to-motion through architecture and discrete/continuous representation perspectives. | abstract | [Paper](https://arxiv.org/abs/2505.09379) · [Audit](notes/papers.md#text-motion-overview) |

<a id="video"></a>
## Adjacent: compositional human video

| Paper | First public / venue | Why it belongs | Evidence | Links |
|---|---|---|---|---|
| **realis-motion** — RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space | 2026 | Separates subject, background, world-space trajectory and action controls for human video composition. | abstract | [Paper](https://proceedings.mlr.press/v306/liang26ad.html) · [Audit](notes/papers.md#realis-motion) |

## Citation and reuse

Use [references.bib](references.bib) for the exact cited version. Some older author pages only support a minimal curated record; these are explicitly flagged in [audit.json](audit.json). Verify venue-specific formatting before submission. No paper PDFs, datasets or weights are mirrored.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep primary-source provenance, preserve negative and unknown evidence, and rebuild generated views from the structured records.
