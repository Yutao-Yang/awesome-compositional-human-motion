# Paper audit cards

Checked: 2026-11-19. Evidence levels describe reading, not reproduction. Curator boundaries are comparison guidance.

<a id="parametric-motion-graphs"></a>
## Parametric Motion Graphs

**parametric-motion-graphs · 2007 · Classical motion composition · method**

[Primary source](https://graphics.cs.wisc.edu/Papers/2007/HG07/) · [Evidence](https://graphics.cs.wisc.edu/Papers/2007/HG07/PMGFullPaper.pdf) · Citekey: `parametricmotiongraphs2007`

**Authors of cited version:** Rachel Heck; Michael Gleicher.

**Contribution / composition:** Each graph node represents a continuous parameterized motion space constructed by blending aligned examples. Offline sampling finds acceptable transition regions between spaces and stores interpolation structures; runtime queries synthesize a clip and a compatible linear-blend transition rather than merely replaying a discrete edge.

**Mechanism:** Each graph node represents a continuous parameterized motion space constructed by blending aligned examples. Offline sampling finds acceptable transition regions between spaces and stores interpolation structures; runtime queries synthesize a clip and a compatible linear-blend transition rather than merely replaying a discrete edge.

**Input contract:** User-selected action and continuous controls such as travel curvature, punch target, duck height, platform height, and current character state. Action-specific functions translate joystick requests into graph parameters; feasible transition bounds can constrain the requested target.

**Data and split:** Not applicable as a statistical train/test benchmark. Example-based authoring uses separate action collections; the general traversal graph organizes 256 examples and the boxing graph 275 examples into three nodes. No held-out subject or combination protocol is reported.

**Evaluation metrics:** Transition similarity thresholds define acceptable edges. Reported engineering measurements include per-edge construction time (2–147 seconds), complete graph construction time, and storage below 50 KB; there is no modern FID or standardized quantitative naturalness score.

**Evaluation checked:** Sections 5.1–5.2 demonstrate locomotion, mixed traversal, boxing, random walks, searches, and interactive control. The boxing graph has nine edges and takes about 7 minutes 40 seconds to construct; visual examples establish the demonstrated scope rather than measured unseen-composition generalization.

**Full-text source:** https://graphics.cs.wisc.edu/Papers/2007/HG07/PMGFullPaper.pdf

**Reading status:** full_text_checked

**Inspected version:** Official primary PDF fetched 2026-11-19; file SHA-256 retained in private audit receipt.

**Full-text SHA256:** efbb0efd7d9f50960a46e67d5952f3d19f08b195eeb4f979e038a3b399f93979

**Source locator:** §§3.1–3.3 (transition construction), §4 (runtime extraction), §§5.1–5.2 and Figures 6,10 (examples/timing), §6 (limitations).

**Scope / curator boundary:** Smooth parameter spaces and suitable examples are required. An edge cannot represent a source space containing any motion unable to transition to the target; restricting transitions can miss user targets. Linear blending is not a contact-force or dynamics certificate.

**Composition axes:** temporal.

**Metadata:** official; [source](https://graphics.cs.wisc.edu/Papers/2007/HG07/); checked 2026-11-19.

<a id="motion-annotations"></a>
## Motion Synthesis from Annotations

**motion-annotations · 2003 · Classical motion composition · method**

[Primary source](https://escholarship.org/uc/item/23g204tp) · [Evidence](https://jamesobrien.com/papers/Arikan-MSF-2003-08/Arikan-MSF-2003-08.pdf) · Citekey: `motionannotations2003`

**Authors of cited version:** Okan Arikan; David A. Forsyth; James F. O'Brien.

**Contribution / composition:** Uses annotated action timelines and multiscale dynamic programming to assemble motion, including overlapping qualitative constraints.

**Mechanism:** SVM-assisted labeling propagates sparse manual action annotations. Multiscale dynamic programming then selects motion blocks that match a requested timeline while minimizing discontinuity, followed by finer boundary and motion refinement.

**Input contract:** User-painted positive, negative or unconstrained action labels on a timeline, plus optional timed pose, root-position and orientation constraints. Vocabulary is chosen by the animator rather than fixed natural-language task understanding.

**Data and split:** Uses a small annotated motion database, approximately seven minutes in the reported annotation exercise. SVM annotation propagation uses a manually labeled subset with interactive corrections. No held-out actor/action-combination benchmark or train/test percentage is reported for synthesis.

**Evaluation metrics:** Annotation matching and motion-continuity objectives, interactive synthesis behavior, visual naturalness and low-level constraint satisfaction. Annotation speed is demonstrated; no standardized distributional generation or independent physics metric is reported.

**Evaluation checked:** Sections 3–6 demonstrate combinations such as running with jumping or waving and enforced key poses. Coarse-to-fine optimization improves solutions interactively; examples test overlapping qualitative requirements rather than a controlled statistical generalization benchmark.

**Full-text source:** https://jamesobrien.com/papers/Arikan-MSF-2003-08/Arikan-MSF-2003-08.pdf

**Reading status:** full_text_checked

**Inspected version:** Proceedings/author PDF as retrieved 2026-11-19; no printed own-paper arXiv version found.

**Full-text SHA256:** cf9eba6cb88ce07d3f3f3cb282ab8558f751793fc998297927095301b9eb93ac

**Source locator:** Sections 2–3 (annotations/synthesis), 4–5 (search/smoothing), 6 (Results); Figures 1, 5–7.

**Scope / curator boundary:** Cannot invent frames or transitions absent from the database. Incompatible requirements trade annotation satisfaction against continuity, and smoothing may change duration. Painted labels do not supply unseen contact geometry or physical execution.

**Composition axes:** temporal.

**Metadata:** primary-transcribed; [source](https://escholarship.org/uc/item/23g204tp); checked 2026-11-19.

<a id="interactive-motion-examples"></a>
## Interactive motion generation from examples

**interactive-motion-examples · 2002 · Classical motion composition · method**

[Primary source](https://experts.illinois.edu/en/publications/interactive-motion-generation-from-examples/) · [Evidence](https://www.cs.toronto.edu/~jacobson/seminar/arikan-and-forsyth-2002.pdf) · Citekey: `interactivemotionexamples2002`

**Authors of cited version:** Okan Arikan; D. A. Forsyth.

**Contribution / composition:** Cuts and pastes mocap via randomized hierarchical graph search under constraints at interactive speeds.

**Mechanism:** Builds a directed graph over captured motion frames, with transitions scored by pose and velocity compatibility. A hierarchy clusters similar transition alternatives; randomized mutation searches coarse graph paths and progressively refines them into reusable clip sequences. Constraint costs guide selection, while blending and postprocessing address local discontinuities.

**Input contract:** Animator specifies duration and timed body positions, orientation, joint states or whole-body poses. Coordinated characters can be constrained at interaction poses; this is explicit constraint authoring rather than language-conditioned generation.

**Data and split:** No supervised train/validation/test partition applies to graph construction. Demonstrations use roughly 60–80 short motion recordings; scalability is discussed for databases of 50–100 motions. An independently held-out compositional test set is not reported.

**Evaluation metrics:** Visual human-likeness, foot slipping/jerk inspection, constraint satisfaction, synthesis latency and graph preprocessing time; no FID, contact accuracy or statistical generalization metric.

**Evaluation checked:** Section 5 reports acceptable 300-frame solutions in approximately 3–10 seconds on the stated Pentium III machine. Examples combine several source pieces and include constrained interactions; judgments are principally demonstrative rather than a controlled perceptual benchmark.

**Full-text source:** https://www.cs.toronto.edu/~jacobson/seminar/arikan-and-forsyth-2002.pdf

**Reading status:** full_text_checked

**Inspected version:** Author/institution or proceedings PDF as retrieved 2026-11-19; version string not printed for this paper.

**Full-text SHA256:** f115e74b6c496c4dfcf13a291d5fd2a014d9db9721d55c33d31f5c8628f9598f

**Source locator:** Sections 3–4 (graph/hierarchical search), Section 5 (Results), Appendix A (transition cost).

**Scope / curator boundary:** Database coverage directly limits feasible actions. Randomized search is not a completeness guarantee, and visually acceptable transition costs do not establish physical consistency or arbitrary interaction synthesis.

**Composition axes:** temporal.

**Metadata:** official; [source](https://experts.illinois.edu/en/publications/interactive-motion-generation-from-examples/); checked 2026-11-19.

<a id="motion-graphs"></a>
## Motion Graphs

**motion-graphs · 2002 · Classical motion composition · method**

[Primary source](https://graphics.cs.wisc.edu/Papers/2002/KGP02/) · [Evidence](https://graphics.cs.wisc.edu/Papers/2002/KGP02/mograph.pdf) · Citekey: `motiongraphs2002`

**Authors of cited version:** Lucas Kovar; Michael Gleicher; Frédéric Pighin.

**Contribution / composition:** Builds a directed graph of captured clips and synthesized transitions; graph walks satisfy user constraints such as locomotion paths.

**Mechanism:** Constructs a directed graph whose edges are captured motion fragments and synthesized transitions. Candidate connections minimize aligned point-cloud distances over temporal windows, with floor-plane translation/yaw factored out. Locally similar windows are blended, constraint labels are propagated, and problematic graph portions are pruned. Branch-and-bound graph search then minimizes an application-specific additive objective; footplant constraints can be enforced after extraction.

**Input contract:** A captured motion database, optional action/constraint labels, a desired planar path, and restrictions on action types along portions of the path.

**Data and split:** No learned train/validation/test split: demonstrations reuse a finite motion library. Largest example has approximately 6,000 frames/200 seconds; other graphs contain about 3,000 frames.

**Evaluation metrics:** Path-fitting objective measures deviation between requested and synthesized paths. Reports construction/search wall time and animation duration; no FID, semantic retrieval benchmark, or statistical user-study score.

**Evaluation checked:** Section 5 demonstrates walking, sneaking, martial arts and constrained changes between these styles. A 12.8-second sneaking capture plus its mirror yields alternative paths. The walking Hello example needs 58.1 seconds computation for 54.9 seconds animation.

**Full-text source:** https://graphics.cs.wisc.edu/Papers/2002/KGP02/mograph.pdf

**Reading status:** full_text_checked

**Inspected version:** Primary author/proceedings PDF retrieved 2026-11-19; identity fixed by SHA256

**Full-text SHA256:** 314cdb4ffe999411ffe446ddb3cfdf25d59e148dce001ad40723a3406bd5b5cb

**Source locator:** Sections 3.1–3.4, 4.1–4.2, 5.1–5.2 and 6; Figures 6–8.

**Scope / curator boundary:** Transition thresholds require manual selection and can be laborious across diverse movements. Candidate comparison costs quadratically many frame pairs. Only nearby motions admit simple reliable blends; sparse connectivity and source-library coverage bound possible behaviors. Demonstrations do not establish unseen task composition or object-aware manipulation.

**Composition axes:** temporal.

**Metadata:** official; [source](https://graphics.cs.wisc.edu/Papers/2002/KGP02/); checked 2026-11-19.

<a id="prism"></a>
## PRISM: Per-unit Kinematic Motion Generation in a Structured Latent Manifold

**prism · 2026 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2603.08590) · [Evidence](https://arxiv.org/pdf/2603.08590v4) · Citekey: `prism2026`

**Authors of cited version:** Zeyu Ling; Qing Shuai; Teng Zhang; Shiyang Li; Bo Han; Changqing Zou.

**Contribution / composition:** The inspected revision uses a causal temporal VAE with separate kinematic-unit latent tokens, a joint/time structured flow generator, kinematic-tree rotary positional encoding, and depth-dependent flow sampling. A clean-context mask provides prefix continuation and successive segment generation with one frozen generator.

**Mechanism:** The inspected revision uses a causal temporal VAE with separate kinematic-unit latent tokens, a joint/time structured flow generator, kinematic-tree rotary positional encoding, and depth-dependent flow sampling. A clean-context mask provides prefix continuation and successive segment generation with one frozen generator.

**Input contract:** Text and optional clean initial pose frames; long narratives are decomposed into ordered captions and durations shared across compared generators. The evaluated prefix lengths are 1, 5, and 9 frames. Arbitrary body-part or scattered-frame control is explicitly future work.

**Data and split:** Trained on approximately 200,000 public MotionHub SMPL(-X) motion-text pairs; evaluates the HumanML3D split and FlowMDM BABEL protocol, plus 50 narratives in 10 categories containing 4–10 actions. Exact training-source group proportions are not reported in the inspected experimental description.

**Evaluation metrics:** TMR-based R-Precision and MM-Distance measure semantic correspondence; FID measures feature-distribution differences; Diversity measures variability. BABEL transition FID evaluates boundaries. Shared-skeleton slide, float, and jitter errors probe kinematic artifacts; narrative rankings measure human preferences.

**Evaluation checked:** Tables I–IV compare text generation, prefix conditioning, BABEL episodes, and reconstruction; matched 1D/2D, positional-encoding, and sampler ablations isolate design choices. Narrative outputs use frozen common plans and tie-aware ranking. This is paper-reported evidence, not an independent rerun.

**Full-text source:** https://arxiv.org/pdf/2603.08590v4

**Reading status:** full_text_checked

**Inspected version:** arXiv:2603.08590v4 [cs.CV] 24 Aug 2026

**Full-text SHA256:** d10db9f8bd269f1e85af5bc19dc8a0c77b632f31c2d73cd99df3fa0ba25eb065

**Source locator:** §III (causal kinematic-unit VAE, KU-FlowT, KT-RoPE, KAFS), §IV.A–G and Tables I–VIII; Appendix A shared TMR protocol and Appendix B narrative composition/user-study setup; §VI limitations.

**Scope / curator boundary:** The current PDF is retitled PRISM: Per-Unit Kinematic Motion Generation in a Structured Latent Manifold, so earlier streaming-title claims need revision alignment. SMPL body coverage excludes expressive hands/face; full object-conditioned interaction and dynamics are not evaluated.

**Publication / version note:** The inspected v4 PDF is retitled from "PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition". The official BibTeX endpoint still returns that earlier title; this record transcribes the v4 title page and pins the citation to v4.

**Composition axes:** temporal.

**Metadata:** primary-transcribed; [source](https://arxiv.org/pdf/2603.08590v4); checked 2026-11-19.

<a id="timelinecontrol"></a>
## Streaming Multi-Track Timeline Control for 3D Human Motion Generation

**timelinecontrol · 2026 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2610.03873) · [Evidence](https://arxiv.org/pdf/2610.03873v2) · Citekey: `timelinecontrol2026`

**Authors of cited version:** Yangsong Zhang; Anujith Muraleedharan; Rikhat Akizhanov; Gül Varol; Fabio Pizzati; Ivan Laptev.

**Contribution / composition:** TimelineControl combines interval-aware conditioning, causal part representations and part-aware denoising with TimelineMotion annotations.

**Mechanism:** Combines interval-aware instruction encoding with causal, anatomically factored motion features and a part-aware streaming denoiser. Instruction tokens retain their start/end times; learned body-part relevance biases cross-attention. The TimelineMotion construction stitches compatible HumanML3D clips with STMC, then refines boundaries and filters abrupt translation or jitter.

**Input contract:** Incrementally received text instructions with overlapping intervals and body-part relevance; optional spatial targets. Future instructions unavailable at a streaming instant are excluded from conditioning.

**Data and split:** TimelineMotion contains 44,944 synthetic sequences. Source clips for each timeline come from the same HumanML3D partition, preserving its split membership. Evaluates TimelineMotion and MTT test sets plus HumanML3D; exact partition proportions are not restated in the inspected protocol.

**Evaluation metrics:** TMR R-Precision, motion-to-text similarity M2T, source similarity M2M, FID/FID+, transition distance, Temporal AP and ROC-AUC for interval adherence; human preference and control-target errors.

**Evaluation checked:** Compares offline STMC and streaming baselines, including ActionPlan retrained on matching data. Tables 1–4 isolate interval conditioning, skeletal structure, part bias and denoising branches; Appendix C checks temporal-score sensitivity to shifted intervals.

**Full-text source:** https://arxiv.org/pdf/2610.03873v2

**Reading status:** full_text_checked

**Inspected version:** 2610.03873v2

**Full-text SHA256:** 80a46e332c3db90fa2683d64a7f53655bd9916d4c08cade79c8c7fe9e9cb93be

**Source locator:** Sections 4.1–4.4; Sections 5.1–5.4, Tables 1–4; Appendices A and C (data/protocol).

**Scope / curator boundary:** Synthetic compositional references inherit source and stitching biases. Demonstrated streaming alignment is bounded by evaluated instructions; humanoid examples do not establish general autonomous manipulation or independent physical certification.

**Composition axes:** spatial, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.03873); checked 2026-11-19.

<a id="dart"></a>
## DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control

**dart · 2024 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2410.05260) · [Evidence](https://arxiv.org/pdf/2410.05260v3) · Citekey: `dart2025`

**Authors of cited version:** Kaifeng Zhao; Gen Li; Siyu Tang.

**Contribution / composition:** Latent diffusion predicts motion primitives from history and current text; noise optimization or RL provides spatial control.

**Mechanism:** Learns a history-conditioned motion-primitive VAE and text/history-conditioned latent diffusion model. Each primitive contains two history frames and eight generated frames, canonicalized around the pelvis. Scheduled autoregressive training mitigates rollout mismatch. Spatial control operates through latent-noise optimization, or a separately trained reinforcement-learning policy whose actions select latent noise; this differs from training a physics-based low-level humanoid controller.

**Input contract:** An initial motion seed, an ordered stream of text prompts with durations, and optional goals, trajectories or scene geometry for the chosen control application.

**Data and split:** BABEL training recordings train the default model; temporal composition evaluates its released validation set because its test set is unavailable. HumanML3D experiments use only records with available SMPL motion, excluding joint-only/mirrored sources; exact retained counts are not given in Appendix B.

**Evaluation metrics:** FID, R-precision, MM-DIST and diversity assess segments; peak jerk and area under jerk assess 30-frame transition windows. Also reports latency, frames/second, memory, reach time/success, foot skating and foot-floor distance.

**Evaluation checked:** Compares TEACH, DoubleTake, history-conditioned T2M-GPT and FlowMDM; profiles 5,000-frame generation and conducts perceptual comparisons. Optimization and RL goal-reaching are evaluated separately.

**Full-text source:** https://arxiv.org/pdf/2410.05260v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2410.05260v3

**Full-text SHA256:** 16c2579e2e969f131d267dfdff33b744531dd558baaa2a07bd708ea49d9f3127

**Source locator:** Sections 3.1–3.3, 4.1–4.3; Tables 1–4; Appendices B, E and G.

**Scope / curator boundary:** Short local history and a kinematic generative prior do not certify physical execution. HumanML3D subset differences matter for comparison. Goal-reaching results concern the demonstrated control setup, not general dexterous object manipulation or arbitrary scene-task completion.

**Publication / version note:** First public preprint 2024. First public preprint 2024.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.05260); checked 2026-11-19.

<a id="motion-mamba"></a>
## Motion Mamba: Efficient and Long Sequence Motion Generation

**motion-mamba · 2024 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2403.07487) · [Evidence](https://arxiv.org/pdf/2403.07487v4) · Citekey: `motionmamba2024`

**Authors of cited version:** Zeyu Zhang; Akide Liu; Ian Reid; Richard Hartley; Bohan Zhuang; Hao Tang.

**Contribution / composition:** Motion Mamba replaces expensive denoising sequence operations with state-space blocks. Hierarchical Temporal Mamba varies temporal scan depth across the U-shaped network, while Bidirectional Spatial Mamba scans pose features in both directions to couple spatial channels and temporal dependencies.

**Mechanism:** Motion Mamba replaces expensive denoising sequence operations with state-space blocks. Hierarchical Temporal Mamba varies temporal scan depth across the U-shaped network, while Bidirectional Spatial Mamba scans pose features in both directions to couple spatial channels and temporal dependencies.

**Input contract:** Natural-language embeddings condition a diffusion motion generator; sequence duration follows benchmark generation settings. This is a text-to-motion backbone, without an explicit ordered action schedule, object mesh, scene map, or manipulation contact constraints as core input.

**Data and split:** HumanML3D and KIT-ML follow the standard text-motion evaluation protocol. The paper does not restate exact train/validation/test proportions in §4.1. HumanML3D-LS selects original evaluation motions longer than 190 frames; this is a length slice, not a held-out action-combination split.

**Evaluation metrics:** FID measures learned motion-feature distribution mismatch; R-Precision and MM-Distance measure text-motion alignment; Diversity and Multimodality measure overall and same-prompt variation. Average inference time measures latency on a single V100. Evaluations repeat 20 times with 95% confidence intervals.

**Evaluation checked:** Tables 1–2 benchmark HumanML3D and KIT-ML, Table 3 tests the long-sequence slice, and Table 4 ablates temporal scans, spatial scans, latent size, and depth. Qualitative examples and a user study supplement numerical and speed comparisons.

**Full-text source:** https://arxiv.org/pdf/2403.07487v4

**Reading status:** full_text_checked

**Inspected version:** arXiv:2403.07487v4 [cs.CV] 3 Aug 2024

**Full-text SHA256:** 37660be61a5100d6992ea911fc7a2a8f6dcf3d3d51893880f71454650c95e65c

**Source locator:** §3 and Figure 2 (HTM/BSM architecture), §§4.1–4.5, Tables 1–4, Figure 4 (V100 latency).

**Scope / curator boundary:** The long-sequence experiment concerns single-description benchmark clips and cannot establish arbitrary multi-prompt temporal composition. Motion-feature scores and short generation latency do not establish contact correctness, scene compatibility, or full-body physical executability.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.07487); checked 2026-11-19.

<a id="stmc"></a>
## Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation

**stmc · 2024 · Temporal composition & long sequences · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf) · Citekey: `stmc2024`

**Authors of cited version:** Petrovich, Mathis; Litany, Or; Iqbal, Umar; Black, Michael J.; Varol, Gul; Bin Peng, Xue; Rempe, Davis.

**Contribution / composition:** Test-time spatial stitching and temporal score arithmetic operate at every diffusion step.

**Mechanism:** Preprocesses prompts into per-body-part timelines; denoises local crops and combines corresponding pose components repeatedly during sampling.

**Input contract:** Multiple texts with explicit time intervals and body-part assignments, supplied manually or inferred with GPT-3. Compatible overlapping part responsibilities are required; the motion is jointly assembled at every denoising step.

**Data and split:** Backbone models train on HumanML3D. MDM-SMPL excludes HumanAct12 because pose parameters are unavailable. MTT is a manually designed evaluation-only timeline set with atomic text/source-motion references; no newly trained timeline partition or train/test percentage applies to STMC itself.

**Evaluation metrics:** TMR R@1/R@3, motion-to-text M2T and motion-to-motion M2M similarity; FID+ uses five random five-second crops per generated timeline, and transition distance measures local consecutive-pose boundary jumps.

**Evaluation checked:** Table 1 compares single-text, single-track and multi-track sampling with several denoisers. A filtered pairwise human study evaluates one hundred motions for realism and instruction adherence. Improvements are evaluated separately for semantics and transitions, avoiding an aggregate claim of physical correctness. The composition procedure updates all local denoising crops repeatedly rather than stitching final outputs once.

**Full-text source:** https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Proceedings/author PDF as retrieved 2026-11-19; no printed own-paper arXiv version found.

**Full-text SHA256:** b7ee8f2fe147e5862158b74271f6f81215ce76477a47d29712b9a3f26a168473

**Source locator:** Sections 3.1–3.4, 4.1–4.6; Table 1 and user-study protocol.

**Scope / curator boundary:** Inherits base-model failures, unfamiliar stitched poses and imperfect timing. Incompatible parts remain problematic; long-motion TMR embeddings are unreliable, motivating cropped FID+. Contact mechanics and persistent object state are not modeled.

**Composition axes:** spatial, temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/html/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.html); checked 2026-11-19.

<a id="flowmdm"></a>
## Seamless Human Motion Composition with Blended Positional Encodings

**flowmdm · 2024 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2402.15509) · [Evidence](https://arxiv.org/pdf/2402.15509v1) · Citekey: `flowmdm2024`

**Authors of cited version:** German Barquero; Sergio Escalera; Cristina Palmero.

**Contribution / composition:** FlowMDM generates temporally composed text-conditioned motion and evaluates transition quality.

**Mechanism:** Early denoising uses absolute positions for within-action structure; late denoising uses relative positions across boundaries. Pose-centric cross-attention associates each frame with its own condition.

**Input contract:** Ordered text descriptions and durations, expanded to frame-specific conditions. Pose-centric cross-attention associates each frame with its own prompt while the denoising process changes positional-encoding regime.

**Data and split:** Uses the standard BABEL and HumanML3D training/test divisions; exact partition proportions are not restated in Section 4.1. BABEL training may include consecutive annotated actions; HumanML3D lacks explicit transition annotations. Evaluation composes thirty-two sampled text-duration pairs per long sequence.

**Evaluation metrics:** Subsequence R-Precision, matching distance, FID, diversity/multimodality; transition FID, Peak Jerk PJ and Area Under the Jerk AUJ quantify both abrupt spikes and excessive broad smoothing.

**Evaluation checked:** Tables 1–2 compare TEACH, DoubleTake, DiffCollage and MultiDiffusion with matched conditioning/positional choices. Thirty-one transitions between the thirty-two subsequences are evaluated separately; ablations examine positional blending, attention horizon and pose-centric conditioning. Extrapolation tests extend beyond training sequence durations.

**Full-text source:** https://arxiv.org/pdf/2402.15509v1

**Reading status:** full_text_checked

**Inspected version:** 2402.15509v1

**Full-text SHA256:** 9fd900b5bb96bf777e62c9052922f0579b5fae7a6a23cc8242b553861ef690cf

**Source locator:** Sections 3.1–3.3, 4.1–4.4; Tables 1–2; Eq. 4 for PJ/AUJ and supplementary evaluation details.

**Scope / curator boundary:** Finite attention and independent low-frequency subsequence structure can limit distant action relationships. Good jerk or FID values do not establish semantic task prerequisites, foot-support correctness, scene collision freedom or object interaction dynamics.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2402.15509); checked 2026-11-19.

<a id="t2lm"></a>
## T2LM: Long-Term 3D Human Motion Generation from Multiple Sentences

**t2lm · 2024 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2406.00636) · [Evidence](https://arxiv.org/pdf/2406.00636v2) · Citekey: `t2lm2026`

**Authors of cited version:** Taeryung Lee; Fabien Baradel; Thomas Lucas; Kyoung Mu Lee; Gregory Rogez.

**Contribution / composition:** Uses a local 1D-convolutional VQ-VAE decoder to decode a continuous text-predicted latent stream, trained on short clips.

**Mechanism:** Trains a convolutional VQ-VAE whose local temporal receptive fields map motion to a stream of discrete codes. A text-conditioned predictor learns codes from short clips. At inference, multiple sentence-conditioned latent subsequences are assembled and decoded together, allowing local decoder neighborhoods to produce transitions without training on long sequential demonstrations.

**Input contract:** Ordered sentence list and requested segment durations; outputs continuous skeletal motion. The method does not receive an object mesh, scene occupancy or future object-state supervision.

**Data and split:** Trains/evaluates on HumanML3D and BABEL following their cited standard protocols. The paper distinguishes short-clip training from sequential evaluation; exact split proportions and actor-disjointness are not specified in its dataset subsection.

**Evaluation metrics:** R-Precision, FID, MM-Distance, Diversity and reconstruction FID; sliding-scope SS-FID/SS-Diversity and transition-scope TS-FID/TS-Diversity use 80-frame windows, with a 40-frame stride for sliding evaluation.

**Evaluation checked:** Tables 4–5 compare long sequences with DoubleTake, TEACH and MultiAct; Tables 6–7 assess single actions. Codebook and explicit transition-latent ablations test representation choices. The paper reports weaker transition-scope performance than TEACH on BABEL despite stronger overall-window quality.

**Full-text source:** https://arxiv.org/pdf/2406.00636v2

**Reading status:** full_text_checked

**Inspected version:** 2406.00636v2

**Full-text SHA256:** 26a48d5e15d7448654af64229f12805d3e93dd217ff70610864a1032a27bc5ab

**Source locator:** Sections 3, 4.2–4.5; Tables 2–7; discussion following Table 5.

**Scope / curator boundary:** Local continuity does not enforce scene/contact correctness or long-range task causality. Standard feature metrics depend on their learned representation; ST2M is excluded because motion representations differ, preventing direct score equivalence.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2406.00636); checked 2026-11-19.

<a id="amd-autoregressive"></a>
## AMD: Autoregressive Motion Diffusion

**amd-autoregressive · 2023 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2305.09381) · [Evidence](https://arxiv.org/pdf/2305.09381v8) · Citekey: `amdautoregressive2024`

**Authors of cited version:** Bo Han; Hao Peng; Minjing Dong; Yi Ren; Yixuan Shen; Chang Xu.

**Contribution / composition:** Introduces HumanLong3D and conditions iterative diffusion generation on current text plus previous text and action sequences.

**Mechanism:** Autoregressively generates one diffusion-based motion segment per ordered text prompt. A context encoder combines the current prompt, the preceding prompt and preceding generated motion; a duration network predicts a categorical distribution over segment lengths. Training couples temporal motion context and denoising, rather than independently synthesizing clips and interpolating them afterward. The paper also builds HumanLong3D with coherence annotations and HumanMusic from online dance videos.

**Input contract:** Ordered natural-language prompts and prior generated segment context; a music-conditioned variant uses audio features. Segment duration is predicted rather than assumed fixed at deployment.

**Data and split:** HumanLong3D compound-motion experiment partitions examples into training/test/validation at 85/10/5 percent. Exact subject, source-recording or composition-ancestor separation is not specified. HumanML3D provides the short-motion benchmark; AIST++ and HumanMusic provide music experiments.

**Evaluation metrics:** FID measures generated/reference feature-distribution distance; top-3 R-precision and multimodal distance measure text alignment; diversity and multimodality measure across-prompt and within-prompt variation. Music evaluation follows the cited dance protocol.

**Evaluation checked:** Compares joint prediction, independent generation/interpolation and autoregressive prediction on HumanLong3D, alongside short text-to-motion baselines. The duration network covers approximately 2–9.8 seconds per segment in the implementation.

**Full-text source:** https://arxiv.org/pdf/2305.09381v8

**Reading status:** full_text_checked

**Inspected version:** arXiv:2305.09381v8

**Full-text SHA256:** d0c4cca3329f951c588742a33ecf4bbe7bded3b6d0a3f397d37d4f0d968a5c44

**Source locator:** Our Approach; Datasets and Evaluation Metrics; Comparisons on Compound Motion; Tables 1–3; Figure 1.

**Scope / curator boundary:** Longer rollout depends on generated context and can accumulate error. A dataset-example split does not establish unseen skill-pair or actor generalization. Online estimated dance poses and newly collected motion have different provenance and should not be treated as uniform measured ground truth.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.09381); checked 2026-11-19.

<a id="diffcollage"></a>
## DiffCollage: Parallel Generation of Large Content with Diffusion Models

**diffcollage · 2023 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2303.17076) · [Evidence](https://arxiv.org/pdf/2303.17076v1) · Citekey: `diffcollage2023`

**Authors of cited version:** Qinsheng Zhang; Jiaming Song; Xun Huang; Yongxin Chen; Ming-Yu Liu.

**Contribution / composition:** DiffCollage represents large content through a factor graph of overlapping smaller regions. It combines local diffusion scores with overlap corrections to approximate a global score, allowing the regions to denoise concurrently. The same construction is applied to images and long human motion.

**Mechanism:** DiffCollage represents large content through a factor graph of overlapping smaller regions. It combines local diffusion scores with overlap corrections to approximate a global score, allowing the regions to denoise concurrently. The same construction is applied to images and long human motion.

**Input contract:** Pretrained short-content diffusion models and a chosen factor graph; motion factors may carry different text prompts. Overlap structure determines how local constraints communicate, while optional inpainting conditions preserve specified content. It is a sampling composition method rather than a new motion-capture dataset.

**Data and split:** Motion experiments use the HumanML3D test set with an existing short-motion model. Long outputs are 24 seconds, approximately four times average training duration. Exact source-model train/validation proportions are not restated; image experiments additionally use internal landscapes, LHQ, and LSUN Tower.

**Evaluation metrics:** R-Precision and multimodal distance assess text-motion alignment, FID measures distribution mismatch, and Diversity measures variability. Long-motion evaluation randomly crops generated sequences for short-motion evaluators, so its scores characterize local windows rather than complete narrative correctness.

**Evaluation checked:** §5.2 and Table 3 compare parallel factor-graph generation with naive long denoising and autoregressive replacement/reconstruction. Multiple-action demonstrations provide qualitative prompt composition; image experiments additionally test panorama generation, inpainting, and latency scaling.

**Full-text source:** https://arxiv.org/pdf/2303.17076v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2303.17076v1 [cs.CV] 30 Mar 2023

**Full-text SHA256:** 9133ff74be495530f7f7acc9c4062ca155cd030d37b89cdcad460c3f6ac6cd28

**Source locator:** §§3–4 (factor graphs and score assembly), §5.2, Table 3 and motion-composition examples; appendix implementation details.

**Scope / curator boundary:** The factorization approximates the full distribution and depends on informative overlaps. Cropped feature metrics do not prove global ordering, distant consistency, collision freedom, or valid hand-object contact. The motion results should remain distinct from its stronger image-generation evaluation coverage.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2303.17076); checked 2026-11-19.

<a id="priormdm"></a>
## Human Motion Diffusion as a Generative Prior

**priormdm · 2023 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2303.01418) · [Evidence](https://arxiv.org/pdf/2303.01418v3) · Citekey: `priormdm2023`

**Authors of cited version:** Yonatan Shafir; Guy Tevet; Roy Kapon; Amit H. Bermano.

**Contribution / composition:** Introduces DoubleTake sequential composition, ComMDM two-person coordination and DiffusionBlending joint-control model composition.

**Mechanism:** A frozen short-motion diffusion prior is reused for overlapping prompted intervals; a second take refines transitions. Separate small adapters or fine-tuned controlled priors support other composition modes.

**Input contract:** DoubleTake consumes sequential prompts/durations with overlapping handshake regions. ComMDM additionally consumes interaction examples or a prefix; fine-tuned priors consume selected joint controls, and DiffusionBlending combines distinct control-conditioned predictions.

**Data and split:** DoubleTake evaluates BABEL and HumanML3D; fine control uses HumanML3D test prompts/controls. ComMDM uses a small two-person dataset, including its ten-example few-shot setting. Exact aggregate train/test proportions are not restated and the three tasks should not be collapsed into one split.

**Evaluation metrics:** Per-interval text-motion R-Precision/MM-Distance/FID/diversity, transition FID; ComMDM prefix completion reports root/joint L2 errors. Joint-control evaluation measures adherence and generation quality; qualitative studies assess blending.

**Evaluation checked:** Sequential evaluation constructs thirty-two-interval sequences and scores actions and boundaries separately. ComMDM completes three seconds from a one-second prefix and compares communication-layer placement. Fine-tuning and blending compare a common initial MDM against separately controlled models.

**Full-text source:** https://arxiv.org/pdf/2303.01418v3

**Reading status:** full_text_checked

**Inspected version:** 2303.01418v3

**Full-text SHA256:** 5dd735fb15e2ddaaa8ab87e8ba99db0c96582229fe67e1216a41b8539c7b13fe

**Source locator:** Sections 3.1–3.3, 4.1–4.3; Tables 1–3 and fine-control quantitative results.

**Scope / curator boundary:** DoubleTake needs overlap/refinement design; ComMDM needs interaction data and fine control requires extra training. These are distinct reuse mechanisms, not a universal zero-training composer. None guarantees physically valid contact or persistent object-state reasoning.

**Publication / version note:** First public preprint; conference publication 2024. First public preprint; conference publication 2024.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2303.01418); checked 2026-11-19.

<a id="st2m"></a>
## Sequential Texts Driven Cohesive Motions Synthesis with Natural Transitions

**st2m · 2023 · Temporal composition & long sequences · method**

[Primary source](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.pdf) · Citekey: `st2m2023`

**Authors of cited version:** Li, Shuai; Zhuang, Sisi; Song, Wenfeng; Zhang, Xinyu; Chen, Hejia; Hao, Aimin.

**Contribution / composition:** Combines previous/current text semantics with learnable transition tokens and a transition loss.

**Mechanism:** Uses semantic fusion attention to combine current sentence features with preceding motion context. A transformer infers learnable starting transition snippet codes from the previous generated motion; an autoregressive generator then continues the current action. A dedicated transition loss encourages continuity. STDM is synthesized to supply longer sequential text-motion examples.

**Input contract:** Sequential text descriptions, generated previous motion/snippet context, and sequence lengths. Historical semantics are learned rather than treating each sentence as an independent clip.

**Data and split:** Evaluates BABEL-TEACH and STDM. STDM has 5,289 sequences totaling 20.02 hours. Section 4.3 specifies train/test/validation proportions 0.8/0.15/0.05; it does not establish subject- or source-ancestor-disjoint grouping.

**Evaluation metrics:** Text-motion feature R-Precision and matching distance, FID, diversity, multimodality, plus transition fluency: L1 distance between the last frame of one generated action and the first frame of the next.

**Evaluation checked:** Contrasts isolated T2M, joint-text training, snippet-code transfer and TEACH with/without spherical interpolation. Twenty evaluation repeats produce 95% confidence intervals. Tables 2–3 report sequential quality and transition fluency; ablations inspect semantic fusion and transition inference.

**Full-text source:** https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Author/institution or proceedings PDF as retrieved 2026-11-19; version string not printed for this paper.

**Full-text SHA256:** 18c58f22a5cfd41ac1077e9f856555236982fd8eafd11798895194aeb30bb662

**Source locator:** Sections 3.1–3.4; Sections 4.1–4.5; Tables 1–3; transition fluency Eq. 7.

**Scope / curator boundary:** Endpoint distance measures boundary jumps rather than natural braking, support transfer or continuous collision freedom. Synthetic sequences and a custom paired feature extractor complicate comparison with methods using different BABEL representations.

**Composition axes:** temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.html); checked 2026-11-19.

<a id="multi-act-2022"></a>
## MultiAct: Long-Term 3D Human Motion Generation from Multiple Action Labels

**multi-act-2022 · 2022 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2212.05897) · [Evidence](https://arxiv.org/pdf/2212.05897v3) · Citekey: `multiact20222023`

**Authors of cited version:** Taeryung Lee; Gyeongsik Moon; Kyoung Mu Lee.

**Contribution / composition:** Recurrently conditions on prior motion and the next action label to generate transitions and long multi-action sequences.

**Mechanism:** MultiAct recurrently predicts a transition and next action through MACVAE, a motion-and-action-conditioned variational autoencoder. Separate latent variables encode the previous-motion context and current action. A face-front canonicalization removes heading and location while retaining the gravity relationship, avoiding the floor-orientation loss caused by full root zeroing. An ACTOR model produces the initial action before recurrent continuation.

**Input contract:** A sequence of discrete action labels and previous generated motion; transition and action durations are part of the sampled training/generation setting, not free-form language understanding.

**Data and split:** Uses BABEL training split for learning and released validation split for testing, extracting alternating action and transition intervals. Test previous-motion inputs are unseen examples; no independently held-out action-pair split or new proportional split is declared in the main paper.

**Evaluation metrics:** FID against training and test feature distributions, top-1/top-5 action recognition, diversity across actions and multimodality within actions. Transition FID and action accuracy are also measured along long rollouts.

**Evaluation checked:** Compares MACVAE to action-conditioned generation combined with interpolation or a motion-transition model. Ablations remove separate latents and vary canonicalization or previous-motion input; long-horizon plots track action accuracy and transition distribution.

**Full-text source:** https://arxiv.org/pdf/2212.05897v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2212.05897v3

**Full-text SHA256:** e933ea9a7d53a182b4d76aee54676694140531fae90f266d91fc8e21af0a37a7

**Source locator:** MACVAE and Long-Term Motion Generation sections; Datasets; Evaluation metrics; Tables 1–3; Figures 4–6.

**Scope / curator boundary:** Discrete action categories provide less detailed control than text or geometry. Recurrent generation is assessed on BABEL’s annotated transitions, and favorable feature scores do not certify foot contact, object consistency, or arbitrary physical task sequencing.

**Publication / version note:** First public preprint in December 2022; revised 2023. First public preprint in December 2022; revised 2023.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.05897); checked 2026-11-19.

<a id="teach"></a>
## TEACH: Temporal Action Composition for 3D Humans

**teach · 2022 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2209.04066) · [Evidence](https://arxiv.org/pdf/2209.04066v2) · Citekey: `teach2022`

**Authors of cited version:** Nikos Athanasiou; Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** TEACH extends a text-motion variational Transformer with past-motion conditioning: it generates all frames of one action non-autoregressively, then conditions the next action on a short history. Training on adjacent action pairs teaches continuity; alignment and spherical interpolation further smooth transitions.

**Mechanism:** TEACH extends a text-motion variational Transformer with past-motion conditioning: it generates all frames of one action non-autoregressively, then conditions the next action on a short history. Training on adjacent action pairs teaches continuity; alignment and spherical interpolation further smooth transitions.

**Input contract:** An ordered list of action descriptions, individual action durations, and the previous generated action tail. The main configuration uses five past frames. The model generates body motion and root displacement, without receiving manipulated object meshes or object-state trajectories.

**Data and split:** Uses original BABEL training/validation splits with approximately 23,400 training and 5,700 validation action pairs at 30 fps. Results are reported on validation because BABEL test data were unavailable; references to test pairs in some captions should not be mistaken for a public test evaluation.

**Evaluation metrics:** Average Positional Error (APE) and Average Variational Error (AVE) compare root, trajectory, local, and global joint behavior with reference motion. Transition distance measures the joint-position gap between consecutive actions, both before and after alignment, exposing boundary discontinuity.

**Evaluation checked:** Table 1 compares independent, jointly generated, and past-conditioned action pairs; Table 2 tests alignment/interpolation and transition distances; Table 3 varies past-context length. Qualitative longer chains test repeated action-level rollout beyond pairwise training.

**Full-text source:** https://arxiv.org/pdf/2209.04066v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2209.04066v2 [cs.CV] 12 Sep 2022

**Full-text SHA256:** bfdfb838ecd7f112454e720a87cbec38cbbeef156563cbbf8f3f3bebb01d1f32

**Source locator:** §3 (hierarchical variational architecture), §§4.1–4.6, Tables 1–3; appendix D.1 explicitly states original splits and validation reporting.

**Scope / curator boundary:** Pairwise BABEL supervision and validation-set reporting limit claims about unseen independent recordings and new action combinations. Autoregressive rollout can accumulate errors, while interpolation does not establish scene feasibility or contact-rich manipulation. Position-based comparison to one reference underestimates valid alternative realizations.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2209.04066); checked 2026-11-19.

<a id="fusion"></a>
## FUSION: Full-Body Unified Motion Prior for Body and Hands via Diffusion

**fusion · 2026 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2601.03959) · [Evidence](https://arxiv.org/pdf/2601.03959v1) · Citekey: `fusion2026`

**Authors of cited version:** Enes Duran; Nikos Athanasiou; Muhammed Kocabas; Michael J. Black; Omid Taheri.

**Contribution / composition:** Unifies body and hand datasets into a full-body motion prior, with optimization-driven object-motion and self-interaction applications.

**Mechanism:** Unconditional SMPL-X diffusion prior jointly models body/hands; task losses backpropagate through denoising to optimize noise. Local hand transfer preserves body wrists and filters additional penetration.

**Input contract:** Unconditional whole-body/hand prior optimized for supplied keypoint tracks, object-motion trajectories or LLM-generated timed self-contact constraints. Object-guided synthesis assumes object motion and a stable grasp, so future interaction is partially prescribed.

**Data and split:** Source pools include 145,100 body-motion clips and 41,148 augmented hand-motion clips of 120 frames. Pairing produces approximately 17.4M full-body frames; these quantities describe different construction stages. ARCTIC/GRAB test sources and task-specific test conditions are described, but aggregate source-ancestor split grouping is not fully enumerated.

**Evaluation metrics:** Trajectory failure percentage, location error, MotionCritic body realism, hand quality/contact/penetration measures and human preference. MotionCritic excludes local hand articulation to match its expected representation.

**Evaluation checked:** Keypoint control is compared with TLControl; hand/body ablations assess the benefit of unified training. Object-guided and self-interaction demonstrations optimize denoising noise with task losses. Human comparison separately assesses motion realism against HMP and captured motion.

**Full-text source:** https://arxiv.org/pdf/2601.03959v1

**Reading status:** full_text_checked

**Inspected version:** 2601.03959v1

**Full-text SHA256:** ac0ece417fefa4e887ec5b4f1fbc4c28647a10685f06443a59e19d79398c527f

**Source locator:** Sections 3.1–3.3, 4–5; Table 1; supplementary Sections 9–12 (metrics, ablations, self-contact).

**Scope / curator boundary:** Randomly combined hand/body motion lacks sequence-level semantic correlation. Fixed-grasp guidance limits contact changes, and the learned prior is not a text-plus-initial-state dynamic HOI generator. Body-only realism scores cannot validate dexterous hand or object dynamics.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2601.03959); checked 2026-11-19.

<a id="frankenmotion"></a>
## FrankenMotion: Part-level Human Motion Generation and Composition

**frankenmotion · 2026 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2601.10909) · [Evidence](https://arxiv.org/pdf/2601.10909v1) · Citekey: `frankenmotion2026`

**Authors of cited version:** Chuqiao Li; Xianghui Xie; Yong Cao; Andreas Geiger; Gerard Pons-Moll.

**Contribution / composition:** Learns hierarchical part/action/sequence-conditioned diffusion instead of test-time pose stitching.

**Mechanism:** CLIP action/part embeddings are PCA-reduced to 50 dimensions, expanded framewise and concatenated with noisy motion through an MLP; sequence and diffusion-step features are extra tokens. Unknown labels are zeroed; Beta-distributed random masking improves sparse-conditioning robustness.

**Input contract:** Sequence-level text, action intervals and part-level labels at seven anatomical regions; missing labels are masked. Framewise embeddings and a sequence token supply hierarchical conditions to one diffusion generator.

**Data and split:** FrankenStein extends multi-granularity action/part annotations and divides sequences 80% training, 10% validation and 10% test. The split is not a newly established cross-dataset person-identity split. Fifty manually reviewed annotation samples provide a limited label audit.

**Evaluation metrics:** R-Precision and M2T similarity for semantic correctness, FID and diversity for realism. Separate TMR-style evaluators cover seven parts, action level and full sequences; MP-retrieval handles multiple positive captions.

**Evaluation checked:** Adapted UniMotion, STMC and DART use a matched pose representation; STMC backbone is retrained on the new annotation pairs. Experiments compare conditioning granularities, missing-input robustness and composing fine-grained part/action controls, with ablations of label/masking strategies.

**Full-text source:** https://arxiv.org/pdf/2601.10909v1

**Reading status:** full_text_checked

**Inspected version:** 2601.10909v1

**Full-text SHA256:** d5663bdf6265dcbcab9bb04b14e4e17f73f380cb906070f1f3d564661e11524b

**Source locator:** Sections 3–4; dataset split paragraph, evaluation protocol and comparison tables; limitations and supplementary label audit.

**Scope / curator boundary:** LLM annotations and evaluator specialization can bias semantic conclusions. Minute-long generation in one pass is explicitly unsupported. Part-level controllability does not imply natural contact-rich manipulation, and retrained/adapted baselines need the same information contract for fair interpretation.

**Composition axes:** semantic, spatial, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2601.10909); checked 2026-11-19.

<a id="mixermdm"></a>
## MixerMDM: Learnable Composition of Human Motion Diffusion Models

**mixermdm · 2025 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2504.01019) · [Evidence](https://arxiv.org/pdf/2504.01019v1) · Citekey: `mixermdm2025`

**Authors of cited version:** Pablo Ruiz-Ponce; German Barquero; Cristina Palmero; Sergio Escalera; José García-Rodríguez.

**Contribution / composition:** Learns adversarial dynamic mixing of pretrained single-person and interaction diffusion models.

**Mechanism:** Learns a small attention-based mixer that predicts dynamic spatiotemporal interpolation weights between denoising outputs from frozen individual-motion and interaction-motion models. Two discriminators encourage the mixed motion to preserve both priors, avoiding a need for paired mixed-motion ground truth. Compatible coordinate representations are explicitly aligned before mixing.

**Input contract:** Interaction-level text plus per-person text descriptions and the two pretrained diffusion predictions at each denoising step. Tests interchangeable interaction/individual backbones.

**Data and split:** HumanML3D supplies individual-model data; InterHuman supplies interaction-model and mixer data. Evaluation uses the InterHuman test set. Exact train/validation/test ratios and subject-grouping guarantees are not restated in the inspected protocol.

**Evaluation metrics:** Alignment applies Top-3 R-Precision separately to individual and interaction conditions; Adaptability measures variation under individual condition changes. Human-study average rank/first-place rate supplement feature-based evaluation.

**Evaluation checked:** Table 1 compares DiffusionBlending, DualMDM and fine-tuning using global, temporal, spatial and joint mixing weights. Ten repeated evaluations give 95% intervals; Table 3 tests reuse across pretrained-model combinations. User ratings favor the learned mixer on quality and alignment.

**Full-text source:** https://arxiv.org/pdf/2504.01019v1

**Reading status:** full_text_checked

**Inspected version:** 2504.01019v1

**Full-text SHA256:** fd099bb01279db61dcf000cbbf53b8043b74837846d6000c5e2ef388a8353e6d

**Source locator:** Sections 3.2–3.4, 4.1–4.5; Tables 1–3; Limitations and Future Work.

**Scope / curator boundary:** Requires additional training and inference computation, adversarial stability tuning and compatible output representations. Mixing model distributions does not construct a provenance-preserving human-object dataset or prove unseen action-order generalization.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2504.01019); checked 2026-11-19.

<a id="salad"></a>
## SALAD: Skeleton-aware Latent Diffusion for Text-driven Motion Generation and Editing

**salad · 2025 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2503.13836) · [Evidence](https://arxiv.org/pdf/2503.13836v1) · Citekey: `salad2025`

**Authors of cited version:** Seokhyeon Hong; Chaelin Kim; Serin Yoon; Junghyun Nam; Sihun Cha; Junyong Noh.

**Contribution / composition:** Models joint-frame-word relationships and edits generated motion by cross-attention modulation without explicit user masks.

**Mechanism:** Trains a skeleto-temporal VAE with skeletal pooling and temporal compression, preserving joint/frame structure in latent space. A denoiser separately models skeletal, temporal and word-level relations. At inference, cross-attention maps support word swapping, attention reweighting and left/right attention mirroring without training a dedicated editor or requiring an explicit edit mask.

**Input contract:** Natural-language descriptions and requested sequence length; editing manipulates the attention of a source generation using changed words or weights, rather than directly accepting arbitrary captured motion.

**Data and split:** HumanML3D and KIT-ML motion sequences are mirrored and divided into training/test/validation at 80/15/5 percent. No unseen action-combination or subject-disjoint protocol is reported. The editing study uses 15 videos per method and 16 participants.

**Evaluation metrics:** FID measures motion feature distributions; R-precision and MM-Dist measure text alignment; diversity and multimodality measure variation. Reconstruction evaluation reports motion-feature errors and parameter counts. Editing ratings measure preservation, target-text alignment and overall quality on five-point scales.

**Evaluation checked:** Table 1 averages 20 evaluations with 95 percent confidence intervals. Compares generation with diffusion/token baselines and editing with MDM and MotionFix; ablates guidance, parameterization, VAE and FiLM components.

**Full-text source:** https://arxiv.org/pdf/2503.13836v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2503.13836v1

**Full-text SHA256:** 3193515bfccc890418fedaef12080917dfd6e5d5b212e3ae42dfc72a93d78be1

**Source locator:** Sections 3, 4.1–4.5 and 5; Tables 1–4; Figures 3 and 7; Supplement A–C.

**Scope / curator boundary:** Diversity remains limited and competes with fidelity. Only a single person and bounded text/motion lengths are modeled. The authors explicitly state that editing real recorded motions is not directly addressed; attention preservation ratings are not an exact frame/joint invariance guarantee.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2503.13836); checked 2026-11-19.

<a id="demogen"></a>
## Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models

**demogen · 2025 · Body-part & semantic composition · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Towards_Decompositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Models_CVPR_2026_paper.pdf) · [Evidence](https://arxiv.org/pdf/2512.22324v1) · Citekey: `demogen2026`

**Authors of cited version:** Zhang, Jianrong; Fan, Hehe; Yang, Yi.

**Contribution / composition:** Trains compositional scores to reconstruct holistic motion without individual-concept motion targets.

**Mechanism:** Frozen-VAE motion latents are denoised with summed concept-conditioned predictions (latent-aware), or decomposed cross-attention (semantic-aware). Exp uses decomposed captions; OSS splits text embeddings with orthogonality; SC adds semantic consistency against decomposed embeddings.

**Input contract:** Holistic captions or decomposed concept texts. Explicit decomposition supplies separate text embeddings; orthogonal self-supervision divides latent semantics without external component motion targets, while semantic-consistency supervision uses decomposed caption embeddings.

**Data and split:** HumanML3D and DeCompML support single-caption/compositional tests; MTT evaluates timelines/multiple concepts. DeCompML relabels HumanML3D captions into 87,384 two-sentence groups including mirroring augmentation. Original benchmark partitions are used; a new independently recorded component-motion split is not provided.

**Evaluation metrics:** R-Precision, MM-Distance, FID, diversity and multimodality; MTT also uses TMR-Score and transition distance. These assess the recomposed motion, not direct per-primitive ground-truth trajectory recovery.

**Evaluation checked:** Sections 4.3–4.5 compare latent-aware and semantic-aware formulations, explicit versus self-supervised decomposition and generality across diffusion architectures. Caption-decomposition ablations vary component count; component visualizations inspect disentanglement without treating missing component trajectories as supervised truth.

**Full-text source:** https://arxiv.org/pdf/2512.22324v1

**Reading status:** full_text_checked

**Inspected version:** 2512.22324v1

**Full-text SHA256:** d17e7dbbeda26a1a354e33ccf48c8c8f81650a02a08f3c9cc9637cd1ab1f5303

**Source locator:** Sections 3.1–3.4, 4.1–4.5; Tables 1–7; Appendices G–I (decomposition/data/metrics).

**Scope / curator boundary:** Explicit decomposition degrades with three/four texts when source captions lack sufficient details. Semantic disentanglement remains an empirical interpretation, not a physical primitive identity guarantee. Decomposed descriptions and reconstruction scores do not certify object-aware feasibility or causal task order.

**Publication / version note:** First preprint 26 December 2025; CVPR 2026 publication. First preprint 26 December 2025; CVPR 2026 publication.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Towards_Decompositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Models_CVPR_2026_paper.html); checked 2026-11-19.

<a id="coma"></a>
## CoMA: Compositional Human Motion Generation with Multi-modal Agents

**coma · 2024 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2412.07320) · [Evidence](https://arxiv.org/pdf/2412.07320v2) · Citekey: `coma2025`

**Authors of cited version:** Shanlin Sun; Gabriel De Araujo; Jiaqi Xu; Shenghan Zhou; Hanwen Zhang; Ziheng Huang; Chenyu You; Xiaohui Xie.

**Contribution / composition:** CoMA combines GPT-4o text recaptioning and temporal/body-part decomposition, a spatially aware masked generator (SPAM), trajectory editing, motion captioning, and visual self-correction. Four part-specific codebooks feed a shared whole-body decoder; factorized spatial and temporal attention coordinates the generated token streams.

**Mechanism:** CoMA combines GPT-4o text recaptioning and temporal/body-part decomposition, a spatially aware masked generator (SPAM), trajectory editing, motion captioning, and visual self-correction. Four part-specific codebooks feed a shared whole-body decoder; factorized spatial and temporal attention coordinates the generated token streams.

**Input contract:** Natural-language requests and optional source motion or local edits. Agents transform rich prompts into shorter base-generation and part-edit instructions; rendered motions support visual critique. The complete agent system and its standalone SPAM generator are different evaluation objects.

**Data and split:** Standard HumanML3D counts are 23,384 train, 1,460 validation, and 4,384 test samples. Appendix A separately constructs a complex-motion split of 20,108/2,932/2,172 samples, placing complex motions in test. These sample counts should not be presented as unique original recordings.

**Evaluation metrics:** R-Precision and MM-Distance measure semantic alignment; FID and Multimodality characterize distribution and prompt diversity. Captioning uses BLEU, ROUGE, CIDEr, and BERTScore. Motion Alignment Score compares rendered-video and text embeddings; user studies judge rich-prompt fidelity and quality.

**Evaluation checked:** Tables 2–3 primarily benchmark SPAM on standard and fine-grained descriptions; Table 4 evaluates captioning and Tables 5–7 test architecture and complex motions. The complete agent pipeline is evaluated with a 54-participant user study rather than assumed identical to SPAM benchmark scores.

**Full-text source:** https://arxiv.org/pdf/2412.07320v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2412.07320v2 [cs.CV] 7 Jan 2025

**Full-text SHA256:** 01446d27be1674f4438644c38a4faf55aa72dfc7e10bafbda4df911f842b30ad

**Source locator:** §§3–4 (agents and SPAM), §5 and Tables 2–6; appendix A (complex split/Table 7), B (54-participant study), F.4 (MAS).

**Scope / curator boundary:** Large-model calls, recaptioning, and rendered self-critique add cost and dependencies. Synthetic fine-grained language and complex-split construction affect comparability. Visual agreement and retrieval scores do not certify motion preservation, collision freedom, or interaction physics.

**Publication / version note:** AAAI 40(11), 9206–9214; DOI 10.1609/aaai.v40i11.37878. Published author list differs from the arXiv record; bibliography below cites the arXiv version. First public preprint 2024; later venue not independently checked in this intake.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2412.07320); checked 2026-11-19.

<a id="energymogen"></a>
## EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space

**energymogen · 2024 · Body-part & semantic composition · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf) · [Evidence](https://arxiv.org/pdf/2412.14706v2) · Citekey: `energymogen2025`

**Authors of cited version:** Zhang, Jianrong; Fan, Hehe; Yang, Yi.

**Contribution / composition:** Combines latent and text-attention energy formulations for concept conjunction and negation.

**Mechanism:** Classifier-free diffusion predictions implement latent-aware energy composition. Cross-attention provides semantic-aware composition and adaptive text-embedding gradient updates; Synergistic Energy Fusion reconciles the two. Main inference uses five latent vectors and 50 diffusion steps.

**Input contract:** Multiple textual concepts, including conjunction and negation, applied to a pretrained latent diffusion motion model. Energy-weighted score composition and adaptive cross-attention text updates provide alternative controls whose predictions are fused.

**Data and split:** HumanML3D uses 80/5/15 training/validation/test percentages. KIT-ML reports processed 4,888/300/830 motions; MTT supplies evaluation-only compositional texts/source motions. Motion VAE and denoising model training precede inference energy composition.

**Evaluation metrics:** Standard R-Precision, MM-Distance, FID, diversity and multimodality for single-caption generation; MTT R-Precision, TMR-Score, FID and transition distance evaluate composition and multi-concept synthesis.

**Evaluation checked:** Tables compare latent- and skeleton-based generation, latent-aware and semantic-aware energy variants, adaptive gradient descent and synergistic fusion. Main sampling uses five latent vectors and fifty diffusion steps. Supplementary ablations vary guidance weights, latent count and attention-gradient parameters.

**Full-text source:** https://arxiv.org/pdf/2412.14706v2

**Reading status:** full_text_checked

**Inspected version:** 2412.14706v2

**Full-text SHA256:** 977757dc3ad5ee41ca7afa58802f648343618adf2ec560953e2ed307ff5ec865

**Source locator:** Sections 3–5.4, Tables 1–3; Appendices D–E, I (datasets/metrics), J (limitations).

**Scope / curator boundary:** Appendix J shows failure on completely novel concepts. Energy arithmetic is an inference control mechanism, not a physics certificate or independent primitive decomposition. Synthetic augmentation and MTT semantic gains do not establish general object-contact accuracy or causal long-task completion.

**Publication / version note:** First preprint arXiv:2412.14706 in 2024; CVPR 2025. First preprint arXiv:2412.14706 in 2024; CVPR 2025.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.html); checked 2026-11-19.

<a id="parco"></a>
## ParCo: Part-Coordinating Text-to-Motion Synthesis

**parco · 2024 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2403.18512) · [Evidence](https://arxiv.org/pdf/2403.18512v2) · Citekey: `parco2024`

**Authors of cited version:** Qiran Zou; Shangyuan Yuan; Shian Du; Yu Wang; Chang Liu; Yi Xu; Jie Chen; Xiangyang Ji.

**Contribution / composition:** Separate part tokenizers and lightweight generators communicate through a coordination module.

**Mechanism:** Partitions a skeleton into six anatomical streams and learns separate part VQ tokenizers. Lightweight autoregressive text-conditioned generators predict part tokens while a coordination module exchanges information between streams. Their decoders reconstruct a unified whole-body sequence; this reduces whole-body token complexity while preserving inter-part dependencies.

**Input contract:** A natural-language motion description; variable output duration is predicted autoregressively rather than supplied as ground-truth length. Part streams are internal representations, not independent user-assigned task labels.

**Data and split:** HumanML3D and KIT-ML use the cited standard train/validation/test divisions. Numerical proportions are not restated. A diagnostic additionally divides HumanML3D test captions into four approximately equal length quartiles, not four independent training splits.

**Evaluation metrics:** R-Precision Top-1/2/3, FID, multimodal distance, diversity and multimodality, computed with the established pretrained text-motion evaluator. Diagnostic left/right instruction tests and caption-length subsets supplement these scores.

**Evaluation checked:** Tables 1–2 compare generation against contemporary models, distinguishing access to true motion length. Ablations test part decomposition and coordination. The paper also reports that real training motions score better than real test motions under the evaluator, exposing feature-extractor bias.

**Full-text source:** https://arxiv.org/pdf/2403.18512v2

**Reading status:** full_text_checked

**Inspected version:** 2403.18512v2

**Full-text SHA256:** b78a1c7857a1bf02032fdc1c378ae41ea0ca9f74643ee80ddbc5fb5814c03e0c

**Source locator:** Sections 3–4; Tables 1–5; supplementary Appendix B (caption-length splits).

**Scope / curator boundary:** Six-part factorization alone is not evidence of arbitrary simultaneous semantic composition. Evaluator training-distribution bias can make generated samples outperform real test motions; semantic accuracy and physical validity need complementary checks.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.18512); checked 2026-11-19.

<a id="amd-anatomical"></a>
## AMD:Anatomical Motion Diffusion with Interpretable Motion Decomposition and Fusion

**amd-anatomical · 2023 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2312.12763) · [Evidence](https://arxiv.org/pdf/2312.12763v3) · Citekey: `amdanatomical2026`

**Authors of cited version:** Beibei Jing; Youjia Zhang; Zikai Song; Junqing Yu; Wei Yang.

**Contribution / composition:** Parses complex text into anatomical scripts and fuses script and text guidance in diffusion.

**Mechanism:** Uses fine-tuned ChatGPT-3.5 to decompose complex descriptions into concise anatomical scripts. Sentence-BERT retrieves reference motions for these scripts. Two diffusion branches model the original prompt and the prompt plus scripts/reference actions; a Bernoulli fusion schedule switches their contributions during denoising. This is the anatomical AMD, distinct from Autoregressive Motion Diffusion despite the shared acronym.

**Input contract:** Original text plus automatically decomposed scripts and retrieved reference-motion tokens. Retrieval depends on a motion-text database; masked-joint and in-between demonstrations additionally constrain unedited motion.

**Data and split:** Evaluates HumanML3D and KIT-ML and constructs SLCD1/SLCD2 complex-language test subsets from HumanML3D. The reviewed experiment text does not specify subset cardinalities, a new train/validation/test proportion, or a composition-ancestor exclusion protocol.

**Evaluation metrics:** Top-3 R-precision, FID, multimodal distance, diversity and multimodality. Complex-text tables use ground-truth motion lengths; evaluation repeats 20 times, except multimodality five times, with 95 percent confidence intervals.

**Evaluation checked:** Compares against MDM, TM2T, MotionDiffuse, T2M-GPT and other text-motion systems. Ablations remove decomposition or reference information and vary fusion probability. Editing demonstrations fix endpoint quarters or lower-body joints.

**Full-text source:** https://arxiv.org/pdf/2312.12763v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2312.12763v3

**Full-text SHA256:** 89c430f73efd2bf747b6a16060d5abde23fc269fb2e99525e55117c16e7f28f1

**Source locator:** Text Decomposition; Motion Diffusion and Fusion; Training and Inference; Experiments; Tables 1–3 and Figures 5–7; Conclusion limitation paragraph.

**Scope / curator boundary:** Reference quality and database breadth directly limit generation; LLM decomposition can add excessive constraints and reduce multimodality. Complex language subsets are not equivalent to systematically withheld skill combinations, and demonstrated ball/grab semantics do not imply generated physical object trajectories.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.12763); checked 2026-11-19.

<a id="finemogen"></a>
## FineMoGen: Fine-Grained Spatio-Temporal Motion Generation and Editing

**finemogen · 2023 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2312.15004) · [Evidence](https://arxiv.org/pdf/2312.15004v1) · Citekey: `finemogen2023`

**Authors of cited version:** Mingyuan Zhang; Huirong Li; Zhongang Cai; Jiawei Ren; Lei Yang; Ziwei Liu.

**Contribution / composition:** Uses structured part/time descriptions and mixture attention for fine-grained generation and instruction-based editing.

**Mechanism:** Spatio-Temporal Mixture Attention builds global attention templates with explicit part/time influence and sparsely activated experts. An LLM modifies structured descriptions for editing, after which the diffusion model regenerates the sequence.

**Input contract:** Fine-grained text assigned to body parts and temporal phases, with sequence length. Editing additionally uses prior description/context and an instruction; this is not arbitrary mesh-conditioned interaction.

**Data and split:** HumanML3D, KIT-ML and BABEL complement HuMMan-MoGen: 2,968 videos, 160 action types and 102,336 annotations. The checked §4 reports test evaluations but does not give an independently auditable subject/recording split ratio for HuMMan-MoGen.

**Evaluation metrics:** FID, R-precision, multimodal distance, diversity and multimodality use benchmark embeddings. Temporal composition tables compare text alignment and motion distributions; these metrics do not independently establish physical contacts.

**Evaluation checked:** Tables 1–2 evaluate standard text-to-motion; Table 3 tests temporal composition; Table 4 is a zero-shot ablation without training on temporal-composition data. Evaluations repeat twenty times with reported intervals.

**Full-text source:** https://arxiv.org/pdf/2312.15004v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2312.15004v1

**Full-text SHA256:** 3c1651e98e68a89b7f35d14aa67ea5658d3053d77c46825ce22d4dc3b7eab0f9

**Source locator:** §§3.1–3.5; §§4.1–4.6, Tables 1–4; §5 limitations.

**Scope / curator boundary:** The structured description format restricts interfaces, and editing depends on LLM interpretation. A temporal-composition result should not be restated as an object-state or source-ancestry generalization test.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.15004); checked 2026-11-19.

<a id="sinc"></a>
## SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation

**sinc · 2023 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2304.10417) · [Evidence](https://arxiv.org/pdf/2304.10417v3) · Citekey: `sinc2024`

**Authors of cited version:** Nikos Athanasiou; Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** Studies simultaneous actions through body-part motion composition and synthetic training examples.

**Mechanism:** GPT-3 identifies active body parts; body-part motion combinations create synthetic examples for text-to-motion training.

**Input contract:** Two or more simultaneous action descriptions combined as one free-form text. GPT-3 assigns active body parts to source motions; compatible parts are combined into synthetic whole-body examples used alongside real single/pair actions.

**Data and split:** BABEL supplies 2,851 training simultaneous motions and 1,232 validation motions. Removing redundant stand labels and action pairs seen in training yields 667 evaluation sequences. Also uses 24,066/8,711 single-action train/validation segments. Validation is explicitly used as test, not an independent third partition.

**Evaluation metrics:** Average Positional Error APE, Average Variance Error AVE and TEMOS motion-embedding score. Body-part assignment accuracy is separately assessed against human yes/no labels, ignoring optional-part ambiguity.

**Evaluation checked:** Tables 2–3 compare single-action generation, direct GPT-guided stitching and training with real/synthetic pairs. Synthetic/real mixing proportions and shared versus separate text encoders are ablated. Real validation pairs evaluate generation beyond merely reconstructing synthetic training outputs. Real and synthetic pairs retain distinct experimental roles throughout the comparison.

**Full-text source:** https://arxiv.org/pdf/2304.10417v3

**Reading status:** full_text_checked

**Inspected version:** 2304.10417v3

**Full-text SHA256:** eedcb7cba7fda40a6e04ba6fcab5dc3e9edd0eaa864dc4db12ab990e09ba4fc6

**Source locator:** Sections 3.1–3.3, 4.1–4.6; Tables 1–3; Appendix E evaluation extensions.

**Scope / curator boundary:** Compatible parts need not preserve balance, scene contacts or object responsibilities. Most experiments focus on action pairs; metric/perceptual mismatch remains. Synthetic source combinations do not automatically provide force-valid or provenance-independent human-object examples.

**Composition axes:** data, semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.10417); checked 2026-11-19.

<a id="rg-dno"></a>
## Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization

**rg-dno · 2026 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2605.08054) · [Evidence](https://arxiv.org/pdf/2605.08054v1) · Citekey: `rgdno2026`

**Authors of cited version:** Hanchao Liu; Fang-Lue Zhang; Shining Zhang; Tai-Jiang Mu; Shi-Min Hu.

**Contribution / composition:** Combines retrieved and random diffusion noise through task-aware spatial/temporal masks for difficult constraints.

**Mechanism:** Relational task parsing allocates constraints to retrieval and optimization. Separate retrieved/random noises are optimized, reward-guided masks select their mixture, and final DNO refines the combined initialization.

**Input contract:** Differentiable constraint functions, optional text, a pretrained generator and a searchable motion database. Constraint difficulty/relationships can be manually specified or inferred by an LLM.

**Data and split:** Base MDM-RoHM is trained on the HumanML3D training split, but retrieval uses the whole dataset. Tests define narrow-gap, low-barrier and counted-step tasks; these are not strict source-held-out retrieval evaluations.

**Evaluation metrics:** Foot skating, maximum joint acceleration, constraint error and maximum scene penetration assess feasibility. Counted-step success, joint semantic success and pace score assess numerical/action consistency.

**Evaluation checked:** Compares ProgMoGen+DNO and MaskControl under specified difficult constraints, including 0.4 m gaps. Spatial/temporal masks, retrieval, rewards, task parsing and task difficulty are ablated.

**Full-text source:** https://arxiv.org/pdf/2605.08054v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2605.08054v1

**Full-text SHA256:** 358e199a97ab84504af76cc7d4d4a4f6d1b78ae6c72cbc4f9e06896e05bbacd9

**Source locator:** §§4.1–4.5/Algorithm 1; §§5.1–5.6, Tables 1–5; limitations in §5.6.

**Scope / curator boundary:** Adds several optimization phases and roughly 300 additional steps relative to DNO. Diversity contracts under severe constraints; unnatural motion and text misalignment remain possible. Whole-dataset retrieval limits independent generalization claims.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2605.08054); checked 2026-11-19.

<a id="motionlab"></a>
## MotionLab: Unified Human Motion Generation and Editing via the Motion-Condition-Motion Paradigm

**motionlab · 2025 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2502.02358) · [Evidence](https://arxiv.org/pdf/2502.02358v5) · Citekey: `motionlab2025`

**Authors of cited version:** Ziyan Guo; Zeyu Hu; De Wen Soh; Na Zhao.

**Contribution / composition:** MotionLab formulates tasks as source motion, condition, and target motion. Its rectified-flow MotionFlow Transformer provides modality-specific paths with joint attention, aligned rotary position encoding, and task instruction modulation. Staged multitask training introduces modalities and tasks while replaying previous tasks.

**Mechanism:** MotionLab formulates tasks as source motion, condition, and target motion. Its rectified-flow MotionFlow Transformer provides modality-specific paths with joint attention, aligned rotary position encoding, and task instruction modulation. Staged multitask training introduces modalities and tasks while replaying previous tasks.

**Input contract:** Task instruction plus text, optional source motion, joint trajectories, temporal keyframes, or style reference. Generation uses an empty source; editing transforms a supplied source. Future full trajectories are task-specific controls, not evidence of unconstrained text-only generation.

**Data and split:** Uses HumanML3D for text generation, trajectories, in-betweening, and style transfer, and MotionFix for editing. The inspected experimental setup names the datasets but does not restate exact split proportions or independent subject/recording grouping. All motions are retargeted to a common 22-joint, 20-fps representation.

**Evaluation metrics:** FID, Diversity, R-Precision, and MM-Distance assess generation distributions/alignment; foot skating probes plausibility; AITS measures latency. Average Error measures keyframe/trajectory deviation, AvgR editing retrieval, SRA/CRA style/content recognition, and TSI source-trajectory preservation.

**Evaluation checked:** Section 6 compares six tasks with specialist baselines and ablates instruction modulation, modality paths, aligned positions, and training stages. Main Tables 3–5 cover generation and editing, with in-between/style details in supplements. Timing is recomputed on one RTX 4090D.

**Full-text source:** https://arxiv.org/pdf/2502.02358v5

**Reading status:** full_text_checked

**Inspected version:** arXiv:2502.02358v5 [cs.CV] 22 Jul 2025

**Full-text SHA256:** aa38185437aec9e102d2fda8035bee299c985ebabaf36894951b764423374387

**Source locator:** §4 (MCM task definitions), §5 and Figure 2 (MFT/training), §6 setup and metrics, Tables 3–9; supplementary in-between and style experiments.

**Scope / curator boundary:** Multitask breadth does not imply equal supervision or unseen-combination generalization. MotionFix target retrieval and recognizer-based style scores provide partial proxies for edit correctness. Body-only representation and foot-skating metrics do not validate detailed hand-object interactions or scene dynamics.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2502.02358); checked 2026-11-19.

<a id="bamm"></a>
## BAMM: Bidirectional Autoregressive Motion Model

**bamm · 2024 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2403.19435) · [Evidence](https://arxiv.org/pdf/2403.19435v3) · Citekey: `bamm2024`

**Authors of cited version:** Ekkasit Pinyoanuntapong; Muhammad Usama Saleem; Pu Wang; Minwoo Lee; Srijan Das; Chen Chen.

**Contribution / composition:** Bidirectional autoregressive motion-token generation predicts ending and supports completion and long-sequence synthesis.

**Mechanism:** Encodes motion with a residual vector quantizer, then learns a masked bidirectional autoregressive transformer over token sequences. Its attention design combines causal token prediction with context from unmasked tokens; an end token supports duration prediction. A second refinement stage predicts residual codes and supports editing through constrained token completion.

**Input contract:** Text, optionally specified motion length, and motion tokens retained as editing/completion constraints. Long composition chains prompts through constrained generation rather than learning explicit object-state transitions.

**Data and split:** HumanML3D and KIT-ML are evaluated using standard sequence partitions. The dataset protocol states 80% training, 5% validation and 15% test. It does not claim cross-dataset identity deduplication or a held-out action-combination split.

**Evaluation metrics:** R-Precision Top-1/2/3, MM-Dist, FID, diversity and multimodality from the standard learned text-motion embedding; generation length and runtime analyses complement these distributional metrics.

**Evaluation checked:** Tables 2–3 compare text-conditioned generation with both predicted and supplied lengths, averaging 20 runs with 95% confidence intervals. Ablations examine masking/attention and duration estimation. Qualitative applications include motion completion, editing and long-sequence composition.

**Full-text source:** https://arxiv.org/pdf/2403.19435v3

**Reading status:** full_text_checked

**Inspected version:** 2403.19435v3

**Full-text SHA256:** 1dd6989b8f265b5fabd83afa1f70fe437b92cfeb423f25f4bd551935f9750056

**Source locator:** Sections 3.1–3.4, 4.1–4.3; Tables 2–3; application figures for editing/completion.

**Scope / curator boundary:** Long composition and editing are broader applications than the core single-caption quantitative benchmark. Learned feature scores do not measure object contact, task-order causality or continuous physical feasibility, and duration conditions must match for fair comparisons.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.19435); checked 2026-11-19.

<a id="infinite-motion"></a>
## Infinite Motion: Extended Motion Generation via Long Text Instructions

**infinite-motion · 2024 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2407.08443) · [Evidence](https://arxiv.org/pdf/2407.08443v2) · Citekey: `infinitemotion2024`

**Authors of cited version:** Mengtian Li; Chengshuo Zhai; Shengxiang Yao; Zhifeng Xie; Keyu Chen; Yu-Gang Jiang.

**Contribution / composition:** Extends and reassembles text-motion data, using timestamped text for long narrative generation, local editing and independent sequence splicing.

**Mechanism:** Builds HumanML3D-Extend by selecting compatible short motions, aligning root positions, interpolating boundary frames and refining feet using quadratic Bezier curves. Text descriptions receive cumulative timestamps. The generation pipeline fine-tunes MLD on extended sequences, then trains a timestamp stitcher that denoises transitions between independently supplied motion segments. Applications include timed local editing, interactive text modification and sequence splicing.

**Input contract:** Long text with temporal information and, for stitching/editing, existing motion segments or unchanged context. Timestamps are explicit control signals rather than automatically inferred task boundaries.

**Data and split:** Experiments name HumanML3D-Extend train/test sets and also evaluate its trained model on original HumanML3D test sequences. The reviewed full text does not state numeric split proportions or demonstrate source-recording/ancestor isolation before reassembly.

**Evaluation metrics:** FID, top-1/2/3 R-precision, MM-Dist, diversity and multimodality assess generation. APE and AVE assess root/body positional and variance differences; transition distance measures consecutive-pose jumps in body-local coordinates.

**Evaluation checked:** Tables compare short- and extended-benchmark results, several stitch lengths and DoubleTake. Extended examples commonly last 30–40 seconds and contain four or five actions; these are reassembled sequences, not newly captured continuous performance.

**Full-text source:** https://arxiv.org/pdf/2407.08443v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2407.08443v2

**Full-text SHA256:** 4760679184c23f21b8729dc4e2167af697570f27d8a0a6b710d42a8b297eaa41

**Source locator:** Section 3 dataset construction and generation; Algorithm 1; Sections 4.1–4.4 and 5; Tables 2–5; conclusion limitations.

**Scope / curator boundary:** Interpolation and foot refinement can alter source motion. Cross-source stitching requires consistent body representation. Reported benchmark improvement does not establish semantic dependency correctness, collision freedom, or independent withheld-composition generalization; split ancestry needs an additional audit.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2407.08443); checked 2026-11-19.

<a id="motionfix"></a>
## MotionFix: Text-Driven 3D Human Motion Editing

**motionfix · 2024 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2408.00712) · [Evidence](https://arxiv.org/pdf/2408.00712v3) · Citekey: `motionfix2024`

**Authors of cited version:** Nikos Athanasiou; Alpár Cseke; Markos Diomataris; Michael J. Black; Gül Varol.

**Contribution / composition:** MotionFix mines semantically related source/target motion pairs with a retrieval model and collects human instructions describing the change. TMED learns conditional diffusion over the target using separate source-motion and text encodings, with independently dropped conditions enabling dual-condition classifier-free guidance.

**Mechanism:** MotionFix mines semantically related source/target motion pairs with a retrieval model and collects human instructions describing the change. TMED learns conditional diffusion over the target using separate source-motion and text encodings, with independently dropped conditions enabling dual-condition classifier-free guidance.

**Input contract:** A complete source motion and natural-language editing instruction; source and target can have different durations. The model learns edit relationships from explicit triplets rather than treating a new action description as equivalent to an instruction about a supplied motion.

**Data and split:** The dataset contains 6,730 triplets and is randomly partitioned into 5,387 training, 330 validation, and 1,013 test triplets, described as 80/5/15%. The paper specifies triplet-level random splitting; it does not claim a cross-subject or source-recording-disjoint evaluation.

**Evaluation metrics:** Motion-to-motion retrieval ranks the reference target against candidates using learned embeddings; top-K recall and average rank assess target proximity. The rank of the source indicates how much the output changes, but high source similarity alone is not successful editing.

**Evaluation checked:** Section 5 compares TMED with text-motion-only baselines, body-part inpainting, and source initialization approaches. Data-size and condition-guidance ablations examine the value of paired editing supervision; qualitative edits show changed speed, direction, posture, or repetition.

**Full-text source:** https://arxiv.org/pdf/2408.00712v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2408.00712v3 [cs.CV] 24 Nov 2024

**Full-text SHA256:** b6096d8de52d0467c56581c8c82e3932e27583dde95022676e7eb3c2552adfb5

**Source locator:** §3 (pair mining/annotation and 5387/330/1013 partition), §4 (TMED and guidance), §§5.1–5.3 (retrieval protocol, comparisons, ablations).

**Scope / curator boundary:** One valid target is not the unique correct realization of an instruction, and embedding retrieval does not separately guarantee preservation of every unchanged detail. Random triplet splitting should not be read as independent-person generalization. No mesh-conditioned interaction or dynamics benchmark is claimed.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2408.00712); checked 2026-11-19.

<a id="motionclr"></a>
## Pay Attention and Move Better: Harnessing Attention for Interactive Motion Generation and Training-free Editing

**motionclr · 2024 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2410.18977) · [Evidence](https://arxiv.org/pdf/2410.18977v2) · Citekey: `motionclr2025`

**Authors of cited version:** Ling-Hao Chen; Shunlin Lu; Wenxun Dai; Zhiyang Dou; Xuan Ju; Jingbo Wang; Taku Komura; Lei Zhang.

**Contribution / composition:** MotionCLR explicitly models word-motion correspondence and manipulates attention for interactive generation edits.

**Mechanism:** Builds a diffusion motion generator with explicitly separated self-attention and word-level cross-attention. It studies their temporal/semantic roles and edits attention during inference to emphasize or erase an action, substitute content, mix examples or manipulate repetitions. The base denoiser is trained; editing operations do not require retraining for each edit.

**Input contract:** Word-level text embeddings and attention edits; some applications preserve source-motion information or use a grounding reference. These controls differ from object/scene-aware action planning.

**Data and split:** Primarily trains on HumanML3D; supplementary results include KIT-ML. Standard benchmark partitions are used but exact ratios are not restated in the inspected implementation subsection. MotionFix is used for an editing comparison.

**Evaluation metrics:** Standard R-Precision/FID/MM-Distance/diversity/multimodality; IoU between attention activation, root-speed activation and TMR moment-retrieval activation; editing semantic and motion-preservation measures.

**Evaluation checked:** Section 5 verifies generation and word-motion correspondence before evaluating editing applications. Five activation-coherence experiments include negative controls; attention manipulations are compared with task-specific baselines. Table 3 examines editing while supplementary tables extend datasets and applications.

**Full-text source:** https://arxiv.org/pdf/2410.18977v2

**Reading status:** full_text_checked

**Inspected version:** 2410.18977v2

**Full-text SHA256:** a1f8095c524319b388452db1cdb5056301391d70ba93d70b7087df28df91bfe4

**Source locator:** Sections 3–5; Tables 1–3; Section 6 and discussion of robustness; Appendix A.6.

**Scope / curator boundary:** Attention correspondence is threshold-dependent and does not guarantee faithful local causal control. Hallucinations remain; training-free describes inference editing, not the full pipeline. Physical contact and task-completion correctness are outside the reported benchmark.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.18977); checked 2026-11-19.

<a id="gmd"></a>
## Guided Motion Diffusion for Controllable Human Motion Synthesis

**gmd · 2023 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2305.12577) · [Evidence](https://arxiv.org/pdf/2305.12577v3) · Citekey: `gmd2023`

**Authors of cited version:** Korrawe Karunratanakul; Konpat Preechakul; Supasorn Suwajanakorn; Siyu Tang.

**Contribution / composition:** Adds spatial objectives to text-to-motion diffusion through emphasis projection, imputation and dense guidance.

**Mechanism:** Emphasis projection rebalances global root features against local pose features. Imputation enforces explicit known coordinates; dense guidance propagates sparse constraint gradients through the denoising prediction. A trajectory diffusion model can supply intermediate root paths.

**Input contract:** Text and a differentiable objective, optionally a supplied complete trajectory, timed keyframe locations, target and 2D obstacle SDF. Different control modes provide different information.

**Data and split:** HumanML3D supplies training and text-to-motion tests under the cited benchmark protocol. Trajectory-conditioned comparisons impute real test trajectories; keyframe and obstacle examples are separate. A new subject/compositional split is not specified.

**Evaluation metrics:** FID, R-precision and diversity measure synthesis; trajectory/keyframe error and foot skating examine control. Constraint objectives and obstacle visualizations do not amount to a full contact-dynamics benchmark.

**Evaluation checked:** §6 separates text-only, trajectory-conditioned, sparse-keyframe and obstacle tasks. Ablations examine root representation, emphasis and guidance rather than changing all conditions simultaneously.

**Full-text source:** https://arxiv.org/pdf/2305.12577v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2305.12577v3

**Full-text SHA256:** d1699db8dfc015cbb46ec519a61182af549e9131d3d52af451655ae481c061af

**Source locator:** §§3–5; §§6.1–6.5, Tables 1–3; §7 and supplementary representation/guidance discussions.

**Scope / curator boundary:** Performance depends on the pretrained motion prior, representation and usable constraint gradients. Goal satisfaction can trade against naturalness. The method does not maintain articulated-object state across long manipulation tasks.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.12577); checked 2026-11-19.

<a id="mmm"></a>
## MMM: Generative Masked Motion Model

**mmm · 2023 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2312.03596) · [Evidence](https://arxiv.org/pdf/2312.03596v2) · Citekey: `mmm2024`

**Authors of cited version:** Ekkasit Pinyoanuntapong; Pu Wang; Minwoo Lee; Chen Chen.

**Contribution / composition:** Text-conditioned masked motion tokens support in-betweening, body-part changes and long sequence synthesis.

**Mechanism:** Learns a VQ motion tokenizer with an 8,192-entry factorized codebook, then trains a text-conditioned transformer to reconstruct randomly masked tokens. Iterative parallel decoding retains confident tokens and remasks uncertain ones. Arbitrary temporal masks enable in-betweening; long generation first synthesizes prompt-specific segments and fills transition tokens. Upper-body editing uses separately pretrained upper/lower tokenizers and specialized conditioning rather than arbitrary joint editing in the default whole-body tokenizer.

**Input contract:** Text prompts, requested motion length, and optional visible motion tokens or an upper/lower-body editing partition.

**Data and split:** HumanML3D and KIT-ML use motion-sequence training/validation/test proportions of 80/5/15 percent, following the T2M protocol. No subject-disjoint or held-out semantic-combination split is reported for the composition demonstrations.

**Evaluation metrics:** FID, top-k R-precision, text-motion multimodal distance, diversity and multimodality use pretrained T2M embeddings. Average inference time per sentence (AITS) and length-dependent timing assess efficiency.

**Evaluation checked:** Quantitative generation evaluation repeats 20 times with 95 percent confidence intervals. Tables 1–2 compare benchmark generation; timing uses the same RTX A5000. Qualitative comparisons show in-betweening, upper-body replacement and sequential stories, with masking/iteration ablations.

**Full-text source:** https://arxiv.org/pdf/2312.03596v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2312.03596v2

**Full-text SHA256:** aaaa000e2059dfb61ef4aab05d61cf34d588e96b6834364e842dabd3fce409f0

**Source locator:** Sections 3.1–3.2, 4, 5 and 6; Tables 1–2; Supplement B and J.

**Scope / curator boundary:** Fine details for exceptionally long single descriptions remain difficult because training motions reach at most about 196 frames. The model does not support multi-person interactions. Token-space preservation and attractive stitching examples do not establish object-state continuity or systematically unseen skill composition.

**Publication / version note:** First public preprint 2023. First public preprint 2023.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.03596); checked 2026-11-19.

<a id="omnicontrol"></a>
## OmniControl: Control Any Joint at Any Time for Human Motion Generation

**omnicontrol · 2023 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2310.08580) · [Evidence](https://arxiv.org/pdf/2310.08580v2) · Citekey: `omnicontrol2024`

**Authors of cited version:** Yiming Xie; Varun Jampani; Lei Zhong; Deqing Sun; Huaizu Jiang.

**Contribution / composition:** Combines analytic spatial guidance and learned realism guidance for multi-joint control within text-to-motion diffusion.

**Mechanism:** Converts relative pose features to world-space joints for gradient-based spatial correction. A control network supplies realism residuals so constraints and whole-body coordination are refined together during denoising.

**Input contract:** Text plus selected joints, keyframe times and target xyz positions. Quantitative controls come from ground-truth motion trajectories; manually authored constraints are demonstrated separately.

**Data and split:** HumanML3D and KIT-ML use the cited Guo evaluation protocol. Models generate 196 frames; control densities are 1, 2, 5, 49 and 196 keyframes. No semantic-combination or subject holdout is newly established.

**Evaluation metrics:** FID, R-precision and diversity assess distribution/text quality. Trajectory failure, location failure and average positional error assess constraints. Foot skating uses 2.5 cm displacement at foot height below 5 cm.

**Evaluation checked:** Pelvis-only comparisons use matched constraints; all-joint and sampled joint-combination tests are separate. Appendix A.8 excludes KIT skating because the data lack reliable ground-height consistency.

**Full-text source:** https://arxiv.org/pdf/2310.08580v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2310.08580v2

**Full-text SHA256:** 5adbd5b18228230603561e57d8461e94e7679b7c7038ee8495230901df0ccd5d

**Source locator:** §§3.1–3.3; §4 and Tables 1–3; Appendices A.4–A.5, A.8, A.10–A.11.

**Scope / curator boundary:** Conflicting joint constraints can produce unnatural motion; skating remains and inference is expensive. GT trajectory control is a stronger information setting than text and initial state alone.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2310.08580); checked 2026-11-19.

<a id="dno"></a>
## Optimizing Diffusion Noise Can Serve As Universal Motion Priors

**dno · 2023 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2312.11994) · [Evidence](https://arxiv.org/pdf/2312.11994v2) · Citekey: `dno2024`

**Authors of cited version:** Korrawe Karunratanakul; Konpat Preechakul; Emre Aksan; Thabo Beeler; Supasorn Suwajanakorn; Siyu Tang.

**Contribution / composition:** Optimizes latent diffusion noise to satisfy editing, refinement and completion objectives without task-specific retraining.

**Mechanism:** Differentiates a motion-space objective through deterministic diffusion sampling. DDIM inversion initializes editing noise; normalized gradients and temporal noise decorrelation stabilize optimization and preserve the learned prior.

**Input contract:** An input motion or noisy/partial observations and differentiable constraints. Editing experiments optimize without text conditioning, even when text originally generated the input motion.

**Data and split:** Editing uses six input actions with sixteen random pelvis edits each, giving 96 edits. Refinement samples 300 HumanML3D test motions and adds 5 cm noise, including 6/8/10-joint partial observations.

**Evaluation metrics:** Objective error measures target-joint distance; content preservation uses action-specific frame rules. Foot skating and jitter assess artifacts; refinement additionally reports MPJPE and FID against held-out motion features.

**Evaluation checked:** Compares GMD and optimization-based priors, tests MDM/MLD/GMD backbones, and ablates gradient normalization and decorrelation. The small editing set and refinement test are distinct experiments.

**Full-text source:** https://arxiv.org/pdf/2312.11994v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2312.11994v2

**Full-text SHA256:** 723fee492b2375a17aae1d280ff42d244b70943667a5ece7186bc3958caef379

**Source locator:** §§3–5; §6.1/Table 1, §6.2/Table 2, §6.3/Table 3; §7.

**Scope / curator boundary:** Observation coverage and the underlying prior limit recovery. Unrealistic local optima remain possible, and optimization is slow: the stated editing setup takes roughly three minutes on a 3090.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.11994); checked 2026-11-19.

<a id="motionclip"></a>
## MotionCLIP: Exposing Human Motion Generation to CLIP Space

**motionclip · 2022 · Motion editing & in-betweening · method**

[Primary source](https://arxiv.org/abs/2203.08063) · [Evidence](https://arxiv.org/pdf/2203.08063v1) · Citekey: `motionclip2022`

**Authors of cited version:** Guy Tevet; Brian Gordon; Amir Hertz; Amit H. Bermano; Daniel Cohen-Or.

**Contribution / composition:** MotionCLIP trains a Transformer motion autoencoder whose latent code aligns with frozen CLIP text and rendered-image embeddings. Reconstruction and geometric losses retain motion information, while semantic alignment supports text-driven decoding, interpolation, action arithmetic, and style changes directly in the learned latent space.

**Mechanism:** MotionCLIP trains a Transformer motion autoencoder whose latent code aligns with frozen CLIP text and rendered-image embeddings. Reconstruction and geometric losses retain motion information, while semantic alignment supports text-driven decoding, interpolation, action arithmetic, and style changes directly in the learned latent space.

**Input contract:** Text or image embeddings can drive decoding; existing motions provide codes for editing and interpolation. Text labels and rendered frames supervise alignment during training. Semantic latent arithmetic differs from explicit per-joint constraints or a scheduled chain of independently specified actions.

**Data and split:** Training uses BABEL/AMASS at 30 fps, cut into 60-frame sequences whose action labels are concatenated; recognition follows the BABEL-60 benchmark. Exact train/test counts and percentages are not restated in the inspected setup. Semantic editing demonstrations do not constitute a held-out combination split.

**Evaluation metrics:** Top-1 and Top-5 action-recognition accuracy measure class information on BABEL-60. Pairwise user preference measures text-driven action generation and style transfer; architecture/loss ablations test semantic representation. No FID-based generation leaderboard is reported here, and these measures do not directly quantify edit locality.

**Evaluation checked:** Section 4 tests text-to-motion, action recognition/generation, interpolation, and style editing. Comparing text-only versus image/text alignment and reconstruction components helps separate CLIP alignment effects. Abstract prompts and pop-culture examples demonstrate qualitative semantic transfer rather than verified object interaction.

**Full-text source:** https://arxiv.org/pdf/2203.08063v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2203.08063v1 [cs.CV] 15 Mar 2022

**Full-text SHA256:** 2975f021d7c1370c44c130ff7b63875ed055881ac4415cb37aa5ed486a288585

**Source locator:** §3 and Figures 2–3 (alignment/autoencoder), §4 application experiments and ablations; concluding discussion of directional limitations; supplementary experimental settings.

**Scope / curator boundary:** The model struggles with directional language and detailed controls. CLIP alignment inherits image/text biases and may map unfamiliar descriptions to nearby known actions. Latent addition provides no strict source-preservation, temporal ordering, contact, or physical-validity guarantee.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2203.08063); checked 2026-11-19.

<a id="holden-deep-motion"></a>
## A Deep Learning Framework for Character Motion Synthesis and Editing

**holden-deep-motion · 2016 · Motion editing & in-betweening · method**

[Primary source](https://www.research.ed.ac.uk/en/publications/a-deep-learning-framework-for-character-motion-synthesis-and-edit/) · [Evidence](https://www.pure.ed.ac.uk/ws/files/25269752/motionsynthesis.pdf) · Citekey: `holdendeepmotion2016`

**Authors of cited version:** Daniel Holden; Jun Saito; Taku Komura.

**Contribution / composition:** Convolutional motion manifolds support high-level trajectory generation and optimization for constraints and style transfer.

**Mechanism:** Trains a temporal convolutional autoencoder to represent a motion manifold, then independent feedforward networks map high-level controls into that latent space. Optimization of hidden activations imposes kinematic constraints; Gram-matrix feature statistics transfer style. Foot-contact phase information resolves locomotion ambiguity, and constraint optimization cleans generated motion.

**Input contract:** Drawn terrain/root trajectories, speed/contact timing or hand/foot trajectories; optional style-reference clips and positional/bone-length constraints. Text and object geometry are not conditioning inputs.

**Data and split:** Builds a large mocap database, using overlapping 240-frame training windows. Experimental examples include trajectory profiles and punching/kicking data withheld from network training; exact partition percentages and subject-separated split are not reported.

**Evaluation metrics:** Runtime breakdown, generated frames per second, qualitative trajectory/constraint satisfaction and temporal smoothness; compares autoencoder variants with/without pooling/dropout. No standardized text-motion FID or task success benchmark is reported.

**Evaluation checked:** Section 8 demonstrates locomotion speed changes, endpoint controls, latent-space editing, multiple styles and a 200-character crowd. Table 1 reports computation times on a GTX 660; comparison figures show temporal noise when representation components are removed.

**Full-text source:** https://www.pure.ed.ac.uk/ws/files/25269752/motionsynthesis.pdf

**Reading status:** full_text_checked

**Inspected version:** Author/institution or proceedings PDF as retrieved 2026-11-19; version string not printed for this paper.

**Full-text SHA256:** 56b5890eac9d0ceb43ff77ef7e6cfe1e63f5e670eb8bc0d764d07672f494fb4d

**Source locator:** Sections 4–7; Section 8 Experimental Results and Table 1; Section 9 Discussions.

**Scope / curator boundary:** Kinematic latent optimization does not enforce dynamics. High-level ambiguities need task-specific handling, and the reported withheld examples do not establish arbitrary new action combinations or scene-aware manipulation.

**Composition axes:** editing.

**Metadata:** official; [source](https://www.research.ed.ac.uk/en/publications/a-deep-learning-framework-for-character-motion-synthesis-and-edit/); checked 2026-11-19.

<a id="momask"></a>
## MoMask: Generative Masked Modeling of 3D Human Motions

**momask · 2023 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2312.00063) · [Evidence](https://arxiv.org/pdf/2312.00063v1) · Citekey: `momask2023`

**Authors of cited version:** Chuan Guo; Yuxuan Mu; Muhammad Gohar Javed; Sen Wang; Li Cheng.

**Contribution / composition:** Hierarchical residual quantization and masked token generation provide a discrete motion prior with text-guided temporal inpainting.

**Mechanism:** Tokenizes motion with hierarchical residual vector quantization: a base code sequence captures coarse content and subsequent code layers encode residual detail. A text-conditioned masked transformer iteratively predicts the base layer; a residual transformer generates the remaining quantization layers. Classifier-free guidance is applied to both. Temporal inpainting keeps selected reference intervals and regenerates the remainder under text conditioning.

**Input contract:** A sentence and sequence length, or a text instruction plus reference temporal regions for inpainting. The base representation is frame-sequence oriented rather than an explicit independent joint-token interface.

**Data and split:** HumanML3D and KIT-ML are mirrored and partitioned into training/test/validation at 80/15/5 percent. These ordinary motion-language splits are not described as withheld composition-pair or subject splits.

**Evaluation metrics:** FID assesses real/generated motion feature distributions; top-k R-precision and multimodal distance assess semantic alignment; multimodality assesses variation for one prompt. VQ reconstruction errors, inference cost and user preference provide supplementary evaluation.

**Evaluation checked:** Table 1 compares text generation against diffusion and token models. Inference-time comparisons use the same Nvidia 2080Ti; ablations vary quantization layers, dropout and decoding. Figure 6 shows temporally specified text-guided inpainting.

**Full-text source:** https://arxiv.org/pdf/2312.00063v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2312.00063v1

**Full-text SHA256:** 69de7fc3144a25308e7bc56a3fcc294cd2e18ea9024392601dd87951b0045aba

**Source locator:** Sections 3.1–3.3, 4 and 5; Table 1; Figures 5–6; quantization ablations and Discussion limitations.

**Scope / curator boundary:** The authors report limited diversity, a required target length, and difficulty with rapidly changing root motion such as spinning. Tokenization and temporal inpainting do not establish cross-dataset skill transfer, object interaction or physical task completion.

**Publication / version note:** First public preprint 2023. First public preprint 2023.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.00063); checked 2026-11-19.

<a id="remodiffuse"></a>
## ReMoDiffuse: Retrieval-Augmented Motion Diffusion Model

**remodiffuse · 2023 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2304.01116) · [Evidence](https://arxiv.org/pdf/2304.01116v1) · Citekey: `remodiffuse2023`

**Authors of cited version:** Mingyuan Zhang; Xinying Guo; Liang Pan; Zhongang Cai; Fangzhou Hong; Huirong Li; Lei Yang; Ziwei Liu.

**Contribution / composition:** Reuses training-database motion and text examples inside diffusion rather than simply concatenating retrieved clips.

**Mechanism:** Hybrid retrieval combines CLIP semantic similarity and length-related kinematic compatibility. Semantic-modulated attention absorbs retrieved motion/text features; condition mixture combines text/retrieval/unconditional predictions with tuned weights.

**Input contract:** Target text and expected motion length plus a retrieval database built from training examples. Retrieved motion is a reference condition; no future test trajectory is intended as input.

**Data and split:** HumanML3D and KIT-ML benchmark train/test protocols are used. The retrieval store consists of training entities. Rarity is computed relative to training captions; this is not a separately constructed unseen skill-pair split.

**Evaluation metrics:** FID, R-precision, multimodal distance, diversity and multimodality measure generation. Tail-5% MM distance and bin-balanced MM distance examine rare-caption behavior according to nearest training-text similarity.

**Evaluation checked:** Standard test tables and retrieval/attention ablations are evaluated, with twenty repeated runs and confidence intervals. Rarity-stratified analysis distinguishes common from uncommon text conditions.

**Full-text source:** https://arxiv.org/pdf/2304.01116v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2304.01116v1

**Full-text SHA256:** acce93d3c24949807ad15839690dbc2db4873c3fc34e989d9e9bdae18107dc51

**Source locator:** §§3.1–3.5; §4.1–4.4, Tables 2–4; rarity evaluation around Figure 5.

**Scope / curator boundary:** Database coverage and retrieved reference quality constrain benefits. Rarity in embedding space is not equivalent to semantic compositional novelty, and motion-distribution gains do not certify contact, dynamics or task completion.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.01116); checked 2026-11-19.

<a id="t2m-gpt"></a>
## T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations

**t2m-gpt · 2023 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2301.06052) · [Evidence](https://arxiv.org/pdf/2301.06052v4) · Citekey: `t2mgpt2023`

**Authors of cited version:** Jianrong Zhang; Yangsong Zhang; Xiaodong Cun; Shaoli Huang; Yong Zhang; Hongwei Zhao; Hongtao Lu; Xi Shen.

**Contribution / composition:** T2M-GPT first trains a convolutional VQ-VAE to compress motion into discrete indices, using exponential-moving-average code updates and code reset. A text-conditioned causal Transformer predicts indices autoregressively; deliberately corrupted input indices reduce the discrepancy between teacher-forced training and sampled inference.

**Mechanism:** T2M-GPT first trains a convolutional VQ-VAE to compress motion into discrete indices, using exponential-moving-average code updates and code reset. A text-conditioned causal Transformer predicts indices autoregressively; deliberately corrupted input indices reduce the discrepancy between teacher-forced training and sampled inference.

**Input contract:** A CLIP text embedding initializes generation; sampled motion-code tokens become subsequent context and a learned end token terminates output. No object geometry, scene map, or explicit body-part schedule is required in its principal text-to-motion task.

**Data and split:** HumanML3D and KIT-ML each use 80% training, 5% validation, and 15% test motions following the cited benchmark protocol. Model selection minimizes validation FID; test results are then reported. HumanML3D is processed at 20 fps and KIT-ML at 12.5 fps.

**Evaluation metrics:** R-Precision and MM-Distance measure text-motion correspondence in pretrained feature spaces; FID measures generated/reference distribution mismatch; Diversity measures across-sample variation and Multimodality variation for one prompt. Reconstruction FID and retrieval quantify tokenizer quality separately from full generation.

**Evaluation checked:** Tables 1–2 compare benchmark generation, and Table 3 tests EMA/code-reset combinations. Appendix ablations vary corruption rate, architecture, losses, and dataset amount. Metrics are repeated 20 times with confidence intervals; length-conditioned competitors are marked separately.

**Full-text source:** https://arxiv.org/pdf/2301.06052v4

**Reading status:** full_text_checked

**Inspected version:** arXiv:2301.06052v4 [cs.CV] 24 Sep 2023

**Full-text SHA256:** 682b4818d0d4bc9799fe9038341162a6e63477dfbc31e597411cecb3b1966197

**Source locator:** §§3.1–3.2 (VQ-VAE/GPT), §4.1 (80/5/15 protocols), Tables 1–3; appendix C (corruption), E (metrics), G (limitations).

**Scope / curator boundary:** Token quantization limits fine-grained edit resolution and can introduce jitter; autoregressive errors remain possible despite corruption training. A strong short-text benchmark result does not establish long ordered composition, unseen object manipulation, or physically executable control.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2301.06052); checked 2026-11-19.

<a id="tmr"></a>
## TMR: Text-to-Motion Retrieval Using Contrastive 3D Human Motion Synthesis

**tmr · 2023 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2305.00976) · [Evidence](https://arxiv.org/pdf/2305.00976v2) · Citekey: `tmr2023`

**Authors of cited version:** Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** Learns text-motion embeddings using contrastive retrieval and motion synthesis, supplying a retrieval benchmark and evaluator foundation.

**Mechanism:** Extends a TEMOS-style text-motion variational model with symmetric InfoNCE contrastive training while retaining motion reconstruction and distribution-alignment losses. Similar sentence pairs are filtered from the negative set to avoid repelling semantically equivalent descriptions. Text and motion embeddings support retrieval; sliding windows enable localization in longer recordings.

**Input contract:** A text query or motion query for retrieval, with a candidate gallery. The decoder is a training aid and generation branch; retrieval is not itself motion composition.

**Data and split:** After preprocessing and mirroring, HumanML3D has 23,384/1,460/4,380 training/validation/test motions, and KIT has 4,888/300/830. These are processed counts, not independent captured-person counts. Testing selects the first caption per motion.

**Evaluation metrics:** Recall at ranks 1/2/3/5/10 and median rank for text-to-motion and motion-to-text retrieval. Four protocols vary gallery size and treatment of semantically similar captions; localization examples inspect window similarities.

**Evaluation checked:** Tables 1–2 compare TMR with TEMOS and the Guo evaluator under matched retrieval protocols. Ablations isolate reconstruction, contrastive learning and negative filtering. Additional long-sequence retrieval illustrates temporal grounding without a separate localization-trained model.

**Full-text source:** https://arxiv.org/pdf/2305.00976v2

**Reading status:** full_text_checked

**Inspected version:** 2305.00976v2

**Full-text SHA256:** a981b14b9c261432b8af7cd2b8fcccbfe2b0d35dc80f26093dfa38510bd0d995

**Source locator:** Sections 3.1–3.3, 4.1–4.3; retrieval protocol and Tables 1–2; long-sequence retrieval examples.

**Scope / curator boundary:** Retrieval performance depends on gallery construction and ambiguous language. Embedding similarity can support evaluation but is not an independent physics or contact measure; cross-dataset actor independence is not established by these sequence partitions.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.00976); checked 2026-11-19.

<a id="mld"></a>
## Executing Your Commands via Motion Diffusion in Latent Space

**mld · 2022 · Generative backbones & representations · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.pdf) · Citekey: `mld2023`

**Authors of cited version:** Chen, Xin; Jiang, Biao; Liu, Wen; Huang, Zilong; Fu, Bin; Chen, Tao; Yu, Gang.

**Contribution / composition:** MLD compresses motions with a VAE before conditional latent diffusion, substantially reducing denoising cost.

**Mechanism:** First trains a transformer-based motion VAE to reconstruct sequences in a compact latent space, then freezes that representation and trains conditional denoising diffusion over its latents. Frozen CLIP text embeddings or learned action embeddings condition the denoiser; classifier-free guidance balances fidelity and variation. The decoder maps generated latents back to whole motion sequences, reducing denoising cost relative to raw-frame diffusion.

**Input contract:** Text plus sequence length, a predefined action category, or an empty condition for unconditional generation. Future motion is output rather than a required trajectory condition.

**Data and split:** Text experiments inherit HumanML3D and KIT protocols. UESTC action evaluation reports FIDtrain and FIDtest, whereas HumanAct12 reports training-reference FID. The main text does not restate all numeric split proportions or add a semantic-combination holdout.

**Evaluation metrics:** FID, R-precision, MM-Dist, diversity and multimodality measure generation. MPJPE, Procrustes-aligned MPJPE and acceleration error assess VAE reconstruction; AITS and elapsed time assess computational efficiency; action accuracy assesses action-conditioned samples.

**Evaluation checked:** Text evaluation repeats 20 times with 95 percent confidence intervals. Tables compare text, action and unconditional tasks; VAE and latent-dimension ablations distinguish reconstruction from diffusion quality.

**Full-text source:** https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Primary author/proceedings PDF retrieved 2026-11-19; identity fixed by SHA256

**Full-text SHA256:** 28b2170d37d283b6e1ee119dcdae6f3aca57801782d3c25a8b8f5345ae2f1286

**Source locator:** Sections 3.1–3.3, 4.1–4.5, 5 and 6; Tables 1–5.

**Scope / curator boundary:** Sequence latents do not expose a direct joint/frame editing correspondence. The stated maximum sequence length remains bounded by the dataset; articulated body generation does not cover detailed hands or faces. Efficient benchmark generation alone does not validate temporal skill composition or object-conditioned behavior.

**Publication / version note:** First preprint arXiv:2212.04048 in 2022; CVPR 2023. First preprint arXiv:2212.04048 in 2022; CVPR 2023.

**Composition axes:** representation.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.html); checked 2026-11-19.

<a id="mdm"></a>
## Human Motion Diffusion Model

**mdm · 2022 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2209.14916) · [Evidence](https://arxiv.org/pdf/2209.14916v2) · Citekey: `mdm2022`

**Authors of cited version:** Guy Tevet; Sigal Raab; Brian Gordon; Yonatan Shafir; Daniel Cohen-Or; Amit H. Bermano.

**Contribution / composition:** MDM uses a classifier-free Transformer diffusion model predicting clean motion rather than noise, making position, velocity, and foot-contact losses available directly. It supports text-, action-, and unconditional generation; clamping known regions during denoising enables temporal in-betweening and body-part editing.

**Mechanism:** MDM uses a classifier-free Transformer diffusion model predicting clean motion rather than noise, making position, velocity, and foot-contact losses available directly. It supports text-, action-, and unconditional generation; clamping known regions during denoising enables temporal in-betweening and body-part editing.

**Input contract:** Text embeddings, action labels, or no condition depending on the trained model. Editing supplies observed frames or joints. Main text benchmarks use reference motion lengths, an important difference from autonomous length prediction and free-form narrative planning.

**Data and split:** HumanML3D/KIT follow benchmark splits, with exact text-motion proportions not restated in the inspected setup. UESTC uses the cross-subject protocol and HumanAct12 the provided sequences. Main text results use 20 evaluations; Multimodality uses five.

**Evaluation metrics:** R-Precision/MM-Distance assess text alignment, FID feature-distribution mismatch, Diversity overall variation, and Multimodality same-condition variation. Action tasks add recognition accuracy; unconditional evaluation adds KID and precision/recall. User comparisons supplement learned-feature proxies.

**Evaluation checked:** Tables 1–2 evaluate text generation, Tables 3–4 action generation, and Table 5 unconditional generation; §5.1 demonstrates inpainting. Backbone and guidance sweeps are reported. Crucially, text experiments do not apply geometric losses because joints/contact are explicit in the representation.

**Full-text source:** https://arxiv.org/pdf/2209.14916v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2209.14916v2 [cs.CV] 3 Oct 2022

**Full-text SHA256:** cfe20558dfb4670e9a23e52cff289bb305ebace9b079333e9541e3dfa2b2669c

**Source locator:** §3 and Equations 2–5 (clean prediction/geometric losses), §§4.1–4.2, Tables 1–5, §5.1 (editing), Figure 4 (guidance/user study).

**Scope / curator boundary:** Foot-contact losses improve selected visible artifacts but do not establish dynamical validity. Inpainting is primarily demonstrated qualitatively, and benchmark scores do not certify edit preservation or action ordering. Expensive iterative diffusion and fixed evaluator assumptions affect practical comparisons.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2209.14916); checked 2026-11-19.

<a id="motion-puzzle"></a>
## Motion Puzzle: Arbitrary Motion Style Transfer by Body Part

**motion-puzzle · 2022 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2202.05274) · [Evidence](https://arxiv.org/pdf/2202.05274v2) · Citekey: `motionpuzzle2022`

**Authors of cited version:** Deok-Kyeong Jang; Soomin Park; Sung-Hee Lee.

**Contribution / composition:** Transfers multiple local motion styles to body parts using topology-aware features, AdaIN and attention without style labels or paired motions.

**Mechanism:** Disentangles source motion content from style using spatial-temporal skeleton graph encoders. Body-part adaptive normalization transfers global feature statistics while part attention transfers time-varying patterns. Multiple exemplar styles can be assigned independently to legs, spine and arms, then decoded into one continuous motion without style-label supervision.

**Input contract:** One content-motion sequence and one or more target style-motion exemplars, with body-part assignments. Exemplar motion supplies style rather than text or object affordances.

**Data and split:** Training uses CMU-derived 21-joint, 60-fps clips with overlap and mirroring/temporal augmentation. Evaluation uses held-out and unseen clips plus the labeled Xia dataset; an exact independent train/test proportion is not reported in the inspected protocol.

**Evaluation metrics:** Fréchet Motion Distance from action-classifier features, content recognition accuracy CRA and style recognition accuracy SRA; per-joint positional differences inspect locality of part changes.

**Evaluation checked:** Section 7 demonstrates independently mixed part styles, interpolation and a minute-long heterogeneous sequence. Table 2 evaluates 2,500 stylized samples per method over ten trials; ablations remove part attention or part-aware normalization. Outputs share foot-sliding cleanup postprocessing.

**Full-text source:** https://arxiv.org/pdf/2202.05274v2

**Reading status:** full_text_checked

**Inspected version:** 2202.05274v2

**Full-text SHA256:** ea0cbd5554ef4f2c025ee5a246aaf21ded33c976b590cd0020e567f832c4a330

**Source locator:** Sections 3–5; Sections 7.1–7.3 and Table 2; Section 8 Limitations and Future Work.

**Scope / curator boundary:** Contact and environmental interaction are not modeled, so contact-related content can change. Strong style classification can trade off with content preservation; unseen style transfer does not guarantee physically compatible simultaneous skills.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2202.05274); checked 2026-11-19.

<a id="motiondiffuse"></a>
## MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model

**motiondiffuse · 2022 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2208.15001) · [Evidence](https://arxiv.org/pdf/2208.15001v1) · Citekey: `motiondiffuse2022`

**Authors of cited version:** Mingyuan Zhang; Zhongang Cai; Liang Pan; Fangzhou Hong; Xinying Guo; Lei Yang; Ziwei Liu.

**Contribution / composition:** Text-conditioned diffusion models human motion and provides a foundation for fine-grained guided synthesis.

**Mechanism:** Applies a denoising diffusion model directly to human motion, with a text encoder and efficient linear-transformer motion decoder. Timestep/text-dependent stylization blocks modulate denoising. For body-part control, predicted noises from separate text prompts are masked and combined with a consistency correction; time-varying control similarly composes padded interval-specific noises. These operations reuse a trained prior without separately captured composite supervision.

**Input contract:** Natural-language description and motion length; optional descriptions assigned to body masks or time intervals. Action-conditioned experiments replace action indices with their semantic descriptions.

**Data and split:** Uses HumanML3D and KIT-ML benchmark test sets, plus HumanAct12 and UESTC action experiments. The reviewed full-text experimental description inherits dataset protocols without restating numerical sequence-split proportions or a systematic withheld-combination split.

**Evaluation metrics:** FID and R-precision are principal metrics; MM-Dist evaluates text-motion feature distance, diversity and multimodality evaluate sample variation. Retrieval compares a matching caption to 31 randomly selected distractors; reports top-1/2/3 accuracy.

**Evaluation checked:** Tables 1–2 evaluate text generation with real motion lengths and 20 repetitions/95 percent confidence intervals. Additional action and manipulation experiments and architecture ablations test pretrained CLIP and efficient attention.

**Full-text source:** https://arxiv.org/pdf/2208.15001v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2208.15001v1

**Full-text SHA256:** dac6aa8d785f490533312ab8dd900e49213c0fc53699b9f029d2dccb88bec2e0

**Source locator:** Sections 3.2–3.5 and 4.1–4.3; Equations 10–11; Tables 1–3.

**Scope / curator boundary:** Part/time noise composition is demonstrated under chosen masks and intervals, not an arbitrary task dependency benchmark. Denoising cost is substantial and the kinematic objective does not enforce object dynamics or guaranteed collision/contact consistency. A familiar caption split does not isolate unseen skill pairs.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2208.15001); checked 2026-11-19.

<a id="temos"></a>
## TEMOS: Generating diverse human motions from textual descriptions

**temos · 2022 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2204.14109) · [Evidence](https://arxiv.org/pdf/2204.14109v2) · Citekey: `temos2022`

**Authors of cited version:** Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** TEMOS learns paired variational Transformer encoders for text and motion with a shared decoder. Reconstruction, embedding-similarity, Gaussian-prior, and cross-modal distribution losses align their latent distributions; sampling from the text latent generates multiple plausible motions for a description.

**Mechanism:** TEMOS learns paired variational Transformer encoders for text and motion with a shared decoder. Reconstruction, embedding-similarity, Gaussian-prior, and cross-modal distribution losses align their latent distributions; sampling from the text latent generates multiple plausible motions for a description.

**Input contract:** Natural language and requested duration, implemented through decoder positional encodings. A frozen DistilBERT supplies language features. Generation requires no initial ground-truth pose, unlike several compared earlier methods, and does not model manipulated object geometry.

**Data and split:** KIT protocol extracts 1,784 training, 566 validation, and 587 test motions; common comparison uses 520 test sequences available from a baseline. KIT-SMPL maps to 2,888 annotated AMASS sequences. This differs from later 80/5/15 KIT protocols and should not be pooled blindly.

**Evaluation metrics:** Average Positional Error (APE) and Average Variance Error (AVE) compare root, trajectory, local, and global joint coordinates after canonicalization. Single-random, latent-mean, average-of-ten, and best-of-ten sampling results have distinct interpretations; best-of-ten uses reference-based selection.

**Evaluation checked:** Table 1 compares earlier text-motion systems; Table 2 separates deterministic and variational sampling; Tables 3–4 ablate architecture/losses and frozen language features. Appendix C documents metric implementation corrections and human-study details, useful for fair reproduction.

**Full-text source:** https://arxiv.org/pdf/2204.14109v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2204.14109v2 [cs.CV] 22 Jul 2022

**Full-text SHA256:** dc09335fbd3b0efb6cccbb61b231b4c49acdadd687b0a1c8cce42051b55d86aa

**Source locator:** §3 architecture/losses, §4.1 exact KIT counts and 520-sequence subset, Tables 1–4; appendices A.5 and C (sampling and metric caveats).

**Scope / curator boundary:** One-reference coordinate errors penalize diverse valid outputs, while oracle best-of-ten overstates a deployable single sample. KIT is dominated by limited movement categories. The model lacks detailed object/contact inputs, and a shared semantic latent does not itself prove compositional generalization.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2204.14109); checked 2026-11-19.

<a id="actor"></a>
## Action-Conditioned 3D Human Motion Synthesis with Transformer VAE

**actor · 2021 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2104.05670) · [Evidence](https://arxiv.org/pdf/2104.05670) · Citekey: `actor2021`

**Authors of cited version:** Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** ACTOR samples variable-duration SMPL sequences from categorical actions using a Transformer VAE.

**Mechanism:** Uses a transformer variational autoencoder to learn action-conditioned distributions over variable-duration SMPL motion. Action-dependent latent tokens encode sequences, while the decoder combines a sampled latent with positional encodings to produce all frames in parallel. Rotation and body-coordinate reconstruction losses improve geometry beyond unconstrained joint-location output.

**Input contract:** An action category, desired sequence length and latent noise; the action vocabulary is dataset-specific. Inputs are discrete labels rather than compositional free-form language or object meshes.

**Data and split:** UESTC follows the official cross-subject protocol: 10,650 training and 13,350 test sequences after retaining eight static viewpoints. NTU-13 and HumanAct12 protocols provide no separate test split, so their FID uses training references.

**Evaluation metrics:** Action-classifier FID, recognition accuracy, overall diversity and per-action multimodality. UESTC distinguishes training-reference FIDtr from held-out FIDtest; classification evaluates generated data as augmentation.

**Evaluation checked:** Ablations examine rotation/vertex losses, latent regularization, root translation and variable length. Experiments compare action-conditioned baselines and assess recognizing real held-out actions after training on generated motions. Tables separate datasets with genuinely held-out evaluation from training-distribution matching.

**Full-text source:** https://arxiv.org/pdf/2104.05670

**Reading status:** full_text_checked

**Inspected version:** Author/institution or proceedings PDF as retrieved 2026-11-19; version string not printed for this paper.

**Full-text SHA256:** 33613983a89f3ce731236ca82205a9a1c43084cc1e7959d08b7128fbb9457ec9

**Source locator:** Sections 3.1–3.2; Sections 4.1–4.3, Tables 1–4; supplementary implementation and duration studies.

**Scope / curator boundary:** Actions are trimmed single-category sequences. Single-action realism and augmentation do not demonstrate action-order composition. Monocularly recovered training motion and fixed-length recognition networks introduce evaluation artifacts, especially outside their usual duration range.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2104.05670); checked 2026-11-19.

<a id="skeleton-aware-retarget"></a>
## Skeleton-Aware Networks for Deep Motion Retargeting

**skeleton-aware-retarget · 2020 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2005.05732) · [Evidence](https://arxiv.org/pdf/2005.05732v1) · Citekey: `skeletonawareretarget2020`

**Authors of cited version:** Kfir Aberman; Peizhuo Li; Dani Lischinski; Olga Sorkine-Hornung; Daniel Cohen-Or; Baoquan Chen.

**Contribution / composition:** Skeleton-aware convolutions and pooling map homeomorphic skeletons into a common primal-skeleton motion latent space.

**Mechanism:** Introduces skeleton-aware convolution, pooling and unpooling operators that respect articulated adjacency. Homeomorphic skeleton graphs reduce to a shared primal structure, permitting separate encoders/decoders to exchange latent motion across skeletons with different bone counts and proportions. Unpaired retargeting combines reconstruction, cycle/latent consistency, adversarial realism and end-effector constraints; forward kinematics connects rotations with positional supervision.

**Input contract:** A source skeletal motion, source offsets and target skeleton offsets/structure. The method assumes compatible main limbs/end effectors and a graph homeomorphism, not arbitrary unrelated anatomy.

**Data and split:** Mixamo group A contains 24 characters: 20 train and four unseen test characters; evaluation uses 106 test motions. Cross-structural group B has five characters, four train and one test. Motions are available across characters for quantitative ground truth although training is unpaired.

**Evaluation metrics:** Retargeting error averages Euclidean joint-position discrepancy to target ground truth, normalized by skeleton height; Table 2 scales this by 1,000. Reconstruction and denoising experiments also compare conventional versus skeleton-aware operators.

**Evaluation checked:** Compares NKN, PMnet, rotation copying and a CycleGAN adaptation; ablates shared latents, operators and adversarial loss. Cross-structural experiments insert joints along existing branches rather than creating new functional limbs.

**Full-text source:** https://arxiv.org/pdf/2005.05732v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2005.05732v1

**Full-text SHA256:** 4bcc7909d54711b9ed8b9edef39569837bd519bdcc75e9585991efb48064b71e

**Source locator:** Sections 3–5, 6.1–6.3; Equation 10; Tables 1–2; Figures 7–10.

**Scope / curator boundary:** Compatible topology and end-effectors restrict scope. Retargeting preserves existing motion semantics and is not independent skill synthesis. Positional accuracy does not guarantee exact contact, stable physics, finger dexterity or validity for a new robot with different actuation.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2005.05732); checked 2026-11-19.

<a id="unpaired-style"></a>
## Unpaired Motion Style Transfer from Video to Animation

**unpaired-style · 2020 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/2005.05751) · [Evidence](https://arxiv.org/pdf/2005.05751v1) · Citekey: `unpairedstyle2020`

**Authors of cited version:** Kfir Aberman; Yijia Weng; Dani Lischinski; Daniel Cohen-Or; Baoquan Chen.

**Contribution / composition:** The style-transfer network separates temporally varying motion content from a temporally invariant style code. A convolutional decoder uses adaptive instance normalization to inject style, with reconstruction, adversarial, and latent constraints; aligned 2D/3D style embeddings allow style extraction from video poses.

**Mechanism:** The style-transfer network separates temporally varying motion content from a temporally invariant style code. A convolutional decoder uses adaptive instance normalization to inject style, with reconstruction, adversarial, and latent constraints; aligned 2D/3D style embeddings allow style extraction from video poses.

**Input contract:** A content motion and reference style from a 3D motion or estimated 2D joints in a short video. Training uses unpaired motions carrying style labels rather than paired same-content examples across every style. Output rotations can directly animate a character.

**Data and split:** Two motion collections yield approximately 1,500 and 10,500 overlapping 32-frame clips; each has disjoint train/test samples with 10% held out. Separate experiments exclude an entire style to test unseen-style transfer. This clip split does not establish source-recording independence.

**Evaluation metrics:** Human ratings measure realism, content preservation, and style transfer. PCA/t-SNE visualizations examine content/style organization and phase behavior. Table 1 reports preference and realism ratios; the paper does not introduce FID-based standardized text-motion evaluation.

**Evaluation checked:** Section 5 compares against Holden-style transfer and other baselines, tests seen/unseen styles, style interpolation, video-derived style, and loss/representation ablations. User questions distinguish whether the content was retained from whether the target style was transferred.

**Full-text source:** https://arxiv.org/pdf/2005.05751v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2005.05751v1 [cs.GR] 12 May 2020

**Full-text SHA256:** 35ab434af7cce3df4f9c170dd14fdd4de4ed037c5649ef0a823675523b638fba

**Source locator:** §§3–4 (content/style encoders, AdaIN and training collections), §5 and Table 1; unseen-style and content-code analyses in Figures 5–8.

**Scope / curator boundary:** Small style vocabularies can overfit: unseen-style generalization improves with the larger collection. Style/content separation is learned rather than formally identifiable, and temporal convolutions do not guarantee contact preservation. The task concerns appearance of motion, not semantic task ordering or object manipulation.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2005.05751); checked 2026-11-19.

<a id="language2pose"></a>
## Language2Pose: Natural Language Grounded Pose Forecasting

**language2pose · 2019 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/1907.01108) · [Evidence](https://arxiv.org/pdf/1907.01108v2) · Citekey: `language2pose2019`

**Authors of cited version:** Chaitanya Ahuja; Louis-Philippe Morency.

**Contribution / composition:** Joint language-to-pose embedding is trained with a short-to-long curriculum for sentence-conditioned animation.

**Mechanism:** Learns a shared latent space for natural-language descriptions and pose sequences using jointly trained language/pose encoders and a pose decoder. Cross-modal reconstruction, pose autoencoding and latent-alignment losses train the mapping. A curriculum starts with short sequence prefixes and progressively increases duration; Smooth L1 reduces sensitivity to outliers.

**Input contract:** A natural-language description controls a generated pose animation, including speed/direction details. No object geometry or scene representation is supplied, and outputs are not dynamically executed.

**Data and split:** Uses KIT Motion-Language data. Twenty percent of the data is randomly held out for evaluation; the paper does not establish subject- or mother-recording-disjoint grouping for that random partition.

**Evaluation metrics:** Average Position Error APE by joint grouping and Probability of Correct Keypoints PCK; subjective comparisons judge animation quality and language correspondence. Coordinate errors are evaluated against paired reference trajectories.

**Evaluation checked:** Compares the joint language-to-pose model with prior language-to-motion mappings and encoder/decoder design variants. Section 6 probes root/joint errors and qualitative speed/direction examples, while a user study complements deterministic coordinate reconstruction measures.

**Full-text source:** https://arxiv.org/pdf/1907.01108v2

**Reading status:** full_text_checked

**Inspected version:** 1907.01108v2

**Full-text SHA256:** 0190b9879cd44507b33c2510fa14293abcd8b40f2f415a71368943c2d1de2865

**Source locator:** Sections 4.1–4.4; Sections 5.1–5.4; Section 6, Table 1 and user-study results.

**Scope / curator boundary:** One-to-many language-motion ambiguity makes paired coordinate error an incomplete realism metric. Curriculum reconstruction results do not demonstrate unseen multi-action composition, object interaction, contact consistency or independent physical validity; random sample holdout may retain related motions.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/1907.01108); checked 2026-11-19.

<a id="plappert-bidirectional"></a>
## Learning a bidirectional mapping between human whole-body motion and natural language using deep recurrent neural networks

**plappert-bidirectional · 2017 · Generative backbones & representations · method**

[Primary source](https://arxiv.org/abs/1705.06400) · [Evidence](https://arxiv.org/pdf/1705.06400v2) · Citekey: `plappertbidirectional2018`

**Authors of cited version:** Matthias Plappert; Christian Mandery; Tamim Asfour.

**Contribution / composition:** Sequence-to-sequence RNN learns shared continuous language/motion representations without manual motion segmentation.

**Mechanism:** Trains two probabilistic sequence-to-sequence recurrent models, one mapping whole-body motion to words and the other mapping language to motion. Motion uses the common Master Motor Map representation with root and joint parameters, while the motion decoder predicts a mixture distribution and stopping probability. Multiple hypotheses can be sampled and ranked by model likelihood, without explicit action segmentation.

**Input contract:** A motion sequence for captioning or a natural-language sentence for motion synthesis. This is a bidirectional translation framework, not a multimodal task planner.

**Data and split:** Uses KIT Motion-Language release 2016-10-10. After filtering, 2,846 motions and 6,187 captions remain. Random training/validation/test split is 80/10/10 percent; every motion and all associated captions stay together. Training uses offset downsampling augmentation.

**Evaluation metrics:** Corpus BLEU, with up to four-gram matches, evaluates generated descriptions. Text-to-motion is evaluated by recaptioning generated motion and computing BLEU, including relative retention against the motion-captioning baseline; likelihood ranks hypotheses.

**Evaluation checked:** Tables 2–4 report caption and round-trip scores on training/test sets. Qualitative examples include locomotion, wiping, kicking and handed waving. Latent-space experiments explore how semantic changes affect representations.

**Full-text source:** https://arxiv.org/pdf/1705.06400v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:1705.06400v2

**Full-text SHA256:** 456ddb4b4293ae43c3ad856357a7fd9bc5d17176433f03b3a38bd6b456a80ed6

**Source locator:** Sections 3, 4.1–4.3, 5.1, 5.3.3 and 5.4.3; Tables 2–4; Figure 8.

**Scope / curator boundary:** Round-trip evaluation inherits errors and biases of the learned captioner, so it is not independent physical or motion-fidelity evidence. The authors discuss ambiguity and why positional MSE is insufficient. Random recording splits do not establish unseen skill-combination, subject or object-task generalization.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/1705.06400); checked 2026-11-19.

<a id="cosmi"></a>
## COSMI: COmpositional Synthesis of Multi-object Interactions

**cosmi · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2610.03252) · [Evidence](https://arxiv.org/pdf/2610.03252v1) · Citekey: `cosmi2026`

**Authors of cited version:** Daniel Eskandar; Ilya A. Petrov; Gerard Pons-Moll.

**Contribution / composition:** Composes contact-local captured interactions and learns a text-conditioned multi-object diffusion model.

**Mechanism:** Transfer interacting body parts with their objects, use mirrored sources, semantic feasibility and geometric rejection; weight-shared object slots implement variable-count diffusion.

**Input contract:** Text, object meshes/names and initial poses for variable numbers of objects. Captured local interaction parts and their associated objects are transferred together; semantic/geometric gates reject unsuitable combinations before text-conditioned diffusion learns the assembled corpus.

**Data and split:** Uses composition holdout rather than actor holdout: approximately 187k training and 35k test sequences. Test excludes all black-chair instances and five combinations: walking/apple, sitting/flip-phone, camera/mug, foot-interaction/drinking and standing/water-bottle. Individual component skills remain available in training.

**Evaluation metrics:** FID, R-Precision Top-1/3, MM-Distance, diversity, foot sliding, object jerk, temporal/body contact accuracy and frame penetration. Articulated objects add hinge error and sweep; every test sequence has three generations.

**Evaluation checked:** Tables 2–4 compare one-to-five-object and two-/three-rigid-object tiers with adapted MDM/PriorMDM/HIMO. Generalization is reported per held-out composition/object; slot weighting, text/geometry and guidance ablations examine coordination. Held-out subsets therefore test specific recombinations, not new captured actors.

**Full-text source:** https://arxiv.org/pdf/2610.03252v1

**Reading status:** full_text_checked

**Inspected version:** 2610.03252v1

**Full-text SHA256:** 79d8df8770af044e5924d48c7572a4af8c318640f80527b912686a3859f337f4

**Source locator:** Sections 3–5; Data split/Protocol/Metrics; Tables 2–4; Appendix A split details and evaluator appendix.

**Scope / curator boundary:** Sustained concurrent interactions are the target, not dependent multistage activities. Synthetic hours are not independent human capture. Finger precision and contact physics remain limited, and repeated source clips across compositions prevent interpreting holdout as new-person generalization.

**Composition axes:** data, object-contact, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.03252); checked 2026-11-19.

<a id="duethoi"></a>
## DuetHOI: Language-Guided Bimanual Hand--Object Motion Generation with Articulation Planning and Contact Refinement

**duethoi · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2603.08390v3) · [Evidence](https://arxiv.org/pdf/2603.08390v3) · Citekey: `duethoi2026`

**Authors of cited version:** Zhi Wang; Yuyan Liu; Liu liu; Ruonan Liu; Ruixuan Liu.

**Contribution / composition:** Contact intent and articulation planning condition structured hand/object generation; proximity refinement fixes objects while correcting hands.

**Mechanism:** ContactVAE samples contact intent; conditional-prior ArtPlanner predicts scalar articulation, ManiVAE compresses hands, and DualFormer couples token/time streams. ProxiRefine corrects hands while fixing generated object motion.

**Input contract:** Language, known object geometry/initial state and sampled contact intent. ArtPlanner produces a scalar articulation reference, while DualFormer couples hand/object tokens; ProxiRefine keeps generated object motion fixed while correcting hand poses.

**Data and split:** ARCTIC tests single/bimanual and rigid/articulated modes; GRAB tests rigid modes. One model trains jointly over available modes, masking absent hands. Main text says baselines share splits but does not enumerate participant partitions/proportions; these are deferred to supplemental protocol rather than independently established here.

**Evaluation metrics:** Phy, contact F1, articulated hand MPJPEA, object translation/rotation error OTE/ORE, sample/object diversity SD/OD, contact rate/stability and relative-nearest-neighbor error NN-Rel. Metrics cover geometry, accuracy, diversity and persistence.

**Evaluation checked:** Tables 1–3 compare adapted Text2HOI, LatentHOI and MDM with the same raw task conditions. Ablations remove contact intent, articulation planning, hand compression, stream coordination and object-fixed refinement; per-mode results include unseen-category examples. Unseen-oven evidence is qualitative Figure 5, not an enumerated quantitative category-holdout split.

**Full-text source:** https://arxiv.org/pdf/2603.08390v3

**Reading status:** full_text_checked

**Inspected version:** 2603.08390v3

**Full-text SHA256:** ea88d09156fee5ceca08a2e8d1bedd00b0ef6204206a6707bda7d81c00b32d70

**Source locator:** Method sections ContactVAE/ArtPlanner/ManiVAE/DualFormer/ProxiRefine; Experiments and Tables 1–3; limitations section.

**Scope / curator boundary:** Hand-centric rather than whole-body. Supports one articulation scalar and one instruction, explicitly excluding coupled joints and inter-task transitions. Proximity/physical-plausibility scores are not executed dynamics. StructBiHOI and DuetHOI revisions share one arXiv identity, preventing duplicate-paper counting.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2603.08390); checked 2026-11-19.

<a id="trace"></a>
## Harnessing Coupled Stream Completion For Human-Object Interaction Modeling

**trace · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2609.32551) · [Evidence](https://arxiv.org/pdf/2609.32551v2) · Citekey: `trace2026`

**Authors of cited version:** Dawei Guan; Di Yang; Jiangtao Wang.

**Contribution / composition:** TRACE separates body, hand, and object motion through aligned temporal VAEs, then couples all latent streams with a joint flow network whose velocity predictions depend on the complete interaction state. Decoded estimates receive contact, object-frame anchoring, and timing supervision; a language branch also supports interaction understanding.

**Mechanism:** TRACE separates body, hand, and object motion through aligned temporal VAEs, then couples all latent streams with a joint flow network whose velocity predictions depend on the complete interaction state. Decoded estimates receive contact, object-frame anchoring, and timing supervision; a language branch also supports interaction understanding.

**Input contract:** Text, object geometry encoded by 1,024-point BPS, and optional observed streams for completion. The architecture predicts continuous body/hand/object states jointly; future object motion is not assumed supplied for ordinary text-to-HOI generation.

**Data and split:** Uses the official InterAct train/test partition, converting mixed SMPL-H/SMPL-X data consistently to SMPL-H. The inspected experimental section does not report exact partition proportions or assert cross-dataset ancestor-disjointness. Generation, completion, and understanding share preprocessing and evaluators.

**Evaluation metrics:** R-Precision/MM-Distance assess language alignment; FID/Diversity distribution and variation. Foot Skating Ratio, penetration ratio, contact ratio, and contact precision/recall/F1 probe geometric interaction. Understanding adds BLEU-1/4, ROUGE, CIDEr, and BERTScore for generated descriptions.

**Evaluation checked:** Section 4 compares retrained HOI-Diff and other HOI baselines, completion variants, and language-generation baselines under the common protocol. Twenty repeated evaluations report means and 95% confidence intervals; coupled-flow and geometric-supervision ablations test the proposed mechanisms.

**Full-text source:** https://arxiv.org/pdf/2609.32551v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2609.32551v2 [cs.CV] 29 Sep 2026

**Full-text SHA256:** c352abc8eb595c806e383556b56cb9b0556417b08dbd9a978b65632beb85f112

**Source locator:** §3 (split VAE, coupled flow, geometric objectives), §4 setup/metrics and Tables 1–2; completion and coupling ablations in experimental subsections.

**Scope / curator boundary:** Interaction metrics depend on thresholded proxy contacts and fitted body geometry. Coupled latent responses and improved feature scores do not prove force consistency, continuous collision freedom, or generalization to unseen data sources. All numerical findings here are inspected paper claims rather than reproduced results.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2609.32551); checked 2026-11-19.

<a id="pami"></a>
## PAMI: Part Anchored Motion for Text to Human-Object Interaction Generation

**pami · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2609.38466) · [Evidence](https://arxiv.org/pdf/2609.38466v1) · Citekey: `pami2026`

**Authors of cited version:** Chuqiao Li; Xianghui Xie; Yong Cao; Andreas Geiger; Gerard Pons-Moll.

**Contribution / composition:** Body-part-relative object votes structure a latent interaction model; coarse generation is followed by contact-oriented surface refinement.

**Mechanism:** Represents object trajectories as learned votes from human body-part anchors plus a free-motion component. A part-factorized VAE preserves human/object coupling; a text- and mesh-conditioned rectified-flow generator samples the latent. A recursive refiner reads long-range body-to-surface and short-range hand surface probes to correct interaction geometry.

**Input contract:** Text description and canonical object mesh encoded with basis-point features. Human/body-part state and relative object trajectories are outputs/latent structure, not prescribed future generation trajectories.

**Data and split:** Evaluates the standard InterAct benchmark and uses its training partition for normalization. Exact split counts, proportions and actor/object grouping are not reported in the inspected experimental setup; inherited benchmark membership should not be interpreted as a newly verified compositional split.

**Evaluation metrics:** R-Precision, MM-Dist, FID, diversity, foot-skating ratio, penetration depth, contact ratio and contact precision/recall/F1 for hands and full body. Tables report generation variability/confidence intervals.

**Evaluation checked:** Table 1 compares HOI generators. Tables 2–3 ablate part-factorization, anchoring/voting and refiner geometry; supplementary experiments evaluate recursion depth. The refiner is also applied without retraining to LIGHT and InterAct-generated outputs.

**Full-text source:** https://arxiv.org/pdf/2609.38466v1

**Reading status:** full_text_checked

**Inspected version:** 2609.38466v1

**Full-text SHA256:** 06d3a9ab84d721d18373f7d86d581a1af3b6d343bf80b9750189b96365768cdb

**Source locator:** Sections 3.1–3.3, 4.1–4.3; Tables 1–3; Appendices A–C, including generator/refiner ablations.

**Scope / curator boundary:** Single human and single rigid object with known canonical geometry. The bounded refiner cannot repair a wrong action, severe temporal misalignment or large trajectory error; novel-shape generalization remains future work. Contact refinement is not a force-based grasp or continuous collision certificate.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2609.38466); checked 2026-11-19.

<a id="sk-hoi"></a>
## Surface Keypoint Representation for Multi-Object and Articulated Human-Object Interaction Generation

**sk-hoi · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2608.03158) · [Evidence](https://arxiv.org/pdf/2608.03158v1) · Citekey: `skhoi2026`

**Authors of cited version:** Xiaogang Peng; Zeyu Han; Zichong Meng; Yiming Xie; Jihua Zhu; Gang Hua; Huaizu Jiang.

**Contribution / composition:** Represents rigid components with surface-keypoint trajectories, predicts spatiotemporal contact-distance fields and synthesizes contact-guided whole-body motion.

**Mechanism:** Three transformer/flow-matching stages generate rigid-component keypoints, contact-distance fields and body markers; inference optimizes body diffusion noise against contact and object-SDF penetration losses.

**Input contract:** Text and geometry/initial state for rigid components of multiple or articulated objects. Three flow-based stages predict surface keypoints, contact-distance fields and body markers; inference noise optimization enforces surface contact and object-SDF constraints.

**Data and split:** Evaluates ParaHome, HIMO, ARCTIC and OMOMO task settings. ParaHome composition holdout contains 118 two-object and 35 three-object sequences whose object combinations are unseen while each individual object occurs in training. Main benchmark overall partition proportions are not restated.

**Evaluation metrics:** FID, R-Precision, diversity, foot sliding, object jerk, temporal/body contact accuracy and SDF penetration. Object-trajectory studies report translation/orientation errors; GT-conditioned OMOMO also reports MPJPE/root error. Codec reconstruction has marker/keypoint error and contact precision/recall.

**Evaluation checked:** Tables compare coordinate representations and contact encodings, staged generation and optimization. Extra composition-holdout tests explicitly distinguish individual-object familiarity from unseen combinations; slot permutations test component-order robustness.

**Full-text source:** https://arxiv.org/pdf/2608.03158v1

**Reading status:** full_text_checked

**Inspected version:** 2608.03158v1

**Full-text SHA256:** 83a8a0cc97f1bb83d7150b9d1184e9dfd593956e08c54b05277eba5e014bd827

**Source locator:** Sections 3.1–3.4, 4.1–4.3; Tables 1–5; Appendix E and Tables 8–10 (held-out compositions/slot order).

**Scope / curator boundary:** Remaining floating/penetration and imperfect three-object geometric results remain visible. Inference optimization costs roughly four minutes per 124 frames. Rigid-component point trajectories avoid explicit joint typing but do not guarantee articulation mechanics, grasp forces or dynamic feasibility.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2608.03158); checked 2026-11-19.

<a id="dechoi"></a>
## Decoupled Generative Modeling for Human-Object Interaction Synthesis

**dechoi · 2025 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2512.19049) · [Evidence](https://arxiv.org/pdf/2512.19049v1) · Citekey: `dechoi2026`

**Authors of cited version:** Hwanhee Jung; Seunggwan Lee; Jeongyoon Yoon; SeungHyeon Kim; Giljoo Nam; Qixing Huang; Sangpil Kim.

**Contribution / composition:** DecHOI separates goal-conditioned trajectory planning from contact-oriented action generation.

**Mechanism:** Trajectory diffusion generates human/object paths; action diffusion then conditions densely on these predicted positions. Distal-joint adversarial training and reconstruction guidance target contact and grounded feet.

**Input contract:** Text, human/object initial states, object geometry and desired object goal. Trajectory diffusion predicts intermediate human/object paths; action diffusion conditions on those predictions. Dense future paths are internal outputs, unlike externally supplied waypoint baselines.

**Data and split:** FullBodyManipulation supplies approximately ten hours of interaction, with the existing OMOMO partition; 3D-FUTURE supplies unseen furniture shapes. Exact subject counts/proportions are not restated in the inspected setup. Comparisons remove intermediate waypoints from sparse-control baselines to match the harder input setting.

**Evaluation metrics:** Start/end object error Ts/Te, foot height/sliding, Top-3 R-Precision, FID, diversity, contact precision/recall/F1/rate, hand/body penetration, MPJPE, root/object translation and object rotation difference.

**Evaluation checked:** Tables 1–2 compare CHOIS, HOIFHLI and OMOMO variants. Ablations examine decoupled planning, distal-joint adversarial training and reconstruction guidance; DynaPlan illustrates moving-obstacle adaptation. Appendix B discusses foot-hovering versus sliding and contact-penetration tradeoffs.

**Full-text source:** https://arxiv.org/pdf/2512.19049v1

**Reading status:** full_text_checked

**Inspected version:** 2512.19049v1

**Full-text SHA256:** 4509be969487f003683dc3986caeb51e414a2d544b94fc48cc0987fbb889871e

**Source locator:** Sections 3.1–3.3, 4.1–4.5; Tables 1–2; Appendices B–D (metric tradeoffs, guidance, DynaPlan).

**Scope / curator boundary:** Rigid objects only; DynaPlan uses one manipulated object and one moving obstacle. Guidance has no simulation-based feasibility guarantee. Baselines with true object trajectories consume stronger information and should not be conflated with initial/goal-conditioned generation.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2512.19049); checked 2026-11-19.

<a id="hoifhli"></a>
## Human-Object Interaction from Human-Level Instructions

**hoifhli · 2025 · Human-object & articulated interaction · method**

[Primary source](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_Human-Object_Interaction_from_Human-Level_Instructions_ICCV_2025_paper.pdf) · [Evidence](https://arxiv.org/pdf/2406.17840v3) · Citekey: `hoifhli2025`

**Authors of cited version:** Wu, Zhen; Li, Jiaman; Xu, Pei; Liu, C. Karen.

**Contribution / composition:** Language planning orchestrates contextual full-body manipulation with finger interactions and RL reference tracking.

**Mechanism:** LLM scene planning and A* navigation feed CoarseNet; predicted contact phases drive grasp generation, wrist-relative RefineNet and FingerNet. RL separately tracks the generated reference.

**Input contract:** Human-level instruction and explicit scene/object geometry/state. LLM scene planning and A* navigation provide target poses/waypoints; contact-phase and grasp synthesis drive coarse/refined body and finger networks. A separate RL policy tracks the generated reference.

**Data and split:** Uses FullBodyManipulation for body/object generation, GRAB for finger interactions and HumanML3D for navigation, following standard source partitions. Exact ratios are not enumerated in the main protocol. High-level planner evaluation uses twenty-five designed instructions rather than a learned held-out task split.

**Evaluation metrics:** Planner object-position/orientation error rates; waypoint error Txy, foot height/sliding, contact precision/recall/F1, contact coverage, intersection volume, MPJPE and object translation/rotation errors; perceptual preference complements these.

**Evaluation checked:** Section 7 separates scene planning, coarse/refined/finger generation and physics tracking. Tables compare CoarseNet variants and grasp alternatives, including provided contact phases; supplementary navigation testing uses HumanML3D test data. Tracking is an additional trained execution stage.

**Full-text source:** https://arxiv.org/pdf/2406.17840v3

**Reading status:** full_text_checked

**Inspected version:** 2406.17840v3

**Full-text SHA256:** abc21ebd6b0aa5a402522c8e8a92c823a55a2181da62339c2e9ea8ffc8212c49

**Source locator:** Sections 3–6; Sections 7.1–7.4 and Tables 2–3; supplementary implementation/navigation and tracker evaluations.

**Scope / curator boundary:** Planner-produced future targets are material conditions. Reference-tracking success is not a reference-free policy, and environmental perception remains future work. Multi-stage runtime includes expensive grasp optimization/tracker training; geometry-conditioned generation does not by itself establish broad task autonomy.

**Composition axes:** object-contact, scene-state, temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_Human-Object_Interaction_from_Human-Level_Instructions_ICCV_2025_paper.html); checked 2026-11-19.

<a id="interact"></a>
## InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation

**interact · 2025 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2509.09555) · [Evidence](https://arxiv.org/pdf/2509.09555v1) · Citekey: `interact2025`

**Authors of cited version:** Sirui Xu; Dongting Li; Yucheng Zhang; Xiyan Xu; Qi Long; Ziyin Wang; Yunzhi Lu; Shuchang Dong; Hezi Jiang; Akshat Gupta; Yu-Xiong Wang; Liang-Yan Gui.

**Contribution / composition:** Consolidates HOI sources, refines artifacts and hands, augments under contact invariance, and benchmarks six generation/completion tasks.

**Mechanism:** Consolidates seven whole-body HOI sources with common surface markers, object BPS geometry and checked human/GPT-4 text annotations. Optimization corrects body/contact artifacts, then hands; augmentation shifts object trajectories and realigns humans while preserving near-contact distances. A transformer diffusion baseline jointly predicts motion and marker-to-object contact vectors, with interaction-aware text features and optional contact guidance. Six tasks distinguish language generation, inpainting, prediction and simulated imitation.

**Input contract:** Task-dependent text/action labels, object shape and trajectories, human motion, past HOI or complete reference interactions. Object-conditioned human generation uses future object motion as an input and is not unconstrained object-trajectory generation.

**Data and split:** Supplement C: text/action generation partitions each source 9:1 train/test; object-to-human separates 168 training and 29 unseen test objects; human-to-object uses 10:1. Prediction trains on 90 percent and tests on the held-out BEHAVE 10 percent.

**Evaluation metrics:** FID, R-precision, MM-Dist, diversity/multimodality; penetration depth/contact ratio; marker error, foot sliding, contact precision/recall/accuracy/F1; object translation/quaternion error; imitation success.

**Evaluation checked:** Tables 2–8 separate correction, generation and conditional prediction. Corrected versus raw PhysHOI imitation is demonstrated on four selected sequences over 2,048 environments; this is a narrower experiment than full-corpus executability.

**Full-text source:** https://arxiv.org/pdf/2509.09555v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2509.09555v1

**Full-text SHA256:** 9cf4c8115c13e2fe38f891d378a59b9edc5a3e9f8b2dcb87ac9cfe3065b86a04

**Source locator:** Sections 3.1–3.3, 4 and 5.1–5.5; Tables 2–8; Supplement C.2–C.7 and E.

**Scope / curator boundary:** Synthetic augmentation is not new motion capture. Hands are corrected under assumptions suitable for grasp conformity rather than high dexterity. Contact/penetration improvements and text-feature scores do not establish force consistency, independent ancestor-disjoint composition or arbitrary object generalization.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.09555); checked 2026-11-19.

<a id="interactmove"></a>
## InteractMove: Text-Controlled Human-Object Interaction Generation in 3D Scenes with Movable Objects

**interactmove · 2025 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2509.23612) · [Evidence](https://arxiv.org/pdf/2509.23612v1) · Citekey: `interactmove2025`

**Authors of cited version:** Xinhao Cai; Minghang Zheng; Xin Jin; Yang Liu.

**Contribution / composition:** InterActMove introduces text-conditioned joint human/object generation in scenes with movable objects. AGCA first grounds the referenced object, predicts hand-object affordances, and denoises interaction with local scene features. Contact/penetration losses and test-time penetration guidance encourage target interaction and scene compatibility.

**Mechanism:** InterActMove introduces text-conditioned joint human/object generation in scenes with movable objects. AGCA first grounds the referenced object, predicts hand-object affordances, and denoises interaction with local scene features. Contact/penetration losses and test-time penetration guidance encourage target interaction and scene compatibility.

**Input contract:** Free-form text and a 3D scene containing separate object point clouds; a pretrained grounding module selects the target instance. Object geometry, affordance features, and surrounding local geometry condition generated body motion and object trajectories.

**Data and split:** The constructed dataset contains 618 sequences, 71 objects, 21 scenes, and approximately 2.2 million frames. Evaluation also uses the movable-object subset of TRUMANS. Exact train/test proportions and subject/recording split units are not reported in the inspected main experiment description.

**Evaluation metrics:** Goal Distance averages minimum human-object surface distance; Multimodality measures L2 variation for a fixed prompt/scene. Physical Realism is a pretrained frame classifier score, not a dynamics calculation. Non-collision Score measures the proportion of frames without detected penetration.

**Evaluation checked:** Tables 2–3 compare interaction generation on the new dataset and TRUMANS subset; ablations remove grounding, affordance, local scene modeling, and collision-aware components. Scene/object augmentation adjusts object placement and interaction trajectories before diffusion-based refinement.

**Full-text source:** https://arxiv.org/pdf/2509.23612v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2509.23612v1 [cs.CV] 28 Sep 2025

**Full-text SHA256:** ee36cc373249145f984a3fbf2f1c8bc5832f253ee0e53152c58214f091b522d2

**Source locator:** §3 and Table 1 (dataset/augmentation), §§4.1–4.5 (AGCA), §5.1 metric definitions, Tables 2–4 (comparisons and ablations).

**Scope / curator boundary:** Grounding mistakes propagate through the pipeline. Learned realism and sampled geometric collision scores are incomplete physical proxies. Exact partition details remain a reporting gap, and scene augmentation must not be counted as independent captured interaction. No force-based certification is established.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.23612); checked 2026-11-19.

<a id="primhoi"></a>
## PrimHOI: Compositional Human-Object Interaction via Reusable Primitives

**primhoi · 2025 · Human-object & articulated interaction · method**

[Primary source](https://openaccess.thecvf.com/content/ICCV2025/html/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.html) · [Evidence](https://openaccess.thecvf.com/content/ICCV2025/papers/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.pdf) · Citekey: `primhoi2025`

**Authors of cited version:** Jia, Kai; Liu, Tengyu; Pei, Mingtao; Zhu, Yixin; Huang, Siyuan.

**Contribution / composition:** Composes relative-geometry interaction primitives spatially and temporally through hierarchical planning, targeting unseen multi-object tasks.

**Mechanism:** Factors interactions into relative-geometry primitives such as grasp, clamp and support. Symbolic state transitions compose these primitives, geometric optimization builds key poses, and a retrained contact-guided diffusion controller fills temporal intervals while preserving active constraints.

**Input contract:** Task instruction, known objects and relative contact geometry. LLM/PDDL-HOI planning produces subgoal graphs, then primitive contact factors specify key poses and object paths; LocalControl generates intermediate human motion with contact constraints and post-optimization.

**Data and split:** Primitive sources mix OMOMO, BEHAVE and analytic support functions; LocalControl retrains on a No-Walk HumanML3D variant. No conventional held-out-task percentage is reported. Planner tests three designed tasks, with five/five/ten trials, distinct from low-level contact-guidance experiments.

**Evaluation metrics:** Planner success rate, action-count efficiency and solution diversity. Motion tests report maximum joint acceleration and constraint errors, plus human-rated success/naturality on 1–10 scales. FID/R-Precision/diversity apply only to matched training-data variants.

**Evaluation checked:** Tables 1–3 compare direct GPT planning, primitive hints and PDDL-HOI, then IK/ProgMoGen and LocalControl with/without intermediate trajectories and multiple runs. Authors explicitly avoid relying on distribution FID for out-of-distribution multi-object cases.

**Full-text source:** https://openaccess.thecvf.com/content/ICCV2025/papers/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Proceedings/author PDF as retrieved 2026-11-19; no printed own-paper arXiv version found.

**Full-text SHA256:** 4becca53b7ade207b983ec52163fcf7363761a9c3d2289d1dcb646bdecf74da1

**Source locator:** Sections 3.1–3.4, 4.1–4.4; Tables 1–3; Appendix B evaluation details.

**Scope / curator boundary:** Hand-designed primitive vocabulary and small designed task battery bound zero-shot claims. Requires known geometry and reliable symbolic preconditions; primitive planning differs from a unified learned sequence generator. Public repository presence does not establish a released runnable implementation.

**Composition axes:** object-contact, scene-state, temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/ICCV2025/html/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.html); checked 2026-11-19.

<a id="himo"></a>
## HIMO: A New Benchmark for Full-Body Human Interacting with Multiple Objects

**himo · 2024 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2407.12371) · [Evidence](https://arxiv.org/pdf/2407.12371v1) · Citekey: `himo2024`

**Authors of cited version:** Xintao Lv; Liang Xu; Yichao Yan; Xin Jin; Congsheng Xu; Shuwen Wu; Yifan Liu; Lincheng Li; Mengxiao Bi; Wenjun Zeng; Xiaokang Yang.

**Contribution / composition:** Multi-object full-body mocap with text and temporal segments; diffusion branches and autoregressive segments support timeline control.

**Mechanism:** Dual human/object diffusion branches exchange information through mutual interaction; segmented generation conditions later intervals on preceding motion.

**Input contract:** Text descriptions and two/three object geometries/initial states; the segmented variant additionally consumes explicit interval descriptions and previous generated segment context. Human/object diffusion branches exchange mutual-interaction information.

**Data and split:** HIMO uses train/test/validation proportions 0.8/0.15/0.05. Two-object and three-object partitions are evaluated separately. The paper does not establish source-ancestor or actor-disjoint grouping from these proportions; segmented generation should not be interpreted as a separate independent capture split.

**Evaluation metrics:** Contrastively trained joint human-object/text feature R-Precision, MM-Distance, FID, diversity and multimodality. Feature scores measure synchronized human/object distribution and language agreement; additional geometry/motion analyses supplement them.

**Evaluation checked:** Baseline comparisons distinguish full-sequence HIMO-Gen from autoregressive HIMO-SegGen, with maximum lengths of 300 and 100 frames. Tables assess two-/three-object generation, unseen geometry and timeline composition, plus ablations of cross-branch mutual interaction and segment conditioning. Captured clips, temporal segments and augmented examples retain different counting units.

**Full-text source:** https://arxiv.org/pdf/2407.12371v1

**Reading status:** full_text_checked

**Inspected version:** 2407.12371v1

**Full-text SHA256:** ad94c75d2b5fad5d8128b6d4b9884bcc3ac4631854590192f4a41d6a59cd372a

**Source locator:** Sections 3–4; Section 5 Dataset Details/Evaluation Metrics; Tables 2–4 and supplementary baseline details.

**Scope / curator boundary:** Captured interactions cover a bounded set of two/three-object settings. Explicit schedules provide temporal structure; distributional language/HOI scores do not independently certify grasp support, collision-free transitions, causal object-state prerequisites or unseen-person generalization.

**Composition axes:** object-contact, spatial, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2407.12371); checked 2026-11-19.

<a id="cg-hoi"></a>
## CG-HOI: Contact-Guided 3D Human-Object Interaction Generation

**cg-hoi · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2311.16097) · [Evidence](https://arxiv.org/pdf/2311.16097v2) · Citekey: `cghoi2024`

**Authors of cited version:** Christian Diller; Angela Dai.

**Contribution / composition:** Joint diffusion with cross-attention models human motion, object motion and surface contact; predicted contact guides inference.

**Mechanism:** Jointly denoises human and object motion while explicitly modeling contact. A contact prediction branch relates body points to the object surface; contact-guided updates at inference encourage coherent human-object trajectories. Geometry conditioning allows generated motion to depend on the target shape instead of treating the object as an unconstrained translation track.

**Input contract:** Text description and object geometry; a forecasting comparison also conditions on observed motion. Text-conditioned and motion-conditioned results are distinguished because their information differs.

**Data and split:** CHAIRS provides approximately 1,300 moving human/object sequences and uses an 80/10/10 split along object classes, keeping test objects unseen. BEHAVE uses its original training/test split, approximately 520 sequences from eight participants and twenty objects.

**Evaluation metrics:** Joint human-object feature R-Precision, FID, diversity and multimodality; contact/geometric quality measures and a 32-participant perceptual study for text correspondence and realism.

**Evaluation checked:** Section 6 compares adapted InterDiff and human-motion diffusion baselines with aligned conditioning. Models are evaluated at 20 fps, generating 32 CHAIRS or 64 BEHAVE frames. Validation FID selects checkpoints; ablations test contact modeling and inference guidance.

**Full-text source:** https://arxiv.org/pdf/2311.16097v2

**Reading status:** full_text_checked

**Inspected version:** 2311.16097v2

**Full-text SHA256:** 3d5c2c6c9b65f4e5ac0333a83b1fc11d39eb0e081d9127f53d70c4220d6db53d

**Source locator:** Sections 4–5 (joint diffusion/contact guidance); Sections 6.1–6.4, Table 1 and contact ablations. Section 6.6 (Limitations).

**Scope / curator boundary:** Restricted to a single object and expensive captured 3D HOI supervision; multi-object long tasks remain unmodeled. Short-clip unseen-object evaluation does not establish long task-chain generalization, and contact proximity guidance does not certify stable grasp dynamics.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2311.16097); checked 2026-11-19.

<a id="chois"></a>
## Controllable Human-Object Interaction Synthesis

**chois · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2312.03913) · [Evidence](https://arxiv.org/pdf/2312.03913v2) · Citekey: `chois2024`

**Authors of cited version:** Jiaman Li; Alexander Clegg; Roozbeh Mottaghi; Jiajun Wu; Xavier Puig; C. Karen Liu.

**Contribution / composition:** Joint human/object/contact diffusion combines geometry supervision with contact guidance and connects to planning for extended manipulation.

**Mechanism:** Transformer denoises synchronized human poses, object poses and hand-contact labels; object geometry loss improves waypoint adherence and sampling guidance constrains contacts.

**Input contract:** Object mesh, initial human/object pose, text and sparse future object waypoints. Joint diffusion predicts body/object/contact labels; geometry loss and sampling guidance align motion with waypoints and encourage hand contact.

**Data and split:** FullBodyManipulation/OMOMO uses fifteen training subjects and two test subjects; vacuum/mop articulated cases are excluded. Seventeen unseen 3D-FUTURE objects test geometry transfer, with waypoints extracted every thirty frames from same-category held-out human-object recordings.

**Evaluation metrics:** Start/end/waypoint errors Ts/Te/Txy, foot sliding/height, FID/R-Precision, contact precision/recall/F1 and penetration; GT body/object errors and perceptual preference provide complementary measures.

**Evaluation checked:** Tables 1–2 compare generation on captured and unseen geometry with object-motion-conditioned and waypoint-driven baselines. Guidance and geometry-loss ablations isolate controllability and contact. Extended scene demonstrations obtain object routes through planning rather than learning task-level navigation from initial state alone. Baseline conditions must distinguish sparse waypoints from full future object trajectories.

**Full-text source:** https://arxiv.org/pdf/2312.03913v2

**Reading status:** full_text_checked

**Inspected version:** 2312.03913v2

**Full-text SHA256:** f2db1581b361fa982a3be8ccc9a1aaa9b158003a649347f48ccb286ea5cffabc

**Source locator:** Sections 3.1–3.4, 4.1–4.5; Tables 1–2; unseen-object conditions in Section 4.1.

**Scope / curator boundary:** Future waypoints are required conditioning, not generated task trajectories. Rigid-object scope and kinematic contact guidance limit claims of articulated manipulation or force-valid grasping. Retaining source category trajectories for unseen meshes tests shape adaptation rather than unrestricted new-task discovery.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.03913); checked 2026-11-19.

<a id="interdiff"></a>
## InterDiff: Generating 3D Human-Object Interactions with Physics-Informed Diffusion

**interdiff · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2308.16905) · [Evidence](https://arxiv.org/pdf/2308.16905v1) · Citekey: `interdiff2023`

**Authors of cited version:** Sirui Xu; Zhengyuan Li; Yu-Xiong Wang; Liang-Yan Gui.

**Contribution / composition:** Interaction diffusion forecasts human/object motion and a physics-informed correction predictor refines denoised interactions.

**Mechanism:** Predicts future human-object interaction using a transformer diffusion model conditioned on past interaction and object geometry. A correction scheduler identifies likely penetration or loss of contact and chooses a reference frame attached to a human surface marker or the ground. A separate spatial-temporal graph predictor models simpler object dynamics in those coordinates; its prediction is transformed back and blended into denoising. Components train separately.

**Input contract:** Past human/object motion plus object shape. Typical BEHAVE setup gives ten historical frames and predicts 25 future frames, with autoregressive continuation for longer horizons; no text condition is required.

**Data and split:** Uses official BEHAVE train/test partition. On skeleton-based HOI, 18,352 twenty-frame sequences include 582 evaluation sequences with unseen objects; predicts ten future from ten past frames. Cross-dataset experiment trains on BEHAVE and evaluates GRAB without fine-tuning.

**Evaluation metrics:** MPJPE-H and MPJPE-O measure global human joints/object keypoints in millimeters; translation error is L2, rotation error uses quaternion difference, and penetration measures object vertices inside the human. Best-of-many evaluation explicitly selects lowest candidate errors.

**Evaluation checked:** Tables compare InterRNN, InterVAE and skeletal prediction baselines. A 100-frame rollout tests long-term prediction; user comparisons assess physical fidelity, while correction/reference ablations probe the inductive bias.

**Full-text source:** https://arxiv.org/pdf/2308.16905v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2308.16905v1

**Full-text SHA256:** 0b50fc92ec4d4ffa01fcd2165d29c9e58bb7f48fc9c2b9212b251a84f846ddbf

**Source locator:** Sections 3.1–3.2 and 4.1–4.4; Tables 1–4; Figures 3 and 7.

**Scope / curator boundary:** Intuitive physics is a learned correction, not a dynamics solver. Skeleton-only contacts are ill-defined and omit penetration/contact losses. Best-of-many oracle scores should not be read as single-output accuracy; short forecasting and GRAB visualization do not prove text-conditioned task composition.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2308.16905); checked 2026-11-19.

<a id="omomo"></a>
## Object Motion Guided Human Motion Synthesis

**omomo · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2309.16237) · [Evidence](https://arxiv.org/pdf/2309.16237v1) · Citekey: `omomo2023`

**Authors of cited version:** Jiaman Li; Jiajun Wu; C. Karen Liu.

**Contribution / composition:** OMOMO uses two diffusion stages: object geometry and motion first predict hand positions, then hand positions guide full-body motion synthesis. Geometry-aware hand correction enforces object-relative contact before body generation; captured SMPL-X body/object trajectories provide supervision.

**Mechanism:** OMOMO uses two diffusion stages: object geometry and motion first predict hand positions, then hand positions guide full-body motion synthesis. Geometry-aware hand correction enforces object-relative contact before body generation; captured SMPL-X body/object trajectories provide supervision.

**Input contract:** A known object mesh and its full motion trajectory condition human motion. Future object poses are inputs in this reconstruction/animation setting, so results must not be described as jointly generating object trajectories from only initial object state.

**Data and split:** The dataset has 17 subjects and 15 objects. Fifteen subjects train and two test; one evaluation shares all 15 objects, while another uses 10 training and five unseen test objects. Subject and object generalization therefore have explicitly different settings.

**Evaluation metrics:** Hand JPE, MPJPE, and MPVPE compare hand/body joints and mesh vertices; root translation/orientation errors measure global alignment. Collision percentage, foot sliding, and contact precision/recall/F1 probe geometric plausibility. Best-of-multiple sampling and subjective comparisons require distinct interpretation.

**Evaluation checked:** Tables 2–3 compare GOAL, single-stage diffusion, constraint-free OMOMO, and the full system under both object partitions. User preferences and a smartphone-mounted object-tracking application supplement reference errors. The paper acknowledges remaining penetration despite visually improved hand contact.

**Full-text source:** https://arxiv.org/pdf/2309.16237v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2309.16237v1 [cs.CV] 28 Sep 2023

**Full-text SHA256:** d51b7b9e2921de84e5ca1f78ea787770bc6f341c2a3d7d55998609e9337c102d

**Source locator:** §3 (two-stage generation and hand correction), §4/Table 1 (capture), §5.1 (15/2 subjects, 10/5 objects and metrics), Tables 2–3, §6 application.

**Scope / curator boundary:** Conditioning on the complete object trajectory makes this adjacent to initial-state-conditioned HOI generation. Hand constraints are heuristic and no full-body optimization eliminates all artifacts. Held-out objects are only five specified instances; this does not establish arbitrary scene or manipulation transfer.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2309.16237); checked 2026-11-19.

<a id="procigen"></a>
## Template Free Reconstruction of Human-object Interaction with Procedural Interaction Generation

**procigen · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2312.07063) · [Evidence](https://arxiv.org/pdf/2312.07063v3) · Citekey: `procigen2024`

**Authors of cited version:** Xianghui Xie; Bharat Lal Bhatnagar; Jan Eric Lenssen; Gerard Pons-Moll.

**Contribution / composition:** Procedurally creates varied human-object interaction pairs and trains an image-conditioned reconstruction model for unseen objects.

**Mechanism:** Category-specific autoencoder correspondences transfer contacts to replacement objects; joint pose optimization preserves contact and reduces collisions, followed by textured rendering. HDM reconstructs joint then separate human/object point clouds.

**Input contract:** Procedural generator consumes captured interaction seeds and replacement object shapes with category correspondences. HDM reconstruction consumes an RGB image, then predicts joint and separated human/object point clouds without a known test object template.

**Data and split:** Procigen synthesizes static pairs/images from source interactions rather than temporal clips. Reconstruction is evaluated on captured BEHAVE/InterCap and novel object categories. Exact image train/test percentages are not restated in the main setup; source/category generalization must be distinguished from independent motion splitting.

**Evaluation metrics:** Chamfer-distance-based F-score at one-centimeter threshold, separately for human, object and combined point clouds. Dataset-scale and limited-data ablations evaluate reconstruction coverage; shape fidelity is also visualized with reconstructed surfaces.

**Evaluation checked:** Section 4 compares HDM with interaction reconstruction baselines, procedural training-data variants and joint/separate denoising designs. Real-image tests include unseen categories; supplementary analyses examine data scaling, diffusion refinement and detailed shape fidelity.

**Full-text source:** https://arxiv.org/pdf/2312.07063v3

**Reading status:** full_text_checked

**Inspected version:** 2312.07063v3

**Full-text SHA256:** 790da66b13b69f675867ec9ee1c65900652b1bd8ce5c05464e3d1e8dd991b90a

**Source locator:** Sections 3.1–3.3, 4.1–4.4; reconstruction result tables; supplementary Sections B–C (ablation/limitations).

**Scope / curator boundary:** Static interaction pairs cannot be reported as motion sequences or hours. Seed contact patterns limit synthesized diversity; heavy occlusion and body-shape ambiguity remain. HDM does not handle multiple humans/objects, and contact-preserving optimization is not a dynamic interaction certificate.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.07063); checked 2026-11-19.

<a id="imos"></a>
## IMos: Intent-Driven Full-Body Motion Synthesis for Human-Object Interactions

**imos · 2022 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2212.07555) · [Evidence](https://arxiv.org/pdf/2212.07555v3) · Citekey: `imos2023`

**Authors of cited version:** Anindita Ghosh; Rishabh Dabral; Vladislav Golyanik; Christian Theobalt; Philipp Slusallek.

**Contribution / composition:** Intent-object text encoding and separate variational autoregressors coordinate arms and body for full-body object interaction.

**Mechanism:** Decomposes intent-driven full-body synthesis into grasp, arm and remaining-body generation, with autoregressive variational modules and attention for body coordination. A subsequent object optimizer estimates its six-degree-of-freedom trajectory from generated human motion. The body shape is an explicit condition, allowing motions for held-out subjects.

**Input contract:** Initial full-body pose, an object placed within reach, its geometry/body shape and an action intent encoded through language features. It is not an approach-navigation planner.

**Data and split:** Uses GRAB with S1 for validation, S10 for testing and S2–S9 for training. Lifting examples are excluded as inconsistent, leaving 789/157/115 train/validation/test sequences. Held-out testing includes novel intent-object combinations and body shapes.

**Evaluation metrics:** MPJPE, Average Variance Error, action-feature FID, recognition accuracy, diversity and multimodality. A perceptual study judges realism and correspondence with the intended action label.

**Evaluation checked:** ACTOR, Action2Motion and TEMOS are retrained on GRAB, with the common object optimizer applied for visualization. Table 2 and three ablations test intent embeddings, body attention and arm/body separation; twenty repeats provide 95% intervals.

**Full-text source:** https://arxiv.org/pdf/2212.07555v3

**Reading status:** full_text_checked

**Inspected version:** 2212.07555v3

**Full-text SHA256:** 00e0f1a4a8c3f5d24c4921dfc558397a9571f75b5eb02d7a4a7523f8e926555e

**Source locator:** Sections 3–4; Sections 5.1–5.6; Table 2, Figure 6; dataset split in Section 5.1.

**Scope / curator boundary:** Motion is represented by fifteen keyframes at roughly 8–10 fps before interpolation. The setting assumes a reachable object and lacks scene navigation; object optimization does not certify stable contacts, physical forces or successful long locomotion-manipulation sequences.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.07555); checked 2026-11-19.

<a id="goal"></a>
## GOAL: Generating 4D Whole-Body Motion for Hand-Object Grasping

**goal · 2021 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2112.11454) · [Evidence](https://arxiv.org/pdf/2112.11454v2) · Citekey: `goal2023`

**Authors of cited version:** Omid Taheri; Vasileios Choutas; Michael J. Black; Dimitrios Tzionas.

**Contribution / composition:** GNet predicts a whole-body goal grasp and MNet produces approach motion with coordinated hands, head and body.

**Mechanism:** Generates a whole-body grasping goal with GNet, a conditional generative model conditioned on object geometry/pose, then uses autoregressive MNet to produce approach motion from the starting body state. Interaction-aware vertex offsets connect body and object geometry; optimization refines both goal grasp and generated motion using predicted Euclidean-space interaction features. MNet generates ten future frames per iteration and rolls forward to the grasp.

**Input contract:** An object mesh, its position/orientation, and a starting human pose/shape roughly 0.5–1.5 meters away. No free-text command or future object trajectory is required.

**Data and split:** Trains on GRAB right-hand stable grasps and approach subsequences. Supplement reports approximately 160K/26K/12.5K static frames and 40K/7K/3K motion windows for train/test/validation. Windows contain ten past, one current and ten future frames; exact source-group holdout membership is not restated.

**Evaluation metrics:** Static goals and generated motions receive five-point perceptual ratings for body realism, foot-ground contact, grasp and head orientation. MNet horizon ablations report body/hand/foot vertex distances and pose/translation reconstruction errors. Foot sliding counts frames whose selected ground-near vertex moves over one centimeter.

**Evaluation checked:** Compares GNet before/after optimization and ground-truth grasps, and studies MNet output horizon. Generated motion has 13.7 percent sliding frames versus 6.7 percent for ground truth under its stated metric.

**Full-text source:** https://arxiv.org/pdf/2112.11454v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2112.11454v2

**Full-text SHA256:** 33c5036e9d960596d7222067d92afde3c0b0d3cc6f0e9353e48991d84b108385

**Source locator:** Sections 3.1–3.5, 4.1–4.3 and 5; Tables 1–3; Supplement 6 Data Preparation.

**Scope / curator boundary:** Approach distance is bounded and longer navigation remains future work. The method lacks full surrounding-scene awareness and focuses on grasp acquisition, not subsequent object manipulation or release. Overlapping window counts must not be mistaken for independent captured sequences.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2112.11454); checked 2026-11-19.

<a id="saga"></a>
## SAGA: Stochastic Whole-Body Grasping with Contact

**saga · 2021 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2112.10103) · [Evidence](https://arxiv.org/pdf/2112.10103v3) · Citekey: `saga2022`

**Authors of cited version:** Yan Wu; Jiahao Wang; Yan Zhang; Siwei Zhang; Otmar Hilliges; Fisher Yu; Siyu Tang.

**Contribution / composition:** SAGA combines WholeGrasp-VAE, which samples full-body grasp poses and contacts around an object, with MotionFill-VAE, which fills a transition from an initial body state to the sampled grasp. Marker-based optimization then fits SMPL-X and improves contact and collision behavior.

**Mechanism:** SAGA combines WholeGrasp-VAE, which samples full-body grasp poses and contacts around an object, with MotionFill-VAE, which fills a transition from an initial body state to the sampled grasp. Marker-based optimization then fits SMPL-X and improves contact and collision behavior.

**Input contract:** A target object mesh and starting human state; the method samples an ending whole-body grasp and the intervening motion. It does not require an entire future object path, but its primary interaction is approaching and grasping a stationary target rather than unrestricted long manipulation.

**Data and split:** GRAB right-hand grasps follow the GrabNet object partition: 41 training, four validation, six test objects. MotionFill uses 62-frame approach-to-grasp clips at 30 fps; AMASS supplies 61-frame pretraining clips. HO3D objects test additional shape transfer without a stated statistical split ratio.

**Evaluation metrics:** Contact Ratio measures proximity contact; interpenetration volume/depth quantify mesh intersections; APD measures diversity. Marker ADE compares deterministic predictions, with minimum error over 10 samples for stochastic motion. PSKL-J compares acceleration power spectra as a smoothness proxy.

**Evaluation checked:** Tables 1–2 evaluate grasp sampling and optimization losses; motion experiments compare transition models and local/global completion components. Qualitative HO3D results assess unseen object geometries. Explicitly distinguish best-of-ten reference matching from a single deployed sample.

**Full-text source:** https://arxiv.org/pdf/2112.10103v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2112.10103v3 [cs.CV] 17 Aug 2022

**Full-text SHA256:** 9b95b549bb7c8e95cbbd018ddb1295570f32973f97acd1bc387e46b2b152b92d

**Source locator:** §3 (WholeGrasp/MotionFill and optimizers), §4 experiments and Tables 1–2; supplementary training-data section naming 41/4/6 objects and motion metrics.

**Scope / curator boundary:** Optimization and contact thresholds add sensitivity and runtime. End-grasp quality does not guarantee every intermediate frame is collision-free or dynamically feasible; a stationary target and short approach window limit long manipulation claims. GRAB-derived grouping must preserve object and source ancestry.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2112.10103); checked 2026-11-19.

<a id="interactagent"></a>
## InteractAgent: Agentic Human Motion Interaction with Memory-Augmented Reflection

**interactagent · 2026 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2610.25649) · [Evidence](https://arxiv.org/pdf/2610.25649v2) · Citekey: `interactagent2026`

**Authors of cited version:** Senhe Zhang; Tao Zhang; Yujia Zhang; Zeyu Zhang; Dong Gong.

**Contribution / composition:** Wraps a frozen motion executor with local visual recovery and cross-attempt planning reflection.

**Mechanism:** The same multimodal LLM performs scene analysis, planning, visual evaluation and reflection. A frozen Motion-Agent MotionLLM realizes action lists. Online observation chooses continue/redo/replan; inference-time memory informs later attempts without weight updates.

**Input contract:** Scene images, high-level task text, rendered execution feedback and a frozen motion executor. Reconstructed scene geometry is still needed for rendering and independent penetration measurements.

**Data and split:** Adapts UniHSI and TRUMANS scene/task resources. This is training-free orchestration; checked §4 does not provide a new train/test partition or an auditable per-complexity task inventory, so source split independence remains unspecified.

**Evaluation metrics:** Execution/task success is reported by complexity. Physical validity uses body-scene SDF penetration, including maximum and highest-10%-frame mean, preventing long noninteractive intervals from diluting severe collisions.

**Evaluation checked:** Tables 1–3 compare training-free variants, a supervised UniHSI-CoCo baseline, planner backbones and executors. Ablations separate online feedback from offline/memory reflection.

**Full-text source:** https://arxiv.org/pdf/2610.25649v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2610.25649v2

**Full-text SHA256:** dc1b7952f9f400e97f118f7ec4c4ed18c1051c07d97ee5356e30c83130bf0e33

**Source locator:** §§3.1–3.4/Algorithms 1–2; §4.1–4.2, Tables 1–3; §5.

**Scope / curator boundary:** The planner and visual evaluator share a backbone, so reported success is not an independent physical certificate. Occlusion, view sampling, executor limits and retry cost remain; geometric penetration must be reported separately.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.25649); checked 2026-11-19.

<a id="world2hosi"></a>
## World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation

**world2hosi · 2026 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2610.27725) · [Evidence](https://arxiv.org/pdf/2610.27725v1) · Citekey: `world2hosi2026`

**Authors of cited version:** Jiushu Li; Haoran Wang; Yumeng Liu; Zhiyang Dou; Yuan Liu; Yuexin Ma; Cheng Lin.

**Contribution / composition:** Orchestrates navigation, object and scene interaction experts around persistent scene state, reconciling boundaries and updating object effects.

**Mechanism:** Structured MotionIR and state updates compile expert conditions; incoming-prefix translation/SO(3) offsets decay with quintic smoothstep. Bounded residual RL tracks references and objects move through simulated contacts.

**Input contract:** Human-level instruction, reconstructed/synthetic scene state and available motion experts. MotionIR compiles navigation, object and scene subgoals; state updates carry object effects across stages, while transition alignment and bounded residual RL reconcile executed references.

**Data and split:** Constructs ten ISP scenes and twenty instructions, each run with three random seeds: sixty sequences. This is a designed evaluation suite, not a percentage train/test split. Expert training sources and residual-controller training are separate from the task-level benchmark.

**Evaluation metrics:** Waypoint error Txy, ordered task progress St, geometry score Sg, moving-object contact OCP, severe-penetration frame ratio with two-centimeter threshold, non-contact object displacement NCOD and object-scene penetration; body tracking/continuity measurements supplement task outcomes.

**Evaluation checked:** Experiments compare expert orchestration, scene-state maintenance, boundary alignment and physics correction, with failures and component ablations. Later stages receive task-progress credit only after prerequisite stages are observed, making task-order evaluation materially different from endpoint matching.

**Full-text source:** https://arxiv.org/pdf/2610.27725v1

**Reading status:** full_text_checked

**Inspected version:** 2610.27725v1

**Full-text SHA256:** 529aac9c1b4ee05fd21af98ff85cbf00ec3d2048399f2ba4ff093f86d9f18895

**Source locator:** Sections 3–4; Section 4 Dataset and metrics; main comparison/ablation tables; Appendix A.4 scoring rules.

**Scope / curator boundary:** Expert availability and planning assumptions bound transfer. Bounded residual control cannot rescue fundamentally infeasible references; a multi-expert harness is not one unified text-to-motion model or a cross-dataset dataset-construction method.

**Composition axes:** object-contact, scene-state, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.27725); checked 2026-11-19.

<a id="trumans"></a>
## Scaling Up Dynamic Human-Scene Interaction Modeling

**trumans · 2024 · Human-scene interaction & planning · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.pdf) · Citekey: `trumans2024`

**Authors of cited version:** Jiang, Nan; Zhang, Zhiyuan; Li, Hongjie; Ma, Xiaoxuan; Wang, Zan; Chen, Yixin; Liu, Tengyu; Zhu, Yixin; Huang, Siyuan.

**Contribution / composition:** TRUMANS captures human and part-level dynamic-object interaction across indoor scene configurations; autoregressive diffusion supports extended motion synthesis.

**Mechanism:** Captures whole-body human motion and tracked dynamic objects in reconstructed scenes, then augments human/object appearance and geometry while preserving interaction alignment. An autoregressive diffusion generator rolls out short episodes using local scene context and frame-level action labels; an action-progress indicator maintains continuity across episode boundaries.

**Input contract:** Current/historical body state, local scene occupancy, action labels and progress; dynamic-object context is included for interaction. This is action-controlled scene generation, not free-form text planning.

**Data and split:** Dataset records seven participants across 100 scene configurations for over fifteen hours. Evaluation includes ten unseen indoor scenes from PROX, Replica, ScanNet and ScanNet++; precise training/test proportions within TRUMANS are not stated in the inspected main protocol.

**Evaluation metrics:** Static HSI: contact rate and mean/maximum penetration. Dynamic object-level interaction: FID, diversity, scene penetration and MoCap-discrimination success (Table 3). Downstream mesh/contact tasks report MPVE/MPJPE/PA-MPJPE and contact precision/recall/F1/geodesic error.

**Evaluation checked:** Compares static HSI against scene-generation baselines and dynamic interaction against GRAB-trained IMoS/GOAL. Each trajectory receives five generated variants. Ablations remove data augmentation or the progress indicator; human ratings assess resemblance to captured motion.

**Full-text source:** https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Author/institution or proceedings PDF as retrieved 2026-11-19; version string not printed for this paper.

**Full-text SHA256:** 350d310b20be15ebba1b170d8414d4d6b9ad798f1564c208307a71278c4eccde

**Source locator:** Sections 3.1–3.3, 4.1–4.4; Sections 5.1–5.4, Tables 2–5; Appendix A.4.

**Scope / curator boundary:** Augmentation and scene generalization differ from unseen action-chain or actor generalization. Geometric penetration and foot-contact measurements do not establish dynamics. Action timing/progress is supplied, limiting autonomous high-level planning claims.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.html); checked 2026-11-19.

<a id="circle"></a>
## CIRCLE: Capture In Rich Contextual Environments

**circle · 2023 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2303.17912) · [Evidence](https://arxiv.org/pdf/2303.17912v1) · Citekey: `circle2023`

**Authors of cited version:** Joao Pedro Araujo; Jiaman Li; Karthik Vetrivel; Rishi Agarwal; Deepak Gopinath; Jiajun Wu; Alexander Clegg; C. Karen Liu.

**Contribution / composition:** Captures real human movement in perceived virtual scenes and learns scene-conditioned full-body reaching.

**Mechanism:** Captures full-body reaching while participants view virtual environments through a VR headset. Real capture space remains empty, while the simulator supplies exact scene geometry and rendered observations. A scene-aware transformer refines an initialized motion between a start pose and target wrist location, using local body/scene features from BPS or pretrained PointNet++ encodings. Training combines root, joint position, rotation and forward-kinematics losses.

**Input contract:** Initial body pose, scene geometry and a target right-hand/wrist position; this is contextual reaching, not dynamic object manipulation. Virtual scene contact has no corresponding physical object force feedback.

**Data and split:** 3,018 reaching sequences: random split has 2,565 train/453 test; task split has 2,578 train/440 test, holding out start/goal region pairs (109 training and 19 test tasks). Five subjects perform about ten hours across nine scenes.

**Evaluation metrics:** Success means final wrist within ten centimeters of target. Also measures distance to goal, cumulative scene collision depth, foot sliding, mean vertex/joint-position errors, root translation and joint-orientation discrepancy.

**Evaluation checked:** Tables 2–3 compare scene-conditioned variants, a no-scene baseline and GOAL modified to receive a ground-truth goal pose. All use the same data; task-held-out results degrade, and scene features improve reaching/collision behavior.

**Full-text source:** https://arxiv.org/pdf/2303.17912v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2303.17912v1

**Full-text SHA256:** f851621de2c5cadcf8b45034c761476e907b98f0c9660b49b74aa6f6e3c0f94b

**Source locator:** Sections 3, 4, 5.1–5.3 and 6; Tables 2–3; Figure 6.

**Scope / curator boundary:** The authors note persistent collisions and foot sliding. A nearly static baseline can misleadingly score well on sliding. VR capture does not provide physical contact reactions, and task-held-out reaching does not imply unseen scenes, dexterous grasping or object dynamics.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2303.17912); checked 2026-11-19.

<a id="scenediffuser"></a>
## Diffusion-based Generation, Optimization, and Planning in 3D Scenes

**scenediffuser · 2023 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2301.06015) · [Evidence](https://arxiv.org/pdf/2301.06015v1) · Citekey: `scenediffuser2023`

**Authors of cited version:** Siyuan Huang; Zan Wang; Puhao Li; Baoxiong Jia; Tengyu Liu; Yixin Zhu; Wei Liang; Song-Chun Zhu.

**Contribution / composition:** SceneDiffuser unifies conditional diffusion, differentiable objective guidance, and planning. Scene/object point-cloud features condition denoising; gradients of collision, contact, or task costs steer samples at inference. The framework handles poses, motions, dexterous grasps, path planning, and robot motion planning with task-specific representations.

**Mechanism:** SceneDiffuser unifies conditional diffusion, differentiable objective guidance, and planning. Scene/object point-cloud features condition denoising; gradients of collision, contact, or task costs steer samples at inference. The framework handles poses, motions, dexterous grasps, path planning, and robot motion planning with task-specific representations.

**Input contract:** 3D scene or object point clouds, optional start pose, and differentiable goals or constraints. The generated variable changes by task, so dexterous grasp and robot planning findings should not be merged into a single full-body language-conditioned manipulation claim.

**Data and split:** PROX pose/motion evaluation uses roughly 53,000 training frames from eight scenes and held-out scenes following prior work; four test scenes support human ratings. MultiDex ShadowHand grasp evaluation uses 48 training and 10 unseen test objects. These are distinct task-specific partitions.

**Evaluation metrics:** Human plausible rate, non-collision score, and contact score measure perceived/geometric validity; APD and standard deviation measure diversity. Grasp success is tested in physics under collision-depth settings. Planning experiments additionally report goal success and efficiency, rather than only motion-feature FID.

**Evaluation checked:** Section 5 evaluates five tasks, with Tables 1–2 separating pose/motion and start-pose conditions, and Table 3 testing dexterous grasps. Guided and unguided sampling ablations isolate optimization effects; motion metrics average framewise pose scores.

**Full-text source:** https://arxiv.org/pdf/2301.06015v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2301.06015v1 [cs.CV] 15 Jan 2023

**Full-text SHA256:** 7734045c80ded5304b9603b73257678c1cb4dfe6ae9eda2ecc1bd51c9c20b4ab

**Source locator:** §4 (conditional denoising/objective guidance), §§5.2–5.6, Tables 1–3; §5.2 PROX split and §5.4 MultiDex 48/10-object protocol.

**Scope / curator boundary:** Differentiable surrogate costs and averaged frame scores do not ensure continuous collision freedom or stable dynamic manipulation. Human ratings still show substantial implausibility. Cross-task architectural reuse is not evidence of one joint controller handling every tested output type.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2301.06015); checked 2026-11-19.

<a id="occupancy"></a>
## Revisit Human-Scene Interaction via Space Occupancy

**occupancy · 2023 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2312.02700) · [Evidence](https://arxiv.org/pdf/2312.02700v2) · Citekey: `occupancy2024`

**Authors of cited version:** Xinpeng Liu; Haowen Hou; Yanchao Yang; Yong-Lu Li; Cewu Lu.

**Contribution / composition:** Uses space occupancy to connect locomotion and interaction control; evaluates reaching and extended indoor action sequences.

**Mechanism:** Constructs a Motion Occupancy Base from motion-only data by representing surrounding feasible occupied/free space, turning captured motion into synthetic interaction supervision. A lightweight autoregressive transformer controller predicts future state using historical pose and optional controls. Occupancy-field and penetration losses discourage collisions, and online control guides endpoints or paths.

**Input contract:** Current/history motion, canonical binary occupancy and optional end-effector target or trajectory. A scene can be supplied as occupancy instead of a photorealistic reconstruction. Appendix C.2 additionally conditions on a ten-step future hand-contact trajectory, potentially predicted by OMOMO.

**Data and split:** MOB training excludes 1,393 motion sequences as a test set. The test set yields 30,000 three-second goal-reaching examples. CIRCLE evaluation additionally distinguishes MOB training with CIRCLE excluded from training directly on CIRCLE; overall split proportions are not reported. The OMOMO fine-tuning extension shares all 15 object identities across train/test and reports one evaluation run.

**Evaluation metrics:** Goal-reaching success, distance to goal, cumulative collision depth and foot sliding. Scene/occupancy interaction evaluations compare feasibility and target accuracy rather than language retrieval. The OMOMO extension also reports root translation/rotation error, Hand JPE and MPJPE.

**Evaluation checked:** Main MOB/CIRCLE tests evaluate reaching and collision avoidance with held-out sequences. Appendix C.2 fine-tunes on OMOMO contact trajectories; C.3 demonstrates a rotating door and sudden occupancy changes. These are distinct protocols, not one uniform benchmark.

**Full-text source:** https://arxiv.org/pdf/2312.02700v2

**Reading status:** full_text_checked

**Inspected version:** 2312.02700v2

**Full-text SHA256:** 62af91b6985f0039b608fb2cea8d864fb4c1e743d8edf89e0ef08b10a6775140

**Source locator:** Sections 3–4.5; Sections 5.1–5.2; MOB and CIRCLE quantitative tables and occupancy ablations. Supplementary C.2/Table 4 (OMOMO control) and C.3 (dynamic scenes).

**Scope / curator boundary:** Occupancy supervision assesses geometric compatibility, not force balance. Dynamic-scene and trajectory-conditioned object experiments are present, but shared-object OMOMO evaluation and qualitative door examples do not establish unseen-object or unrestricted task-chain generalization.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.02700); checked 2026-11-19.

<a id="dimos"></a>
## Synthesizing Diverse Human Motions in 3D Indoor Scenes

**dimos · 2023 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2305.12411) · [Evidence](https://arxiv.org/pdf/2305.12411v3) · Citekey: `dimos2023`

**Authors of cited version:** Kaifeng Zhao; Yan Zhang; Shaofei Wang; Thabo Beeler; Siyu Tang.

**Contribution / composition:** DIMOS uses learned motion primitives and scene-aware policies to navigate and perform successive furniture interactions.

**Mechanism:** Policies select latent actions of generative motion primitives; navigation uses walkability features and waypoints, interaction uses SDF proximity and marker goals.

**Input contract:** Initial body state, 3D scene geometry, navigation waypoints and target interaction markers. Policies select latent actions of generative motion primitives, using walkability for travel and signed-distance/proximity features for furniture interaction.

**Data and split:** Primitive training uses AMASS sit/lie actions selected through BABEL plus SAMP data, resampled to forty fps. Interaction evaluation uses ten unseen ShapeNet seats: three armchairs, three straight chairs, three sofas and one L-sofa. Exact motion-source train/test percentage is not reported.

**Evaluation metrics:** Locomotion completion/time, path and collision measures; target-marker accuracy, penetration/contact and diversity for sitting/lying. Kinematic quality and scene goal completion are evaluated separately from policy reward optimization.

**Evaluation checked:** Section 4 compares locomotion with SAMP/GAMMA and fine-grained static-object interaction with scene-aware alternatives. Combined long demonstrations switch travel and interaction policies, showing sequential navigation followed by goal-conditioned sitting/lying in novel furniture layouts.

**Full-text source:** https://arxiv.org/pdf/2305.12411v3

**Reading status:** full_text_checked

**Inspected version:** 2305.12411v3

**Full-text SHA256:** 8bc9226167034c132b0d6e84237ee86e9931f57422f3981cf99b1d290c3e6092

**Source locator:** Sections 3.1–3.3, 4.1–4.3; Tables 1–3; supplementary long-sequence examples.

**Scope / curator boundary:** Policies act in a learned kinematic primitive space, not a torque-level physical humanoid simulator. Mainly static furniture interactions; moving-object manipulation and contact forces are outside scope. Ten novel meshes do not establish arbitrary semantic task-chain generalization.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.12411); checked 2026-11-19.

<a id="unihsi"></a>
## Unified Human-Scene Interaction via Prompted Chain-of-Contacts

**unihsi · 2023 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2309.07918) · [Evidence](https://arxiv.org/pdf/2309.07918v5) · Citekey: `unihsi2024`

**Authors of cited version:** Zeqi Xiao; Tai Wang; Jingbo Wang; Jinkun Cao; Wenwei Zhang; Bo Dai; Dahua Lin; Jiangmiao Pang.

**Contribution / composition:** Compiles language into sequential body-joint/object-part contact constraints and executes them with one physics controller.

**Mechanism:** An LLM planner generates a Chain of Contacts with object, part, joint, contact type and relative direction. A task parser advances contact stages; PPO with an adversarial motion discriminator learns a common low-level policy.

**Input contract:** Language, scene object/part descriptions and optional layouts for planning; meshes/point clouds, humanoid state and the contact plan for execution. Training uses pregenerated plans rather than end-to-end LLM optimization.

**Data and split:** ScenePlan training uses 40 PartNet objects with generated steps. Evaluation uses 40 PartNet objects and ten ScanNet scenarios, with 1,040 and 100 plans. SAMP clips and twenty representative CIRCLE clips train the discriminator.

**Evaluation metrics:** Success rate requires every plan stage within n×10 seconds. Contact error measures requested contact/noncontact joint-part distances; success steps and planner correctness supplement whole-plan success.

**Evaluation checked:** Scenario, horizon, interaction and planner ablations assess the unified controller and LLM interface. Scanned-scene tests are separated from PartNet-derived synthetic layouts.

**Full-text source:** https://arxiv.org/pdf/2309.07918v5

**Reading status:** full_text_checked

**Inspected version:** arXiv:2309.07918v5

**Full-text SHA256:** c8e38861b13205c8bb12770ee8aace905280970336dd95704b2cbbb98ad10bb1

**Source locator:** §§3.1–3.4; §4.1–4.3, Tables 1–3; Appendices A–C.

**Scope / curator boundary:** The framework only interacts with fixed objects and does not model moving/carrying objects. Reported object counts alone do not establish that train/evaluation PartNet identities are disjoint.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2309.07918); checked 2026-11-19.

<a id="coins"></a>
## Compositional Human-Scene Interaction Synthesis with Semantic Control

**coins · 2022 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2207.12824) · [Evidence](https://arxiv.org/pdf/2207.12824v1) · Citekey: `coins2022`

**Authors of cited version:** Kaifeng Zhao; Shaofei Wang; Yan Zhang; Thabo Beeler; Siyu Tang.

**Contribution / composition:** COINS encodes body surface points and objects in a joint latent space, permitting multiple atomic action-object pairs without corresponding composite training examples.

**Mechanism:** COINS synthesizes static human-scene interactions with action-object-instance semantics. PelvisVAE samples global pelvis placement; BodyVAE generates local body vertices and contact, followed by optimization. For composite interactions, separate atomic pelvis distributions are reconciled through latent optimization; action-specific contact statistics produce body-part attention masks, combining independently learned atomic constraints without training on composite examples.

**Input contract:** A 3D scene and one or more explicit action/object-instance pairs, such as sitting on a chair while touching a table. Generated output is a body configuration, not a continuous interaction sequence.

**Data and split:** PROX-S annotates about 32K frames from 43 PROX recordings in 12 indoor scenes. Four named scenes are held out (MPH16, MPH1Library, N0SittingBooth, N3OpenArea), with eight scenes for training; evaluates about 150 action/object-instance combinations.

**Evaluation metrics:** Semantic contact compares action-weighted contact to a threshold from training data. Non-collision is the fraction of vertices with nonnegative scene SDF. Diversity uses 50-cluster entropy and distance to centers; user studies assess naturalness and semantic agreement.

**Evaluation checked:** Compares adapted PiGraph-X and POSA-style interaction baselines and atomic/composite variants. The composite experiment explicitly tests composing interactions learned individually, making its composition evidence narrower but more direct than ordinary text generation.

**Full-text source:** https://arxiv.org/pdf/2207.12824v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2207.12824v1

**Full-text SHA256:** f9029b583ce31e9adca5f30e8a6d2a49de9310d7efe52d0a99ad3bac5efe1ef0

**Source locator:** Sections 3.2–3.3, 4.1–4.4; Supplement B.1 and D; semantic contact definition and composite-generation equations.

**Scope / curator boundary:** Objects not explicitly conditioned can be ignored, requiring scene-SDF postprocessing. Hand contact is limited by noisy estimated hands in training data. Static semantic/geometry consistency does not establish transitions, force balance, object manipulation or long-horizon task execution.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2207.12824); checked 2026-11-19.

<a id="samp"></a>
## Stochastic Scene-Aware Motion Prediction

**samp · 2021 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2108.08284) · [Evidence](https://arxiv.org/pdf/2108.08284v1) · Citekey: `samp2021`

**Authors of cited version:** Mohamed Hassan; Duygu Ceylan; Ruben Villegas; Jun Saito; Jimei Yang; Yi Zhou; Michael Black.

**Contribution / composition:** SAMP combines an autoregressive conditional-VAE MotionNet, an object-conditioned GoalNet, and a path planner. GoalNet samples plausible contact positions/orientations; MotionNet predicts subsequent body state from prior state, local object geometry, target goals, and action information while the planner routes locomotion around obstacles.

**Mechanism:** SAMP combines an autoregressive conditional-VAE MotionNet, an object-conditioned GoalNet, and a path planner. GoalNet samples plausible contact positions/orientations; MotionNet predicts subsequent body state from prior state, local object geometry, target goals, and action information while the planner routes locomotion around obstacles.

**Input contract:** A scene, target object and action label, prior character motion, and interaction goals. Five modeled actions are idle, walk, run, sit, and lie down. Stochastic latent sampling supplies alternative styles; a global planner supports locomotion before the terminal interaction.

**Data and split:** Uses newly captured interaction motions plus ShapeNet objects from sofa, L-shaped sofa, chair, armchair, and table categories. The main description does not specify a standard percentage or subject-disjoint train/test partition. Some baseline comparisons retrain SAMP on NSM training data for compatibility.

**Evaluation metrics:** Diversity measures generated motion variation; execution time measures time to reach an action, with failures beyond three minutes marked infinite. Goal precision measures task accuracy and Fréchet distance compares generated/reference motions. Scene penetration is measured as the fraction of colliding frames.

**Evaluation checked:** Section 5 tests diverse transitions, unseen furniture configurations, goals, and obstacle navigation. Tables 1–4 compare diversity, execution time, precision, and Fréchet distance; ablations remove GoalNet or path planning. Scene collision tests repeat randomized placements ten times.

**Full-text source:** https://arxiv.org/pdf/2108.08284v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2108.08284v1 [cs.CV] 18 Aug 2021

**Full-text SHA256:** c93cfbab9a665a35091d9ba2dc5c00832a093a53c8c2d8fb539509083764130e

**Source locator:** §3 (MotionNet/GoalNet/planner), §4 (motion and ShapeNet preparation), §§5.1–5.2, Tables 1–4 and Figure 6 (GoalNet ablation).

**Scope / curator boundary:** The five-action vocabulary and furniture-centered capture constrain scope. Geometric collision and feature-distribution metrics are not force validation, and autoregressive rollout can drift. NSM comparisons use different supervision availability, which must remain visible rather than treated as perfectly matched training.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2108.08284); checked 2026-11-19.

<a id="pigraphs"></a>
## PiGraphs: Learning Interaction Snapshots from Observations

**pigraphs · 2016 · Human-scene interaction & planning · method**

[Primary source](https://graphics.stanford.edu/projects/pigraphs/) · [Evidence](https://graphics.stanford.edu/projects/pigraphs/pigraphs.pdf) · Citekey: `pigraphs2016`

**Authors of cited version:** Manolis Savva; Angel X. Chang; Pat Hanrahan; Matthew Fisher; Matthias Nießner.

**Contribution / composition:** Probabilistic prototype interaction graphs couple body poses, object geometry, contact and visual attention for scene and pose synthesis.

**Mechanism:** Learns prototypical interaction graphs from RGB-D observations aligned with reconstructed scenes. Nodes represent body joints and object geometry; contact and gaze edges store spatial feature distributions. Sampling poses and arranging retrieved objects maximize learned interaction likelihoods. Aggregating action priors supports new verb-noun combinations and multiple simultaneous static relations.

**Input contract:** Verb-noun interaction specifications, optionally parsed from text, and object/scene geometry. Output is a posed person with arranged scene objects: an interaction snapshot rather than an animated sequence.

**Data and split:** Learns priors from the collected interaction observations. The snapshot study samples five outputs from each of 37 learned PiGraphs under three conditions. A randomized train/test ratio or independently held-out subject partition is not reported for this evaluation.

**Evaluation metrics:** Human match-quality scores on a seven-point Likert scale; 2,072 judgments across 555 stimuli from 75 participants. Interaction likelihoods use contact/gaze histogram similarity and pose/object placement scores.

**Evaluation checked:** Compares full sampling against a naive placement baseline and an average-pose variant. Section 8.4 demonstrates unseen verb-noun retargeting, including failure cases; the main evaluation tests descriptive snapshot quality, not temporal task success.

**Full-text source:** https://graphics.stanford.edu/projects/pigraphs/pigraphs.pdf

**Reading status:** full_text_checked

**Inspected version:** Author/institution or proceedings PDF as retrieved 2026-11-19; version string not printed for this paper.

**Full-text SHA256:** f52d9de4715137b4b3c881474fb598ff92b29510fea27b5c8805555d56647677

**Source locator:** Sections 4–7, especially 7.4.3; Sections 8.2–8.5; Figure 10 (study), Figure 11 (novel combinations).

**Scope / curator boundary:** Explicitly restricted to static scenes without interaction dynamics or ordering. Sampling can get trapped by poor initial placements; commodity depth resolution limits small objects. Novel static relations do not establish continuous locomotion-manipulation composition.

**Composition axes:** scene-state.

**Metadata:** primary-transcribed; [source](https://graphics.stanford.edu/projects/pigraphs/); checked 2026-11-19.

<a id="core4d"></a>
## CORE4D: A 4D Human-Object-Human Interaction Dataset for Collaborative Object REarrangement

**core4d · 2025 · Multi-person & collaborative interaction · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.pdf) · Citekey: `core4d2025`

**Authors of cited version:** Liu, Yun; Zhang, Chengwen; Xing, Ruofan; Tang, Bingda; Yang, Bowen; Yi, Li.

**Contribution / composition:** Combines real collaborative object rearrangement recordings with collaboration retargeting to additional object shapes.

**Mechanism:** Combines captured two-person object rearrangement with synthetic retargeting to new object shapes. Real acquisition combines inertial/optical body tracking, gloves, object tracking and multiple camera views. Synthetic generation iterates contact-candidate selection and contact-guided human-object retargeting, scoring plausibility with a learned discriminator plus interpenetration penalties. The dataset has roughly 1K captured and 10K synthetic collaborative sequences.

**Input contract:** Two human bodies, an object and its geometry; forecasting uses past collaborative interaction, while synthesis benchmarks condition on object motion. These inputs differ from text-only generation.

**Data and split:** Supplement Table 3 lists 482 real and 10,016 synthetic training sequences, 225 real S1 sequences for seen objects, and 255 real S2 sequences for novel objects. Synthetic examples never enter testing. Humanoid application separately uses 16 training boxes/504 clips, with six boxes/386 clips held out.

**Evaluation metrics:** Forecasting measures MPJPE, object translation/rotation errors, five-centimeter-threshold hand contact and penetration. Synthesis uses root-relative joint/vertex errors and FID. Supplement F defines vertex error on humans, unlike the main-text object-vertex wording; this inconsistency remains unresolved.

**Evaluation checked:** Compares MDM/InterDiff/CAHMP forecasting and MDM/CHOIS/OMOMO synthesis; synthetic-data and humanoid lifting experiments test augmentation utility.

**Full-text source:** https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Primary author/proceedings PDF retrieved 2026-11-19; identity fixed by SHA256

**Full-text SHA256:** 13af14a59b0ae66d42dd176a3e2fba52b08fdad8b47644ced0603fb232aaaa51

**Source locator:** Main Sections 3.1–3.4, 4.1–4.4 and 5, Tables 2–6; official Supplement E/Table 3, F.1–F.2, I.1–I.2. Supplemental URL: https://openaccess.thecvf.com/content/CVPR2025/supplemental/Liu_CORE4D_A_4D_CVPR_2025_supplemental.pdf

**Scope / curator boundary:** Captures are indoors and synthetic examples lack visual streams. Main text says 37 real objects, while the supplement lists 38. Retargeted descendants are not independent captures; object-path synthesis and simulated box lifting do not establish general text-driven collaborative control. Supplementary F.2 calls Cacc accuracy but describes a contact-error percentage, whereas the main table marks higher as better; that source ambiguity is retained rather than silently resolved.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.html); checked 2026-11-19.

<a id="hhoi-text"></a>
## Learning to Generate Human-Human-Object Interactions from Textual Descriptions

**hhoi-text · 2025 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2511.20446) · [Evidence](https://arxiv.org/pdf/2511.20446v3) · Citekey: `hhoitext2026`

**Authors of cited version:** Jeonghyeon Na; Sangwon Baik; Inhee Lee; Junyoung Lee; Hanbyul Joo.

**Contribution / composition:** The method learns separate score-based priors for human-object and human-human configurations, then combines their scores during guided sampling. Consistency and collision constraints reconcile shared humans across factors, enabling a variable number of people around one object without paired multi-person training for every composition.

**Mechanism:** The method learns separate score-based priors for human-object and human-human configurations, then combines their scores during guided sampling. Consistency and collision constraints reconcile shared humans across factors, enabling a variable number of people around one object without paired multi-person training for every composition.

**Input contract:** An object mesh, textual description, and desired participant count. Generated variables are body poses, scales, rotations, and translations in object/person-centered coordinates. This is static HHOI configuration generation, not continuous multi-person motion or temporal manipulation synthesis.

**Data and split:** Combines CORE4D-derived samples, multiview captures, and synthetic image-derived samples across 19 object categories. After preprocessing, training/test samples are split 9:1. The appendix does not claim subject/recording-disjoint grouping; repeated person-reference transformations must not be counted as independent captures.

**Evaluation metrics:** Body-pose FD and interpersonal-distance FD compare distributions; multiview CLIP Score assesses prompt similarity. Desired-person-count success tests 3–5 people. Human-human/object penetration ratios and selected hand/hip contact distances probe geometry, while user preferences judge realism and text coherence.

**Evaluation checked:** Tables 1–2 compare dyadic and multi-human generation against adapted GenZI and depth-optimization baselines; physical metrics and qualitative failures supplement these scores. The real/synthetic data preparation and sample counts are detailed in appendix A.

**Full-text source:** https://arxiv.org/pdf/2511.20446v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2511.20446v3 [cs.CV] 3 Jul 2026

**Full-text SHA256:** aaee773c1f2061892316781a6111ba2165d7baa248ab2f220f7edd11c0cdb032

**Source locator:** §§3.1–3.3 (HOI/HHI score composition), §5.1 metric definitions, Tables 1–2; appendix A.2–A.3 (9:1 split, sources/statistics).

**Scope / curator boundary:** Composition of static pairwise priors does not ensure globally compatible dynamic cooperation. CLIP similarity and person-count success do not establish task completion. Random sample splitting and synthetic reconstruction can preserve correlated geometry or pose errors across evaluation data.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2511.20446); checked 2026-11-19.

<a id="freemotion"></a>
## FreeMotion: A Unified Framework for Number-free Text-to-Motion Synthesis

**freemotion · 2024 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2405.15763) · [Evidence](https://arxiv.org/pdf/2405.15763v1) · Citekey: `freemotion2024`

**Authors of cited version:** Ke Fan; Junshu Tang; Weijian Cao; Ran Yi; Moran Li; Jingyu Gong; Jiangning Zhang; Yabiao Wang; Chengjie Wang; Lizhuang Ma.

**Contribution / composition:** Factorizes conditional motion generation into generation and interaction modules to support variable participant counts and spatial controls.

**Mechanism:** Factorizes an arbitrary-size group motion distribution into recursively conditioned individual motions. A pretrained single-person diffusion module handles movement quality, while an interaction module injects previously generated people through attention. Two-stage training first uses LLM-separated individual captions, then learns interaction conditioning; guidance optionally adds spatial constraints.

**Input contract:** Group interaction text decomposed into individual descriptions, already generated partner motions, and optional joint/location controls. Number of people is variable at inference despite principally two-person supervision.

**Data and split:** Trains and evaluates on InterHuman, described here as 6,022 motions with 16,756 descriptions. Exact partition proportions and identity grouping are not restated in Section 5.1. Larger groups are generation demonstrations rather than separately captured multi-person test ground truth.

**Evaluation metrics:** InterGen protocol: FID, R-Precision, text-motion distance, diversity and multimodality, measuring distribution quality and text correspondence. Spatial-control studies supplement standard two-person metrics.

**Evaluation checked:** Section 5 compares number-free generation with two-person baselines and ablates the generation/interaction design. Qualitative examples extend to additional participants and spatially controlled interactions, illustrating recursive reuse of learned pairwise coordination.

**Full-text source:** https://arxiv.org/pdf/2405.15763v1

**Reading status:** full_text_checked

**Inspected version:** 2405.15763v1

**Full-text SHA256:** fb4959f2468688c1e86f79c014fa25880d5d9107b696ca7f86c4f792dbfe2449

**Source locator:** Sections 3.2, 4.1–4.5; Sections 5.1–5.4; quantitative comparison and component-ablation tables.

**Scope / curator boundary:** Recursive factorization can propagate earlier errors and need not enforce globally consistent group contacts. Evaluation on two-person data does not by itself validate arbitrary group sizes, physical interaction forces or compositional novelty of individual action assignments.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2405.15763); checked 2026-11-19.

<a id="intermask"></a>
## InterMask: 3D Human Interaction Generation via Collaborative Masked Modeling

**intermask · 2024 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2410.10010) · [Evidence](https://arxiv.org/pdf/2410.10010v3) · Citekey: `intermask2025`

**Authors of cited version:** Muhammad Gohar Javed; Chuan Guo; Li Cheng; Xingyu Li.

**Contribution / composition:** Collaboratively predicts masked discrete motion tokens for two people and also supports reaction generation.

**Mechanism:** Shared 2D VQ-VAE preserves spatial/temporal tokens; collaborative transformer combines self, spatiotemporal and cross-person attention. Iterative confidence remasking generates both actors jointly.

**Input contract:** Text for joint two-person generation; reaction completion additionally provides one actor motion. A shared spatial-temporal VQ codec represents both people, and a collaborative masked transformer iteratively predicts/remasks tokens with cross-person attention.

**Data and split:** Evaluates InterHuman and InterX with the corresponding standard dataset protocols. Exact actor/sequence train/validation/test proportions are not restated in the inspected setup. InterX includes richer body/hand representation; its scores should not be merged numerically with InterHuman results.

**Evaluation metrics:** Feature FID, R-Precision, MM-Distance, diversity and multimodality using the established interaction evaluators. Reaction-generation and ablation results assess conditional completion in addition to joint text-driven synthesis.

**Evaluation checked:** Tables compare diffusion/autoregressive interaction generators and masked-model variants. Codec reconstruction and attention/masking ablations test whether preserving spatial tokens and communication improves quality. Inference uses iterative confidence-based selection rather than one-pass deterministic stitching.

**Full-text source:** https://arxiv.org/pdf/2410.10010v3

**Reading status:** full_text_checked

**Inspected version:** 2410.10010v3

**Full-text SHA256:** 8e7b2fb983bf371a8577399cf5ddf73c5eb01756ce30764939f497b120d31409

**Source locator:** Sections 3.1–3.4, 4.1–4.4; main comparison/ablation tables; Appendix E implementation and limitations.

**Scope / curator boundary:** Two-person scope does not establish arbitrary actor count or object-state planning. Surface conversion can expose inter-person penetration; fast actions may jerk and dataset dance bias remains. Learned interaction embeddings do not independently validate contact forces or chronological task success.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.10010); checked 2026-11-19.

<a id="inter-x"></a>
## Inter-X: Towards Versatile Human-Human Interaction Analysis

**inter-x · 2023 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2312.16051) · [Evidence](https://arxiv.org/pdf/2312.16051v1) · Citekey: `interx2023`

**Authors of cited version:** Liang Xu; Xintao Lv; Yichao Yan; Xin Jin; Shuwen Wu; Congsheng Xu; Yifan Liu; Yizhou Zhou; Fengyun Rao; Xingdong Sheng; Yunhui Liu; Wenjun Zeng; Xiaokang Yang.

**Contribution / composition:** Captured full-body interactions with hand gestures and detailed part-level text support perceptual and generative benchmarking.

**Mechanism:** Captures two-person whole-body motion including hands using optical motion capture and fits SMPL-X sequences. Adds detailed text, action classes, actor/reactor order, relationships and personality annotations. Rather than proposing one new universal generator, it adapts existing text/action generation, reaction, recognition and captioning models into a common interaction benchmark, preserving both participants’ global translations to maintain relative geometry.

**Input contract:** Downstream task determines input: text, action category, actor motion, interaction motion, or relationship/personality attributes. Human-human interaction and expressive hand motion are central; dynamic object manipulation is not the primary task.

**Data and split:** Main generation experiments partition sequences into train/test/validation at 80/15/5 percent. Personality prediction explicitly uses person-ID splits with the same proportions, a separate protocol that must not be attributed to all tasks.

**Evaluation metrics:** Generation uses FID, diversity, multimodality, top-1/2/3 R-precision and MM-Dist. Action tasks include recognition accuracy; captioning adds BLEU, ROUGE, CIDEr and BERTScore; personality regression uses R-squared.

**Evaluation checked:** Compares adapted diffusion/VAE interaction models, action generators, reaction generators and skeleton classifiers. Experiments and ablations emphasize expressive hand representation and actor/reactor asymmetry; qualitative comparisons contrast Inter-X and InterHuman-trained outputs.

**Full-text source:** https://arxiv.org/pdf/2312.16051v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2312.16051v1

**Full-text SHA256:** 8e6c7f97eff3416bea481d9b85c9eb70ec6e761203ee64c124fca607350c6e9e

**Source locator:** Sections 3–5, 6.1–6.4 and 7; Tables 1–5; Supplement A.1–A.4.

**Scope / curator boundary:** Indoor non-professional captures omit facial expressions, and atomic interactions dominate rather than long uninterrupted interaction chains. Most task splits are sequence-level, so they should not be described as actor-disjoint. Rich annotations and baseline generation do not establish unseen compositional pairs or physically certified interpersonal contacts.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.16051); checked 2026-11-19.

<a id="intergen"></a>
## InterGen: Diffusion-based Multi-human Motion Generation under Complex Interactions

**intergen · 2023 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2304.05684) · [Evidence](https://arxiv.org/pdf/2304.05684v3) · Citekey: `intergen2024`

**Authors of cited version:** Han Liang; Wenqian Zhang; Wenxuan Li; Jingyi Yu; Lan Xu.

**Contribution / composition:** Two cooperative weight-sharing denoisers exchange mutual attention to generate coordinated two-person motion from text.

**Mechanism:** Shared denoisers, mutual attention, world-frame joint representation and spatial-relation regularization with damping preserve interpersonal coordination.

**Input contract:** Text describing a two-person interaction, plus optional partial/prefix controls in applications. Two weight-sharing denoisers use mutual attention; world-frame joints and relation losses preserve relative positions/orientations.

**Data and split:** InterHuman supplies synchronized paired motion and descriptions. Mirroring and person-order swapping augment data; Section 5 follows the HumanML3D partition protocol without printing new percentages there. A cross-person identity-disjoint or independently held-out composition guarantee is not stated.

**Evaluation metrics:** R-Precision Top-1/2/3, MM-Distance, FID, diversity and multimodality from joint-interaction/text embeddings. Component studies evaluate spatial relation regularization and coordinated denoising; perceptual evaluation supplements feature scores.

**Evaluation checked:** Comparisons retrain single-person baselines for two-person output on the same InterHuman training data. ComMDM is additionally reported in its original small-data setup, which is a different training contract. Ablations inspect mutual attention, shared weights, representation and regularization scheduling. The retained world frame preserves the two actors’ relative geometry.

**Full-text source:** https://arxiv.org/pdf/2304.05684v3

**Reading status:** full_text_checked

**Inspected version:** 2304.05684v3

**Full-text SHA256:** 3cce82911e5d4a8246dd3b6ec92966f5cba7982db11f176fd79e4c44e54f5136

**Source locator:** Sections 3–4 (dataset/model), Section 5 Experiments; quantitative comparison and ablation tables; regularization schedule Eq. 14.

**Scope / curator boundary:** Two-person generation is the demonstrated contract. Skeletal relation losses are not contact dynamics; no persistent manipulated-object state is represented. Mirroring/swapping are data transformations, not new people or independent captures, and feature quality need not imply mesh-level collision freedom.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.05684); checked 2026-11-19.

<a id="remos"></a>
## ReMoS: 3D Motion-Conditioned Reaction Synthesis for Two-Person Interactions

**remos · 2023 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2311.17057) · [Evidence](https://arxiv.org/pdf/2311.17057v2) · Citekey: `remos2024`

**Authors of cited version:** Anindita Ghosh; Rishabh Dabral; Vladislav Golyanik; Christian Theobalt; Philipp Slusallek.

**Contribution / composition:** Spatiotemporal cross-attention generates a second person’s body and hand response to a given actor motion; contributes ReMoCap.

**Mechanism:** Cascaded diffusion first generates reactive body joints using joint spatiotemporal cross-attention, then hands with proximity-derived interaction masks; reaction/kinematic losses and inference guidance improve alignment.

**Input contract:** Complete actor motion conditions a generated reactor sequence. Cascaded diffusion predicts reactive body and then fingers; proximity-derived hand masks and reaction/kinematic guidance improve correspondence. This conditions on another person rather than generating both freely from text.

**Data and split:** ReMoCap Lindy Hop trains on pairs (A,C), (B,D), (B,C) and tests (A,D), so people recur but partnerships differ. Ninjutsu uses roughly 3:1 train/test with twenty-eight test sequences. ExPI trains on (A,B) and tests (C,D) using its common-action protocol.

**Evaluation metrics:** MPJPE and MPJVE, body/hand FID, latent diversity and human-rated quality/plausibility. Body-only and detailed-hand benchmarks are distinguished because ExPI lacks finger supervision.

**Evaluation checked:** Section 5 compares InterFormer, MixNMatch, ComMDM, RAIG and adapted interaction generation, with cascade/attention/guidance ablations. ReMoCap provides approximately 2.04 hours, including contact-heavy dance and martial arts; editing applications vary conditioned actor movements.

**Full-text source:** https://arxiv.org/pdf/2311.17057v2

**Reading status:** full_text_checked

**Inspected version:** 2311.17057v2

**Full-text SHA256:** b2f77bf99b5e53a2b2d90d0761e0c0540a32ecaa7c2dc73488e59b5eb80391d0

**Source locator:** Sections 3–5; main quantitative/user-study tables; supplementary Appendix B.1 (dataset preparation/splits).

**Scope / curator boundary:** Given actor trajectories provide substantial future information. Fast contact-heavy sequences can remain spatially misaligned. Novel partnership is not new-person independence, and proximity masks or low joint error do not establish actual contact forces or safe reactive execution.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2311.17057); checked 2026-11-19.

<a id="hiphi"></a>
## HiPHI: A Large-Scale Benchmark for High-Precision Human Motion and Object-Interaction

**hiphi · 2026 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2608.16222) · [Evidence](https://arxiv.org/pdf/2608.16222v2) · Citekey: `hiphi2026`

**Authors of cited version:** Jiahao Ji; Ji Ma; Runhan Zhang; Runyi Yu; Wenjia Wang; Weiheng Chi; Qianqian Peng; Weichao Yan; Yongfei Gu; Ye Tian; Ting Wu; Longwei Li; Chun Yuan; Ruoli Dai; Lei Han.

**Contribution / composition:** HiPHI organizes studio optical motion capture through FrameNet frames and lexical units, expanding motion seeds by direction, speed, amplitude, body-part participation, and object/contact factors. The release provides BVH motion plus aligned mesh/object trajectories for a stricter interaction subset and benchmarks humanoid tracking.

**Mechanism:** HiPHI organizes studio optical motion capture through FrameNet frames and lexical units, expanding motion seeds by direction, speed, amplitude, body-part participation, and object/contact factors. The release provides BVH motion plus aligned mesh/object trajectories for a stricter interaction subset and benchmarks humanoid tracking.

**Input contract:** This is a dataset/benchmark rather than a text-to-motion generator. Semantic Frame-LU indices, actor metadata, human kinematics, and object state support downstream retrieval and control; recorded future trajectories are supervision, not initial-state-only generative inputs.

**Data and split:** Reports 617.5 hours from 132 performers and 214 Frame-LUs, including 245.7 object-state-aligned hours. No conventional train/validation/test proportions or held-out-subject generation split is reported in the inspected benchmark. Tracking comparisons use common retargeting/control settings, not an independent composition test.

**Evaluation metrics:** Projected-grid occupancy, effective occupancy, and long-tail share measure motion-space coverage. Jerk, acceleration, below-ground depth, floating share, and support drift probe kinematics; sparse-skeleton non-conflict and near-surface grounding assess interaction geometry. Tracking/recovery and hardware demonstrations assess downstream usability.

**Evaluation checked:** Section 5 compares equal-size coverage samples, motion quality, and Unitree G1 tracking against existing datasets; appendix analyses vary projection and grid settings. Table 2 explicitly separates body precision and object geometry; real hardware examples cover locomotion and object-related actions.

**Full-text source:** https://arxiv.org/pdf/2608.16222v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2608.16222v2 [cs.RO] 8 Sep 2026

**Full-text SHA256:** e9405b3f84961304476370bab953c8e6222dc5e50ef948f3ce40f44010440a4e

**Source locator:** §§3–4 (FrameNet construction/capture), §§5.1–5.4 and Tables 1–2, Figures 7–8; §7 limitations; appendices B/E geometry and robustness details.

**Scope / curator boundary:** Only single-person studio motion is captured; forces and tactile signals are not directly measured. Sparse centerline geometry and 20-cm near-surface thresholds are not dense-mesh contact certification. Hardware demonstrations cannot establish all 617.5 hours are executable or every asset is already released.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2608.16222); checked 2026-11-19.

<a id="robomocap"></a>
## RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning

**robomocap · 2026 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2611.10994) · [Evidence](https://arxiv.org/pdf/2611.10994v1) · Citekey: `robomocap2026`

**Authors of cited version:** Mayur Deshmukh; Aaron Tung; Junyi Li; Nikash Bhardwaj; Ademi Adeniji; Vincent Liu; Michael Cho; Jiafei Duan.

**Contribution / composition:** Pairs egocentric/wrist observations with optical whole-body capture for locomotion, transport and manipulation; benchmarks reconstruction, foot estimation and retargeting.

**Mechanism:** Synchronizes head/wrist cameras and inertial sensors with optical body/object capture. Fits SMPL-X to marker trajectories with participant-consistent shape, reconstructs calibrated scene geometry, and fuses vision-estimated MANO articulation with optical wrists. Per-stream validity masks distinguish observed optical motion from estimated fingers and missing measurements.

**Input contract:** Egocentric observations for body reconstruction; captured body trajectories for humanoid retargeting. Dataset contains locomotion, manipulation and longer activities rather than being a text-conditioned generator.

**Data and split:** Contains over 200 hours from fourteen participants. Hand fine-tuning uses 34.9 minutes and a 9.2-minute test set with participant membership shared with the dataset protocol; exact overall split counts/proportions are not specified in the inspected main text. Reconstruction baselines are evaluated pretrained, without RoboMoCap fine-tuning.

**Evaluation metrics:** Local/world/sequence/Procrustes MPJPE, MPJRE, velocity/acceleration error and jerk; sole-marker contact F1, footprint/step error, skating and penetration. Retargeting reports body fidelity, joint-limit and collision measures.

**Evaluation checked:** Benchmarks egocentric body reconstruction, foot placement/contact and robot retargeting. Dataset analyses quantify heading-travel disagreement and support transitions, showing why headset direction alone is insufficient for lower-body motion.

**Full-text source:** https://arxiv.org/pdf/2611.10994v1

**Reading status:** full_text_checked

**Inspected version:** 2611.10994v1

**Full-text SHA256:** beceb0117ce7125a88a579adad4fa569f56653f3f92f56aa124d13adefa6662c

**Source locator:** Sections 3–4.5; Sections 5.1–5.3; Tables 4–6 and Figure 4; annotation distinction in Section 4.4.

**Scope / curator boundary:** Finger articulation is vision-derived, not optical hand ground truth. Optical marker fit and coordinate alignment do not certify contact forces. Retargeting geometry metrics are distinct from successful physical robot execution or accepted compositional training samples.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2611.10994); checked 2026-11-19.

<a id="finemotion"></a>
## FineMotion: A Dataset and Benchmark with both Spatial and Temporal Annotation for Fine-grained Motion Generation and Editing

**finemotion · 2025 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2507.19850) · [Evidence](https://arxiv.org/pdf/2507.19850v1) · Citekey: `finemotion2025`

**Authors of cited version:** Bizhu Wu; Jinheng Xie; Meidan Ding; Zhe Kong; Jianfeng Ren; Ruibin Bai; Rong Qu; Linlin Shen.

**Contribution / composition:** Adds aligned body-part descriptions for motion snippets and complete sequences, supporting fine-grained generation and spatial/temporal editing.

**Mechanism:** Produces fine-grained motion language through temporal segmentation, PoseFix-based pose-pair change descriptions, human correction of a small subset, and Gemini conversion of ordered snippet descriptions into coherent body-part-motion paragraphs. FineMotion contains 21,346 human and 420,968 automatic snippet descriptions plus whole-motion paragraphs. Baseline MDM, T2M-GPT and MoMask are adapted to coarse and detailed text using T5-Base to avoid CLIP truncation.

**Input contract:** Coarse text optionally accompanied by temporally aligned detailed snippet descriptions or paragraphs. Temporal editing replaces descriptions and regenerates corresponding motion; the dataset supplies language rather than new independent motion capture.

**Data and split:** Inherits HumanML3D sequence partitions: 80 percent training, five percent validation and 15 percent test. Human-annotated snippets cover roughly five percent of motions. The paper does not declare a separately held-out body-part-combination or actor protocol.

**Evaluation metrics:** FID assesses motion distributions; top-1/2/3 R-precision and MM-Dist assess semantic alignment; diversity and multimodality assess variation. Annotation validity and human-versus-automatic detailed-text settings are compared separately.

**Evaluation checked:** Tables test coarse-only and coarse-plus-detail training/testing, different automatic/human descriptions and model families. Editing examples demonstrate zero-shot temporal changes, while supplementary experiments analyze annotation granularity and component choices.

**Full-text source:** https://arxiv.org/pdf/2507.19850v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2507.19850v1

**Full-text SHA256:** 9dc01d569ec9d16927d897d62dec75787262807871d20d26fe4c586fa17ce8b6

**Source locator:** Sections 3.1.1–3.1.3, 3.2, 4.1–4.5; Table 2; Supplement 16 limitations.

**Scope / curator boundary:** Automatically inferred language can retain pose-estimation/model biases despite stronger grounding than caption-only expansion. Temporal editing is easier than spatial editing under this representation, explicitly left for future work. Dataset enrichment does not establish independent new actions or physically valid object interactions.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2507.19850); checked 2026-11-19.

<a id="motionmillion"></a>
## Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data

**motionmillion · 2025 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2507.07095) · [Evidence](https://arxiv.org/pdf/2507.07095v1) · Citekey: `motionmillion2025`

**Authors of cited version:** Ke Fan; Shunlin Lu; Minyue Dai; Runyi Yu; Lixing Xiao; Zhiyang Dou; Junting Dong; Lizhuang Ma; Jingbo Wang.

**Contribution / composition:** MotionMillion builds web-video motion/text data through shot detection, person tracking, confidence/transition filtering, world-grounded human reconstruction, and jitter filtering. GPT-4o captions are rewritten by Llama for linguistic diversity. A wavelet-assisted finite-scalar-quantization tokenizer feeds scalable text-conditioned autoregressive Transformers.

**Mechanism:** MotionMillion builds web-video motion/text data through shot detection, person tracking, confidence/transition filtering, world-grounded human reconstruction, and jitter filtering. GPT-4o captions are rewritten by Llama for linguistic diversity. A wavelet-assisted finite-scalar-quantization tokenizer feeds scalable text-conditioned autoregressive Transformers.

**Input contract:** Text descriptions condition body-motion generation, with T5-XL language features and discrete motion tokens. The corpus contains reconstructed human motion and expanded captions, not measured object trajectories or contact forces. Caption rewrites share the same motion identity.

**Data and split:** The paper reports about two million motions and over 2,000 hours; training and evaluation sets are used for reconstruction and generation, but exact split proportions and video/performer grouping are not reported in the inspected setup. HumanML3D and Motion-X are also used for cross-dataset reconstruction.

**Evaluation metrics:** MPJPE measures motion-tokenizer reconstruction; mean/max acceleration and jerk quantify temporal roughness. FID and R@1/2/3 assess generation distribution and text retrieval; MotionMillion-Eval uses human text-alignment, smoothness, and plausibility scores on 126 prompts. These metrics have differing supervision assumptions.

**Evaluation checked:** Section 5 tests tokenizer transfer across MotionUnion-related data, wavelet ablation, model scaling, and long text-conditioned sequences. Tables 2–3 separate reconstruction accuracy and smoothing, while Table 4 compares model sizes on MotionMillion; additional criteria appear in the supplement.

**Full-text source:** https://arxiv.org/pdf/2507.07095v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2507.07095v1 [cs.CV] 9 Jul 2025

**Full-text SHA256:** 23f15f7ae6f951c872a554fa8666c3f9388c7d956e8862f3d453799217a70908

**Source locator:** §3 data pipeline, §§4.2–4.3 (wavelet FSQ/scaled Transformer), §§5.1–5.3 and Tables 2–4; appendix §§8–9 distribution and scoring criteria.

**Scope / curator boundary:** Web-video reconstruction and automatic captions introduce pseudo-label and semantic errors. More captions do not create independent captured motions. Filtering by smoothness can suppress legitimate dynamics, and unreported source-level partitioning limits leakage assessment. No object-conditioned manipulation guarantee is established.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2507.07095); checked 2026-11-19.

<a id="vimogen-mbench"></a>
## The Quest for Generalizable Motion Generation: Data, Model, and Evaluation

**vimogen-mbench · 2025 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2510.26794) · [Evidence](https://arxiv.org/pdf/2510.26794v2) · Citekey: `vimogenmbench2026`

**Authors of cited version:** Jing Lin; Ruisi Wang; Junzhe Lu; Ziqi Huang; Guorui Song; Ailing Zeng; Xian Liu; Chen Wei; Wanqi Yin; Qingping Sun; Zhongang Cai; Lei Yang; Ziwei Liu.

**Contribution / composition:** Combines mocap, web-derived and video-generated motion in ViMoGen-228K; introduces ViMoGen and hierarchical MBench evaluation.

**Mechanism:** Builds ViMoGen-228K from filtered optical mocap, recovered in-the-wild video motion and synthetic video motion. A diffusion transformer shares parameters between text-to-motion and motion-to-motion branches; an adaptive selector uses video-derived initialization when appropriate. A distilled light variant reduces dependence on expensive video inference.

**Input contract:** Text prompts plus optionally a noisy video-recovered motion prior. MBench renders generated bodies to evaluate rare semantics and condition following with a vision-language judge alongside geometric/temporal measurements.

**Data and split:** Long mocap is segmented into nonoverlapping five-second clips; seventeen selected mocap datasets contribute approximately 172k clips. MBench uses curated test prompt suites and quality samples rather than a simple percentage holdout. An overall 228K train/test ratio is not reported.

**Evaluation metrics:** Nine dimensions: generalizability, motion-condition consistency, jitter, dynamic degree, foot floating/sliding, ground/body penetration and pose quality. Appendix F also uses standard HumanML3D R-Precision/FID/MM-Distance/diversity metrics.

**Evaluation checked:** Tables 2–7 compare generators, branch selection and dual-branch training. Human judgments validate dimension-wise alignment. Main results improve semantic scores but do not dominate all geometric metrics; table values expose those tradeoffs.

**Full-text source:** https://arxiv.org/pdf/2510.26794v2

**Reading status:** full_text_checked

**Inspected version:** 2510.26794v2

**Full-text SHA256:** 0715de219d4733b155761cd482b4bdb85b1259540415693eb7617339137ace78

**Source locator:** Sections 2–5, Tables 1–7; Appendices C (MBench), D (data), F (HumanML3D); limitations paragraph.

**Scope / curator boundary:** Single-person only; distorted video priors can survive refinement. Curated rare prompts are not proof of training-corpus absence in proprietary video models. VLM semantic scores and human correlations do not replace physical task execution.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2510.26794); checked 2026-11-19.

<a id="instructmotion"></a>
## Learning Generalizable Human Motion Generator with Reinforcement Learning

**instructmotion · 2024 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2405.15541) · [Evidence](https://arxiv.org/pdf/2405.15541v1) · Citekey: `instructmotion2024`

**Authors of cited version:** Yunyao Mao; Xiaoyang Liu; Wengang Zhou; Zhenbo Lu; Houqiang Li.

**Contribution / composition:** Uses reinforcement learning and contrastive text-motion rewards on paired data and synthetic text-only prompts to improve generalization.

**Mechanism:** Fine-tunes a supervised T2M-GPT motion-token generator with PPO, treating autoregressive token production as a Markov decision process. Rewards use pretrained contrastive text/motion encoders: generated-motion distance to text, and optionally to paired ground-truth motion. An LLM decomposes existing captions into meta motions, recombines them into novel descriptions and uses human filtering to remove implausible combinations. Synthetic prompts need no paired motion for RL fine-tuning.

**Input contract:** A textual motion description; optional paired motion contributes an additional reward during training. This is reward-based generator adaptation, not human preference annotation or physical environment execution.

**Data and split:** Benchmarks evaluate HumanML3D and KIT-ML test sets following their standard evaluation protocol. Synthetic descriptions have separate training/test prompt subsets, but the reviewed text does not state numerical partition proportions or a constituent-skill exclusion rule.

**Evaluation metrics:** Top-1/2/3 R-precision, FID, MM-Dist and diversity use pretrained feature spaces. Human evaluations rank motions on paired-test, unpaired-training and unpaired-test prompts; quantitative tables repeat 20 evaluations for confidence intervals.

**Evaluation checked:** Compares T2M-GPT baseline and MoMask, studies synthetic-data scaling and reward components, and shows qualitative novel-description examples. These tests probe transfer to recombined language beyond paired supervision.

**Full-text source:** https://arxiv.org/pdf/2405.15541v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2405.15541v1

**Full-text SHA256:** c3d06c9d0c49b9c18a2e9a40659cc963c6eaeb783da6203a1182bb7347f26cae

**Source locator:** Sections 3.1, 4.1–4.3, 5 and 6; Tables 1–3; Figures 3 and 5.

**Scope / curator boundary:** Reward models themselves are trained on limited paired data and prioritize coarse semantic alignment over fine motion. Optimizing learned alignment can exploit evaluator biases. Synthetic prompt generalization does not by itself establish unseen physical skills, object-state consistency, or independent contact-quality improvement.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2405.15541); checked 2026-11-19.

<a id="parahome"></a>
## ParaHome: Parameterizing Everyday Home Activities Towards 3D Generative Modeling of Human-Object Interactions

**parahome · 2024 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2401.10232) · [Evidence](https://arxiv.org/pdf/2401.10232v2) · Citekey: `parahome2025`

**Authors of cited version:** Jeonghwan Kim; Jisoo Kim; Jeonghyeon Na; Hanbyul Joo.

**Contribution / composition:** Captures full-body, hand, multi-object and articulated-object activity in a home setting, including sequential and concurrent manipulations.

**Mechanism:** New capture system aligns multicamera object tracking with IMU body/glove motion and post-processing. Baselines study text-conditioned body/hand synthesis and transformer object-state-conditioned body synthesis.

**Input contract:** Capture combines multicamera object markers with body IMUs/gloves and calibrated alignment. Generation studies use text for body/hand output or complete future object-state sequences plus initial person-object relation for body motion.

**Data and split:** Studio-home recordings provide continuous activities, not independent synthetic skill combinations. Generation compares ParaHome, HumanML3D and evenly mixed training data against unseen mixed-data motions. Exact train/test proportions and participant-grouping units are not specified in the inspected main protocol.

**Evaluation metrics:** Camera/object marker coverage, reprojection/alignment errors and temporal jerk; text generation R-Precision, multimodal distance, FID, diversity/multimodality. Object-guided synthesis reports root-centered joints/wrists, global root/joint errors and foot skating.

**Evaluation checked:** Tables 1–3 separate capture-system validation from learned generation experiments. Mixed-data training and latent interpolation demonstrate body/hand representation compatibility; object-state encoder experiments measure how temporal/spatial cues help reconstruct corresponding human movement.

**Full-text source:** https://arxiv.org/pdf/2401.10232v2

**Reading status:** full_text_checked

**Inspected version:** 2401.10232v2

**Full-text SHA256:** 4a0ded5d597194826cd7ff92125582bf26f87feba74f52e22cd2c527e51ea0fa

**Source locator:** Sections 3–4 (capture/validation), 5.1–5.2 and Tables 1–3; Section 6 limitations.

**Scope / curator boundary:** Single home setup, artificial markers and restricted objects limit transfer. Future object trajectories are a stronger condition than initial-state generation. Interpolated styles do not demonstrate robust unseen skill composition; paper capture totals differ between 207/208 and should retain source-specific wording.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2401.10232); checked 2026-11-19.

<a id="motionx"></a>
## Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset

**motionx · 2023 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2307.00818) · [Evidence](https://arxiv.org/pdf/2307.00818v2) · Citekey: `motionx2024`

**Authors of cited version:** Jing Lin; Ailing Zeng; Shunlin Lu; Yuanhao Cai; Ruimao Zhang; Haoqian Wang; Lei Zhang.

**Contribution / composition:** Motion-X constructs expressive SMPL-X body/hand/face motion with a progressive whole-body annotation pipeline and semantic plus pose text. The method combines 2D keypoints, learning-based fitting, and text annotation, then evaluates whether the resulting corpus improves text-driven motion generation and whole-body mesh recovery.

**Mechanism:** Motion-X constructs expressive SMPL-X body/hand/face motion with a progressive whole-body annotation pipeline and semantic plus pose text. The method combines 2D keypoints, learning-based fitting, and text annotation, then evaluates whether the resulting corpus improves text-driven motion generation and whole-body mesh recovery.

**Input contract:** The dataset supplies RGB observations, pseudo/real fitted whole-body parameters, semantic sequence text, and detailed body/face descriptions. Text-motion benchmarks condition generation on captions; this is not inherently a human-object interaction dataset with tracked movable object states.

**Data and split:** Motion-X is randomly divided into 80% training, 5% validation, and 15% test. The reported unit is dataset motions; no subject- or original-video-disjoint guarantee is stated. Additional annotation-pipeline evaluation uses COCO-WholeBody and EHF, while downstream reconstruction tests EHF/AGORA.

**Evaluation metrics:** 2D AP/AR assess keypoints; MPVPE, PA-MPVPE, and PA-MPJPE assess 3D fitting. FID, R-Precision, MM-Distance, Diversity, and Multimodality assess motion generation via learned embeddings. Twenty runs are used except five for Multimodality.

**Evaluation checked:** Tables 3–4 evaluate annotation quality and generation baselines; later tables compare HumanML3D training, body/face text additions, and downstream mesh recovery. MLD, MDM, MotionDiffuse, and T2M-GPT provide distinct benchmark baselines, not all diffusion architectures.

**Full-text source:** https://arxiv.org/pdf/2307.00818v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2307.00818v2 [cs.CV] 26 Jan 2024

**Full-text SHA256:** d2567d3814e272336bc481a11b61dcc2e7e704dbe1d38c836eafb56896f5ed94

**Source locator:** §3 annotation pipeline, §4 dataset, §§5.1–5.3, Tables 3–7; §5.2 explicitly states 80/5/15 and repetition protocol; appendix metric definitions.

**Scope / curator boundary:** Automatic fits are pseudo-ground truth and can retain occlusion/depth errors. Random motion partitions do not independently demonstrate source-actor generalization. Expressive hand/face coverage and feature improvements do not establish object contact accuracy or physically executable manipulation.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2307.00818); checked 2026-11-19.

<a id="best-automated-metric"></a>
## What is the Best Automated Metric for Text to Motion Generation?

**best-automated-metric · 2023 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2309.10248) · [Evidence](https://arxiv.org/pdf/2309.10248v1) · Citekey: `bestautomatedmetric2023`

**Authors of cited version:** Jordan Voas; Yili Wang; Qixing Huang; Raymond Mooney.

**Contribution / composition:** Studies alignment between automated metrics and human judgments, separating sample-level and average model-level correlation; introduces MoBERT.

**Mechanism:** Collects human naturalness and prompt-faithfulness ratings for motions from several text-to-motion systems, then tests which automated scores correlate with people at sample and model levels. Introduces MoBERT, a learned reference-free motion-language evaluator; also investigates coordinate errors with root/component scaling rather than assuming embedding metrics are sufficient.

**Input contract:** Generated motion and its text prompt; reference trajectories are required by coordinate-error alternatives but not MoBERT. The contribution is evaluation methodology, not a compositional generator.

**Data and split:** Samples 400 HumanML3D test prompts, producing 2,000 motions across five sources including real motion; filtering retains 1,400 rated pairs from 280 prompts. Human-score regression uses ten-fold cross-validation, fitting 90% of annotated samples and predicting 10%; source-actor-disjoint grouping is not reported.

**Evaluation metrics:** Sample/model-level Pearson human-score correlations, inter-rater Krippendorff alpha, coordinate AE/AVE variants, FID, R-Precision, multimodal distance and MoBERT-based predictions. FID correlation is computed at model level only.

**Evaluation checked:** Each accepted pair has three ratings on naturalness and faithfulness. Qualification, gold questions and viewing-time checks filter annotators. Results compare correlations and caution that model ranking and individual-sample evaluation can behave differently.

**Full-text source:** https://arxiv.org/pdf/2309.10248v1

**Reading status:** full_text_checked

**Inspected version:** 2309.10248v1

**Full-text SHA256:** bc2bf1f607d922335c6382741361c0c293e51fba9b1cb54cd5f12974b1336b8c

**Source locator:** Sections 3.1–3.3, 4.1–4.2 (including Model Evaluation Process: ten-fold cross-validation), 5; Section 6.1 Limitations; Table 1 and result figures.

**Scope / curator boundary:** Human labels cover a small fraction of HumanML3D and limited generators. Learned-evaluator behavior on new domains needs renewed human validation; high correlation within this study does not establish object contact, dynamics or task-order correctness.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2309.10248); checked 2026-11-19.

<a id="behave"></a>
## BEHAVE: Dataset and Method for Tracking Human Object Interactions

**behave · 2022 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2204.06950) · [Evidence](https://arxiv.org/pdf/2204.06950v1) · Citekey: `behave2022`

**Authors of cited version:** Bharat Lal Bhatnagar; Xianghui Xie; Ilya A. Petrov; Cristian Sminchisescu; Christian Theobalt; Gerard Pons-Moll.

**Contribution / composition:** Multi-view RGB-D body-object interaction data with body/object fits and contacts across everyday objects and locations.

**Mechanism:** Introduces RGB-D recordings and fitted body/object/contact annotations for natural full-body object interaction. The method jointly registers SMPL and a prescanned rigid object to multi-view depth observations. Neural predictions provide human-surface correspondence, object orientation and explicit contact correspondences, which enter optimization to align body/object meshes rather than fitting them independently. The released fits are pseudo-ground truth from this capture/optimization pipeline.

**Input contract:** Multi-view RGB-D, human/object segmentation and known rigid object mesh; tracking estimates human pose/shape, object pose and contact. This is observation-conditioned reconstruction, not text-driven motion generation.

**Data and split:** Experiments compare reconstruction on the dataset and its reference annotations. The reviewed main paper does not state explicit train/test sequence counts, proportions or actor/object-disjoint partition membership; later papers’ official splits should not be retroactively inferred here.

**Evaluation metrics:** Human SMPL vertex-to-vertex error and object vertex-to-vertex error are reported in centimeters. Qualitative contact plausibility supplements geometric error; tables ablate orientation and contact terms and compare body registration.

**Evaluation checked:** Compares PHOSA adapted to its input setup, IPNet and LoopReg, then tests learned object orientation and contact fitting. The authors note that contact removal can produce conspicuous floating despite small differences in aggregate vertex error.

**Full-text source:** https://arxiv.org/pdf/2204.06950v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2204.06950v1

**Full-text SHA256:** a36f6129acfc3fd1b00a1b807537af619e59b8ab30ffa33587ff39e777b3ba7c

**Source locator:** Sections 3, 4.1–4.4 and 5.1–5.4; Tables 1–3; Figures 3–5.

**Scope / curator boundary:** Known object geometry, RGB-D acquisition and fitted supervision constrain applicability. Occlusion and noisy point clouds remain relevant; contact annotations are not measured force or friction labels. The dataset supports HOI studies but does not itself demonstrate generative composition, task execution or continuous collision-free motion.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2204.06950); checked 2026-11-19.

<a id="humanml3d"></a>
## Generating Diverse and Natural 3D Human Motions From Text

**humanml3d · 2022 · Datasets & compositional evaluation · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf) · Citekey: `humanml3d2022`

**Authors of cited version:** Guo, Chuan; Zou, Shihao; Zuo, Xinxin; Wang, Sen; Ji, Wei; Li, Xingyu; Cheng, Li.

**Contribution / composition:** Introduces HumanML3D and a stochastic text-to-motion baseline.

**Mechanism:** Samples duration from text, then generates motion snippets with a temporal VAE.

**Input contract:** Natural-language description and sampled output duration. A text-conditioned temporal VAE predicts short movement snippet codes, whose decoder reconstructs continuous joint motion; curriculum training progressively lengthens predicted sequences.

**Data and split:** HumanML3D combines 14,616 motions and 44,970 descriptions from AMASS/HumanAct12. Both HumanML3D and KIT-ML use 0.8/0.15/0.05 training/test/validation partitions, with mirrored motion and left/right caption augmentation. These sequence partitions do not establish cross-dataset person deduplication or held-out action combinations.

**Evaluation metrics:** Contrastively trained text/motion embeddings provide R-Precision and multimodal distance; FID measures distribution similarity, diversity spans generated motions and multimodality compares different outputs per caption. Human preference complements these learned-feature measures.

**Evaluation checked:** Section 5 compares deterministic language-to-motion baselines with adapted stochastic generators. Ablations examine movement codes, length modeling and curriculum choices. The dataset expands semantic coverage and provides a common evaluation representation; its real-motion statistics are reference values, not model successes. Mirrored annotations are derived observations rather than independent source recordings.

**Full-text source:** https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf

**Reading status:** full_text_checked

**Inspected version:** Proceedings/author PDF as retrieved 2026-11-19; no printed own-paper arXiv version found.

**Full-text SHA256:** 5b80ce5d73992bec6736dc62e622db15da50394c49ccf433d6bc7a3c90a491ed

**Source locator:** Sections 3–4 (model/data), Section 5 and Table 1; Section 5.1.1 evaluation metrics and baseline tables.

**Scope / curator boundary:** One-to-many captions and evaluator training bias complicate ranking. Shared units/representation alone do not provide scene geometry, object trajectories, compositional labels or physically valid contacts. Future motion is generated, while duration is separately sampled/provided.

**Composition axes:** data.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2022/html/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.html); checked 2026-11-19.

<a id="intercap"></a>
## InterCap: Joint Markerless 3D Tracking of Humans and Objects in Interaction

**intercap · 2022 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2209.12354) · [Evidence](https://arxiv.org/pdf/2209.12354v2) · Citekey: `intercap2022`

**Authors of cited version:** Yinghao Huang; Omid Tehari; Michael J. Black; Dimitrios Tzionas.

**Contribution / composition:** InterCap estimates jointly moving SMPL-X humans and rigid objects from synchronized multiview RGB-D observations. Segmentation, detected joints, object pose initialization, and temporally coupled optimization combine depth fitting, pose priors, contact encouragement, and collision constraints to reconstruct captured interactions without optical body markers.

**Mechanism:** InterCap estimates jointly moving SMPL-X humans and rigid objects from synchronized multiview RGB-D observations. Segmentation, detected joints, object pose initialization, and temporally coupled optimization combine depth fitting, pose priors, contact encouragement, and collision constraints to reconstruct captured interactions without optical body markers.

**Input contract:** Multiple calibrated RGB-D streams and known scanned object geometry. The method reconstructs observed interaction rather than generating new motion from text. Fitted body/object trajectories and proximity-derived contact are dataset outputs with their own reconstruction uncertainty.

**Data and split:** The capture dataset contains multiple subjects and everyday object interactions; the reconstruction method is evaluated on captured sequences, not a learned text-generation split. A conventional training/validation/test percentage is not applicable to its main optimization experiment and is not reported as a generation benchmark.

**Evaluation metrics:** Body/object vertex-to-segmented-point-cloud distances quantify observation fit. Mean penetration depth characterizes reconstructed contact frames; contact maps threshold closest human-object distances at 4.5 mm. Per-frame comparisons with the segmented depth observations assess fitting accuracy, separately from qualitative render inspection; no independent full-body ground-truth trajectory is assumed.

**Evaluation checked:** Section 5 analyzes contact heatmaps, reconstruction errors, object/human alignment, and mesh penetration. Real data average vertex-to-cloud errors are 20.29 mm for bodies and 18.50 mm for objects; these are sensor-fit distances, not independent full-surface ground-truth errors.

**Full-text source:** https://arxiv.org/pdf/2209.12354v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2209.12354v2 [cs.CV] 1 Oct 2022

**Full-text SHA256:** f66ed1c0eef06977f7d9b414939e10c500cc85ee6fcff1a83c07b92e62dcaebe

**Source locator:** §3 InterCap optimization, §4 dataset/capture, §5 experiments (contact heatmaps, mesh penetration, fitting accuracy); §§3.3–3.4 depth fitting and manually annotated contact constraints.

**Scope / curator boundary:** Occlusion, depth noise, segmentation, and object initialization limit accuracy. Contact is inferred from fitted geometry and should not be treated as force sensing. Markerless capture improves accessibility but cannot establish exact dense contact or any text-conditioned compositional generation capability.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2209.12354); checked 2026-11-19.

<a id="mocapact"></a>
## MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control

**mocapact · 2022 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2208.07363) · [Evidence](https://arxiv.org/pdf/2208.07363v3) · Citekey: `mocapact2023`

**Authors of cited version:** Nolan Wagener; Andrey Kolobov; Felipe Vieira Frujeri; Ricky Loynd; Ching-An Cheng; Matthew Hausknecht.

**Contribution / composition:** Provides a multi-task resource for simulated humanoid control and reusable motion-capture skills.

**Mechanism:** Trains PPO experts to track overlapping mocap snippets in dm_control, then releases noisy expert rollouts including states, actions, reference poses, rewards and value/advantage estimates. Offline distillation learns a single hierarchical multi-clip policy; a separate autoregressive GPT predicts actions from motion history to continue physically simulated movement.

**Input contract:** For tracking, humanoid proprioception and a short future mocap reference. Downstream high-level control uses the learned motor embedding; GPT continuation receives a historical state/action prompt rather than future reference.

**Data and split:** 836 source clips produce 2,589 overlapping four-to-six-second snippets. Generalization experiments hold out 10% of source clips and train on 90%, avoiding merely holding out overlapping snippet frames. GPT also evaluates held-out prompts; exact prompt counts are not restated.

**Evaluation metrics:** Normalized tracking reward and episode length, per-joint angle error, downstream task returns and continuation duration. Large release contains 67 million transitions; small release 5.5 million, reflecting simulator rollouts rather than fresh human captures.

**Evaluation checked:** Compares behavioral cloning with clip-, advantage- and reward-weighted regression. Applications test multi-clip tracking, high-level transfer and stable motion completion in simulation. Expert failure examples include highly dynamic clips that are only partially reproduced.

**Full-text source:** https://arxiv.org/pdf/2208.07363v3

**Reading status:** full_text_checked

**Inspected version:** 2208.07363v3

**Full-text SHA256:** b6070a10696f581953d72d77ec9d7b02c1a3b767c30f2fb9a4303d8230542db6

**Source locator:** Sections 4.1–4.2, 5.1–5.2; Tables 1–4; Figure 6 (held-out clips); Appendix C.

**Scope / curator boundary:** Source artifacts and tracker limitations transfer into rollout quality. Simulated control supervision is not a human-object interaction corpus, language-compositional generalization benchmark or real-humanoid deployment result.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2208.07363); checked 2026-11-19.

<a id="babel"></a>
## BABEL: Bodies, Action and Behavior with English Labels

**babel · 2021 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2106.09696) · [Evidence](https://arxiv.org/pdf/2106.09696v2) · Citekey: `babel2021`

**Authors of cited version:** Abhinanda R. Punnakkal; Arjun Chandrasekaran; Nikos Athanasiou; Alejandra Quiros-Ramirez; Michael J. Black.

**Contribution / composition:** Adds sequence and temporally localized action language to AMASS, supporting action understanding and temporal composition.

**Mechanism:** Adds sequence-level and temporally localized English action labels to AMASS motion. Annotators identify all simultaneous actions and label transitions; raw descriptions are embedded with Word2Vec, clustered and manually organized into 260 action categories, allowing multiple category memberships. The paper analyzes co-occurrence and temporal transitions and benchmarks skeleton-based action recognition using an adapted 2s-AGCN joint stream.

**Input contract:** Body motion is the input to recognition; language/action intervals are annotations. Transition graphs describe observed category statistics rather than an evaluated continuous generative policy.

**Data and split:** Original recognition study randomly partitions 13,220 source sequences into 60 percent train, 20 percent validation and 20 percent test. Evaluates 60- and 120-category subsets; action segments are further chunked into five-second sequences. Split is sequence-level, not claimed actor-disjoint.

**Evaluation metrics:** Top-1 and Top-5 recognition accuracy; Top-1-norm averages per-category accuracy to expose long-tail bias. Descriptive analysis counts simultaneous-action pairs and temporally adjacent transitions; these counts are not generation-quality scores.

**Evaluation checked:** Compares standard cross-entropy and class-balanced focal-loss training. Reports substantial performance degradation when expanding categories, highlighting the challenge of rare actions. Examples and random walks illustrate plausible action ordering, not verified generated body trajectories.

**Full-text source:** https://arxiv.org/pdf/2106.09696v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2106.09696v2

**Full-text SHA256:** c1b17fce70bbcaae955e92d91d17c89d5581971446ffff6d4be0ce595910574c

**Source locator:** Sections 3.1–3.4, 4.1–4.2 and 5; Tables 2–3; BABEL action recognition splits and Metrics paragraphs.

**Scope / curator boundary:** Labels derive from annotator interpretation of body-only captures; some object/social semantics lack tracked corresponding entities. Long-tail categories and ambiguous boundaries complicate learning. Overlapping actions and source recordings require ancestry-aware evaluation before claiming unseen combinations or independent cross-dataset composition.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2106.09696); checked 2026-11-19.

<a id="grab"></a>
## GRAB: A Dataset of Whole-Body Human Grasping of Objects

**grab · 2020 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2008.11200) · [Evidence](https://arxiv.org/pdf/2008.11200v1) · Citekey: `grab2020`

**Authors of cited version:** Omid Taheri; Nima Ghorbani; Michael J. Black; Dimitrios Tzionas.

**Contribution / composition:** GRAB captures whole-body interaction with 51 objects using optical markers and individualized SMPL-X fitting. Proximity and mesh intersection analysis derive detailed body-object contact. GrabNet separately learns a coarse conditional VAE plus refinement network to synthesize right-hand grasps from object geometry.

**Mechanism:** GRAB captures whole-body interaction with 51 objects using optical markers and individualized SMPL-X fitting. Proximity and mesh intersection analysis derive detailed body-object contact. GrabNet separately learns a coarse conditional VAE plus refinement network to synthesize right-hand grasps from object geometry.

**Input contract:** Captured observations supply body, finger, face, and rigid object trajectories; GrabNet receives object shape/geometry to predict a hand grasp. Static grasp synthesis is distinct from generating a complete body/object manipulation sequence from text and initial state.

**Data and split:** GrabNet holds out four validation and six test objects, leaving 41 for training; supplementary data counts are roughly 320k/31k/65k training/validation/test grasp samples. These are frames/grasps, not independent motion sequences. GRAB itself contains 1,334 sequences and approximately 1.62 million frames.

**Evaluation metrics:** Closest-reference vertex distance measures grasp resemblance; contact comparisons assess similarity of contact patterns; AMT ratings score realism from one to five. Capture analyses measure contact prevalence and mesh penetration. MoSh++ synthetic fitting evaluation has separate subject/pose partitions.

**Evaluation checked:** Table 2 evaluates six unseen test objects, comparing generated and recorded grasp ratings and nearest-reference geometry. Contact heatmaps and intent-specific statistics characterize use/pass/lift/off-hand interactions. Synthetic model-fitting tests should remain separate from GrabNet generalization results.

**Full-text source:** https://arxiv.org/pdf/2008.11200v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2008.11200v1 [cs.CV] 25 Aug 2020

**Full-text SHA256:** f571520fbaf585403a8a23679e977269e59b6c5e263c14835aea6abe85993ddb

**Source locator:** §3/Table 1 (capture/contact/statistics), §4/Table 2 (GrabNet), supplementary S.8–S.9 (object partitions/evaluation), S.10 (marker bias).

**Scope / curator boundary:** Studio markers can influence contact and conceal touch regions; mesh proximity is not measured force. GrabNet evaluates right hands, while dataset breadth includes more body parts. Grasp-frame counts cannot substitute for independent actors or full continuous interactions in downstream splitting.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2008.11200); checked 2026-11-19.

<a id="amass"></a>
## AMASS: Archive of Motion Capture as Surface Shapes

**amass · 2019 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/1904.03278) · [Evidence](https://arxiv.org/pdf/1904.03278v1) · Citekey: `amass2019`

**Authors of cited version:** Naureen Mahmood; Nima Ghorbani; Nikolaus F. Troje; Gerard Pons-Moll; Michael J. Black.

**Contribution / composition:** Unifies heterogeneous optical mocap collections through MoSh++ and a common parametric body surface representation.

**Mechanism:** Unifies optical mocap archives with MoSh++, optimizing a common SMPL-family body surface, shape and soft-tissue motion from heterogeneous marker sets. Improvements include explicit dynamics, hand articulation and missing-marker-dependent priors. Manual inspection corrects or excludes problematic recordings before a common parameterized release.

**Input contract:** Raw optical marker trajectories with marker identities and a parametric body model. This is a reconstruction/archive pipeline, not language-conditioned motion generation or explicit interaction annotation.

**Data and split:** Original release combines fifteen datasets, 346 subjects, 11,451 motions and 42 hours. SSM validation uses two subjects for shape-weight fitting and one held out. Pose calibration holds out 20% of motion files; initial 200 frames of remaining files fit weights and remaining frames validate.

**Evaluation metrics:** Mean scan-to-model surface distance in millimeters from 10,000 sampled scan points per frame; marker errors and comparisons across shape/dynamic settings. No ground-truth quantitative hand-articulation evaluation is available.

**Evaluation checked:** Synchronized 4D scans in SSM evaluate MoSh++ against MoSh, including marker-set and soft-tissue ablations. Archive-scale counts describe represented data, whereas SSM tests reconstruction accuracy; these are separate claims.

**Full-text source:** https://arxiv.org/pdf/1904.03278v1

**Reading status:** full_text_checked

**Inspected version:** 1904.03278v1

**Full-text SHA256:** 2390a1d295d7519cdefcbe970eaa19bf2a8944ff06d1ada9debe07bf68bc2f94

**Source locator:** Sections 3.1–3.3, 4.1–4.3; Section 5 and Table 1; SSM protocol and hand-evaluation caveat.

**Scope / curator boundary:** Common body representation does not add object trajectories, semantic action chains, trustworthy contact forces or independent train/test grouping for downstream tasks. Sparse hand markers and absent hand ground truth limit articulation accuracy claims; released-fit quality still varies by source.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/1904.03278); checked 2026-11-19.

<a id="kitml"></a>
## The KIT Motion-Language Dataset

**kitml · 2016 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/1607.03827) · [Evidence](https://arxiv.org/pdf/1607.03827v2) · Citekey: `kitml2018`

**Authors of cited version:** Matthias Plappert; Christian Mandery; Tamim Asfour.

**Contribution / composition:** Aggregates mocap in a capture-independent representation with crowdsourced natural-language descriptions.

**Mechanism:** Aggregates optical motion capture from KIT and CMU and converts it into the capture-independent Master Motor Map representation. A WebGL interface lets volunteers inspect animated motion and write English descriptions. Annotation selection starts with unannotated recordings, then uses language-model perplexity to prioritize unusual or inconsistent descriptions. Releases preserve original motion, converted motion, captions and provenance metadata with dated dataset versions.

**Input contract:** No single generative model is proposed. The resource pairs full-body motion recordings with sentence descriptions and links them to source-database identities for downstream motion-language research.

**Data and split:** The authors explicitly choose not to define a canonical train/validation/test split because researchers may use different subsets. October 2016 release contains 3,911 recordings from 111 subjects and 6,278 captions; downstream papers’ splits are separate choices.

**Evaluation metrics:** Dataset statistics include duration, vocabulary, annotation counts and participant distribution. Four-gram language-model perplexity measures annotation surprise for collection/quality control; it is not a motion-generation accuracy or semantic-composition metric.

**Evaluation checked:** Evaluates and documents the annotation workflow, motion-format conversion and dataset coverage rather than comparing synthesized motions under a fixed benchmark. Source metadata permits additional subject/capture information to be retrieved where available.

**Full-text source:** https://arxiv.org/pdf/1607.03827v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:1607.03827v2

**Full-text SHA256:** 4111d46dd6047f24f8caf7a3fc40806b6a38388a1e0e94623c23a634c5eaabed

**Source locator:** Sections III–IV; Section V.A Structure and V.B Content; Table I; perplexity definition and explicit no-split paragraph.

**Scope / curator boundary:** Coverage reflects original capture distributions and volunteer annotations, with differing detail, grammar and interpretation. Body-only motion does not supply tracked manipulated objects or scenes. A standardized motion representation enables reuse but does not guarantee compositional supervision, independent skill holdouts or physics labels.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/1607.03827); checked 2026-11-19.

<a id="maskadapt"></a>
## MaskAdapt: Learning Flexible Motion Adaptation via Mask-Invariant Prior for Physics-Based Characters

**maskadapt · 2026 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2603.29272) · [Evidence](https://arxiv.org/pdf/2603.29272v2) · Citekey: `maskadapt2026`

**Authors of cited version:** Soomin Park; Eunseong Lee; Kwang Bin Lee; Sung-Hee Lee.

**Contribution / composition:** MaskAdapt learns an adversarial base policy with observation masks and a mask-invariant regularizer, then trains a residual adaptation policy controlling selected parts. The base preserves non-adapted behavior while residual rewards teach new local motions or tracking, allowing dynamic changes of the controlled body region.

**Mechanism:** MaskAdapt learns an adversarial base policy with observation masks and a mask-invariant regularizer, then trains a residual adaptation policy controlling selected parts. The base preserves non-adapted behavior while residual rewards teach new local motions or tracking, allowing dynamic changes of the controlled body region.

**Input contract:** Proprioception, body-part masks, and task/reference signals; text-driven examples rely on a pretrained kinematic generator supplying partial trajectories. The simulated character has 22 bodies and 63 degrees of freedom, so this is embodied policy adaptation rather than unrestricted body-motion decoding.

**Data and split:** Base motions come from LAFAN1, composition clips from AMASS, and partial-tracking trajectories from a BABEL-trained generator. No percentage train/validation/test split is reported for a compositional dataset. Three specified composition cases and task-specific simulations form the principal evaluation.

**Evaluation metrics:** Normalized Shannon entropy of reference-frame visitation measures behavioral coverage, separately for adapted and preserved parts. Location/strike/heading success rates assess goals; tracking and pose errors assess partial imitation. These metrics are not equivalent to held-out semantic-combination accuracy.

**Evaluation checked:** Tables 1–2 compare AMP/base regularization and three composition cases; Table 3 compares goal tasks with AdaptNet/CML; Table 4 evaluates partial tracking. Composition collects 1,000 frames in ten parallel environments, with separate text-conditioned tracking trials and qualitative mask switches.

**Full-text source:** https://arxiv.org/pdf/2603.29272v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2603.29272v2 [cs.CV] 2 Apr 2026

**Full-text SHA256:** ae0d314ba1bca428feecae1407b2ff23f167840419fe90ef32a39bac71e7574c

**Source locator:** §3 base/residual policy and mask invariance; §§4.1–4.3, Tables 1–4 and Figures 5–8; conclusion limitations and supplementary task settings.

**Scope / curator boundary:** Conflicting commands on mechanically coupled parts can fail, such as different leg tasks. Partial tracking inherits the kinematic generator’s semantic errors. Evaluation in a particular simulator and selected reference combinations does not establish robust manipulation or real-hardware transfer.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2603.29272); checked 2026-11-19.

<a id="simdiff"></a>
## SimDiff: Simulator-constrained Diffusion Model for Physically Plausible Motion Generation

**simdiff · 2025 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2509.20927) · [Evidence](https://arxiv.org/pdf/2509.20927v1) · Citekey: `simdiff2025`

**Authors of cited version:** Akihisa Watanabe; Jiawei Ren; Li Siyao; Yichen Peng; Erwin Wu; Edgar Simo-Serra.

**Contribution / composition:** Conditions diffusion on environment coefficients and reports unseen combinations of environmental parameters.

**Mechanism:** Fine-tunes a diffusion generator using physically tracked motion and conditions it on simulator parameters. Physics projection is interpreted as guidance, motivating a learned denoiser that internalizes environment-dependent corrections instead of requiring simulator projection at each inference step. Tracking failures are filtered from the simulation-derived training corpus.

**Input contract:** Text plus explicit gravity and wind parameters; outputs skeletal motion. Environmental coefficients are supplied conditions, not inferred scene physics or semantic skill assignments.

**Data and split:** Uses converted HumanML3D motions. In standard gravity/no wind, 18,201 successfully tracked motions fine-tune the model. Diverse-environment training varies one parameter at a time across thirty conditions; evaluation composes simultaneously changed gravity/wind. A new source-clip percentage split is not reported.

**Evaluation metrics:** R-Precision, FID, multimodal distance and diversity; bone-based penetration, floating and sliding, with five-millimeter ground tolerance. Environment experiments evaluate adaptation/tracking and compare inference speed.

**Evaluation checked:** Sections 5.3–5.4 distinguish fixed-environment physical plausibility from unseen parameter-combination tests. Compares original MDM and physics-corrected baselines, with DDPM/DDIM variants and an A100 inference-speed analysis.

**Full-text source:** https://arxiv.org/pdf/2509.20927v1

**Reading status:** full_text_checked

**Inspected version:** 2509.20927v1

**Full-text SHA256:** 3cb189b97ced2face5f5d92fdf3d7f7da2da0800afe5162088daf4e020c8aaa2

**Source locator:** Sections 3–4; Sections 5.1–5.4, Tables 1–2 and Figure 4; Section 6 future work.

**Scope / curator boundary:** Composition concerns environmental factors, not novel human action semantics. Metrics operate on joints instead of full surfaces, and feasibility inherits the MetaMotivo controller/filter. Uneven terrain, richer environmental interactions and object contact are outside the demonstrated scope.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.20927); checked 2026-11-19.

<a id="closd"></a>
## CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control

**closd · 2024 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2410.03441) · [Evidence](https://arxiv.org/pdf/2410.03441v1) · Citekey: `closd2024`

**Authors of cited version:** Guy Tevet; Sigal Raab; Setareh Cohan; Daniele Reda; Zhengyi Luo; Xue Bin Peng; Amit H. Bermano; Michiel van de Panne.

**Contribution / composition:** Closes a feedback loop between an autoregressive text/target-conditioned diffusion planner and an RL tracker for task sequences.

**Mechanism:** Combines DiP, an autoregressive text/target-conditioned diffusion planner, with a universal PHC-style physics tracker. The tracker executes planned frames, then its actual simulated motion supplies the next planner prefix. Closed-loop PPO fine-tuning keeps the planner fixed and adapts the tracker across tasks. A high-level state machine switches text and target conditions when explicit task-success events occur; it is not learned open-ended task planning.

**Input contract:** Text plus the target location of a selected body joint; actual executed motion history closes the loop. Tasks include locomotion goal reaching, striking, sitting and getting up.

**Data and split:** DiP trains on HumanML3D and the tracker on AMASS. Text generation follows HumanML3D benchmark evaluation without a new declared proportional split. Task success uses 1,000 episodes per task with randomized placements; these are environment trials, not held-out motion-recording identities.

**Evaluation metrics:** Task-specific success rates; FID, R-precision, MM-Dist and diversity; physical proxies measure ground penetration, floating and skating. Runtime, generation FPS and plan-length/diffusion-step ablations assess efficiency.

**Evaluation checked:** Tables compare task-specific and multitask agents, open-loop execution, no fine-tuning and altered replanning lengths. Physics improves skating while feature-distribution scores can degrade relative to the unconstrained DiP planner.

**Full-text source:** https://arxiv.org/pdf/2410.03441v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2410.03441v1

**Full-text SHA256:** 84a64f6cae3b7c4ce9054b3d6735eda8c98dcb6577f0c64d38ba9a33eb0245f7

**Source locator:** Sections 4.1–4.4, 5.1–5.3 and 6; Tables 1–3; task success definitions and physics metric paragraph.

**Scope / curator boundary:** Demonstrated state-machine task sequences do not establish arbitrary task generalization or dexterous manipulation. A single lightweight tracker omits PHC’s full recovery machinery. Simulation success and selected-joint targets do not establish force-accurate human data or real-robot transfer.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.03441); checked 2026-11-19.

<a id="mhc"></a>
## Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots

**mhc · 2024 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2408.07295) · [Evidence](https://arxiv.org/pdf/2408.07295v4) · Citekey: `mhc2026`

**Authors of cited version:** Pranay Dugar; Aayam Shrestha; Fangzhou Yu; Bart van Marum; Alan Fern.

**Contribution / composition:** Masked Humanoid Controller learns one policy to track selectively masked motion directives while obeying locomotion commands. A staged curriculum, offset-aware future directives, motion/style rewards, perturbations, and dynamics randomization teach compatibility between whole-body mimicry, upper-body motion, standing, and joystick walking.

**Mechanism:** Masked Humanoid Controller learns one policy to track selectively masked motion directives while obeying locomotion commands. A staged curriculum, offset-aware future directives, motion/style rewards, perturbations, and dynamics randomization teach compatibility between whole-body mimicry, upper-body motion, standing, and joystick walking.

**Input contract:** Motion target trajectories with body-part masks, root velocity/turn commands, standing indicator, and robot proprioception. Outputs are joint PD setpoints for Digit. The policy combines control modalities; a natural-language generator is not part of the principal system.

**Data and split:** Uses 75 retargeted trajectories partitioned into setA (20), setB (20), and setC (35), with increasing difficulty and mixed AMASS/animation/optimized/video sources. Models trained on A, AB, and ABC are evaluated across sets; this is not a random percentage subject split.

**Evaluation metrics:** Mean End-Effector Position Error (EMEPE) measures specified limb positions relative to the torso; root drift measures global locomotion/standing error; failure percentage measures terminated episodes. Perturbation tests apply 50N/100N torso forces; hardware tests omit root error when global localization is unavailable.

**Evaluation checked:** Tables 2–5 compare walking/standing, offset-aware baselines, dataset scaling, and curriculum ablations. Full/partial mimicry follows each directive once, while locomotion episodes last ten seconds. Real Digit tests evaluate the 20 setA motions and demonstrate upper-body tracking with locomotion.

**Full-text source:** https://arxiv.org/pdf/2408.07295v4

**Reading status:** full_text_checked

**Inspected version:** arXiv:2408.07295v4 [cs.RO] 21 Apr 2026

**Full-text SHA256:** 984f5f01fcc4d79fb5b8a795b68e926e1fa37b4663dd9f95dbc3a38005836966

**Source locator:** Method sections Motion Directives/Curriculum/Reward Design; Motion Directive Dataset (20/20/35), Experimental Setup and Metrics, Tables 2–5; Real-World Experiments and conclusion.

**Scope / curator boundary:** The chosen motion corpus avoids the most aggressive behaviors and robot morphology restricts transfer. Inconsistent directives and limited mask patterns remain open issues. Real-world task demonstrations do not establish text-semantic composition or arbitrary object interaction.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2408.07295); checked 2026-11-19.

<a id="maskedmimic"></a>
## MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

**maskedmimic · 2024 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2409.14393) · [Evidence](https://arxiv.org/pdf/2409.14393v1) · Citekey: `maskedmimic2024`

**Authors of cited version:** Chen Tessler; Yunrong Guo; Ofir Nabati; Gal Chechik; Xue Bin Peng.

**Contribution / composition:** Unifies masked keyframes, objects, text and mixed descriptions as partial motion constraints for simulated character control.

**Mechanism:** First trains a fully constrained physics tracker, then distills it into a partially constrained controller through conditional variational motion inpainting. Randomly masked targets teach a learned prior to infer missing motion. One unified controller consumes heterogeneous goal tokens and combines sparse keyframes, language, objects and terrain without task-specific fine-tuning.

**Input contract:** Proprioception, optional partial joint targets, text embeddings, object bounding boxes and terrain; missing conditions are masked. Simple finite-state goal programs switch constraints to create longer behaviors.

**Data and split:** Filtered AMASS supplies motion, HumanML3D supplies language and object-interaction data supplies sitting conditions. Evaluates AMASS training/test partitions and held-out sitting objects. Exact aggregate partition proportions are not reported; held-out objects are distinct from held-out motion categories.

**Evaluation metrics:** Success rate, global MPJPE, observed-joint MPOJPE, path/orientation error and task-specific target errors. Full tracking fails if average joint deviation exceeds 0.5 meters in any frame.

**Evaluation checked:** Tables compare full-body/VR tracking, irregular terrain, path following and object interactions. Evaluations use the prior mean for precision, while latent sampling explores diversity. The same model handles all tested tasks, and finite-state constraints enable sequential demonstrations.

**Full-text source:** https://arxiv.org/pdf/2409.14393v1

**Reading status:** full_text_checked

**Inspected version:** 2409.14393v1

**Full-text SHA256:** 31e79502e14262b6c9cec33eb4531e4f2f611e9d277a7d243b6f61c5d714b37d

**Source locator:** Sections 5–6.5, Sections 7.1–7.3; Tables 1–6; goal-program description in task evaluation.

**Scope / curator boundary:** Goal engineering still specifies task sequences. Simulator success and sparse-target agreement do not certify arbitrary language-task composition, manipulable-object dynamics or real-robot transfer; performance depends on filtered reference coverage and teacher quality.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2409.14393); checked 2026-11-19.

<a id="diffmimic"></a>
## DiffMimic: Efficient Motion Mimicking with Differentiable Physics

**diffmimic · 2023 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2304.03274) · [Evidence](https://arxiv.org/pdf/2304.03274v2) · Citekey: `diffmimic2023`

**Authors of cited version:** Jiawei Ren; Cunjun Yu; Siwei Chen; Xiao Ma; Liang Pan; Ziwei Liu.

**Contribution / composition:** Uses differentiable physics for efficient reference motion imitation.

**Mechanism:** Optimizes a motion-imitation policy through differentiable Brax physics using analytical gradients propagated along simulated trajectories. The policy produces proportional-derivative joint targets from local body state and a reference phase. Demonstration replay replaces simulated states with corresponding reference states when deviation exceeds a threshold, helping avoid poor local minima and unstable long-horizon gradients. No learned world-model approximation is required.

**Input contract:** A reference motion clip and its phase, simulated humanoid state, and known physics configuration. This is clip-conditioned control/learning, not semantic composition or text-conditioned synthesis.

**Data and split:** Per-motion imitation setup has no dataset-level train/test recording split. Reference clips are inherited from AMP’s mixture of mocap and authored animation. Cyclic-motion policies train with four-second rollouts and are evaluated for 20-second continuation.

**Evaluation metrics:** Average root-relative Euclidean joint pose error in meters, aligned by dynamic time warping; sample count and wall time measure training efficiency. Evaluation includes completing 20-second cyclic rollouts without falling.

**Evaluation checked:** Compares DeepMimic, Spacetime Bound and AMP. Ablations compare full-horizon differentiation, short truncation, random demonstration replacement and threshold replay; per-frame errors expose behavior hidden by average imitation scores.

**Full-text source:** https://arxiv.org/pdf/2304.03274v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2304.03274v2

**Full-text SHA256:** 5565c8970cc201c47f7a4951a10433705c7ba298859099d713a86e23fcfc174d

**Source locator:** Sections 3.1–3.3, 4.1–4.4 and 5; Figures 2–4 and 6–8; Equation 4.1.

**Scope / curator boundary:** Differentiable contact can produce noisy gradients and local minima, and the simulator relaxes joint limits for smoother optimization. Replaying demonstration states is a training intervention, not demonstrated autonomous recovery. Efficient reference imitation does not establish unseen motion composition, language grounding or object-interaction planning.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.03274); checked 2026-11-19.

<a id="phc"></a>
## Perpetual Humanoid Control for Real-time Simulated Avatars

**phc · 2023 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2305.06456) · [Evidence](https://arxiv.org/pdf/2305.06456v3) · Citekey: `phc2023`

**Authors of cited version:** Zhengyi Luo; Jinkun Cao; Alexander Winkler; Kris Kitani; Weipeng Xu.

**Contribution / composition:** Scales physics-based imitation with recovery from falls and noisy reference motion.

**Mechanism:** Progressive multiplicative control allocates capacity for difficult motions and recovery.

**Input contract:** Full future reference motion and simulated humanoid state for imitation; recovery observations handle falls and imperfect upstream pose estimates. Progressive multiplicative control adds capacity for difficult motions without residual external forces.

**Data and split:** High-quality tests contain 11,313 AMASS training, 140 AMASS test and 140 Human3.6M motion sequences after excluding human-object interactions. Additional noisy/image-derived inputs test robustness. These are motion imitation partitions, not a language or compositional action split.

**Evaluation metrics:** Imitation success, global/local MPJPE, acceleration/velocity error and recovery behavior. Tables distinguish controllers with residual force control from PHC without it; results average three runs.

**Evaluation checked:** Table 1 compares UHC with/without residual forces on captured trajectories. Further tests assess recovery, noisy poses and real-time upstream reconstruction. Ablations examine primitive capacity and recovery training, showing physics-based imitation as an infrastructure component. Recovery transitions are trained deliberately rather than inferred from imitation success alone.

**Full-text source:** https://arxiv.org/pdf/2305.06456v3

**Reading status:** full_text_checked

**Inspected version:** 2305.06456v3

**Full-text SHA256:** 7032182d647e65d6c850a3b8e699fbcd3aa8b978fa8475e6227d029091ec8cda

**Source locator:** Sections 3.1–3.3, 4.1–4.4; Table 1 and recovery/noisy-input result tables; limitations.

**Scope / curator boundary:** Consumes privileged future references; success is tracking rather than autonomous generation or task planning. Progressive training is costly, and scene/terrain awareness remains limited. Excluding object interaction prevents interpreting reported rates as human-object contact or loco-manipulation execution accuracy.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.06456); checked 2026-11-19.

<a id="pulse"></a>
## Universal Humanoid Motion Representations for Physics-Based Control

**pulse · 2023 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2310.04582) · [Evidence](https://arxiv.org/pdf/2310.04582v2) · Citekey: `pulse2024`

**Authors of cited version:** Zhengyi Luo; Jinkun Cao; Josh Merel; Alexander Winkler; Jing Huang; Kris Kitani; Weipeng Xu.

**Contribution / composition:** PULSE first trains a stronger PHC+ motion imitator, then distills its motor knowledge into a variational bottleneck with a proprioception-conditioned latent prior. A frozen decoder maps latent actions into motor controls, while new high-level RL policies learn downstream tasks in that reusable action space.

**Mechanism:** PULSE first trains a stronger PHC+ motion imitator, then distills its motor knowledge into a variational bottleneck with a proprioception-conditioned latent prior. A frozen decoder maps latent actions into motor controls, while new high-level RL policies learn downstream tasks in that reusable action space.

**Input contract:** Robot/humanoid proprioception and task goals, including reference poses, VR controller positions, target speed, reaching/striking, or terrain context. A task-specific high-level policy is trained for each downstream problem; this is not zero-shot natural-language skill composition.

**Data and split:** Cleaned AMASS contains 11,313 training and 138 test sequences after removing unsuitable artifacts. The split is explicitly sequence-based in reported counts; real VR data add 14 trajectories. Downstream RL tasks use simulator goal distributions rather than a common held-out text-motion partition.

**Evaluation metrics:** Success requires average per-joint tracking distance below 0.5m throughout the reference. Global/root-relative MPJPE, velocity error, and acceleration error measure imitation; VR uses three-controller tracking error when full-body truth is unavailable. Normalized undiscounted return evaluates generative downstream tasks.

**Evaluation checked:** Table 1 compares PHC/PHC+/PULSE imitation; Table 2 compares VR tracking against ASE/CALM variants; task learning curves test reach, speed, strike, and terrain. Representation/prior ablations examine coverage and control benefits, while failure recovery is part of the imitator.

**Full-text source:** https://arxiv.org/pdf/2310.04582v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2310.04582v2 [cs.CV] 12 Apr 2024

**Full-text SHA256:** cd435bb5c24db5ce04c4d05376903ec95fdf4c57d27b9e976d8d01360ba6649c

**Source locator:** §§4.1–4.3 (PHC+, variational distillation, downstream RL), §5 metrics/experiments, Tables 1–2; appendix B.1 (cleaning/counts), B.2 (control).

**Scope / curator boundary:** Simulator rewards and cleaned reference coverage influence results. Reusing a latent action space still requires task-policy training and does not imply arbitrary semantic combinations. Controller tracking is insufficient to assess detailed object grasping, tactile realism, or real humanoid deployment.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2310.04582); checked 2026-11-19.

<a id="ase"></a>
## ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters

**ase · 2022 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2205.01906) · [Evidence](https://arxiv.org/pdf/2205.01906v2) · Citekey: `ase2022`

**Authors of cited version:** Xue Bin Peng; Yunrong Guo; Lina Halper; Sergey Levine; Sanja Fidler.

**Contribution / composition:** Learns reusable latent motor skills from unsegmented motion using adversarial imitation and unsupervised RL.

**Mechanism:** Pretrains a latent-conditioned simulated humanoid with adversarial imitation of unsegmented motion transitions and a mutual-information skill-discovery objective. A discriminator rewards mocap-like movement while an encoder encourages distinguishable latent skills. Downstream high-level RL selects latent codes, reusing the low-level policy and discriminator motion prior.

**Input contract:** Low-level proprioception and a continuous latent skill. Downstream tasks add goal locations, speed, heading or target-object state and hand-designed task rewards; no text-compositional interface is learned.

**Data and split:** Pretraining uses 187 unsegmented clips totaling approximately thirty minutes, including locomotion and sword/shield behaviors. There is no conventional held-out mocap train/test percentage: downstream control tasks evaluate reuse of the pretrained skill space rather than reconstruction of withheld clips.

**Evaluation metrics:** Task returns and learning curves, reach/location/speed/steering errors through corresponding reward objectives, strike performance, qualitative skill diversity and imitation quality. Ablations compare latent/objective and motion-prior designs.

**Evaluation checked:** Sections 9–10 test reaching with a sword tip, controlling travel speed/direction, moving to a location and striking a target. Baselines include policies trained from scratch and other skill-prior approaches; demonstrations show natural transitions among reusable skills.

**Full-text source:** https://arxiv.org/pdf/2205.01906v2

**Reading status:** full_text_checked

**Inspected version:** 2205.01906v2

**Full-text SHA256:** e4151dfddd0f79ef496092b58c10ef67b519e9a5be3b4d5b2067c575124050c7

**Source locator:** Sections 5.1–5.5, 7.1–7.2; Sections 9–10; Figures 6–10 and task learning curves.

**Scope / curator boundary:** Learned latent availability is bounded by the motion corpus and simulated embodiment. Reward-driven composition is distinct from unseen language combinations or dataset composition. Attached sword/shield geometry does not establish dexterous grasping or general object manipulation.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2205.01906); checked 2026-11-19.

<a id="physdiff"></a>
## PhysDiff: Physics-Guided Human Motion Diffusion Model

**physdiff · 2022 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2212.02500) · [Evidence](https://arxiv.org/pdf/2212.02500v3) · Citekey: `physdiff2023`

**Authors of cited version:** Ye Yuan; Jiaming Song; Umar Iqbal; Arash Vahdat; Jan Kautz.

**Contribution / composition:** Interleaves motion diffusion with a simulator-based imitation projection instead of applying physics only after generation.

**Mechanism:** A PPO-trained motion imitation policy tracks selected denoised estimates in IsaacGym. The projected simulated motion conditions subsequent diffusion steps; projection scheduling favors later, lower-noise stages.

**Input contract:** Text or an action label and motion duration, together with a pretrained denoiser and imitation controller. SMPL body attributes condition tracking; PD targets and residual forces support imitation.

**Data and split:** Text-to-motion uses HumanML3D. Action-to-motion uses HumanAct12 and UESTC sequences provided by the cited ACTOR protocol. The checked sections do not establish an independent semantic-combination or object-interaction split.

**Evaluation metrics:** FID and text R-precision or action-classification accuracy assess generation. Penetrate and Float measure mesh-ground distances with 5 mm tolerance; Skate measures contacting-foot displacement. Phys-Err sums these distance quantities.

**Evaluation checked:** Compares MDM/MotionDiffuse backbones, number and timing of projections, and postprocessing-only alternatives. Late-step projection is evaluated separately from simply increasing simulator calls.

**Full-text source:** https://arxiv.org/pdf/2212.02500v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2212.02500v3

**Full-text SHA256:** b29ad1febf19f8a82d242b5b779048bd037f71cc3e0cb2fa593f30e6f63cc9d4

**Source locator:** §§3.1–3.2; §4.1–4.4 and Tables 1–4; Appendices A–C.

**Scope / curator boundary:** Projection is expensive and depends on controller coverage. Residual-force-assisted simulation and ground-artifact metrics do not establish unassisted physical feasibility, object-contact correctness or hardware execution.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.02500); checked 2026-11-19.

<a id="amp"></a>
## AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

**amp · 2021 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2104.02180) · [Evidence](https://arxiv.org/pdf/2104.02180v2) · Citekey: `amp2022`

**Authors of cited version:** Xue Bin Peng; Ze Ma; Pieter Abbeel; Sergey Levine; Angjoo Kanazawa.

**Contribution / composition:** Learns motion-style rewards from unstructured clips alongside task rewards; reports emergent skill composition.

**Mechanism:** Learns a discriminator-based motion-style reward from transitions in an unstructured reference-motion collection and combines it with a task reward in goal-conditioned reinforcement learning. Least-squares adversarial training, gradient penalty and a replay buffer stabilize imitation. Policies output joint PD targets; they need not synchronize to or select a specific reference clip. Task-directed temporal skill selection emerges from optimizing task and style together.

**Input contract:** Character state, a task goal and an example motion dataset defining style. The high-level task reward is engineered; language is not the input condition.

**Data and split:** Uses task-specific motion collections and per-task policy learning, not a recording-level held-out train/test composition split. Single-clip imitation compares three independent training seeds, 32 episodes per model and maximum 20-second episodes.

**Evaluation metrics:** Normalized task returns measure task fulfillment; DTW-aligned root-relative pose error in meters measures single-clip imitation. Learning curves and sample counts evaluate efficiency/stability; qualitative sequences illustrate style and transitions.

**Evaluation checked:** Demonstrates humanoid, dog and T-Rex control. Importantly, the strike prior contains walking-only and punching-only clips: the policy learns walk-then-punch without a combined demonstration. Compares tracking-based imitation and ablates discriminator gradient penalty/velocity features.

**Full-text source:** https://arxiv.org/pdf/2104.02180v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2104.02180v2

**Full-text SHA256:** 93d9e8e40b3908d65e8b88ae3dcbe8d4cd69071d13f3234ad927462477472a29

**Source locator:** Sections 5–8.5 and 9; Tables 1–3; Figure 9; Appendix task rewards.

**Scope / curator boundary:** Task-specific policy/discriminator data induce dependencies that complicate transferring priors to new tasks. Discussion focuses mainly on temporal composition and identifies spatial composition as future work. Emergent behavior is simulation/task-reward evidence, not held-out free-text skill-pair generation or measured human interaction data.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2104.02180); checked 2026-11-19.

<a id="deepmimic"></a>
## DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

**deepmimic · 2018 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/1804.02717) · [Evidence](https://arxiv.org/pdf/1804.02717v3) · Citekey: `deepmimic2018`

**Authors of cited version:** Xue Bin Peng; Pieter Abbeel; Sergey Levine; Michiel van de Panne.

**Contribution / composition:** DeepMimic trains physics-based policies with PPO to maximize imitation and task rewards. Pose, joint velocity, end-effector, and center-of-mass terms reproduce reference clips; reference-state initialization and early termination improve difficult-skill learning. Multi-clip objectives and policy composition enable broader behavioral repertoires.

**Mechanism:** DeepMimic trains physics-based policies with PPO to maximize imitation and task rewards. Pose, joint velocity, end-effector, and center-of-mass terms reproduce reference clips; reference-state initialization and early termination improve difficult-skill learning. Multi-clip objectives and policy composition enable broader behavioral repertoires.

**Input contract:** Proprioception, reference phase, and optional task goals or terrain observations. Policies output PD targets for articulated simulated characters, including humanoid, Atlas, T-Rex, and dragon. Explicit reference skills and rewards supply the behavior specification rather than free-form text.

**Data and split:** Not applicable as a conventional supervised train/test dataset split. Policies learn designated reference clips and are evaluated on simulator episodes, task goals, perturbations, and terrain. Table 2 lists skill-specific training samples and performance rather than held-out human/recording proportions.

**Evaluation metrics:** Normalized episode return measures achievement of imitation/task rewards relative to possible reward bounds. Training-sample counts and learning curves measure efficiency; task trials assess recovery, terrain traversal, target accuracy, and skill composition. These rewards are method-specific and not general motion-distribution scores.

**Evaluation checked:** Section 6/Table 2 evaluate acrobatic and locomotion skills across characters, while subsequent experiments add task adaptation, perturbation recovery, multi-skill agents, and obstacle traversal. Ablations assess reference initialization and termination; qualitative videos support motion-quality judgments.

**Full-text source:** https://arxiv.org/pdf/1804.02717v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:1804.02717v3 [cs.GR] 27 Jul 2018

**Full-text SHA256:** 4bd4cc353bd2dc19da99bb21a254cbfdb9840e49940ce69d484eb6d45bfa348f

**Source locator:** §4 rewards/training, §5 environments/characters, §6 and Table 2 (normalized returns and samples), task adaptation, robustness, multi-skill and ablation subsections.

**Scope / curator boundary:** Learned skills depend on reference coverage, simulator fidelity, and reward design; multi-clip capabilities do not prove unseen linguistic task combinations. Simulated Atlas morphology is not hardware deployment. Contact emerging in simulation should not be generalized to dexterous human-object manipulation.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/1804.02717); checked 2026-11-19.

<a id="grail"></a>
## GRAIL: Generating Humanoid Loco-Manipulation from World Models

**grail · 2026 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2606.05160) · [Evidence](https://arxiv.org/pdf/2606.05160v2) · Citekey: `grail2026`

**Authors of cited version:** Tianyi Xie; Haotian Zhang; Jinhyung Park; Zi Wang; Bowen Wen; Jiefeng Li; Xueting Li; Qingwei Ben; Haoyang Weng; Yufei Ye; David Minor; Tingwu Wang; Chenfanfu Jiang; Sanja Fidler; Jan Kautz; Linxi Fan; Yuke Zhu; Zhengyi Luo; Umar Iqbal; Ye Yuan.

**Contribution / composition:** Grounds generated videos in known 3D scenes/assets, recovers HOI, retargets and trains trackers and visual policies.

**Mechanism:** Uses asset-conditioned video generation in a known scene, recovers aligned human-object motion, retargets it and trains a task-general humanoid tracker. An object-aware adapter augments a pretrained whole-body controller; visual policies are subsequently distilled for egocentric execution. Synthetic data generation and robot deployment are separate pipeline stages.

**Input contract:** Text/task instructions, known object assets, scene configurations and initial states; tracking uses reference trajectories and privileged simulated state during training. Final visual policies use onboard observations.

**Data and split:** HOI comparison uses twenty ComAsset objects. Synthetic G1 data exceeds 20,000 sequences from 1,000 object assets paired with 1,000 procedurally generated terrain configurations; tracking comparison evaluates 124 motions across 43 objects. Real pick-up separates five seen and five unseen objects, ten trials per object. A single global split ratio is not reported.

**Evaluation metrics:** Contact distance, penetration ratio, VLM interaction rating, human/object acceleration smoothness, InterMimic tracking deviations and frame-wise success; G1 tracking SR/object position/local MPJPE; real task success.

**Evaluation checked:** Section 4 separates generated HOI, loco-manipulation tracking and sim-to-real pick-up/stairs. Baseline and adapter ablations test components. Table 3 reports 84% seen-object and 80% unseen-object pick-up success in the stated small trial set.

**Full-text source:** https://arxiv.org/pdf/2606.05160v2

**Reading status:** full_text_checked

**Inspected version:** 2606.05160v2

**Full-text SHA256:** caef6ba780b835d9d61297a1bacf175ee8f59be5463e1a0644ba1f688f136009

**Source locator:** Sections 3.1–3.4; Sections 4.1–4.3, Tables 1–3; Appendix C evaluation settings. Section 6 (Limitations).

**Scope / curator boundary:** Assumes known 3D assets and simulator-ready scenes. Occlusion, fast motion and inconsistent generated appearance degrade reconstruction; failures are filtered. New motion families can require tracker retraining. Synthetic data and small task-specific real deployment do not establish arbitrary general task-chain composition.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2606.05160); checked 2026-11-19.

<a id="intermimicgen"></a>
## InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

**intermimicgen · 2026 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2610.06850) · [Evidence](https://arxiv.org/pdf/2610.06850v1) · Citekey: `intermimicgen2026`

**Authors of cited version:** Yucheng Zhang; Sirui Xu; Jinhong Li; Liuyu Bian; Anatulya Nandi; Derek Zhang; Xiangchen Liu; Xueting Li; Umar Iqbal; Yu-Xiong Wang; Liang-Yan Gui.

**Contribution / composition:** Retargets heterogeneous HOI, learns a generalist simulation tracker and iteratively retains task-preserving perturbations that execute successfully.

**Mechanism:** Retargets heterogeneous human-object recordings using interaction meshes, finger-opposition constraints and contact-preserving cleanup. A generalist PPO tracker executes whole-body/object references. Self-evolution edits object placement or body posture while preserving interaction type, intended contacts, object and outcome; each round fine-tunes the tracker, executes candidates and retains successful rollouts. Accepted descendants seed further rounds rather than introducing new task semantics.

**Input contract:** Reference body/object motion, robot morphology and explicit interaction geometry/contact intent. Outputs retargeted references and executable simulated rollouts; text-to-motion is not the learning objective.

**Data and split:** Collection combines 9,030 InterAct and 7,029 HiPHI sequences. Tracking benchmark groups 15 objects into bimanual, sitting and grasping; evaluates trained reference execution, not a declared held-out-recording percentage. Five augmentation rounds use verified seed descendants.

**Evaluation metrics:** Hand-contact preservation, slip, penetration, foot sliding, MPJPE, end-effector error, joint acceleration/limits; tracking success means full reference completion without failure thresholds. Reports body/object errors on successes, augmentation growth and before/after tracking success.

**Evaluation checked:** Compares dexterous retargeters and per-object specialists against one generalist. Hardware paths differ: G1 uses SONIC with finger replay; Booster uses its deployment stack; Vega uses direct retargeted trajectories and slower playback.

**Full-text source:** https://arxiv.org/pdf/2610.06850v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2610.06850v1

**Full-text SHA256:** bfbe3c4dc58e0c8949c67dc0a5776ade10ef9bcc0259ecf3a26fabe6af0a1e1f

**Source locator:** Sections 3.2–3.4 and 4.1–4.5; Tables 1–3; Appendices A, C.2, E.2–E.4, G and H.

**Scope / curator boundary:** Validated augmentation densifies existing semantics and may favor easier objects or compound reference errors. Contact preservation treats penetration as zero distance and is not independent grasp-force certification. Real-world examples must not be described as direct transfer of one identical generalist policy across all embodiments.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.06850); checked 2026-11-19.

<a id="weave"></a>
## Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions

**weave · 2026 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2609.16683) · [Evidence](https://arxiv.org/pdf/2609.16683v1) · Citekey: `weave2026`

**Authors of cited version:** Liu Cao; Xingze Wu; Jingzhi Cui; Botian Xu; Mingzhi Pei; Ruoqu Chen; Mengdi Xu.

**Contribution / composition:** Contact-aware retargeting and approach completion feed a geometry/contact-aware whole-body and finger controller; releases simulated robot-object rollouts.

**Mechanism:** Constructs executable interaction references, then tracks them with coordinated body and finger control.

**Input contract:** Retargeted human-object references, geometry/contact descriptors and simulated robot/object state. Approach completion adds locomotion prefixes before manipulation; coordinated body/finger control tracks expected contacts with local reference information.

**Data and split:** Nine-object G1 reference data divide into 7,869 training trajectories (19.56 h) and 1,605 test trajectories (3.67 h). Test sequences use the same objects, with three approach variants per training interaction and five per test interaction, introducing a stated distribution shift.

**Evaluation metrics:** Clip-balanced tracking errors, completion success and progress; root/body/finger/object position-orientation measures and contact-related termination. Pooled rates weighted by trajectory count are distinguished from equal-object averages.

**Evaluation checked:** Compares object specialists and a unified multi-object policy; evaluates train performance, transfer to unseen sequences and an oracle trained directly on test references. Failure/termination checks include positional deviation and lost expected contact for ten control steps. The oracle isolates reference-trackability from generalization of the trained controller.

**Full-text source:** https://arxiv.org/pdf/2609.16683v1

**Reading status:** full_text_checked

**Inspected version:** 2609.16683v1

**Full-text SHA256:** 593052d04a83591d6136563f86cfc50b1249e3dfc50f04de56b962655b4a5cc4

**Source locator:** Sections III–IV (reference/control), Section V.A–V.C; Figures 3–5; evaluation metrics and train/test/oracle protocol.

**Scope / curator boundary:** Released simulator rollouts are not hardware recordings. Unseen sequence results use familiar objects and harder generated approach prefixes; they do not demonstrate arbitrary new geometry/tasks. Contact-aware tracking is distinct from generating novel human task sequences.

**Composition axes:** embodiment, object-contact, physical-skill, scene-state, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2609.16683); checked 2026-11-19.

<a id="beyondmimic"></a>
## BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion

**beyondmimic · 2025 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2508.08241) · [Evidence](https://arxiv.org/pdf/2508.08241v4) · Citekey: `beyondmimic2025`

**Authors of cited version:** Qiayuan Liao; Takara E. Truong; Xiaoyu Huang; Yuman Gao; Guy Tevet; Koushil Sreenath; C. Karen Liu.

**Contribution / composition:** BeyondMimic trains robust whole-body tracking policies with adaptive motion sampling and sim-to-real randomization, distills their action trajectories into latent diffusion, and guides diffusion at inference with differentiable task costs. Combining costs enables fresh waypoint, joystick, obstacle, and motion-inpainting objectives without task-specific RL retraining.

**Mechanism:** BeyondMimic trains robust whole-body tracking policies with adaptive motion sampling and sim-to-real randomization, distills their action trajectories into latent diffusion, and guides diffusion at inference with differentiable task costs. Combining costs enables fresh waypoint, joystick, obstacle, and motion-inpainting objectives without task-specific RL retraining.

**Input contract:** Robot proprioception and task commands, optional keyframes, waypoints, or scene obstacles; low-level latent actions generate joint commands. Scene-aware guidance uses environmental localization information, whereas many tracking demonstrations run onboard without external motion capture.

**Data and split:** Reference motions are drawn from several prior collections, Unitree-retargeted LAFAN1, and animation packs; supplementary Table S8 lists validated motions. No standard human/recording-disjoint train/validation/test ratio is reported. Unseen tasks mean new test-time cost objectives, not necessarily unseen source motion categories.

**Evaluation metrics:** Tracking errors measure global/local pose accuracy; motion completion without falling defines cartwheel transfer success. Learning curves and failure rates assess adaptive sampling; task-specific navigation/command errors and hardware rollouts assess guided control. Latency and deployment constraints affect practical feasibility.

**Evaluation checked:** The Results section separates scalable tracking from inference-time skill repurposing. Adaptive-sampling ablations compare difficult segments, latent-diffusion ablations test cartwheel sim-to-sim transfer, and real Unitree G1 examples demonstrate selected skills, transitions, and guided tasks.

**Full-text source:** https://arxiv.org/pdf/2508.08241v4

**Reading status:** full_text_checked

**Inspected version:** arXiv:2508.08241v4 [cs.RO] 13 Nov 2025

**Full-text SHA256:** 6219a2b66ccdab4233a1043439bceaaea3252dadbb037b470671584fc1487db1

**Source locator:** Results: Scalable Learning, Versatile Control, Adaptive Sampling and Latent Diffusion ablations; Methods motion tracking/diffusion guidance; supplementary S2/Table S8 and deployment settings.

**Scope / curator boundary:** Guidance relies on tractable differentiable objectives and remains sensitive to data support and modeling errors. Successful G1 demonstrations are task-specific, not proof of arbitrary manipulation or semantic language composition. Per-motion tracking and distilled general policies should be distinguished in comparisons.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2508.08241); checked 2026-11-19.

<a id="gmr"></a>
## Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking

**gmr · 2025 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2510.02252) · [Evidence](https://arxiv.org/pdf/2510.02252v1) · Citekey: `gmr2025`

**Authors of cited version:** Joao Pedro Araujo; Yanjie Ze; Pei Xu; Jiajun Wu; C. Karen Liu.

**Contribution / composition:** Studies how retargeting quality affects BeyondMimic tracking on LAFAN1 and introduces GMR.

**Mechanism:** General Motion Retargeting maps human and robot key bodies, aligns rest-pose frames and applies nonuniform local Cartesian scaling. Two inverse-kinematics stages prioritize orientation and then translation/orientation with limits. The paper separately investigates how retargeting artifacts affect independently developed BeyondMimic tracking policies rather than tuning a tracker per retargeter.

**Input contract:** Human BVH/SMPL motion, robot morphology and user-defined key-body correspondence/weights. Outputs robot root/joint trajectories; subsequent RL tracking consumes those references.

**Data and split:** Uses twenty-one selected LAFAN1 sequences lasting five seconds to two minutes, excluding most complex non-foot environmental contacts. Trains a separate tracker per trajectory; this is not a conventional training/held-out motion split. User study samples fifteen motions.

**Evaluation metrics:** Full-sequence success rate, global/root-relative body-position errors and joint-angle error; user preference for resemblance to the original human clip. Tracking errors are measured while the policy remains alive.

**Evaluation checked:** Each policy receives 100 nominal, 4,096 domain-randomized and 100 ROS/MuJoCo sim-to-sim rollouts. Compares GMR, PHC, ProtoMotions and proprietary Unitree retargets; the study identifies penetration, self-intersection, velocity spikes and initialization sensitivity.

**Full-text source:** https://arxiv.org/pdf/2510.02252v1

**Reading status:** full_text_checked

**Inspected version:** 2510.02252v1

**Full-text SHA256:** cc910a8606c2de1d87c5f34a9e1753165f3cdbefe2b1d61f1bf608dbd419f0a5

**Source locator:** Sections III.A–III.E, IV (GMR), V; Table I and tracking/user-study result tables.

**Scope / curator boundary:** Trajectory-specific policy success is not zero-shot motion generalization. Sim-to-sim robustness is not a broad real-robot deployment benchmark. Retargeting quality supports composition pipelines but does not demonstrate language-conditioned generation or object-contact preservation.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2510.02252); checked 2026-11-19.

<a id="exbody"></a>
## Expressive Whole-Body Control for Humanoid Robots

**exbody · 2024 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2402.16796) · [Evidence](https://arxiv.org/pdf/2402.16796v2) · Citekey: `exbody2024`

**Authors of cited version:** Xuxin Cheng; Yandong Ji; Junming Chen; Ruihan Yang; Ge Yang; Xiaolong Wang.

**Contribution / composition:** Tracks upper-body expression while lower-body velocity control enables robust locomotion, with real robot demonstrations.

**Mechanism:** Learns expressive humanoid control by separating upper-body imitation goals from root movement commands. Human mocap is retargeted by joint-axis mapping; the lower body is free to maintain balance and locomote instead of copying incompatible leg motion. Reference-state initialization and root-command distributions sampled from real motion guide PPO exploration. Reward terms combine upper-body joint/keypoint tracking, velocity/orientation tracking and regularization.

**Input contract:** Upper-body reference joint/keypoint trajectories, root velocity, roll/pitch/yaw and height commands, plus deployable proprioception. A text-to-motion model may supply references upstream but is separate from the motor policy.

**Data and split:** Trains on 780 selected CMU clips totaling 13,383 seconds, filtering strong object/person/terrain interactions. Table II lists selected real-world test expressions and separate diffusion-generated examples; no random proportional or actor-disjoint split is specified.

**Evaluation metrics:** Mean episode length (MEL), linear-velocity tracking reward (MELV), roll/pitch tracking reward (MERP), key-body tracking reward (MEK); distribution plots and real-robot demonstrations supplement these reward-based measures.

**Evaluation checked:** Simulation comparison samples 10,000 trajectories across 4,096 environments. Ablations add AMP, remove reference-state initialization, sample random commands or impose full-body tracking. Unitree H1 demonstrations show expressive motion during locomotion.

**Full-text source:** https://arxiv.org/pdf/2402.16796v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2402.16796v2

**Full-text SHA256:** 3529a700d69a37c2b1307b05762a9a7cde49368a76707c72d37c8ae118eb5780

**Source locator:** Sections II–IV; Tables II–IV; Figures 3–9; data curation, reward and real-world-results paragraphs.

**Scope / curator boundary:** Leg imitation is deliberately relaxed; root/upper-body reward scores are not full-body reconstruction accuracy. Demonstrated bottle or basketball gestures do not establish contact-rich manipulation. Hardware morphology, torque and limited environmental interaction restrict claims beyond expressive locomotion.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2402.16796); checked 2026-11-19.

<a id="cfgcomposer"></a>
## CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction

**cfgcomposer · 2026 · Audio, dance & gesture composition · method**

[Primary source](https://arxiv.org/abs/2611.15101) · [Evidence](https://arxiv.org/pdf/2611.15101v1) · Citekey: `cfgcomposer2026`

**Authors of cited version:** Pengyang Shi; Jinlu Zhang; Chunze Lin; Yizhou Wang; Li Yi.

**Contribution / composition:** CFGComposer combines frozen audio-to-motion and text-to-motion diffusion experts, deriving a missing cross-modal score term relative to naive product-of-experts fusion. A jointly trained audio-text denoiser estimates an epsilon-space correction; an inference weight interpolates or amplifies that correction over the composed expert prediction.

**Mechanism:** CFGComposer combines frozen audio-to-motion and text-to-motion diffusion experts, deriving a missing cross-modal score term relative to naive product-of-experts fusion. A jointly trained audio-text denoiser estimates an epsilon-space correction; an inference weight interpolates or amplifies that correction over the composed expert prediction.

**Input contract:** Speech audio encoded with Whisper, a gesture caption, and a framewise gesture-window mask. Five-second clips contain 300 frames and 60 robot joints after G1/BrainCo retargeting. Specified timing is an input, not automatically inferred from unrestricted speech semantics.

**Data and split:** BEAT-derived annotated clips yield 775 training and 195 validation examples after five temporal-offset augmentations per annotation. No separately described held-out test set or speaker/annotation-group split is given in the inspected setup; correlation between offset variants therefore needs checking before reuse.

**Evaluation metrics:** G-MSE measures joint error in gesture windows, F-MSE full-clip error, BA audio/motion beat alignment, SRGR semantics-weighted keypoint recall, FID feature-distribution mismatch, and DIV variation. Blind human comparisons assess naturalness, semantic accuracy, beat matching, and diversity.

**Evaluation checked:** Table I compares prior AT2M systems; ablations compare naive PoE, finetuning, mixed-data training, and correction-scale sweeps. The operating scale 0.7 is selected using semantic fidelity. A real G1 demonstration supplements automatic and preference evaluation.

**Full-text source:** https://arxiv.org/pdf/2611.15101v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2611.15101v1 [cs.SD] 11 Nov 2026

**Full-text SHA256:** dc9b367482c3f9384e10612f683d735b613bd958ad66bdb80bf3d63a86d1cc2f

**Source locator:** §III inputs, §IV score derivation, §V/Algorithms 1–2 training/inference, §VI.A (775/195 clips), Table I, §VI.C scale ablations and deployment.

**Scope / curator boundary:** The method is not training-free: a joint model learns the correction. At scale one its defined correction returns the joint prediction algebraically; probabilistic interpretation does not independently prove estimator accuracy. Sparse paired data, validation-only reporting, and whole-body captions limit generalization claims.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2611.15101); checked 2026-11-19.

<a id="moco"></a>
## Multi-Modal Controlled Coherent Motion Generation

**moco · 2026 · Audio, dance & gesture composition · method**

[Primary source](https://feifeifeiliu.github.io/MOCO/) · [Evidence](https://arxiv.org/pdf/2609.11439v1) · Citekey: `moco2026`

**Authors of cited version:** Liu, Yifei; Cao, Qiong; Yi, Hongwei; Jiang, Huaiguang; Ding, Changxing.

**Contribution / composition:** Combines text, speech and trajectory denoisers by body region and recurrently assembles a holistic motion at each diffusion step.

**Mechanism:** Four modality/component denoisers use body masks; a timeline can reassign parts and an LLM can plan intervals.

**Input contract:** Concurrent speech audio, text intervals and optional trajectory. Four component/modality denoisers assign speech to upper-body/facial detail and text to lower body; holistic assembly repeats each diffusion step, with timeline overrides and optional LLM planning.

**Data and split:** Text training uses the AMASS portion of HumanML3D in SMPL-X; BEAT2 speakers with IDs below ten supply 10.15 training hours. A 1,000-clip test benchmark combines forty lower-body texts and BEAT2 test audio, each with two texts/two neighboring audio clips.

**Evaluation metrics:** Text-side FID+, R1 and TMR M2T/M2M; speech-side FID-A, beat consistency and L1 diversity. Five random five-second crops contribute to FID+; human preference measures coherence, timing and instruction following.

**Evaluation checked:** Table 2 compares Weighted Sum, Pseudo-Text and SynTalker. Since baselines cannot accept asynchronous inputs, their text/audio intervals are synchronized. Additional studies test component assembly, trajectory guidance and control overrides, distinguishing benchmark consistency from broad semantic coverage.

**Full-text source:** https://arxiv.org/pdf/2609.11439v1

**Reading status:** full_text_checked

**Inspected version:** 2609.11439v1

**Full-text SHA256:** 601d2b7e530966a072601ff922f8689ad9f1cb33bd12d37f8756e7ec44990a42

**Source locator:** Sections 3.1–3.4, 4.1–4.4; Table 2; Appendices E/H and extended user-study tables.

**Scope / curator boundary:** Default fixed part allocation can conflict when text and speech both control upper-body actions. Curated lower-body text and familiar audio-source evaluation do not establish arbitrary cross-modal generalization, object interaction or physically executed gait.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://feifeifeiliu.github.io/MOCO/); checked 2026-11-19.

<a id="emage"></a>
## EMAGE: Towards Unified Holistic Co-Speech Gesture Generation via Expressive Masked Audio Gesture Modeling

**emage · 2024 · Audio, dance & gesture composition · method**

[Primary source](https://arxiv.org/abs/2401.00374) · [Evidence](https://arxiv.org/pdf/2401.00374v5) · Citekey: `emage2024`

**Authors of cited version:** Haiyang Liu; Zihao Zhu; Giorgio Becherini; Yichen Peng; Mingyang Su; You Zhou; Xuefei Zhe; Naoya Iwamoto; Bo Zheng; Michael J. Black.

**Contribution / composition:** Audio and masked gesture hints drive holistic face/body/hand/global motion with compositional quantized priors; introduces BEAT2.

**Mechanism:** Constructs BEAT2 mesh-level holistic gestures and learns compositional quantized priors for face, upper/lower body and hands. A masked gesture module models supplied or missing pose hints; audio-conditioned reconstruction coordinates stream-specific latent codes with spatial/temporal attention. Missing modalities allow training on partially annotated sources.

**Input contract:** Audio, speaker identity and optional masked gesture hints; outputs facial expression, hands, body and global motion. Part decomposition concerns co-speech streams rather than semantic locomotion/manipulation skills.

**Data and split:** BEAT2 retains sixty hours from twenty-five speakers after finger-quality filtering: twenty-seven standard and thirty-three additional hours. Main reported generation uses Standard speaker 2 with 85/7.5/7.5 train/validation/test; appendix states this ratio per speaker.

**Evaluation metrics:** Fréchet Gesture Distance FGD, beat consistency BC, diversity, facial mean-squared error and lip vertex distance LVD. Dataset user comparisons assess perceived body/face quality separately.

**Evaluation checked:** Tables 4–7 compare holistic/face generation, input hint designs and multi-dataset training. Baselines receive added lower-body modules where required. Section 5 distinguishes reconstruction fidelity from audio-conditioned generation and examines masked-body conditioning.

**Full-text source:** https://arxiv.org/pdf/2401.00374v5

**Reading status:** full_text_checked

**Inspected version:** 2401.00374v5

**Full-text SHA256:** 85d17bc5a8a4678d3205380a9ddb0d8f7cb4a78c6f161884ef1071aca8da91bb

**Source locator:** Sections 3–4; Section 5.1–5.3 and Tables 3–7; Appendices A (metrics), B (dataset/splits).

**Scope / curator boundary:** Speaker-2 quantitative results are not unseen-speaker generalization. Pseudo-ground-truth fitting and retained stream noise affect quality; co-speech beat/facial scores do not establish action order, human-object contact or physically valid locomotion.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2401.00374); checked 2026-11-19.

<a id="lodge"></a>
## Lodge: A Coarse to Fine Diffusion Network for Long Dance Generation Guided by the Characteristic Dance Primitives

**lodge · 2024 · Audio, dance & gesture composition · method**

[Primary source](https://arxiv.org/abs/2403.10518) · [Evidence](https://arxiv.org/pdf/2403.10518v3) · Citekey: `lodge2024`

**Authors of cited version:** Ronghui Li; YuXiang Zhang; Yachao Zhang; Hongwen Zhang; Jie Guo; Yan Zhang; Yebin Liu; Xiu Li.

**Contribution / composition:** Global diffusion generates characteristic dance primitives; parallel local diffusion expands them into detailed long sequences, with a foot refinement component.

**Mechanism:** Uses global diffusion to generate characteristic dance primitives from long music context and local diffusion to expand them into detailed windows in parallel. Hard boundary keymotions connect adjacent windows; soft primitives are mirrored, beat-aligned and choreography-augmented to guide expressive motion. A foot-refinement block operates through forward-kinematics foot features, and a genre discriminator encourages musical-style consistency.

**Input contract:** Music features, dance genre and generated characteristic motion primitives. Optional primitives guide local generation; this is music-conditioned choreography rather than text/object task composition.

**Data and split:** FineDance experiments use 20 music pieces in its test set and generate 1,024-frame/34.13-second samples; reviewed text does not restate full train/validation counts. AIST++ follows Bailando’s protocol, training at 30 FPS and interpolating outputs to 60 FPS for evaluation.

**Evaluation metrics:** Kinematic/geometric FID measure motion-feature distribution discrepancy; DIVk/DIVg measure feature variation. Beat Alignment Score measures movement/music synchronization; Foot Skating Ratio counts contact frames with excessive sliding; runtime measures generation efficiency.

**Evaluation checked:** Compares FACT, MNET, Bailando and EDGE, with ablations on primitives, mirroring, beat alignment, soft cues and foot refinement. Both long FineDance and shorter AIST++ evaluations separate choreography from local motion detail.

**Full-text source:** https://arxiv.org/pdf/2403.10518v3

**Reading status:** full_text_checked

**Inspected version:** arXiv:2403.10518v3

**Full-text SHA256:** 29df9d2776926ba2c16a2ec3abaea743443d19291fed6d9214d9b90a5bf264c3

**Source locator:** Sections 3.2–3.4, 4.1–4.4 and 5; Tables 1–5; Foot Refine Block and evaluation metric definitions.

**Scope / curator boundary:** Kinematic FID is a statistical proxy, not physics certification. The method cannot generate detailed hand gestures or facial expressions. Long dance continuity and beat synchronization do not establish object-state dependencies, natural locomotion-to-manipulation transitions or semantic skill holdouts.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.10518); checked 2026-11-19.

<a id="edge"></a>
## EDGE: Editable Dance Generation From Music

**edge · 2022 · Audio, dance & gesture composition · method**

[Primary source](https://arxiv.org/abs/2211.10658) · [Evidence](https://arxiv.org/pdf/2211.10658v2) · Citekey: `edge2022`

**Authors of cited version:** Jonathan Tseng; Rodrigo Castellon; C. Karen Liu.

**Contribution / composition:** EDGE trains a music-conditioned diffusion Transformer with Jukebox audio features and geometric/foot-contact losses. Diffusion inpainting enforces selected joints or frames, while overlapping conditioned windows enable long dance synthesis and editable transitions without retraining separate editing models.

**Mechanism:** EDGE trains a music-conditioned diffusion Transformer with Jukebox audio features and geometric/foot-contact losses. Diffusion inpainting enforces selected joints or frames, while overlapping conditioned windows enable long dance synthesis and editable transitions without retraining separate editing models.

**Input contract:** Music features, requested motion duration, and optional temporal or jointwise constraints. Supplied poses/joints are preserved during denoising; long sequences concatenate overlapping windows. Music-conditioned dance differs from text-ordered locomotion followed by object manipulation.

**Data and split:** Uses the original AIST++ train/test split, with training examples cut into five-second clips at 30 fps. Exact split counts/proportions are not restated in the main experimental setup. Additional in-the-wild music tests probe audio transfer rather than held-out human-object interaction.

**Evaluation metrics:** Kinetic/geometric feature distances measure diversity; beat alignment measures correspondence between music and motion events. Physical Foot Contact (PFC) evaluates foot/contact plausibility from motion signals. Pairwise human judgments yield Elo ratings and win rates with confidence intervals.

**Evaluation checked:** Table 1 compares FACT, Bailando, and guidance variants; Table 2 tests in-the-wild music and Jukebox-feature ablations. Examples demonstrate joint constraints, in-betweening, and long generation. The paper questions whether standard feature FID reliably matches perceived dance quality.

**Full-text source:** https://arxiv.org/pdf/2211.10658v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2211.10658v2 [cs.SD] 27 Nov 2022

**Full-text SHA256:** a86c11da4bc5005b450f5f9ee1f78b32ebdabc86d1e067ff45b9424081ffb4d2

**Source locator:** §3 diffusion/audio/geometric losses and editing (Figure 3), §4 experimental protocol and Tables 1–2, Equation 10 PFC; appendix A human study.

**Scope / curator boundary:** Contact-aware losses and PFC are kinematic proxies, not physics-simulator or force validation. Window stitching does not guarantee global choreographic semantics. Dance-domain training and audio transfer cannot establish general text composition, detailed hands, or scene/object interaction.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2211.10658); checked 2026-11-19.

<a id="finedance"></a>
## FineDance: A Fine-grained Choreography Dataset for 3D Full Body Dance Generation

**finedance · 2022 · Audio, dance & gesture composition · method**

[Primary source](https://arxiv.org/abs/2212.03741) · [Evidence](https://arxiv.org/pdf/2212.03741v4) · Citekey: `finedance2023`

**Authors of cited version:** Ronghui Li; Junfan Zhao; Yachao Zhang; Mingyang Su; Zeping Ren; Han Zhang; Yansong Tang; Xiu Li.

**Contribution / composition:** Full-body music-dance dataset with detailed hand motion and dance genres; its retrieval and generation mechanisms provide an adjacent composition setting.

**Mechanism:** Introduces paired full-body/hand dance capture with genre labels and a FineNet generation-retrieval pipeline. A body/hand expert diffusion generator creates candidate fragments; genre-matching and boundary-coherence scores select candidates, followed by short interpolation at joins. Separate hand modeling improves detailed expressive dance relative to body-only generation.

**Input contract:** Music temporal features and mel-spectrogram, previous generated fragment and learned genre-matching signals. The generation process assembles successive four-second music-aligned segments.

**Data and split:** FineDance@Genre divides paired music/dance recordings so each pair belongs to one set but dancers may overlap. FineDance@Dancer instead separates dancer identities. Main results report @Genre only; precise partition proportions are deferred to supplementary details and not numerically stated in the inspected main protocol.

**Evaluation metrics:** Body/hand FID, body/hand diversity, multimodality and Genre Matching Score; a thirty-person study including fifteen dancers evaluates perceived dance qualities.

**Evaluation checked:** Compares retrieval and generation baselines on FineDance and AIST++, including body-hand expert ablations. Tables 1–2 distinguish generated candidate diversity from final retrieval quality. Genre and coherence terms are examined through component studies.

**Full-text source:** https://arxiv.org/pdf/2212.03741v4

**Reading status:** full_text_checked

**Inspected version:** 2212.03741v4

**Full-text SHA256:** deb4746922a06f6f4de90ee3329fc4be831db1de02111a0a79a293d49fb1aedc

**Source locator:** Sections 3–4.3; Section 5 experimental protocol, Tables 1–2; supplementary dataset discussion and user study.

**Scope / curator boundary:** Overlapping dancers in the main benchmark prevent claims of unseen-dancer generalization. Genre fit and smooth joins do not evaluate object contact or task causality. Dance genres are intentionally unbalanced, reflecting collection distribution rather than equal semantic coverage.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.03741); checked 2026-11-19.

<a id="interaction-survey"></a>
## A Survey on Human Interaction Motion Generation

**interaction-survey · 2025 · Surveys & field maps · method**

[Primary source](https://arxiv.org/abs/2503.12763) · [Evidence](https://arxiv.org/pdf/2503.12763v2) · Citekey: `interactionsurvey2025`

**Authors of cited version:** Kewei Sui; Anindita Ghosh; Inwoo Hwang; Bing Zhou; Jian Wang; Chuan Guo.

**Contribution / composition:** Organizes human-human, human-object and human-scene generation with datasets and evaluation; useful for backward citation chasing across interaction types.

**Mechanism:** Narrative technical survey organizes interaction motion by human-human, human-object, human-scene and mixed entities. Preliminaries compare body/object/scene representations, conditioning modalities and model families. Method discussions separate semantic coordination, spatial/physical constraints and scene context; dataset tables summarize acquisition and scope. It is a secondary taxonomy and bibliography, not a newly trained interaction generator or pooled empirical benchmark.

**Input contract:** Not applicable as model inputs: the review catalogs text, partner motion, object/scene geometry, audio and related conditioning used by primary methods.

**Data and split:** Not applicable: no new training/validation/test split or meta-analysis dataset is defined. A reproducible database-search query, inclusion/exclusion flow and pooled statistical protocol are not reported as a formal systematic-review methodology.

**Evaluation metrics:** Reviews MPJPE and trajectory errors, FID/naturalness measures, diversity/multimodality, foot skating, contact/penetration, text retrieval, beat consistency and user studies. These are metrics discussed from primary papers, not newly measured survey results.

**Evaluation checked:** Section 6 organizes evaluation into fidelity, diversity and condition coherence, emphasizing that interactive constraints need complementary measures. Tables compare method families and dataset properties; Section 7 discusses scaling data, richer interactions and evaluation challenges.

**Full-text source:** https://arxiv.org/pdf/2503.12763v2

**Reading status:** full_text_checked

**Inspected version:** arXiv:2503.12763v2

**Full-text SHA256:** 41bd882d84ba725c7ac915876f011797814f66a7f2ba27126defd117c03deb38

**Source locator:** Sections 3.1–3.3, 4.1–4.4, 5, 6.1–6.4 and 7; Tables 1–9, especially Table 9 evaluation taxonomy.

**Scope / curator boundary:** Cross-paper numbers and taxonomies do not ensure compatible data splits, representations or evaluators. Survey capability descriptions must be checked against primary methods before asserting unseen skill composition, physical validity or deployment. No survey-wide controlled experiment establishes those claims.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2503.12763); checked 2026-11-19.

<a id="video-motion-survey"></a>
## Human Motion Video Generation: A Survey

**video-motion-survey · 2025 · Surveys & field maps · method**

[Primary source](https://arxiv.org/abs/2509.03883) · [Evidence](https://arxiv.org/pdf/2509.03883v1) · Citekey: `videomotionsurvey2025`

**Authors of cited version:** Haiwei Xue; Xiangyang Luo; Zhanghao Hu; Xin Zhang; Xunzhi Xiang; Yuqin Dai; Jianzhuang Liu; Zhensong Zhang; Minglei Li; Jian Yang; Fei Ma; Zhiyong Wu; Changpeng Yang; Zonghong Dai; Fei Richard Yu.

**Contribution / composition:** This narrative survey organizes more than 200 human-motion-video papers around input, motion planning, video generation, refinement, and output. It separates vision-, text-, and audio-driven tasks, compares representative architectures, discusses language-model-assisted planning, and catalogs datasets and evaluation practices.

**Mechanism:** This narrative survey organizes more than 200 human-motion-video papers around input, motion planning, video generation, refinement, and output. It separates vision-, text-, and audio-driven tasks, compares representative architectures, discusses language-model-assisted planning, and catalogs datasets and evaluation practices.

**Input contract:** Reviewed conditions include reference images/videos, human pose, text, speech, and music across portrait animation, dance, talking-head, try-on, and holistic-body video tasks. The paper reviews conditioning interfaces rather than presenting a new jointly trained controllable 3D motion generator.

**Data and split:** Not applicable: this is a literature review with no newly trained model and no train/test split. Dataset tables summarize external benchmarks; their subjects, recording protocols, and partitions are heterogeneous. No reproducible systematic-review search query, screening flow, or meta-analysis protocol is specified.

**Evaluation metrics:** No new experimental metric is introduced. Section VI catalogs pixel/perceptual quality measures such as PSNR, SSIM, LPIPS and FID; temporal/video measures such as FVD; alignment and task-specific pose/lip/identity scores, plus broader video-quality benchmarks.

**Evaluation checked:** Taxonomy figures and method tables compare capabilities and pipeline stages; Section VI inventories 64 publicly available human-video datasets and explains evaluation families. These are structured literature summaries, not controlled reruns or an aggregated numerical leaderboard under one common protocol.

**Full-text source:** https://arxiv.org/pdf/2509.03883v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2509.03883v1 [cs.CV] 4 Sep 2025

**Full-text SHA256:** b308dc06f38b5da3de3e136f5e06051acc070b574c1b59f71246e42f76905525

**Source locator:** §I scope/taxonomy, §III motion planning, §IV modality-based generation, §V refinement/output, §VI/Figure 11 and Table VIII (metrics/datasets), §VII challenges.

**Scope / curator boundary:** Coverage is scoped to video synthesis and reflects the reviewed publication window. Photorealism, identity preservation, or plausible rendered movement cannot establish recoverable metric 3D motion, collision-free contact, or executable humanoid control. Cross-paper scores use incompatible data and metrics.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.03883); checked 2026-11-19.

<a id="generative-survey"></a>
## Motion Generation: A Survey of Generative Approaches and Benchmarks

**generative-survey · 2025 · Surveys & field maps · method**

[Primary source](https://arxiv.org/abs/2507.05419) · [Evidence](https://arxiv.org/pdf/2507.05419v1) · Citekey: `generativesurvey2025`

**Authors of cited version:** Aliasghar Khani; Arianna Rampini; Bruno Roy; Larasika Nadela; Noa Kaplan; Evan Atherton; Derek Cheung; Jacky Bibliowicz.

**Contribution / composition:** Reviews generative model families, conditioning, datasets and metrics, emphasizing recent motion-generation literature.

**Mechanism:** Reviews motion-generation methods through generative paradigms, network architectures, conditioning mechanisms and application settings. Organizes GAN, autoencoder, autoregressive and diffusion families, then cross-references datasets and evaluation criteria. Quantitative tables summarize literature usage/trends rather than training a new generator or rerunning every reviewed method.

**Input contract:** Not applicable as a model input. The taxonomy includes unconditional, text-, audio-, scene-, interaction- and control-conditioned generation, with representations and application contexts discussed across categories.

**Data and split:** Not applicable: this is a literature survey, not an experimental train/test dataset. It emphasizes recent top-conference papers, especially since 2023; a preregistered database search, exhaustive exclusion log or numerical evidence-quality screening protocol is not reported.

**Evaluation metrics:** Reviews realism, diversity, ground-truth similarity, condition consistency and efficiency metrics. Table XIV catalogs metrics and their source works, including FID, coordinate errors, semantic retrieval, skating/penetration and runtime; these are surveyed definitions, not newly measured scores.

**Evaluation checked:** Compares architectural/conditioning trends through survey tables and statistical summaries. Dataset inventories help identify inconsistent representations and benchmark choices; discussion highlights physical plausibility, controllability, data limitations and gaps in standardized evaluation.

**Full-text source:** https://arxiv.org/pdf/2507.05419v1

**Reading status:** full_text_checked

**Inspected version:** 2507.05419v1

**Full-text SHA256:** 58912e8e46356b5127b8ff9c91b24e42ee91716fef050a83436b72e68289a4d0

**Source locator:** Sections II–V (representations, generative families, datasets/metrics), Table XIV; statistical analysis and conclusion sections.

**Scope / curator boundary:** Architecture-oriented taxonomy alone does not separate compositional generalization from concatenation, editing or internal factorization. Literature coverage and reported benchmark results are secondary evidence; source papers remain necessary for exact split protocols and causal scientific claims.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2507.05419); checked 2026-11-19.

<a id="text-motion-overview"></a>
## Text-driven Motion Generation: Overview, Challenges and Directions

**text-motion-overview · 2025 · Surveys & field maps · method**

[Primary source](https://arxiv.org/abs/2505.09379) · [Evidence](https://arxiv.org/pdf/2505.09379v1) · Citekey: `textmotionoverview2025`

**Authors of cited version:** Ali Rida Sahili; Najett Neji; Hedi Tabia.

**Contribution / composition:** Reviews text-to-motion through architecture and discrete/continuous representation perspectives.

**Mechanism:** Narrative overview examines text-driven human motion through two intersecting taxonomies: VAE/diffusion/hybrid architecture and discrete/continuous motion representation. It contrasts latent/token modeling, language alignment and generation/editing tradeoffs, then compares commonly used motion-language resources. The paper is a secondary conceptual review, not a new generative system or a standardized reimplementation of surveyed baselines.

**Input contract:** Not applicable as one model condition: surveyed methods typically accept text, with optional motion context, temporal masks, style or scene cues depending on the primary work.

**Data and split:** Not applicable: no new benchmark split is introduced and no unified train/test re-evaluation is reported. The review does not specify a reproducible search-query/inclusion-screening procedure sufficient to treat it as a formal systematic meta-analysis.

**Evaluation metrics:** Discusses FID for generated/reference motion-feature distributions, R-precision for text retrieval, MM-Dist for paired text-motion embedding distance, diversity across outputs and multimodality for one prompt. These definitions summarize literature rather than new experimental measurements.

**Evaluation checked:** Tables 1–5 compare architectural and representation advantages/limitations; Table 6 compares dataset scale, annotations and anatomical coverage. Sections 5–6 discuss scarce data, fine-grained details, ambiguous evaluation, controllability and scene-aware interaction.

**Full-text source:** https://arxiv.org/pdf/2505.09379v1

**Reading status:** full_text_checked

**Inspected version:** arXiv:2505.09379v1

**Full-text SHA256:** 76360c3deb4210cd9734dfc2b0e5172527ad1f6472b0ce38c952401351821626

**Source locator:** Sections 3.1–3.2, 4.1–4.2, 5.1–5.3 and 6.1–6.3; Tables 1–6.

**Scope / curator boundary:** The review’s broad comparative judgments do not control training data, speed hardware or evaluator differences. Its stated model limitations and dataset superlatives require primary-source verification and version context. Standard text-motion feature scores alone do not establish unseen skill-combination or interaction-state generalization.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2505.09379); checked 2026-11-19.

<a id="realis-motion"></a>
## RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space

**realis-motion · 2026 · Adjacent: compositional human video · method**

[Primary source](https://proceedings.mlr.press/v306/liang26ad.html) · [Evidence](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liang26ad/liang26ad.pdf) · Citekey: `realismotion2026`

**Authors of cited version:** Jingyun Liang; Jingkai Zhou; Shikai Li; Chenjie Cao; Lei Sun; Yichen Qian; Weihua Chen; Fan Wang.

**Contribution / composition:** RealisMotion separates subject appearance, background video, world-space trajectory, and action. A ground-aware coordinate system, focal-length calibration, trajectory unprojection, speed alignment, and orientation adjustment edit 3D motion. Wan-based video diffusion injects subject tokens, background channels, and added motion control signals.

**Mechanism:** RealisMotion separates subject appearance, background video, world-space trajectory, and action. A ground-aware coordinate system, focal-length calibration, trajectory unprojection, speed alignment, and orientation adjustment edit 3D motion. Wan-based video diffusion injects subject tokens, background channels, and added motion control signals.

**Input contract:** A reference subject image, background video, trajectory and action controls, with optional text/face cues. Actions may come from a motion bank or text-to-motion generator. An image-to-video variant merges subject/background and consequently loses their independent customization.

**Data and split:** Finetunes Wan-2.1 14B on an internal approximately 3,300-hour video collection. Evaluates trajectory/orientation on a newly assembled 100-video Trajectory100 set and action on RealisDance-Val. Exact training/validation partition proportions and source-identity grouping are not reported in the inspected setup.

**Evaluation metrics:** Translation error in meters and rotation error in degrees measure recovered trajectory/orientation agreement. PSNR, SSIM, LPIPS assess image fidelity/perception; FID and FVD assess image/video feature-distribution mismatch. These are video-control metrics rather than physical human-object motion scores.

**Evaluation checked:** Table 2 compares trajectory control with Wan, Tora, and RealisDance-DiT; Table 3 evaluates action control. Table 4 ablates calibration, body-hand matching, text, extra face input, positional encoding, and random masking. Subject/background customization is largely illustrated qualitatively.

**Full-text source:** https://raw.githubusercontent.com/mlresearch/v306/main/assets/liang26ad/liang26ad.pdf

**Reading status:** full_text_checked

**Inspected version:** Official primary PDF fetched 2026-11-19; file SHA-256 retained in private audit receipt.

**Full-text SHA256:** aef95b4aff6b31851f60d12c027005830fda9f428a3ccf61988393adfde8d7af

**Source locator:** §3 decomposed 3D editing/video injection; §§4.1–4.3, Tables 2–4; supplementary training details and depth-error robustness analysis.

**Scope / curator boundary:** Estimated depth, camera calibration, body recovery, and 3D-to-video alignment remain error sources. Internal training data limit reproducibility. Visually consistent world-space animation does not establish accurate contact, object dynamics, or robot executability; cross-domain characters are demonstrations rather than comprehensive controlled evaluation.

**Composition axes:** appearance-motion, cross-modal.

**Metadata:** official; [source](https://proceedings.mlr.press/v306/liang26ad.html); checked 2026-11-19.
