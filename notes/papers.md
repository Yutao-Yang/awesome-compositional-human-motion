# Paper audit cards

Checked: 2026-11-19. Evidence levels describe reading, not reproduction. Curator boundaries are comparison guidance.

<a id="parametric-motion-graphs"></a>
## Parametric Motion Graphs

**parametric-motion-graphs · 2007 · Classical motion composition · abstract**

[Primary source](https://graphics.cs.wisc.edu/Papers/2007/HG07/) · [Evidence](https://doi.org/10.1145/1230100.1230123) · Citekey: `parametricmotiongraphs2007`

**Authors of cited version:** Rachel Heck; Michael Gleicher.

**Contribution / composition:** Connects parameterized motion synthesis with valid dynamically generated blending transitions.

**Scope / curator boundary:** Example-based blend spaces require appropriate source coverage and valid transitions.

**Composition axes:** temporal.

**Metadata:** official; [source](https://graphics.cs.wisc.edu/Papers/2007/HG07/); checked 2026-11-19.

<a id="motion-annotations"></a>
## Motion Synthesis from Annotations

**motion-annotations · 2003 · Classical motion composition · method**

[Primary source](https://escholarship.org/uc/item/23g204tp) · [Evidence](https://graphics.berkeley.edu/papers/Arikan-MSF-2003-08/Arikan-MSF-2003-08.pdf) · Citekey: `motionannotations2003`

**Authors of cited version:** Okan Arikan; David A. Forsyth; James F. O'Brien.

**Contribution / composition:** Uses annotated action timelines and multiscale dynamic programming to assemble motion, including overlapping qualitative constraints.

**Mechanism:** Coarse-to-fine dynamic programming searches database motion blocks; SVM-assisted annotation expands a small labeled subset.

**Input contract:** Positive, negative and unconstrained timeline labels; optional pose, position and orientation constraints.

**Evaluation checked:** Interactive examples include trip, run and jump constraints and combined walking/carrying semantics.

**Scope / curator boundary:** Requires an annotated motion database; a timeline label does not provide unseen interaction geometry.

**Composition axes:** temporal.

**Metadata:** primary-transcribed; [source](https://escholarship.org/uc/item/23g204tp); checked 2026-11-19.

<a id="interactive-motion-examples"></a>
## Interactive motion generation from examples

**interactive-motion-examples · 2002 · Classical motion composition · abstract**

[Primary source](https://experts.illinois.edu/en/publications/interactive-motion-generation-from-examples/) · [Evidence](https://courses.cs.washington.edu/courses/cse590b/02au/s2002.pdf) · Citekey: `interactivemotionexamples2002`

**Authors of cited version:** Okan Arikan; D. A. Forsyth.

**Contribution / composition:** Cuts and pastes mocap via randomized hierarchical graph search under constraints at interactive speeds.

**Scope / curator boundary:** Reuses available examples; source coverage bounds the realizable actions.

**Composition axes:** temporal.

**Metadata:** official; [source](https://experts.illinois.edu/en/publications/interactive-motion-generation-from-examples/); checked 2026-11-19.

<a id="motion-graphs"></a>
## Motion Graphs

**motion-graphs · 2002 · Classical motion composition · abstract**

[Primary source](https://graphics.cs.wisc.edu/Papers/2002/KGP02/) · [Evidence](https://graphics.cs.wisc.edu/Papers/2002/KGP02/) · Citekey: `motiongraphs2002`

**Authors of cited version:** Lucas Kovar; Michael Gleicher; Frédéric Pighin.

**Contribution / composition:** Builds a directed graph of captured clips and synthesized transitions; graph walks satisfy user constraints such as locomotion paths.

**Scope / curator boundary:** Coverage depends on captured motions and viable graph connections; no open-vocabulary semantic generation.

**Composition axes:** temporal.

**Metadata:** official; [source](https://graphics.cs.wisc.edu/Papers/2002/KGP02/); checked 2026-11-19.

<a id="prism"></a>
## PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition

**prism · 2026 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2603.08590) · [Evidence](https://arxiv.org/abs/2603.08590) · Citekey: `prism2026`

**Authors of cited version:** Zeyu Ling; Qing Shuai; Teng Zhang; Shiyang Li; Bo Han; Changqing Zou.

**Contribution / composition:** Kinematic-unit continuous latents, causal VAE and flow matching support prefix continuation, segment chaining and narrative composition.

**Scope / curator boundary:** Large-model and dataset-scale effects must be separated from factorization; no interaction physics guarantee.

**Publication / version note:** Abstract-level record only. A later HTML revision appears under a different title; version alignment needs further review before method-level claims.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2603.08590); checked 2026-11-19.

<a id="timelinecontrol"></a>
## Streaming Multi-Track Timeline Control for 3D Human Motion Generation

**timelinecontrol · 2026 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2610.03873) · [Evidence](https://arxiv.org/abs/2610.03873) · Citekey: `timelinecontrol2026`

**Authors of cited version:** Yangsong Zhang; Anujith Muraleedharan; Rikhat Akizhanov; Gül Varol; Fabio Pizzati; Ivan Laptev.

**Contribution / composition:** TimelineControl combines interval-aware conditioning, causal part representations and part-aware denoising with TimelineMotion annotations.

**Scope / curator boundary:** New preprint; comparative claims apply to evaluated streaming baselines and require independent replication.

**Composition axes:** spatial, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.03873); checked 2026-11-19.

<a id="dart"></a>
## DartControl: A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control

**dart · 2024 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2410.05260) · [Evidence](https://arxiv.org/abs/2410.05260) · Citekey: `dart2025`

**Authors of cited version:** Kaifeng Zhao; Gen Li; Siyu Tang.

**Contribution / composition:** Latent diffusion predicts motion primitives from history and current text; noise optimization or RL provides spatial control.

**Scope / curator boundary:** Autoregressive primitive history is local; spatial control and scene tasks should be evaluated separately.

**Publication / version note:** First public preprint 2024.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.05260); checked 2026-11-19.

<a id="motion-mamba"></a>
## Motion Mamba: Efficient and Long Sequence Motion Generation

**motion-mamba · 2024 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2403.07487) · [Evidence](https://arxiv.org/abs/2403.07487) · Citekey: `motionmamba2024`

**Authors of cited version:** Zeyu Zhang; Akide Liu; Ian Reid; Richard Hartley; Bohan Zhuang; Hao Tang.

**Contribution / composition:** Hierarchical temporal and bidirectional spatial state-space blocks improve long-motion modeling and efficiency.

**Scope / curator boundary:** Long single-prompt generation differs from ordered multi-prompt composition.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.07487); checked 2026-11-19.

<a id="stmc"></a>
## Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation

**stmc · 2024 · Temporal composition & long sequences · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf) · Citekey: `stmc2024`

**Authors of cited version:** Petrovich, Mathis; Litany, Or; Iqbal, Umar; Black, Michael J.; Varol, Gul; Bin Peng, Xue; Rempe, Davis.

**Contribution / composition:** Test-time spatial stitching and temporal score arithmetic operate at every diffusion step.

**Mechanism:** Preprocesses prompts into per-body-part timelines; denoises local crops and combines corresponding pose components repeatedly during sampling.

**Input contract:** Multi-track text timeline with timing and body-part assignments, provided by user or language model.

**Evaluation checked:** Temporal and simultaneous composition; assess under the paper’s timeline setting rather than single-prompt metrics alone.

**Source locator:** Section 3.3 (Spatial/Temporal stitching); Sections 4.1–4.4; 4.6; Appendix B–C.

**Scope / curator boundary:** Authors report inherited base-model limits, unfamiliar stitched poses, compatible-part restriction and imperfect timing. Proposed late-denoising stitching schedules are future work, not evaluated capability. Prompt-to-part assignment and incompatible overlaps require care; kinematic composition does not establish interaction physics.

**Composition axes:** spatial, temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/html/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.html); checked 2026-11-19.

<a id="flowmdm"></a>
## Seamless Human Motion Composition with Blended Positional Encodings

**flowmdm · 2024 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2402.15509) · [Evidence](https://arxiv.org/html/2402.15509) · Citekey: `flowmdm2024`

**Authors of cited version:** German Barquero; Sergio Escalera; Cristina Palmero.

**Contribution / composition:** FlowMDM generates temporally composed text-conditioned motion and evaluates transition quality.

**Mechanism:** Early denoising uses absolute positions for within-action structure; late denoising uses relative positions across boundaries. Pose-centric cross-attention associates each frame with its own condition.

**Input contract:** Non-overlapping text intervals and durations; can train on singly described clips.

**Evaluation checked:** BABEL and HumanML3D subsequence and transition quality, plus Peak Jerk and Area Under Jerk for discontinuities.

**Scope / curator boundary:** Independent low-frequency subsequence generation can limit relationships across actions; no contact-dynamics certification. Single-human kinematic synthesis; finite attention horizon and text timing remain design constraints, with no object-contact certification.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2402.15509); checked 2026-11-19.

<a id="t2lm"></a>
## T2LM: Long-Term 3D Human Motion Generation from Multiple Sentences

**t2lm · 2024 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2406.00636) · [Evidence](https://arxiv.org/abs/2406.00636) · Citekey: `t2lm2026`

**Authors of cited version:** Taeryung Lee; Fabien Baradel; Thomas Lucas; Kyoung Mu Lee; Gregory Rogez.

**Contribution / composition:** Uses a local 1D-convolutional VQ-VAE decoder to decode a continuous text-predicted latent stream, trained on short clips.

**Scope / curator boundary:** Local receptive fields favor smooth joins but do not guarantee global scene/contact consistency.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2406.00636); checked 2026-11-19.

<a id="amd-autoregressive"></a>
## AMD: Autoregressive Motion Diffusion

**amd-autoregressive · 2023 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2305.09381) · [Evidence](https://arxiv.org/abs/2305.09381) · Citekey: `amdautoregressive2024`

**Authors of cited version:** Bo Han; Hao Peng; Minjing Dong; Yi Ren; Yixuan Shen; Chang Xu.

**Contribution / composition:** Introduces HumanLong3D and conditions iterative diffusion generation on current text plus previous text and action sequences.

**Scope / curator boundary:** Long-text paired data construction and autoregressive accumulated error deserve inspection.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.09381); checked 2026-11-19.

<a id="diffcollage"></a>
## DiffCollage: Parallel Generation of Large Content with Diffusion Models

**diffcollage · 2023 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2303.17076) · [Evidence](https://arxiv.org/abs/2303.17076) · Citekey: `diffcollage2023`

**Authors of cited version:** Qinsheng Zhang; Jiaming Song; Xun Huang; Yongxin Chen; Ming-Yu Liu.

**Contribution / composition:** Factor-graph composition aggregates diffusion outputs over overlapping pieces for large parallel generation, including long text-guided motion.

**Scope / curator boundary:** Generic overlap approximation; motion-specific contact and global semantic correctness are not guaranteed.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2303.17076); checked 2026-11-19.

<a id="priormdm"></a>
## Human Motion Diffusion as a Generative Prior

**priormdm · 2023 · Temporal composition & long sequences · method**

[Primary source](https://arxiv.org/abs/2303.01418) · [Evidence](https://openreview.net/pdf/713790c2a80588d36bcaaefffcf9b8f9c4117583.pdf) · Citekey: `priormdm2023`

**Authors of cited version:** Yonatan Shafir; Guy Tevet; Roy Kapon; Amit H. Bermano.

**Contribution / composition:** Introduces DoubleTake sequential composition, ComMDM two-person coordination and DiffusionBlending joint-control model composition.

**Mechanism:** A frozen short-motion diffusion prior is reused for overlapping prompted intervals; a second take refines transitions. Separate small adapters or fine-tuned controlled priors support other composition modes.

**Input contract:** Interval text prompts; two-person motion examples for ComMDM; prescribed joint or trajectory motion for fine-grained control.

**Evaluation checked:** Off-the-shelf motion diffusion prior compared with task-specific trained models across sequential, parallel and controlled-generation tasks.

**Scope / curator boundary:** DoubleTake needs overlap and refinement design; ComMDM needs interaction examples; composition is not guaranteed physical validity.

**Publication / version note:** First public preprint; conference publication 2024.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2303.01418); checked 2026-11-19.

<a id="st2m"></a>
## Sequential Texts Driven Cohesive Motions Synthesis with Natural Transitions

**st2m · 2023 · Temporal composition & long sequences · abstract**

[Primary source](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.pdf) · Citekey: `st2m2023`

**Authors of cited version:** Li, Shuai; Zhuang, Sisi; Song, Wenfeng; Zhang, Xinyu; Chen, Hejia; Hao, Aimin.

**Contribution / composition:** Combines previous/current text semantics with learnable transition tokens and a transition loss.

**Scope / curator boundary:** Representation and evaluation protocol differ from some BABEL baselines; direct score comparisons need matching representations.

**Composition axes:** temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Sequential_Texts_Driven_Cohesive_Motions_Synthesis_with_Natural_Transitions_ICCV_2023_paper.html); checked 2026-11-19.

<a id="multi-act-2022"></a>
## MultiAct: Long-Term 3D Human Motion Generation from Multiple Action Labels

**multi-act-2022 · 2022 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2212.05897) · [Evidence](https://arxiv.org/abs/2212.05897) · Citekey: `multiact20222023`

**Authors of cited version:** Taeryung Lee; Gyeongsik Moon; Kyoung Mu Lee.

**Contribution / composition:** Recurrently conditions on prior motion and the next action label to generate transitions and long multi-action sequences.

**Scope / curator boundary:** Action-label conditioning is less expressive than free text; recurrent rollout requires long-horizon drift checks.

**Publication / version note:** First public preprint in December 2022; revised 2023.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.05897); checked 2026-11-19.

<a id="teach"></a>
## TEACH: Temporal Action Composition for 3D Humans

**teach · 2022 · Temporal composition & long sequences · abstract**

[Primary source](https://arxiv.org/abs/2209.04066) · [Evidence](https://arxiv.org/abs/2209.04066) · Citekey: `teach2022`

**Authors of cited version:** Nikos Athanasiou; Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** Generates ordered action sequences using a hierarchical Transformer: parallel within each action and autoregressive between actions.

**Mechanism:** Hierarchical action-level autoregression with non-autoregressive motion generation inside each action.

**Input contract:** Ordered natural-language descriptions and action lengths; prior generated action context.

**Evaluation checked:** BABEL sequential text-motion compositions and multiple baselines; no object-conditioned manipulation benchmark claimed.

**Scope / curator boundary:** Uses sequential BABEL supervision; autoregressive rollout and transition continuity require separate assessment.

**Composition axes:** temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2209.04066); checked 2026-11-19.

<a id="fusion"></a>
## FUSION: Full-Body Unified Motion Prior for Body and Hands via Diffusion

**fusion · 2026 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2601.03959) · [Evidence](https://arxiv.org/html/2601.03959) · Citekey: `fusion2026`

**Authors of cited version:** Enes Duran; Nikos Athanasiou; Muhammed Kocabas; Michael J. Black; Omid Taheri.

**Contribution / composition:** Unifies body and hand datasets into a full-body motion prior, with optimization-driven object-motion and self-interaction applications.

**Mechanism:** Unconditional SMPL-X diffusion prior jointly models body/hands; task losses backpropagate through denoising to optimize noise. Local hand transfer preserves body wrists and filters additional penetration.

**Input contract:** Keypoint tracking supplies future joint constraints. HOI uses object motion and a GRABNet grasp assumed stable during motion. Self-interaction uses LLM-derived contacts/timesteps; object motion is not generated.

**Evaluation checked:** HumanML3D tracking errors; MotionCritic body realism; fingertip/hand perception and self-interaction ablations. Standard text-motion FID/R-precision are not reported for its representation.

**Source locator:** §§3.1–3.5, 4.1–4.2, 5.1–5.4; Supplement §10

**Scope / curator boundary:** The object-guided application consumes object motion; it is not evidence for text-plus-initial-state dynamic interaction generation. Random hand/body combinations lack sequence-level semantic correlation. Stable-grasp assumption limits contact changes; controlled prior applications do not establish text+initial-state HOI generation.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2601.03959); checked 2026-11-19.

<a id="frankenmotion"></a>
## FrankenMotion: Part-level Human Motion Generation and Composition

**frankenmotion · 2026 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2601.10909) · [Evidence](https://arxiv.org/html/2601.10909v1) · Citekey: `frankenmotion2026`

**Authors of cited version:** Chuqiao Li; Xianghui Xie; Yong Cao; Andreas Geiger; Gerard Pons-Moll.

**Contribution / composition:** Learns hierarchical part/action/sequence-conditioned diffusion instead of test-time pose stitching.

**Mechanism:** CLIP action/part embeddings are PCA-reduced to 50 dimensions, expanded framewise and concatenated with noisy motion through an MLP; sequence and diffusion-step features are extra tokens. Unknown labels are zeroed; Beta-distributed random masking improves sparse-conditioning robustness.

**Input contract:** Temporally aligned, potentially sparse sequence, action and seven-body-part text; FrankenStein extends existing mocap annotations using LLM reasoning.

**Evaluation checked:** UniMotion, STMC and DART are adapted and retrained on FrankenStein using the same pose representation. Nine separate TMR-style evaluators assess seven parts, actions and sequences using R-Precision/M2T; realism uses FID/Diversity. Evaluations repeat 20 times with 95% confidence intervals. Annotation audit: 50 sequences, three experts.

**Source locator:** Sections 4.1–4.3; 5.1–5.2; 6; Eq. (2)–(4).

**Scope / curator boundary:** Authors explicitly cannot generate minute-long sequences in one pass. Label audit samples only 50 sequences; learned semantic metrics do not establish contact physics. LLM-generated part annotations and adapted benchmark baselines need auditing; abstract promises release rather than proving current reproducibility.

**Composition axes:** semantic, spatial, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2601.10909); checked 2026-11-19.

<a id="mixermdm"></a>
## MixerMDM: Learnable Composition of Human Motion Diffusion Models

**mixermdm · 2025 · Body-part & semantic composition · abstract**

[Primary source](https://arxiv.org/abs/2504.01019) · [Evidence](https://arxiv.org/abs/2504.01019) · Citekey: `mixermdm2025`

**Authors of cited version:** Pablo Ruiz-Ponce; German Barquero; Cristina Palmero; Sergio Escalera; José García-Rodríguez.

**Contribution / composition:** Learns adversarial dynamic mixing of pretrained single-person and interaction diffusion models.

**Scope / curator boundary:** Requires learning a mixer; model composition differs from constructing a reusable motion dataset.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2504.01019); checked 2026-11-19.

<a id="salad"></a>
## SALAD: Skeleton-aware Latent Diffusion for Text-driven Motion Generation and Editing

**salad · 2025 · Body-part & semantic composition · abstract**

[Primary source](https://arxiv.org/abs/2503.13836) · [Evidence](https://arxiv.org/abs/2503.13836) · Citekey: `salad2025`

**Authors of cited version:** Seokhyeon Hong; Chaelin Kim; Serin Yoon; Junghyun Nam; Sihun Cha; Junyong Noh.

**Contribution / composition:** Models joint-frame-word relationships and edits generated motion by cross-attention modulation without explicit user masks.

**Scope / curator boundary:** Zero-shot editing applies to a pretrained SALAD generator; source-motion editing and exact preservation need separate evaluation.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2503.13836); checked 2026-11-19.

<a id="demogen"></a>
## Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models

**demogen · 2025 · Body-part & semantic composition · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Towards_Decompositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Models_CVPR_2026_paper.pdf) · [Evidence](https://arxiv.org/html/2512.22324v1) · Citekey: `demogen2026`

**Authors of cited version:** Zhang, Jianrong; Fan, Hehe; Yang, Yi.

**Contribution / composition:** Trains compositional scores to reconstruct holistic motion without individual-concept motion targets.

**Mechanism:** Frozen-VAE motion latents are denoised with summed concept-conditioned predictions (latent-aware), or decomposed cross-attention (semantic-aware). Exp uses decomposed captions; OSS splits text embeddings with orthogonality; SC adds semantic consistency against decomposed embeddings.

**Input contract:** Exp requires decomposed text; OSS/SC infer concepts without decomposed inference prompts. DeCompML splits HumanML3D captions using GPT-4.1; default decomposition uses two concepts.

**Evaluation checked:** HumanML3D-pretrained models are directly evaluated on MTT and DeCompML. Exp handles multiple-text composition; OSS/SC handle single-text multi-concept generation. DeCompML combines decomposed captions with HumanML3D test motions and uses its text-motion evaluator. MTT reports R-Precision, TMR scores, FID and transition distance.

**Source locator:** Algorithm 1; Sections 3.2–3.4, 4.1–4.4; Table 2–3; Appendix F/Table 11.

**Scope / curator boundary:** Authors find Exp degrades for three/four text components as captions lack information. Component visualization is qualitative; it does not supply independent ground-truth primitive motions. No individual-concept motion ground truth is required, but semantic disentanglement remains an empirical claim; repository release checklist is incomplete.

**Publication / version note:** First preprint 26 December 2025; CVPR 2026 publication.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Towards_Decompositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Models_CVPR_2026_paper.html); checked 2026-11-19.

<a id="coma"></a>
## CoMA: Compositional Human Motion Generation with Multi-modal Agents

**coma · 2024 · Body-part & semantic composition · abstract**

[Primary source](https://arxiv.org/abs/2412.07320) · [Evidence](https://arxiv.org/abs/2412.07320) · Citekey: `coma2025`

**Authors of cited version:** Shanlin Sun; Gabriel De Araujo; Jiaqi Xu; Shenghan Zhou; Hanwen Zhang; Ziheng Huang; Chenyu You; Xiaohui Xie.

**Contribution / composition:** Collaborating language/vision agents control a part-specific masked motion generator and self-correction for detailed long prompts and editing.

**Scope / curator boundary:** Agent decomposition and visual self-critique add dependencies; user studies on rich prompts are distinct from benchmark distribution metrics.

**Publication / version note:** AAAI 40(11), 9206–9214; DOI 10.1609/aaai.v40i11.37878. Published author list differs from the arXiv record; bibliography below cites the arXiv version. First public preprint 2024; later venue not independently checked in this intake.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2412.07320); checked 2026-11-19.

<a id="energymogen"></a>
## EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space

**energymogen · 2024 · Body-part & semantic composition · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf) · [Evidence](https://arxiv.org/html/2412.14706v2) · Citekey: `energymogen2025`

**Authors of cited version:** Zhang, Jianrong; Fan, Hehe; Yang, Yi.

**Contribution / composition:** Combines latent and text-attention energy formulations for concept conjunction and negation.

**Mechanism:** Classifier-free diffusion predictions implement latent-aware energy composition. Cross-attention provides semantic-aware composition and adaptive text-embedding gradient updates; Synergistic Energy Fusion reconciles the two. Main inference uses five latent vectors and 50 diffusion steps.

**Input contract:** Multiple textual concepts, logical conjunction/negation; whole-motion latent representation rather than explicit per-frame body-part stitching.

**Evaluation checked:** HumanML3D/KIT-ML evaluate ordinary text generation. MTT compares combined single text against multiple-text composition using original constituent captions. Metrics follow STMC: R-Precision, TMR-Score, FID, transition distance. CompML contains 5,000 generated pairs from random triples of STMC captions, used with HumanML3D for augmentation experiments.

**Source locator:** Sections 3.1–3.2, 5.1–5.4; Eq. (3)–(4); Table 3; Appendix J/Figure 8.

**Scope / curator boundary:** Appendix J reports failure on completely novel concepts. MTT semantic/transition metrics and synthetic augmentation do not demonstrate real object-contact consistency. Energy composition and text attention are empirical control mechanisms; neither supplies a physical feasibility certificate.

**Publication / version note:** First preprint arXiv:2412.14706 in 2024; CVPR 2025.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.html); checked 2026-11-19.

<a id="parco"></a>
## ParCo: Part-Coordinating Text-to-Motion Synthesis

**parco · 2024 · Body-part & semantic composition · abstract**

[Primary source](https://arxiv.org/abs/2403.18512) · [Evidence](https://arxiv.org/abs/2403.18512) · Citekey: `parco2024`

**Authors of cited version:** Qiran Zou; Shangyuan Yuan; Shian Du; Yu Wang; Chang Liu; Yi Xu; Jie Chen; Xiangyang Ji.

**Contribution / composition:** Separate part tokenizers and lightweight generators communicate through a coordination module.

**Scope / curator boundary:** Part-factorized architecture is not itself evidence of arbitrary simultaneous action composition.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.18512); checked 2026-11-19.

<a id="amd-anatomical"></a>
## AMD:Anatomical Motion Diffusion with Interpretable Motion Decomposition and Fusion

**amd-anatomical · 2023 · Body-part & semantic composition · abstract**

[Primary source](https://arxiv.org/abs/2312.12763) · [Evidence](https://arxiv.org/abs/2312.12763) · Citekey: `amdanatomical2026`

**Authors of cited version:** Beibei Jing; Youjia Zhang; Zikai Song; Junqing Yu; Wei Yang.

**Contribution / composition:** Parses complex text into anatomical scripts and fuses script and text guidance in diffusion.

**Scope / curator boundary:** Depends on language-model decomposition quality; do not conflate with the unrelated Autoregressive Motion Diffusion AMD.

**Composition axes:** semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.12763); checked 2026-11-19.

<a id="sinc"></a>
## SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation

**sinc · 2023 · Body-part & semantic composition · method**

[Primary source](https://arxiv.org/abs/2304.10417) · [Evidence](https://openaccess.thecvf.com/content/ICCV2023/papers/Athanasiou_SINC_Spatial_Composition_of_3D_Human_Motions_for_Simultaneous_Action_ICCV_2023_paper.pdf) · Citekey: `sinc2024`

**Authors of cited version:** Nikos Athanasiou; Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** Studies simultaneous actions through body-part motion composition and synthetic training examples.

**Mechanism:** GPT-3 identifies active body parts; body-part motion combinations create synthetic examples for text-to-motion training.

**Input contract:** Text specifying simultaneous actions and a body-part inventory.

**Evaluation checked:** Compositional generation compared with baselines; improvement from synthetic part compositions is reported.

**Scope / curator boundary:** Kinematic body-part combination is not evidence of physics-valid contact-rich manipulation. Compatible part assignments do not guarantee physical feasibility or coherent object contact.

**Composition axes:** data, semantic, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.10417); checked 2026-11-19.

<a id="motionlab"></a>
## MotionLab: Unified Human Motion Generation and Editing via the Motion-Condition-Motion Paradigm

**motionlab · 2025 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2502.02358) · [Evidence](https://arxiv.org/abs/2502.02358) · Citekey: `motionlab2025`

**Authors of cited version:** Ziyan Guo; Zeyu Hu; De Wen Soh; Na Zhao.

**Contribution / composition:** Unifies generation and editing tasks through a motion-condition-motion formulation, including text, trajectory, style and in-between tasks.

**Scope / curator boundary:** Unified task coverage does not imply every task has equal supervision or generalization; inspect per-task protocol.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2502.02358); checked 2026-11-19.

<a id="bamm"></a>
## BAMM: Bidirectional Autoregressive Motion Model

**bamm · 2024 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2403.19435) · [Evidence](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02316.pdf) · Citekey: `bamm2024`

**Authors of cited version:** Ekkasit Pinyoanuntapong; Muhammad Usama Saleem; Pu Wang; Minwoo Lee; Srijan Das; Chen Chen.

**Contribution / composition:** Bidirectional autoregressive motion-token generation predicts ending and supports completion and long-sequence synthesis.

**Scope / curator boundary:** Long composition is an additional application; detailed semantics and transition protocol require separate checks.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.19435); checked 2026-11-19.

<a id="infinite-motion"></a>
## Infinite Motion: Extended Motion Generation via Long Text Instructions

**infinite-motion · 2024 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2407.08443) · [Evidence](https://arxiv.org/abs/2407.08443) · Citekey: `infinitemotion2024`

**Authors of cited version:** Mengtian Li; Chengshuo Zhai; Shengxiang Yao; Zhifeng Xie; Keyu Chen; Yu-Gang Jiang.

**Contribution / composition:** Extends and reassembles text-motion data, using timestamped text for long narrative generation, local editing and independent sequence splicing.

**Scope / curator boundary:** Reassembled benchmark construction must be distinguished from newly captured continuous long-motion ground truth.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2407.08443); checked 2026-11-19.

<a id="motionfix"></a>
## MotionFix: Text-Driven 3D Human Motion Editing

**motionfix · 2024 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2408.00712) · [Evidence](https://arxiv.org/abs/2408.00712) · Citekey: `motionfix2024`

**Authors of cited version:** Nikos Athanasiou; Alpár Cseke; Markos Diomataris; Michael J. Black; Gül Varol.

**Contribution / composition:** Collects source/target/edit-text triplets and trains TMED conditional diffusion; proposes retrieval-based editing evaluation.

**Scope / curator boundary:** Editing quality must jointly measure requested change and source preservation; retrieval metrics alone do not certify both.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2408.00712); checked 2026-11-19.

<a id="motionclr"></a>
## Pay Attention and Move Better: Harnessing Attention for Interactive Motion Generation and Training-free Editing

**motionclr · 2024 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2410.18977) · [Evidence](https://arxiv.org/abs/2410.18977) · Citekey: `motionclr2025`

**Authors of cited version:** Ling-Hao Chen; Shunlin Lu; Wenxun Dai; Zhiyang Dou; Xuan Ju; Jingbo Wang; Taku Komura; Lei Zhang.

**Contribution / composition:** MotionCLR explicitly models word-motion correspondence and manipulates attention for interactive generation edits.

**Scope / curator boundary:** Training-free editing refers to inference operations on a trained model, not absence of model training.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.18977); checked 2026-11-19.

<a id="mmm"></a>
## MMM: Generative Masked Motion Model

**mmm · 2023 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2312.03596) · [Evidence](https://arxiv.org/abs/2312.03596) · Citekey: `mmm2024`

**Authors of cited version:** Ekkasit Pinyoanuntapong; Pu Wang; Minwoo Lee; Chen Chen.

**Contribution / composition:** Text-conditioned masked motion tokens support in-betweening, body-part changes and long sequence synthesis.

**Scope / curator boundary:** Mask-defined edits require a clear preserved region; token reconstruction and motion preservation should be checked.

**Publication / version note:** First public preprint 2023.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.03596); checked 2026-11-19.

<a id="motionclip"></a>
## MotionCLIP: Exposing Human Motion Generation to CLIP Space

**motionclip · 2022 · Motion editing & in-betweening · abstract**

[Primary source](https://arxiv.org/abs/2203.08063) · [Evidence](https://arxiv.org/abs/2203.08063) · Citekey: `motionclip2022`

**Authors of cited version:** Guy Tevet; Brian Gordon; Amir Hertz; Amit H. Bermano; Daniel Cohen-Or.

**Contribution / composition:** Aligns a motion autoencoder with CLIP text and rendered-image embeddings to support semantic edits and interpolation.

**Scope / curator boundary:** Semantic latent arithmetic offers no strict preservation or physical-contact guarantee.

**Composition axes:** editing.

**Metadata:** official; [source](https://arxiv.org/bibtex/2203.08063); checked 2026-11-19.

<a id="holden-deep-motion"></a>
## A Deep Learning Framework for Character Motion Synthesis and Editing

**holden-deep-motion · 2016 · Motion editing & in-betweening · abstract**

[Primary source](https://www.research.ed.ac.uk/en/publications/a-deep-learning-framework-for-character-motion-synthesis-and-edit/) · [Evidence](https://www.ipab.inf.ed.ac.uk/cgvu/motionsynthesis.pdf) · Citekey: `holdendeepmotion2016`

**Authors of cited version:** Daniel Holden; Jun Saito; Taku Komura.

**Contribution / composition:** Convolutional motion manifolds support high-level trajectory generation and optimization for constraints and style transfer.

**Scope / curator boundary:** Learned kinematic naturalness does not ensure exact trajectory or physical validity.

**Composition axes:** editing.

**Metadata:** official; [source](https://www.research.ed.ac.uk/en/publications/a-deep-learning-framework-for-character-motion-synthesis-and-edit/); checked 2026-11-19.

<a id="momask"></a>
## MoMask: Generative Masked Modeling of 3D Human Motions

**momask · 2023 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2312.00063) · [Evidence](https://arxiv.org/abs/2312.00063) · Citekey: `momask2023`

**Authors of cited version:** Chuan Guo; Yuxuan Mu; Muhammad Gohar Javed; Sen Wang; Li Cheng.

**Contribution / composition:** Hierarchical residual quantization and masked token generation provide a discrete motion prior with text-guided temporal inpainting.

**Scope / curator boundary:** A useful backbone or inpainting capability does not by itself prove composition of independent skills or object-aware tasks. Discrete framewise tokens constrain joint-level editing granularity; baseline generation is not a full composition benchmark.

**Publication / version note:** First public preprint 2023.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.00063); checked 2026-11-19.

<a id="t2m-gpt"></a>
## T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations

**t2m-gpt · 2023 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2301.06052) · [Evidence](https://arxiv.org/abs/2301.06052) · Citekey: `t2mgpt2023`

**Authors of cited version:** Jianrong Zhang; Yangsong Zhang; Xiaodong Cun; Shaoli Huang; Yong Zhang; Hongwei Zhao; Hongtao Lu; Xi Shen.

**Contribution / composition:** CNN VQ-VAE with EMA/code reset and a text-conditioned GPT predicts discrete motion tokens.

**Scope / curator boundary:** Autoregressive token prediction is not equivalent to robust long multi-action generation; tokenizer limits editing precision.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2301.06052); checked 2026-11-19.

<a id="tmr"></a>
## TMR: Text-to-Motion Retrieval Using Contrastive 3D Human Motion Synthesis

**tmr · 2023 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2305.00976) · [Evidence](https://arxiv.org/abs/2305.00976) · Citekey: `tmr2023`

**Authors of cited version:** Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** Learns text-motion embeddings using contrastive retrieval and motion synthesis, supplying a retrieval benchmark and evaluator foundation.

**Scope / curator boundary:** Embedding similarity is evaluator-dependent and does not directly verify contact forces, exact action ordering or object-state effects. Retrieval alignment can miss foot sliding, contact failures or source-preservation errors; metric models are not physical evaluators.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.00976); checked 2026-11-19.

<a id="mld"></a>
## Executing Your Commands via Motion Diffusion in Latent Space

**mld · 2022 · Generative backbones & representations · abstract**

[Primary source](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.pdf) · Citekey: `mld2023`

**Authors of cited version:** Chen, Xin; Jiang, Biao; Liu, Wen; Huang, Zilong; Fu, Bin; Chen, Tao; Yu, Gang.

**Contribution / composition:** MLD compresses motions with a VAE before conditional latent diffusion, substantially reducing denoising cost.

**Scope / curator boundary:** Compact sequence latents obscure explicit frame/body-part correspondence for direct composition.

**Publication / version note:** First preprint arXiv:2212.04048 in 2022; CVPR 2023.

**Composition axes:** representation.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_Executing_Your_Commands_via_Motion_Diffusion_in_Latent_Space_CVPR_2023_paper.html); checked 2026-11-19.

<a id="mdm"></a>
## Human Motion Diffusion Model

**mdm · 2022 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2209.14916) · [Evidence](https://arxiv.org/abs/2209.14916) · Citekey: `mdm2022`

**Authors of cited version:** Guy Tevet; Sigal Raab; Brian Gordon; Yonatan Shafir; Daniel Cohen-Or; Amit H. Bermano.

**Contribution / composition:** MDM predicts clean motion samples in diffusion, facilitating geometric losses and text/action conditioning.

**Scope / curator boundary:** Short standalone kinematic generation provides a prior, not automatic long-sequence or physical-contact validation.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2209.14916); checked 2026-11-19.

<a id="motion-puzzle"></a>
## Motion Puzzle: Arbitrary Motion Style Transfer by Body Part

**motion-puzzle · 2022 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2202.05274) · [Evidence](https://arxiv.org/abs/2202.05274) · Citekey: `motionpuzzle2022`

**Authors of cited version:** Deok-Kyeong Jang; Soomin Park; Sung-Hee Lee.

**Contribution / composition:** Transfers multiple local motion styles to body parts using topology-aware features, AdaIN and attention without style labels or paired motions.

**Scope / curator boundary:** Style combination does not certify simultaneous action correctness or collision-free whole-body motion.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2202.05274); checked 2026-11-19.

<a id="motiondiffuse"></a>
## MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model

**motiondiffuse · 2022 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2208.15001) · [Evidence](https://arxiv.org/abs/2208.15001) · Citekey: `motiondiffuse2022`

**Authors of cited version:** Mingyuan Zhang; Zhongang Cai; Liang Pan; Fangzhou Hong; Xinying Guo; Lei Yang; Ziwei Liu.

**Contribution / composition:** Text-conditioned diffusion models human motion and provides a foundation for fine-grained guided synthesis.

**Scope / curator boundary:** Generation fidelity and semantic-control claims require matched datasets, representations and guidance settings.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2208.15001); checked 2026-11-19.

<a id="temos"></a>
## TEMOS: Generating diverse human motions from textual descriptions

**temos · 2022 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2204.14109) · [Evidence](https://arxiv.org/abs/2204.14109) · Citekey: `temos2022`

**Authors of cited version:** Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** Pairs motion VAE training with a text encoder that predicts compatible latent distributions; generates skeleton or SMPL motion.

**Scope / curator boundary:** Primary benchmark is KIT single descriptions; action transition and body-part composition need separate mechanisms.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2204.14109); checked 2026-11-19.

<a id="actor"></a>
## Action-Conditioned 3D Human Motion Synthesis with Transformer VAE

**actor · 2021 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2104.05670) · [Evidence](https://arxiv.org/abs/2104.05670) · Citekey: `actor2021`

**Authors of cited version:** Mathis Petrovich; Michael J. Black; Gül Varol.

**Contribution / composition:** ACTOR samples variable-duration SMPL sequences from categorical actions using a Transformer VAE.

**Scope / curator boundary:** Fixed action vocabulary; parallel output length depends on resources. No text-composition claim.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2104.05670); checked 2026-11-19.

<a id="skeleton-aware-retarget"></a>
## Skeleton-Aware Networks for Deep Motion Retargeting

**skeleton-aware-retarget · 2020 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2005.05732) · [Evidence](https://arxiv.org/abs/2005.05732) · Citekey: `skeletonawareretarget2020`

**Authors of cited version:** Kfir Aberman; Peizhuo Li; Dani Lischinski; Olga Sorkine-Hornung; Daniel Cohen-Or; Baoquan Chen.

**Contribution / composition:** Skeleton-aware convolutions and pooling map homeomorphic skeletons into a common primal-skeleton motion latent space.

**Scope / curator boundary:** Assumes homeomorphic skeleton graphs; arbitrary topology and contact/mesh consistency are separate problems.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2005.05732); checked 2026-11-19.

<a id="unpaired-style"></a>
## Unpaired Motion Style Transfer from Video to Animation

**unpaired-style · 2020 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/2005.05751) · [Evidence](https://arxiv.org/abs/2005.05751) · Citekey: `unpairedstyle2020`

**Authors of cited version:** Kfir Aberman; Yijia Weng; Dani Lischinski; Daniel Cohen-Or; Baoquan Chen.

**Contribution / composition:** Separates motion content and style, using AdaIN and shared 2D/3D style embeddings to transfer styles from animations or videos.

**Scope / curator boundary:** Training is unpaired but uses style labels; style/content disentanglement is empirical and not a guarantee of contact preservation.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/2005.05751); checked 2026-11-19.

<a id="language2pose"></a>
## Language2Pose: Natural Language Grounded Pose Forecasting

**language2pose · 2019 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/1907.01108) · [Evidence](https://arxiv.org/abs/1907.01108) · Citekey: `language2pose2019`

**Authors of cited version:** Chaitanya Ahuja; Louis-Philippe Morency.

**Contribution / composition:** Joint language-to-pose embedding is trained with a short-to-long curriculum for sentence-conditioned animation.

**Scope / curator boundary:** Pose forecasting quality and human semantic ratings differ from independent simultaneous-action coverage.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/1907.01108); checked 2026-11-19.

<a id="plappert-bidirectional"></a>
## Learning a bidirectional mapping between human whole-body motion and natural language using deep recurrent neural networks

**plappert-bidirectional · 2017 · Generative backbones & representations · abstract**

[Primary source](https://arxiv.org/abs/1705.06400) · [Evidence](https://arxiv.org/abs/1705.06400) · Citekey: `plappertbidirectional2018`

**Authors of cited version:** Matthias Plappert; Christian Mandery; Tamim Asfour.

**Contribution / composition:** Sequence-to-sequence RNN learns shared continuous language/motion representations without manual motion segmentation.

**Scope / curator boundary:** Single-sentence KIT evaluation does not establish arbitrary multi-action compositional generalization.

**Composition axes:** representation.

**Metadata:** official; [source](https://arxiv.org/bibtex/1705.06400); checked 2026-11-19.

<a id="cosmi"></a>
## COSMI: COmpositional Synthesis of Multi-object Interactions

**cosmi · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2610.03252) · [Evidence](https://arxiv.org/html/2610.03252v1) · Citekey: `cosmi2026`

**Authors of cited version:** Daniel Eskandar; Ilya A. Petrov; Gerard Pons-Moll.

**Contribution / composition:** Composes contact-local captured interactions and learns a text-conditioned multi-object diffusion model.

**Mechanism:** Transfer interacting body parts with their objects, use mirrored sources, semantic feasibility and geometric rejection; weight-shared object slots implement variable-count diffusion.

**Input contract:** Text and object conditions; composed sources provide body-part/object relationships for training.

**Evaluation checked:** Benchmark includes unseen interaction combinations and unseen object; text alignment and contact metrics compare models and dataset transfer.

**Scope / curator boundary:** Sustained interactions, rather than dependent multi-stage activities; prompt does not fix path/timing; finger precision remains limited. Synthetic dataset hours are not independent captured hours. Semantic/geometric gating is not force-based validation; release availability is separate.

**Composition axes:** data, object-contact, spatial.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.03252); checked 2026-11-19.

<a id="duethoi"></a>
## DuetHOI: Language-Guided Bimanual Hand--Object Motion Generation with Articulation Planning and Contact Refinement

**duethoi · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2603.08390v3) · [Evidence](https://arxiv.org/html/2603.08390v3) · Citekey: `duethoi2026`

**Authors of cited version:** Zhi Wang; Yuyan Liu; Liu liu; Ruonan Liu; Ruixuan Liu.

**Contribution / composition:** Contact intent and articulation planning condition structured hand/object generation; proximity refinement fixes objects while correcting hands.

**Mechanism:** ContactVAE samples contact intent; conditional-prior ArtPlanner predicts scalar articulation, ManiVAE compresses hands, and DualFormer couples token/time streams. ProxiRefine corrects hands while fixing generated object motion.

**Input contract:** Language, canonical geometry and initial articulation. ArtPlanner’s test reference is predicted from its conditional prior; its training posterior sees GT articulation. This is hand/object generation, without locomotion.

**Evaluation checked:** ARCTIC articulated/rigid and one/two-hand modes; GRAB rigid modes; adapted Text2HOI, LatentHOI and MDM; contact, hand/object errors, diversity and relative consistency; component/refinement ablations.

**Source locator:** Method: Articulation Trajectory Planning, Token-Temporal Interaction Generation, Object-Fixed Hand Refinement; Experiments; Conclusion: Limitations

**Scope / curator boundary:** Hand-centric scope; not whole-body locomotion. v3 replaces earlier StructBiHOI title under the same arXiv identity, so count one paper. One articulation scalar and one instruction at a time; explicitly excludes coupled joints and inter-task transitions. Phy/contact metrics do not establish executed physics. Same arXiv identity as earlier StructBiHOI revisions.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2603.08390); checked 2026-11-19.

<a id="trace"></a>
## Harnessing Coupled Stream Completion For Human-Object Interaction Modeling

**trace · 2026 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2609.32551) · [Evidence](https://arxiv.org/abs/2609.32551) · Citekey: `trace2026`

**Authors of cited version:** Dawei Guan; Di Yang; Jiangtao Wang.

**Contribution / composition:** TRACE retains body, object and hand latent streams while coupling their updates; decoded geometry constrains contacts and completion supports missing streams.

**Scope / curator boundary:** Cross-stream completion may provide future trajectories of other streams; information contracts must be distinguished from pure text generation.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2609.32551); checked 2026-11-19.

<a id="pami"></a>
## PAMI: Part Anchored Motion for Text to Human-Object Interaction Generation

**pami · 2026 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2609.38466) · [Evidence](https://arxiv.org/abs/2609.38466) · Citekey: `pami2026`

**Authors of cited version:** Chuqiao Li; Xianghui Xie; Yong Cao; Andreas Geiger; Gerard Pons-Moll.

**Contribution / composition:** Body-part-relative object votes structure a latent interaction model; coarse generation is followed by contact-oriented surface refinement.

**Scope / curator boundary:** Reported gains concern InterAct comparison settings; body-part anchoring is not evidence of unrestricted multi-object or articulated planning.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2609.38466); checked 2026-11-19.

<a id="sk-hoi"></a>
## Surface Keypoint Representation for Multi-Object and Articulated Human-Object Interaction Generation

**sk-hoi · 2026 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2608.03158) · [Evidence](https://arxiv.org/html/2608.03158v1) · Citekey: `skhoi2026`

**Authors of cited version:** Xiaogang Peng; Zeyu Han; Zichong Meng; Yiming Xie; Jihua Zhu; Gang Hua; Huaizu Jiang.

**Contribution / composition:** Represents rigid components with surface-keypoint trajectories, predicts spatiotemporal contact-distance fields and synthesizes contact-guided whole-body motion.

**Mechanism:** Three transformer/flow-matching stages generate rigid-component keypoints, contact-distance fields and body markers; inference optimizes body diffusion noise against contact and object-SDF penetration losses.

**Input contract:** Text, object BPS geometry and initial human/object state; alternatives supply sparse object waypoints or full future object trajectories. Main generated object paths are predictions, not automatically GT.

**Evaluation checked:** ParaHome, HIMO, ARCTIC and OMOMO; FID, text alignment, foot sliding, interaction geometry/contact and object jerk; representation/contact ablations.

**Source locator:** §§3.1–3.2; 4.1–4.4; Appendix B metrics and G failure cases

**Scope / curator boundary:** Three-stage pipeline; point trajectories avoid explicit joint types but do not inherently certify articulation mechanics. Authors report remaining floating/penetration. Contact optimization costs approximately four minutes per 124 frames; geometric representation is not force/dynamics certification.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2608.03158); checked 2026-11-19.

<a id="dechoi"></a>
## Decoupled Generative Modeling for Human-Object Interaction Synthesis

**dechoi · 2025 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2512.19049) · [Evidence](https://arxiv.org/html/2512.19049v1) · Citekey: `dechoi2026`

**Authors of cited version:** Hwanhee Jung; Seunggwan Lee; Jeongyoon Yoon; SeungHyeon Kim; Giljoo Nam; Qixing Huang; Sangpil Kim.

**Contribution / composition:** DecHOI separates goal-conditioned trajectory planning from contact-oriented action generation.

**Mechanism:** Trajectory diffusion generates human/object paths; action diffusion then conditions densely on these predicted positions. Distal-joint adversarial training and reconstruction guidance target contact and grounded feet.

**Input contract:** Text, object BPS geometry, first human/object poses and final object position. Intermediate waypoints are not prescribed. Action-stage paths are TG predictions; Appendix E.3 separately gives all-frame GT paths as an oracle.

**Evaluation checked:** FullBodyManipulation and unseen same-category 3D-FUTURE geometry; condition/contact/motion/GT errors, ablations, perception study and DynaPlan dynamic planning.

**Source locator:** §§3.2–3.4, 4.1–4.7; Appendices E.2–E.3 and J

**Scope / curator boundary:** Rigid-object scope; DynaPlan supports one manipulated object and one moving obstacle. No explicit physical simulation guarantee; articulated/deformable dynamics remain future work.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2512.19049); checked 2026-11-19.

<a id="hoifhli"></a>
## Human-Object Interaction from Human-Level Instructions

**hoifhli · 2025 · Human-object & articulated interaction · method**

[Primary source](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_Human-Object_Interaction_from_Human-Level_Instructions_ICCV_2025_paper.pdf) · [Evidence](https://arxiv.org/html/2406.17840v3) · Citekey: `hoifhli2025`

**Authors of cited version:** Wu, Zhen; Li, Jiaman; Xu, Pei; Liu, C. Karen.

**Contribution / composition:** Language planning orchestrates contextual full-body manipulation with finger interactions and RL reference tracking.

**Mechanism:** LLM scene planning and A* navigation feed CoarseNet; predicted contact phases drive grasp generation, wrist-relative RefineNet and FingerNet. RL separately tracks the generated reference.

**Input contract:** Full system: instruction, scene/assets and initial states. Low-level CoarseNet additionally requires final object pose and 2D waypoints every 30 frames; planner-generated conditions must be distinguished from GT-extracted paths.

**Evaluation checked:** FullBodyManipulation low-level comparisons include CHOIS+GRIP; waypoint, foot, hand/object contact, intersection and pose metrics plus perception study; physics tracker is evaluated separately.

**Source locator:** §§4, 5.2.1–5.3, 6, 7.2–7.3; Appendix B.5 and C

**Scope / curator boundary:** Planner-generated targets and physics tracking are additional system components and conditions; not a single end-to-end text-only generator. Reference-conditioned physics tracking is not a general reference-free policy. Future target/path conditions are supplied; environmental perception remains a future-work direction.

**Composition axes:** object-contact, scene-state, temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_Human-Object_Interaction_from_Human-Level_Instructions_ICCV_2025_paper.html); checked 2026-11-19.

<a id="interact"></a>
## InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation

**interact · 2025 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2509.09555) · [Evidence](https://arxiv.org/abs/2509.09555) · Citekey: `interact2025`

**Authors of cited version:** Sirui Xu; Dongting Li; Yucheng Zhang; Xiyan Xu; Qi Long; Ziyin Wang; Yunzhi Lu; Shuchang Dong; Hezi Jiang; Akshat Gupta; Yu-Xiong Wang; Liang-Yan Gui.

**Contribution / composition:** Consolidates HOI sources, refines artifacts and hands, augments under contact invariance, and benchmarks six generation/completion tasks.

**Scope / curator boundary:** Augmentation preserves existing interaction intent and cannot be assumed to add new task semantics; source ancestry matters for evaluation.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.09555); checked 2026-11-19.

<a id="interactmove"></a>
## InteractMove: Text-Controlled Human-Object Interaction Generation in 3D Scenes with Movable Objects

**interactmove · 2025 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2509.23612) · [Evidence](https://cxhcmhhh.github.io/InteractMoveProject/static/pdfs/paper.pdf) · Citekey: `interactmove2025`

**Authors of cited version:** Xinhao Cai; Minghang Zheng; Xin Jin; Yang Liu.

**Contribution / composition:** Aligns HOI recordings with scenes containing movable objects and spatial distractors to study text-grounded contextual manipulation.

**Scope / curator boundary:** Aligned/synthetic scene contexts should be distinguished from newly captured scene-conditioned interaction data.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.23612); checked 2026-11-19.

<a id="primhoi"></a>
## PrimHOI: Compositional Human-Object Interaction via Reusable Primitives

**primhoi · 2025 · Human-object & articulated interaction · method**

[Primary source](https://openaccess.thecvf.com/content/ICCV2025/html/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.html) · [Evidence](https://kairobo.github.io/PrimHOI/) · Citekey: `primhoi2025`

**Authors of cited version:** Jia, Kai; Liu, Tengyu; Pei, Mingtao; Zhu, Yixin; Huang, Siyuan.

**Contribution / composition:** Composes relative-geometry interaction primitives spatially and temporally through hierarchical planning, targeting unseen multi-object tasks.

**Mechanism:** Author method overview: LLM compiles a task into PDDL-HOI; symbolic planning yields subgoal graphs. Primitive contact factors generate key poses; object paths precede contact-guided intermediate human motion and constraint post-optimization.

**Input contract:** Task description, scene/object geometry and symbolic domain knowledge; planned subgoals and object/contact trajectories are internal generated conditions, not a claim of text+initial-state-only direct diffusion.

**Evaluation checked:** Official page demonstrates four primitive contact modes, varied shapes/placements and three extended plans. Detailed quantitative evaluation was not re-audited because CVF PDF fetch returned 403.

**Source locator:** Author page: Method Overview, The Three Long Plans, Results; CVF abstract. Full PDF inaccessible via browser tool.

**Scope / curator boundary:** Reusable primitive planning should be separated from learned unified sequence generation; broad zero-shot claims need the paper-specific task protocol. Evidence here is the author’s method overview, not a completed full-paper audit. Linked official repository exposes only README/LICENSE as checked; its URL does not establish released runnable implementation.

**Composition axes:** object-contact, scene-state, temporal.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/ICCV2025/html/Jia_PrimHOI_Compositional_Human-Object_Interaction_via_Reusable_Primitives_ICCV_2025_paper.html); checked 2026-11-19.

<a id="himo"></a>
## HIMO: A New Benchmark for Full-Body Human Interacting with Multiple Objects

**himo · 2024 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2407.12371) · [Evidence](https://arxiv.org/html/2407.12371v1) · Citekey: `himo2024`

**Authors of cited version:** Xintao Lv; Liang Xu; Yichao Yan; Xin Jin; Congsheng Xu; Shuwen Wu; Yifan Liu; Lincheng Li; Mengxiao Bi; Wenjun Zeng; Xiaokang Yang.

**Contribution / composition:** Multi-object full-body mocap with text and temporal segments; diffusion branches and autoregressive segments support timeline control.

**Mechanism:** Dual human/object diffusion branches exchange information through mutual interaction; segmented generation conditions later intervals on preceding motion.

**Input contract:** Whole or segmented text prompts, object geometry and initial states; temporal segments supply fine control.

**Evaluation checked:** HIMO generation, temporal composition and unseen geometry experiments; history-context and model-component ablations.

**Scope / curator boundary:** Abstract reports unseen geometry and temporal composition, but exact split leakage and metrics require full protocol review. Two/three-object captured setting and explicit segment schedules restrict the demonstrated composition contract.

**Composition axes:** object-contact, spatial, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2407.12371); checked 2026-11-19.

<a id="cg-hoi"></a>
## CG-HOI: Contact-Guided 3D Human-Object Interaction Generation

**cg-hoi · 2023 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2311.16097) · [Evidence](https://arxiv.org/abs/2311.16097) · Citekey: `cghoi2024`

**Authors of cited version:** Christian Diller; Angela Dai.

**Contribution / composition:** Joint diffusion with cross-attention models human motion, object motion and surface contact; predicted contact guides inference.

**Scope / curator boundary:** Contact-based physical plausibility remains distinct from dynamic simulation; abstract does not establish arbitrary multi-object composition.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2311.16097); checked 2026-11-19.

<a id="chois"></a>
## Controllable Human-Object Interaction Synthesis

**chois · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2312.03913) · [Evidence](https://arxiv.org/html/2312.03913v2) · Citekey: `chois2024`

**Authors of cited version:** Jiaman Li; Alexander Clegg; Roozbeh Mottaghi; Jiajun Wu; Xavier Puig; C. Karen Liu.

**Contribution / composition:** Joint human/object/contact diffusion combines geometry supervision with contact guidance and connects to planning for extended manipulation.

**Mechanism:** Transformer denoises synchronized human poses, object poses and hand-contact labels; object geometry loss improves waypoint adherence and sampling guidance constrains contacts.

**Input contract:** Language, object BPS geometry, initial human/object state, 2D object positions every 30 frames and final 3D object position.

**Evaluation checked:** OMOMO manipulation benchmark, unseen-object analysis, motion/contact/waypoint metrics, guidance ablations and scene-planner demonstrations.

**Scope / curator boundary:** Sparse future waypoints are required conditions; guidance is not a force-based execution guarantee.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.03913); checked 2026-11-19.

<a id="interdiff"></a>
## InterDiff: Generating 3D Human-Object Interactions with Physics-Informed Diffusion

**interdiff · 2023 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2308.16905) · [Evidence](https://arxiv.org/abs/2308.16905) · Citekey: `interdiff2023`

**Authors of cited version:** Sirui Xu; Zhengyuan Li; Yu-Xiong Wang; Liang-Yan Gui.

**Contribution / composition:** Interaction diffusion forecasts human/object motion and a physics-informed correction predictor refines denoised interactions.

**Scope / curator boundary:** Future prediction conditioned on observed interaction differs from unconstrained text-to-interaction generation.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2308.16905); checked 2026-11-19.

<a id="omomo"></a>
## Object Motion Guided Human Motion Synthesis

**omomo · 2023 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2309.16237) · [Evidence](https://arxiv.org/abs/2309.16237) · Citekey: `omomo2023`

**Authors of cited version:** Jiaman Li; Jiajun Wu; C. Karen Liu.

**Contribution / composition:** Two diffusion stages infer hand positions and full-body manipulation from object motion, with hand contact as an intermediate constraint.

**Scope / curator boundary:** Requires the object trajectory; this is a stronger condition than text and initial state. Single manipulated rigid-object scope.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2309.16237); checked 2026-11-19.

<a id="procigen"></a>
## Template Free Reconstruction of Human-object Interaction with Procedural Interaction Generation

**procigen · 2023 · Human-object & articulated interaction · method**

[Primary source](https://arxiv.org/abs/2312.07063) · [Evidence](https://arxiv.org/html/2312.07063) · Citekey: `procigen2024`

**Authors of cited version:** Xianghui Xie; Bharat Lal Bhatnagar; Jan Eric Lenssen; Gerard Pons-Moll.

**Contribution / composition:** Procedurally creates varied human-object interaction pairs and trains an image-conditioned reconstruction model for unseen objects.

**Mechanism:** Category-specific autoencoder correspondences transfer contacts to replacement objects; joint pose optimization preserves contact and reduces collisions, followed by textured rendering. HDM reconstructs joint then separate human/object point clouds.

**Input contract:** Data synthesis requires captured seed interaction poses and same-category replacement geometry. HDM takes one RGB image without an object template; output is static shape/interaction reconstruction.

**Evaluation checked:** BEHAVE/InterCap reconstruction F-score at 1 cm, data/model ablations, cross-dataset and unseen-shape/category evaluation.

**Source locator:** §§3.1.1–3.1.4, 3.2, 4.1–4.4; Appendix A.3 and C

**Scope / curator boundary:** Interaction-pair synthesis and reconstruction are distinct from continuous motion composition; static data counts must not be reported as motion hours. Static pairs/images, not motion sequences or motion hours. Seed poses limit diversity; occluded-body shape recovery remains difficult. HDM does not handle multi-person/multi-object interactions.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.07063); checked 2026-11-19.

<a id="imos"></a>
## IMos: Intent-Driven Full-Body Motion Synthesis for Human-Object Interactions

**imos · 2022 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2212.07555) · [Evidence](https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.14739) · Citekey: `imos2023`

**Authors of cited version:** Anindita Ghosh; Rishabh Dabral; Vladislav Golyanik; Christian Theobalt; Philipp Slusallek.

**Contribution / composition:** Intent-object text encoding and separate variational autoregressors coordinate arms and body for full-body object interaction.

**Scope / curator boundary:** Intent/action conditioning and near-object motion domain differ from autonomous scene planning.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.07555); checked 2026-11-19.

<a id="goal"></a>
## GOAL: Generating 4D Whole-Body Motion for Hand-Object Grasping

**goal · 2021 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2112.11454) · [Evidence](https://arxiv.org/abs/2112.11454) · Citekey: `goal2023`

**Authors of cited version:** Omid Taheri; Vasileios Choutas; Michael J. Black; Dimitrios Tzionas.

**Contribution / composition:** GNet predicts a whole-body goal grasp and MNet produces approach motion with coordinated hands, head and body.

**Scope / curator boundary:** Near-object starting configuration and grasp endpoint focus; not an extended manipulate-release-navigation system.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2112.11454); checked 2026-11-19.

<a id="saga"></a>
## SAGA: Stochastic Whole-Body Grasping with Contact

**saga · 2021 · Human-object & articulated interaction · abstract**

[Primary source](https://arxiv.org/abs/2112.10103) · [Evidence](https://arxiv.org/abs/2112.10103) · Citekey: `saga2022`

**Authors of cited version:** Yan Wu; Jiahao Wang; Yan Zhang; Siwei Zhang; Otmar Hilliges; Fisher Yu; Siyu Tang.

**Contribution / composition:** Generates whole-body grasping motions using contact as a coordination signal.

**Scope / curator boundary:** Grasping-specific domain; broader scene-aware long-task composition not established by the checked abstract.

**Composition axes:** object-contact.

**Metadata:** official; [source](https://arxiv.org/bibtex/2112.10103); checked 2026-11-19.

<a id="world2hosi"></a>
## World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation

**world2hosi · 2026 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2610.27725) · [Evidence](https://arxiv.org/html/2610.27725v1) · Citekey: `world2hosi2026`

**Authors of cited version:** Jiushu Li; Haoran Wang; Yumeng Liu; Zhiyang Dou; Yuan Liu; Yuexin Ma; Cheng Lin.

**Contribution / composition:** Orchestrates navigation, object and scene interaction experts around persistent scene state, reconciling boundaries and updating object effects.

**Mechanism:** Structured MotionIR and state updates compile expert conditions; incoming-prefix translation/SO(3) offsets decay with quintic smoothstep. Bounded residual RL tracks references and objects move through simulated contacts.

**Input contract:** Language, reconstructed scene/background and object assets, expert-specific initial/goal/path conditions produced by the harness.

**Evaluation checked:** Shared tasks versus external systems, user study, fixed-segment boundary ablation, reference-tracking errors and state-dependent multi-stage demonstrations.

**Scope / curator boundary:** Bounded residuals cannot rescue fundamentally infeasible references; reported task success and tracking error are specific to the evaluated system.

**Composition axes:** object-contact, scene-state, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.27725); checked 2026-11-19.

<a id="trumans"></a>
## Scaling Up Dynamic Human-Scene Interaction Modeling

**trumans · 2024 · Human-scene interaction & planning · abstract**

[Primary source](https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.pdf) · Citekey: `trumans2024`

**Authors of cited version:** Jiang, Nan; Zhang, Zhiyuan; Li, Hongjie; Ma, Xiaoxuan; Wang, Zan; Chen, Yixin; Liu, Tengyu; Zhu, Yixin; Huang, Siyuan.

**Contribution / composition:** TRUMANS captures human and part-level dynamic-object interaction across indoor scene configurations; autoregressive diffusion supports extended motion synthesis.

**Scope / curator boundary:** Arbitrary output length is not equivalent to reliable arbitrary task planning or independent physical execution.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Scaling_Up_Dynamic_Human-Scene_Interaction_Modeling_CVPR_2024_paper.html); checked 2026-11-19.

<a id="circle"></a>
## CIRCLE: Capture In Rich Contextual Environments

**circle · 2023 · Human-scene interaction & planning · abstract**

[Primary source](https://arxiv.org/abs/2303.17912) · [Evidence](https://arxiv.org/abs/2303.17912) · Citekey: `circle2023`

**Authors of cited version:** Joao Pedro Araujo; Jiaman Li; Karthik Vetrivel; Rishi Agarwal; Deepak Gopinath; Jiajun Wu; Alexander Clegg; C. Karen Liu.

**Contribution / composition:** Captures real human movement in perceived virtual scenes and learns scene-conditioned full-body reaching.

**Scope / curator boundary:** Reaching and virtual-context collection do not establish contact-force-realistic general manipulation.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2303.17912); checked 2026-11-19.

<a id="scenediffuser"></a>
## Diffusion-based Generation, Optimization, and Planning in 3D Scenes

**scenediffuser · 2023 · Human-scene interaction & planning · abstract**

[Primary source](https://arxiv.org/abs/2301.06015) · [Evidence](https://arxiv.org/abs/2301.06015) · Citekey: `scenediffuser2023`

**Authors of cited version:** Siyuan Huang; Zan Wang; Puhao Li; Baoxiong Jia; Tengyu Liu; Yixin Zhu; Wei Liang; Song-Chun Zhu.

**Contribution / composition:** SceneDiffuser combines scene-conditioned diffusion with differentiable optimization and goal-oriented planning across human motion, pose, grasp and navigation tasks.

**Scope / curator boundary:** Separate task demonstrations do not by themselves prove a unified long-horizon full-body manipulation system.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2301.06015); checked 2026-11-19.

<a id="occupancy"></a>
## Revisit Human-Scene Interaction via Space Occupancy

**occupancy · 2023 · Human-scene interaction & planning · abstract**

[Primary source](https://arxiv.org/abs/2312.02700) · [Evidence](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06630.pdf) · Citekey: `occupancy2024`

**Authors of cited version:** Xinpeng Liu; Haowen Hou; Yanchao Yang; Yong-Lu Li; Cewu Lu.

**Contribution / composition:** Uses space occupancy to connect locomotion and interaction control; evaluates reaching and extended indoor action sequences.

**Scope / curator boundary:** Hand-trajectory-controlled manipulation is a stronger contract than text plus initial state; generation metrics do not certify dynamics.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.02700); checked 2026-11-19.

<a id="dimos"></a>
## Synthesizing Diverse Human Motions in 3D Indoor Scenes

**dimos · 2023 · Human-scene interaction & planning · method**

[Primary source](https://arxiv.org/abs/2305.12411) · [Evidence](https://arxiv.org/html/2305.12411v3) · Citekey: `dimos2023`

**Authors of cited version:** Kaifeng Zhao; Yan Zhang; Shaofei Wang; Thabo Beeler; Siyu Tang.

**Contribution / composition:** DIMOS uses learned motion primitives and scene-aware policies to navigate and perform successive furniture interactions.

**Mechanism:** Policies select latent actions of generative motion primitives; navigation uses walkability features and waypoints, interaction uses SDF proximity and marker goals.

**Input contract:** Scene geometry, navigation goals/path waypoints and fine-grained target body markers; interaction goals can be generated by COINS.

**Evaluation checked:** Locomotion and fine-grained interaction benchmarks, varied object geometry/orientation and body starts, interaction-sequence demonstrations and feature/reward ablations.

**Scope / curator boundary:** Main interactions are static-scene sitting/lying; RL over motion latents should not be equated to force-based humanoid control.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.12411); checked 2026-11-19.

<a id="coins"></a>
## Compositional Human-Scene Interaction Synthesis with Semantic Control

**coins · 2022 · Human-scene interaction & planning · abstract**

[Primary source](https://arxiv.org/abs/2207.12824) · [Evidence](https://arxiv.org/abs/2207.12824) · Citekey: `coins2022`

**Authors of cited version:** Kaifeng Zhao; Shaofei Wang; Yan Zhang; Thabo Beeler; Siyu Tang.

**Contribution / composition:** COINS encodes body surface points and objects in a joint latent space, permitting multiple atomic action-object pairs without corresponding composite training examples.

**Scope / curator boundary:** Primarily interaction pose synthesis; simultaneous semantic composition should not be confused with continuous long-task generation.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2207.12824); checked 2026-11-19.

<a id="samp"></a>
## Stochastic Scene-Aware Motion Prediction

**samp · 2021 · Human-scene interaction & planning · abstract**

[Primary source](https://arxiv.org/abs/2108.08284) · [Evidence](https://arxiv.org/abs/2108.08284) · Citekey: `samp2021`

**Authors of cited version:** Mohamed Hassan; Duygu Ceylan; Ruben Villegas; Jun Saito; Jimei Yang; Yi Zhou; Michael Black.

**Contribution / composition:** Stochastic scene-aware motion generation combines cluttered navigation and diverse target-object interaction styles.

**Scope / curator boundary:** Captured sitting/lying/walking/running domain; does not establish dexterous dynamic multi-object manipulation.

**Composition axes:** scene-state.

**Metadata:** official; [source](https://arxiv.org/bibtex/2108.08284); checked 2026-11-19.

<a id="pigraphs"></a>
## PiGraphs: Learning Interaction Snapshots from Observations

**pigraphs · 2016 · Human-scene interaction & planning · abstract**

[Primary source](https://graphics.stanford.edu/projects/pigraphs/) · [Evidence](https://graphics.stanford.edu/projects/pigraphs/) · Citekey: `pigraphs2016`

**Authors of cited version:** Manolis Savva; Angel X. Chang; Pat Hanrahan; Matthew Fisher; Matthias Nießner.

**Contribution / composition:** Probabilistic prototype interaction graphs couple body poses, object geometry, contact and visual attention for scene and pose synthesis.

**Scope / curator boundary:** Static interaction snapshots rather than continuous motion sequences.

**Composition axes:** scene-state.

**Metadata:** primary-transcribed; [source](https://graphics.stanford.edu/projects/pigraphs/); checked 2026-11-19.

<a id="core4d"></a>
## CORE4D: A 4D Human-Object-Human Interaction Dataset for Collaborative Object REarrangement

**core4d · 2025 · Multi-person & collaborative interaction · abstract**

[Primary source](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.pdf) · Citekey: `core4d2025`

**Authors of cited version:** Liu, Yun; Zhang, Chengwen; Xing, Ruofan; Tang, Bingda; Yang, Bowen; Yi, Li.

**Contribution / composition:** Combines real collaborative object rearrangement recordings with collaboration retargeting to additional object shapes.

**Scope / curator boundary:** Synthetic retargeted sequences are not independent real captures; collaborative manipulation differs from unconstrained social interaction.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.html); checked 2026-11-19.

<a id="hhoi-text"></a>
## Learning to Generate Human-Human-Object Interactions from Textual Descriptions

**hhoi-text · 2025 · Multi-person & collaborative interaction · abstract**

[Primary source](https://arxiv.org/abs/2511.20446) · [Evidence](https://arxiv.org/abs/2511.20446) · Citekey: `hhoitext2026`

**Authors of cited version:** Jeonghyeon Na; Sangwon Baik; Inhee Lee; Junyoung Lee; Hanbyul Joo.

**Contribution / composition:** Integrates individual HOI and HHI diffusion models through a shared sampling framework to synthesize object-mediated multi-human interactions.

**Scope / curator boundary:** Composition depends on compatibility of separately trained distributions; abstract alone does not establish persistent scene-state correctness.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2511.20446); checked 2026-11-19.

<a id="freemotion"></a>
## FreeMotion: A Unified Framework for Number-free Text-to-Motion Synthesis

**freemotion · 2024 · Multi-person & collaborative interaction · abstract**

[Primary source](https://arxiv.org/abs/2405.15763) · [Evidence](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01249.pdf) · Citekey: `freemotion2024`

**Authors of cited version:** Ke Fan; Junshu Tang; Weijian Cao; Ran Yi; Moran Li; Jingyu Gong; Jiangning Zhang; Yabiao Wang; Chengjie Wang; Lizhuang Ma.

**Contribution / composition:** Factorizes conditional motion generation into generation and interaction modules to support variable participant counts and spatial controls.

**Scope / curator boundary:** Number-free formulation does not establish unlimited-scene scalability or collision-free arbitrary crowded interaction.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2405.15763); checked 2026-11-19.

<a id="intermask"></a>
## InterMask: 3D Human Interaction Generation via Collaborative Masked Modeling

**intermask · 2024 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2410.10010) · [Evidence](https://arxiv.org/html/2410.10010) · Citekey: `intermask2025`

**Authors of cited version:** Muhammad Gohar Javed; Chuan Guo; Li Cheng; Xingyu Li.

**Contribution / composition:** Collaboratively predicts masked discrete motion tokens for two people and also supports reaction generation.

**Mechanism:** Shared 2D VQ-VAE preserves spatial/temporal tokens; collaborative transformer combines self, spatiotemporal and cross-person attention. Iterative confidence remasking generates both actors jointly.

**Input contract:** Main task: text with both actors initially masked. Reaction: full reference actor motion stays unmasked, with optional text; this is future actor-conditioned completion, not a demonstrated causal online policy.

**Evaluation checked:** InterHuman/InterX FID, R-precision, MMDist, diversity/multimodality; attention/masking/tokenizer ablations, reaction tests and user study.

**Source locator:** §§3.1–3.3, 4.1–4.3, 5; Appendices I and J

**Scope / curator boundary:** Two-person interaction and reaction generation do not by themselves establish arbitrary actor-count or object-state task composition. Mesh conversion can reveal inter-person penetration; rapid actions can jerk; dataset dance bias remains. Two-person generation does not establish arbitrary population or persistent object-state reasoning.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.10010); checked 2026-11-19.

<a id="inter-x"></a>
## Inter-X: Towards Versatile Human-Human Interaction Analysis

**inter-x · 2023 · Multi-person & collaborative interaction · abstract**

[Primary source](https://arxiv.org/abs/2312.16051) · [Evidence](https://arxiv.org/abs/2312.16051) · Citekey: `interx2023`

**Authors of cited version:** Liang Xu; Xintao Lv; Yichao Yan; Xin Jin; Shuwen Wu; Congsheng Xu; Yifan Liu; Yizhou Zhou; Fengyun Rao; Xingdong Sheng; Yunhui Liu; Wenjun Zeng; Xiaokang Yang.

**Contribution / composition:** Captured full-body interactions with hand gestures and detailed part-level text support perceptual and generative benchmarking.

**Scope / curator boundary:** Dataset/benchmark contribution; dataset coverage is not evidence of arbitrary compositional generalization.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2312.16051); checked 2026-11-19.

<a id="intergen"></a>
## InterGen: Diffusion-based Multi-human Motion Generation under Complex Interactions

**intergen · 2023 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2304.05684) · [Evidence](https://arxiv.org/html/2304.05684v3) · Citekey: `intergen2024`

**Authors of cited version:** Han Liang; Wenqian Zhang; Wenxuan Li; Jingyi Yu; Lan Xu.

**Contribution / composition:** Two cooperative weight-sharing denoisers exchange mutual attention to generate coordinated two-person motion from text.

**Mechanism:** Shared denoisers, mutual attention, world-frame joint representation and spatial-relation regularization with damping preserve interpersonal coordination.

**Input contract:** Natural-language description; downstream editing/completion variants supply additional motion conditions.

**Evaluation checked:** InterHuman text-to-interaction benchmark, generation quality/diversity and text alignment comparisons, representation/regularization ablations and editing applications.

**Scope / curator boundary:** Demonstrated two-person contract; skeletal relations and proximity losses are not explicit contact dynamics.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.05684); checked 2026-11-19.

<a id="remos"></a>
## ReMoS: 3D Motion-Conditioned Reaction Synthesis for Two-Person Interactions

**remos · 2023 · Multi-person & collaborative interaction · method**

[Primary source](https://arxiv.org/abs/2311.17057) · [Evidence](https://arxiv.org/html/2311.17057v2) · Citekey: `remos2024`

**Authors of cited version:** Anindita Ghosh; Rishabh Dabral; Vladislav Golyanik; Christian Theobalt; Philipp Slusallek.

**Contribution / composition:** Spatiotemporal cross-attention generates a second person’s body and hand response to a given actor motion; contributes ReMoCap.

**Mechanism:** Cascaded diffusion first generates reactive body joints using joint spatiotemporal cross-attention, then hands with proximity-derived interaction masks; reaction/kinematic losses and inference guidance improve alignment.

**Input contract:** Complete actor body/hand motion over the target interval is supplied. Reactor motion is generated; this is future actor-conditioned completion rather than two-person generation from text or causal online reaction.

**Evaluation checked:** ReMoCap Lindy Hop/Ninjutsu, 2C and ExPI; MPJPE/velocity error, body/hand FID, diversity, ablations and user study; appendix adds InterHuman comparisons.

**Source locator:** §§3.1–3.4; 5.1–5.5; Appendix B preparation and C.1

**Scope / curator boundary:** Requires actor motion; reactive completion is a different task from jointly synthesizing both actors from text. Fast contact-heavy sequences can misalign spatially, motivating guidance. Proximity-based hand masks do not establish actual physical contact or force feasibility.

**Composition axes:** multi-person.

**Metadata:** official; [source](https://arxiv.org/bibtex/2311.17057); checked 2026-11-19.

<a id="hiphi"></a>
## HiPHI: A Large-Scale Benchmark for High-Precision Human Motion and Object-Interaction

**hiphi · 2026 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2608.16222) · [Evidence](https://arxiv.org/abs/2608.16222) · Citekey: `hiphi2026`

**Authors of cited version:** Jiahao Ji; Ji Ma; Runhan Zhang; Runyi Yu; Wenjia Wang; Weiheng Chi; Qianqian Peng; Weichao Yan; Yongfei Gu; Ye Tian; Ting Wu; Longwei Li; Chun Yuan; Ruoli Dai; Lei Han.

**Contribution / composition:** Optical whole-body motion and mesh-level object trajectories organized for broad primitive coverage; evaluates diversity, grounding and consistency.

**Scope / curator boundary:** Dataset coverage is not a compositional held-out policy result; marker accuracy should not be equated with all reconstructed body/contact accuracy.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2608.16222); checked 2026-11-19.

<a id="robomocap"></a>
## RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning

**robomocap · 2026 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2611.10994) · [Evidence](https://arxiv.org/abs/2611.10994) · Citekey: `robomocap2026`

**Authors of cited version:** Mayur Deshmukh; Aaron Tung; Junyi Li; Nikash Bhardwaj; Ademi Adeniji; Vincent Liu; Michael Cho; Jiafei Duan.

**Contribution / composition:** Pairs egocentric/wrist observations with optical whole-body capture for locomotion, transport and manipulation; benchmarks reconstruction, foot estimation and retargeting.

**Scope / curator boundary:** Captured human demonstrations and retargeting benchmarks do not establish learned compositional robot policy success.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2611.10994); checked 2026-11-19.

<a id="finemotion"></a>
## FineMotion: A Dataset and Benchmark with both Spatial and Temporal Annotation for Fine-grained Motion Generation and Editing

**finemotion · 2025 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2507.19850) · [Evidence](https://arxiv.org/abs/2507.19850) · Citekey: `finemotion2025`

**Authors of cited version:** Bizhu Wu; Jinheng Xie; Meidan Ding; Zhe Kong; Jianfeng Ren; Ruibin Bai; Rong Qu; Linlin Shen.

**Contribution / composition:** Adds aligned body-part descriptions for motion snippets and complete sequences, supporting fine-grained generation and spatial/temporal editing.

**Scope / curator boundary:** Fine-grained caption alignment is distinct from independently captured new action combinations; claimed benchmark gains are paper-reported.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2507.19850); checked 2026-11-19.

<a id="motionmillion"></a>
## Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data

**motionmillion · 2025 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2507.07095) · [Evidence](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_Go_to_Zero_Towards_Zero-shot_Motion_Generation_with_Million-scale_Data_ICCV_2025_paper.html) · Citekey: `motionmillion2025`

**Authors of cited version:** Ke Fan; Shunlin Lu; Minyue Dai; Runyi Yu; Lixing Xiao; Zhiyang Dou; Junting Dong; Lizhuang Ma; Jingbo Wang.

**Contribution / composition:** Introduces MotionMillion and MotionMillion-Eval for zero-shot, out-of-domain and complex compositional text-to-motion evaluation with a scalable model.

**Scope / curator boundary:** Dataset size is reported sequence count, not independent captures or unique subjects; the claimed generalization scope depends on the benchmark prompts and training ancestry.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2507.07095); checked 2026-11-19.

<a id="vimogen-mbench"></a>
## The Quest for Generalizable Motion Generation: Data, Model, and Evaluation

**vimogen-mbench · 2025 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2510.26794) · [Evidence](https://proceedings.iclr.cc/paper_files/paper/2026/hash/da47bfaf3f3a8d5bbab0d60c5195dc18-Abstract-Conference.html) · Citekey: `vimogenmbench2026`

**Authors of cited version:** Jing Lin; Ruisi Wang; Junzhe Lu; Ziqi Huang; Guorui Song; Ailing Zeng; Xian Liu; Chen Wei; Wanqi Yin; Qingping Sun; Zhongang Cai; Lei Yang; Ziwei Liu.

**Contribution / composition:** Combines mocap, web-derived and video-generated motion in ViMoGen-228K; introduces ViMoGen and hierarchical MBench evaluation.

**Scope / curator boundary:** Synthetic/video-estimated samples are not independent optical captures; VLM judging requires recording model/version and rendering settings.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2510.26794); checked 2026-11-19.

<a id="instructmotion"></a>
## Learning Generalizable Human Motion Generator with Reinforcement Learning

**instructmotion · 2024 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2405.15541) · [Evidence](https://arxiv.org/abs/2405.15541) · Citekey: `instructmotion2024`

**Authors of cited version:** Yunyao Mao; Xiaoyang Liu; Wengang Zhou; Zhenbo Lu; Houqiang Li.

**Contribution / composition:** Uses reinforcement learning and contrastive text-motion rewards on paired data and synthetic text-only prompts to improve generalization.

**Scope / curator boundary:** Semantic reward agreement does not establish physical execution; abstract-only protocol review.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2405.15541); checked 2026-11-19.

<a id="parahome"></a>
## ParaHome: Parameterizing Everyday Home Activities Towards 3D Generative Modeling of Human-Object Interactions

**parahome · 2024 · Datasets & compositional evaluation · method**

[Primary source](https://arxiv.org/abs/2401.10232) · [Evidence](https://arxiv.org/html/2401.10232) · Citekey: `parahome2025`

**Authors of cited version:** Jeonghwan Kim; Jisoo Kim; Jeonghyeon Na; Hanbyul Joo.

**Contribution / composition:** Captures full-body, hand, multi-object and articulated-object activity in a home setting, including sequential and concurrent manipulations.

**Mechanism:** New capture system aligns multicamera object tracking with IMU body/glove motion and post-processing. Baselines study text-conditioned body/hand synthesis and transformer object-state-conditioned body synthesis.

**Input contract:** Text baseline generates human motion. Object-guided baseline supplies object motion over the full target window plus spatial relations/initial state; it does not predict object motion from text+initial state.

**Evaluation checked:** Capture/calibration and post-processing checks; ParaHome-only/HumanML3D-only/mixed text-motion metrics; object-guided positional errors and foot skating; latent interpolation demonstrations.

**Source locator:** §§3.1–3.5, 4.1–4.2, 5.1–5.2, 6; Appendices A and E.1

**Scope / curator boundary:** Real continuous task recordings are distinct from constructed skill combinations; capture/participant grouping and future-condition leakage need independent protocol checks. Single home setup, artificial markers and restricted object collection limit generalization. Text-model interpolation is not proof of robust unseen skill composition. Paper reports inconsistent 207/208 capture totals; retain source distinction.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2401.10232); checked 2026-11-19.

<a id="motionx"></a>
## Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset

**motionx · 2023 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2307.00818) · [Evidence](https://arxiv.org/abs/2307.00818) · Citekey: `motionx2024`

**Authors of cited version:** Jing Lin; Ailing Zeng; Shunlin Lu; Yuanhao Cai; Ruimao Zhang; Haoqian Wang; Lei Zhang.

**Contribution / composition:** Provides expressive SMPL-X motion, sequence semantic labels and frame-level descriptions from a scalable video annotation pipeline.

**Scope / curator boundary:** Automatically estimated motion/labels are not direct contact-force ground truth; not a dedicated compositional split.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2307.00818); checked 2026-11-19.

<a id="best-automated-metric"></a>
## What is the Best Automated Metric for Text to Motion Generation?

**best-automated-metric · 2023 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2309.10248) · [Evidence](https://arxiv.org/abs/2309.10248) · Citekey: `bestautomatedmetric2023`

**Authors of cited version:** Jordan Voas; Yili Wang; Qixing Huang; Raymond Mooney.

**Contribution / composition:** Studies alignment between automated metrics and human judgments, separating sample-level and average model-level correlation; introduces MoBERT.

**Scope / curator boundary:** Correlation results concern the studied models/data and human judgments; they do not prove a universal metric for HOI mechanics, timeline compliance or new domains.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2309.10248); checked 2026-11-19.

<a id="behave"></a>
## BEHAVE: Dataset and Method for Tracking Human Object Interactions

**behave · 2022 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2204.06950) · [Evidence](https://arxiv.org/abs/2204.06950) · Citekey: `behave2022`

**Authors of cited version:** Bharat Lal Bhatnagar; Xianghui Xie; Ilya A. Petrov; Cristian Sminchisescu; Christian Theobalt; Gerard Pons-Moll.

**Contribution / composition:** Multi-view RGB-D body-object interaction data with body/object fits and contacts across everyday objects and locations.

**Scope / curator boundary:** Reconstruction and interaction resource, rather than a benchmark of unseen skill combinations.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2204.06950); checked 2026-11-19.

<a id="humanml3d"></a>
## Generating Diverse and Natural 3D Human Motions From Text

**humanml3d · 2022 · Datasets & compositional evaluation · method**

[Primary source](https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf) · [Evidence](https://openaccess.thecvf.com/content/CVPR2022/papers/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.pdf) · Citekey: `humanml3d2022`

**Authors of cited version:** Guo, Chuan; Zou, Shihao; Zuo, Xinxin; Wang, Sen; Ji, Wei; Li, Xingyu; Cheng, Li.

**Contribution / composition:** Introduces HumanML3D and a stochastic text-to-motion baseline.

**Mechanism:** Samples duration from text, then generates motion snippets with a temporal VAE.

**Input contract:** Natural-language description; sampled or supplied length.

**Evaluation checked:** HumanML3D and KIT-ML; FID, diversity, multimodality, R-precision and text-motion distance. R-precision ranks the paired caption against 31 distractors.

**Scope / curator boundary:** Learned embedding metrics measure statistical/text agreement; they do not certify contact mechanics or novel-combination execution.

**Composition axes:** data.

**Metadata:** official; [source](https://openaccess.thecvf.com/content/CVPR2022/html/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.html); checked 2026-11-19.

<a id="intercap"></a>
## InterCap: Joint Markerless 3D Tracking of Humans and Objects in Interaction

**intercap · 2022 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2209.12354) · [Evidence](https://arxiv.org/abs/2209.12354) · Citekey: `intercap2022`

**Authors of cited version:** Yinghao Huang; Omid Tehari; Michael J. Black; Dimitrios Tzionas.

**Contribution / composition:** Reconstructs whole-body SMPL-X and known objects from synchronized multi-view RGB-D, using contact cues.

**Scope / curator boundary:** Paper describes pseudo ground-truth fits; captured subjects/objects and sensor setting bound evidence.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2209.12354); checked 2026-11-19.

<a id="mocapact"></a>
## MoCapAct: A Multi-Task Dataset for Simulated Humanoid Control

**mocapact · 2022 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2208.07363) · [Evidence](https://arxiv.org/abs/2208.07363) · Citekey: `mocapact2023`

**Authors of cited version:** Nolan Wagener; Andrey Kolobov; Felipe Vieira Frujeri; Ricky Loynd; Ching-An Cheng; Matthew Hausknecht.

**Contribution / composition:** Provides a multi-task resource for simulated humanoid control and reusable motion-capture skills.

**Scope / curator boundary:** Simulated control data; not a human-object composition dataset or real robot execution corpus.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2208.07363); checked 2026-11-19.

<a id="babel"></a>
## BABEL: Bodies, Action and Behavior with English Labels

**babel · 2021 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2106.09696) · [Evidence](https://arxiv.org/abs/2106.09696) · Citekey: `babel2021`

**Authors of cited version:** Abhinanda R. Punnakkal; Arjun Chandrasekaran; Nikos Athanasiou; Alejandra Quiros-Ramirez; Michael J. Black.

**Contribution / composition:** Adds sequence and temporally localized action language to AMASS, supporting action understanding and temporal composition.

**Scope / curator boundary:** Motion derives from AMASS; overlapping annotations do not establish unseen-combination generalization by themselves.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2106.09696); checked 2026-11-19.

<a id="grab"></a>
## GRAB: A Dataset of Whole-Body Human Grasping of Objects

**grab · 2020 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/2008.11200) · [Evidence](https://arxiv.org/abs/2008.11200) · Citekey: `grab2020`

**Authors of cited version:** Omid Taheri; Nima Ghorbani; Michael J. Black; Dimitrios Tzionas.

**Contribution / composition:** Marker-based whole-body, articulated hand/face and object trajectories with detailed grasp interaction.

**Scope / curator boundary:** Source interactions are captured examples; dataset availability does not imply compositional holdout evaluation.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/2008.11200); checked 2026-11-19.

<a id="amass"></a>
## AMASS: Archive of Motion Capture as Surface Shapes

**amass · 2019 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/1904.03278) · [Evidence](https://arxiv.org/abs/1904.03278) · Citekey: `amass2019`

**Authors of cited version:** Naureen Mahmood; Nima Ghorbani; Nikolaus F. Troje; Gerard Pons-Moll; Michael J. Black.

**Contribution / composition:** Unifies heterogeneous optical mocap collections through MoSh++ and a common parametric body surface representation.

**Scope / curator boundary:** Adjacent data infrastructure; a shared body representation does not itself supply compositional labels or object trajectories.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/1904.03278); checked 2026-11-19.

<a id="kitml"></a>
## The KIT Motion-Language Dataset

**kitml · 2016 · Datasets & compositional evaluation · abstract**

[Primary source](https://arxiv.org/abs/1607.03827) · [Evidence](https://arxiv.org/abs/1607.03827) · Citekey: `kitml2018`

**Authors of cited version:** Matthias Plappert; Christian Mandery; Tamim Asfour.

**Contribution / composition:** Aggregates mocap in a capture-independent representation with crowdsourced natural-language descriptions.

**Scope / curator boundary:** General motion-language resource; abstract does not specify a held-out compositional split.

**Composition axes:** data.

**Metadata:** official; [source](https://arxiv.org/bibtex/1607.03827); checked 2026-11-19.

<a id="maskadapt"></a>
## MaskAdapt: Learning Flexible Motion Adaptation via Mask-Invariant Prior for Physics-Based Characters

**maskadapt · 2026 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2603.29272) · [Evidence](https://arxiv.org/abs/2603.29272) · Citekey: `maskadapt2026`

**Authors of cited version:** Soomin Park; Eunseong Lee; Kwang Bin Lee; Sung-Hee Lee.

**Contribution / composition:** Mask-invariant base policy plus residual adaptation enables multi-part composition and text-driven partial tracking.

**Scope / curator boundary:** Targeted body-part adaptation in simulation is not full contact-rich compositional generalization.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2603.29272); checked 2026-11-19.

<a id="simdiff"></a>
## SimDiff: Simulator-constrained Diffusion Model for Physically Plausible Motion Generation

**simdiff · 2025 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2509.20927) · [Evidence](https://arxiv.org/abs/2509.20927) · Citekey: `simdiff2025`

**Authors of cited version:** Akihisa Watanabe; Jiawei Ren; Li Siyao; Yichen Peng; Erwin Wu; Edgar Simo-Serra.

**Contribution / composition:** Conditions diffusion on environment coefficients and reports unseen combinations of environmental parameters.

**Scope / curator boundary:** Environmental-parameter composition differs from composing human action semantics; claims here follow the abstract.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.20927); checked 2026-11-19.

<a id="closd"></a>
## CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control

**closd · 2024 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2410.03441) · [Evidence](https://arxiv.org/abs/2410.03441) · Citekey: `closd2024`

**Authors of cited version:** Guy Tevet; Sigal Raab; Setareh Cohan; Daniele Reda; Zhengyi Luo; Xue Bin Peng; Amit H. Bermano; Michiel van de Panne.

**Contribution / composition:** Closes a feedback loop between an autoregressive text/target-conditioned diffusion planner and an RL tracker for task sequences.

**Scope / curator boundary:** Original arXiv 2024, ICLR 2025; demonstrated task suite does not imply arbitrary long-horizon generalization.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2410.03441); checked 2026-11-19.

<a id="mhc"></a>
## Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots

**mhc · 2024 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2408.07295) · [Evidence](https://arxiv.org/abs/2408.07295) · Citekey: `mhc2026`

**Authors of cited version:** Pranay Dugar; Aayam Shrestha; Fangzhou Yu; Bart van Marum; Alan Fern.

**Contribution / composition:** Masked-motion curriculum learns multimodal control and combines joystick locomotion with partial-body mimicry.

**Scope / curator boundary:** Control-modality combination is adjacent to semantic compositional generation; abstract-level review.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2408.07295); checked 2026-11-19.

<a id="maskedmimic"></a>
## MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

**maskedmimic · 2024 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2409.14393) · [Evidence](https://arxiv.org/abs/2409.14393) · Citekey: `maskedmimic2024`

**Authors of cited version:** Chen Tessler; Yunrong Guo; Ofir Nabati; Gal Chechik; Xue Bin Peng.

**Contribution / composition:** Unifies masked keyframes, objects, text and mixed descriptions as partial motion constraints for simulated character control.

**Scope / curator boundary:** Composing input modalities and task transitions is different from proving arbitrary unseen action combinations.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2409.14393); checked 2026-11-19.

<a id="diffmimic"></a>
## DiffMimic: Efficient Motion Mimicking with Differentiable Physics

**diffmimic · 2023 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2304.03274) · [Evidence](https://arxiv.org/abs/2304.03274) · Citekey: `diffmimic2023`

**Authors of cited version:** Jiawei Ren; Cunjun Yu; Siwei Chen; Xiao Ma; Liang Pan; Ziwei Liu.

**Contribution / composition:** Uses differentiable physics for efficient reference motion imitation.

**Scope / curator boundary:** Motion tracking and training efficiency are adjacent capabilities; no compositional generation claim inferred.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2304.03274); checked 2026-11-19.

<a id="phc"></a>
## Perpetual Humanoid Control for Real-time Simulated Avatars

**phc · 2023 · Physics-based character control · method**

[Primary source](https://arxiv.org/abs/2305.06456) · [Evidence](https://openaccess.thecvf.com/content/ICCV2023/papers/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.pdf) · Citekey: `phc2023`

**Authors of cited version:** Zhengyi Luo; Jinkun Cao; Alexander Winkler; Kris Kitani; Weipeng Xu.

**Contribution / composition:** Scales physics-based imitation with recovery from falls and noisy reference motion.

**Mechanism:** Progressive multiplicative control allocates capacity for difficult motions and recovery.

**Input contract:** Reference pose sequence and simulated humanoid state.

**Evaluation checked:** Large-scale mocap imitation, noisy video/language references and fail-state recovery timing; simulation avatar evidence.

**Scope / curator boundary:** Progressive training is costly; scene/terrain awareness and tighter upstream integration are future directions.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2305.06456); checked 2026-11-19.

<a id="pulse"></a>
## Universal Humanoid Motion Representations for Physics-Based Control

**pulse · 2023 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2310.04582) · [Evidence](https://arxiv.org/abs/2310.04582) · Citekey: `pulse2024`

**Authors of cited version:** Zhengyi Luo; Jinkun Cao; Josh Merel; Alexander Winkler; Jing Huang; Kris Kitani; Weipeng Xu.

**Contribution / composition:** Distills a broad motion imitator into a variational latent representation with proprioception-conditioned prior for downstream hierarchical RL.

**Scope / curator boundary:** Original arXiv year 2023, ICLR 2024; simulator skill reuse is not an unseen language-combination benchmark.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2310.04582); checked 2026-11-19.

<a id="ase"></a>
## ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters

**ase · 2022 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2205.01906) · [Evidence](https://arxiv.org/abs/2205.01906) · Citekey: `ase2022`

**Authors of cited version:** Xue Bin Peng; Yunrong Guo; Lina Halper; Sergey Levine; Sanja Fidler.

**Contribution / composition:** Learns reusable latent motor skills from unsegmented motion using adversarial imitation and unsupervised RL.

**Scope / curator boundary:** Downstream reward functions still specify tasks; reusable skills alone do not establish language-compositional generalization.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2205.01906); checked 2026-11-19.

<a id="amp"></a>
## AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

**amp · 2021 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/2104.02180) · [Evidence](https://arxiv.org/abs/2104.02180) · Citekey: `amp2022`

**Authors of cited version:** Xue Bin Peng; Ze Ma; Pieter Abbeel; Sergey Levine; Angjoo Kanazawa.

**Contribution / composition:** Learns motion-style rewards from unstructured clips alongside task rewards; reports emergent skill composition.

**Scope / curator boundary:** Task-reward-driven simulated control differs from one-shot text-conditioned generation and benchmarked semantic holdouts.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2104.02180); checked 2026-11-19.

<a id="deepmimic"></a>
## DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

**deepmimic · 2018 · Physics-based character control · abstract**

[Primary source](https://arxiv.org/abs/1804.02717) · [Evidence](https://arxiv.org/abs/1804.02717) · Citekey: `deepmimic2018`

**Authors of cited version:** Xue Bin Peng; Pieter Abbeel; Sergey Levine; Michiel van de Panne.

**Contribution / composition:** Combines motion imitation and task objectives for simulated skills, recovery and multi-clip agents.

**Scope / curator boundary:** Simulated character control is adjacent to text-driven compositional generation; no claim of general unseen semantic combinations.

**Composition axes:** physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/1804.02717); checked 2026-11-19.

<a id="grail"></a>
## GRAIL: Generating Humanoid Loco-Manipulation from World Models

**grail · 2026 · Humanoid transfer & loco-manipulation · abstract**

[Primary source](https://arxiv.org/abs/2606.05160) · [Evidence](https://arxiv.org/abs/2606.05160) · Citekey: `grail2026`

**Authors of cited version:** Tianyi Xie; Haotian Zhang; Jinhyung Park; Zi Wang; Bowen Wen; Jiefeng Li; Xueting Li; Qingwei Ben; Haoyang Weng; Yufei Ye; David Minor; Tingwu Wang; Chenfanfu Jiang; Sanja Fidler; Jan Kautz; Linxi Fan; Yuke Zhu; Zhengyi Luo; Umar Iqbal; Ye Yuan.

**Contribution / composition:** Grounds generated videos in known 3D scenes/assets, recovers HOI, retargets and trains trackers and visual policies.

**Scope / curator boundary:** Uses privileged known configurations; generated data is virtual. Real G1 deployment results are separate task-specific policy evidence.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2606.05160); checked 2026-11-19.

<a id="intermimicgen"></a>
## InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

**intermimicgen · 2026 · Humanoid transfer & loco-manipulation · abstract**

[Primary source](https://arxiv.org/abs/2610.06850) · [Evidence](https://arxiv.org/abs/2610.06850) · Citekey: `intermimicgen2026`

**Authors of cited version:** Yucheng Zhang; Sirui Xu; Jinhong Li; Liuyu Bian; Anatulya Nandi; Derek Zhang; Xiangchen Liu; Xueting Li; Umar Iqbal; Yu-Xiong Wang; Liang-Yan Gui.

**Contribution / composition:** Retargets heterogeneous HOI, learns a generalist simulation tracker and iteratively retains task-preserving perturbations that execute successfully.

**Scope / curator boundary:** Augmented executable corpus is simulation-generated; abstract also reports robot transfer, whose task scope requires full-paper review.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2610.06850); checked 2026-11-19.

<a id="weave"></a>
## Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions

**weave · 2026 · Humanoid transfer & loco-manipulation · method**

[Primary source](https://arxiv.org/abs/2609.16683) · [Evidence](https://arxiv.org/html/2609.16683v1) · Citekey: `weave2026`

**Authors of cited version:** Liu Cao; Xingze Wu; Jingzhi Cui; Botian Xu; Mingzhi Pei; Ruoqu Chen; Mengdi Xu.

**Contribution / composition:** Contact-aware retargeting and approach completion feed a geometry/contact-aware whole-body and finger controller; releases simulated robot-object rollouts.

**Mechanism:** Constructs executable interaction references, then tracks them with coordinated body and finger control.

**Input contract:** Robot/object state, geometric and reference interaction information.

**Evaluation checked:** Nine-object simulation suite, trained and held-out sequences plus architecture/optimizer ablations. Approximately 9,000 rollouts/23 hours are simulated execution.

**Scope / curator boundary:** Parallel simulation rollouts are not hardware recordings; training/unseen sequence success is not arbitrary object or task generalization.

**Composition axes:** embodiment, object-contact, physical-skill, scene-state, temporal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2609.16683); checked 2026-11-19.

<a id="beyondmimic"></a>
## BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion

**beyondmimic · 2025 · Humanoid transfer & loco-manipulation · abstract**

[Primary source](https://arxiv.org/abs/2508.08241) · [Evidence](https://arxiv.org/abs/2508.08241) · Citekey: `beyondmimic2025`

**Authors of cited version:** Qiayuan Liao; Takara E. Truong; Xiaoyu Huang; Yuman Gao; Guy Tevet; Koushil Sreenath; C. Karen Liu.

**Contribution / composition:** Combines robust motion tracking with a distilled diffusion policy and test-time cost guidance for navigation and control.

**Scope / curator boundary:** Real hardware evidence is task-specific; does not establish arbitrary object manipulation or semantic composition.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2508.08241); checked 2026-11-19.

<a id="gmr"></a>
## Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking

**gmr · 2025 · Humanoid transfer & loco-manipulation · abstract**

[Primary source](https://arxiv.org/abs/2510.02252) · [Evidence](https://arxiv.org/abs/2510.02252) · Citekey: `gmr2025`

**Authors of cited version:** Joao Pedro Araujo; Yanjie Ze; Pei Xu; Jiajun Wu; C. Karen Liu.

**Contribution / composition:** Studies how retargeting quality affects BeyondMimic tracking on LAFAN1 and introduces GMR.

**Scope / curator boundary:** Retargeting fidelity and tracking robustness are prerequisites, not compositional generation results.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2510.02252); checked 2026-11-19.

<a id="exbody"></a>
## Expressive Whole-Body Control for Humanoid Robots

**exbody · 2024 · Humanoid transfer & loco-manipulation · abstract**

[Primary source](https://arxiv.org/abs/2402.16796) · [Evidence](https://arxiv.org/abs/2402.16796) · Citekey: `exbody2024`

**Authors of cited version:** Xuxin Cheng; Yandong Ji; Junming Chen; Ruihan Yang; Ge Yang; Xiaolong Wang.

**Contribution / composition:** Tracks upper-body expression while lower-body velocity control enables robust locomotion, with real robot demonstrations.

**Scope / curator boundary:** Leg imitation is relaxed; expressive locomotion does not establish dexterous object-task composition.

**Composition axes:** embodiment, physical-skill.

**Metadata:** official; [source](https://arxiv.org/bibtex/2402.16796); checked 2026-11-19.

<a id="cfgcomposer"></a>
## CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction

**cfgcomposer · 2026 · Audio, dance & gesture composition · abstract**

[Primary source](https://arxiv.org/abs/2611.15101) · [Evidence](https://arxiv.org/abs/2611.15101) · Citekey: `cfgcomposer2026`

**Authors of cited version:** Pengyang Shi; Jinlu Zhang; Chunze Lin; Yizhou Wang; Li Yi.

**Contribution / composition:** Composes audio and text motion diffusion scores while learning a cross-modal correction for their dependence; relevant to model-level composition beyond text-only actions.

**Scope / curator boundary:** The correction is jointly trained: this should not be described as entirely training-free combination of independent priors. Reported deployment and benchmarks have not been independently reproduced here.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2611.15101); checked 2026-11-19.

<a id="moco"></a>
## Multi-Modal Controlled Coherent Motion Generation

**moco · 2026 · Audio, dance & gesture composition · method**

[Primary source](https://feifeifeiliu.github.io/MOCO/) · [Evidence](https://feifeifeiliu.github.io/MOCO/) · Citekey: `moco2026`

**Authors of cited version:** Liu, Yifei; Cao, Qiong; Yi, Hongwei; Jiang, Huaiguang; Ding, Changxing.

**Contribution / composition:** Combines text, speech and trajectory denoisers by body region and recurrently assembles a holistic motion at each diffusion step.

**Mechanism:** Four modality/component denoisers use body masks; a timeline can reassign parts and an LLM can plan intervals.

**Input contract:** Concurrent speech audio, action text and target trajectory; no paired multimodal training set required by the author description.

**Evaluation checked:** Author page: 1,000 concurrent-control clips built from 40 text descriptions and 694 speech clips; evaluates text and speech fidelity.

**Source locator:** Author page: Spatially decoupled denoising; Benchmark; Limitations. Project-page audit, not full-paper replication.

**Scope / curator boundary:** Default part assignment can conflict when text and speech both request upper-body actions. Controlled consistency benchmark does not establish arbitrary cross-modal semantic generalization.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://feifeifeiliu.github.io/MOCO/); checked 2026-11-19.

<a id="emage"></a>
## EMAGE: Towards Unified Holistic Co-Speech Gesture Generation via Expressive Masked Audio Gesture Modeling

**emage · 2024 · Audio, dance & gesture composition · abstract**

[Primary source](https://arxiv.org/abs/2401.00374) · [Evidence](https://arxiv.org/abs/2401.00374) · Citekey: `emage2024`

**Authors of cited version:** Haiyang Liu; Zihao Zhu; Giorgio Becherini; Yichen Peng; Mingyang Su; You Zhou; Xuefei Zhe; Naoya Iwamoto; Bo Zheng; Michael J. Black.

**Contribution / composition:** Audio and masked gesture hints drive holistic face/body/hand/global motion with compositional quantized priors; introduces BEAT2.

**Scope / curator boundary:** A compositional representation across body streams is distinct from unseen semantic task-chain generalization.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2401.00374); checked 2026-11-19.

<a id="lodge"></a>
## Lodge: A Coarse to Fine Diffusion Network for Long Dance Generation Guided by the Characteristic Dance Primitives

**lodge · 2024 · Audio, dance & gesture composition · abstract**

[Primary source](https://arxiv.org/abs/2403.10518) · [Evidence](https://arxiv.org/abs/2403.10518) · Citekey: `lodge2024`

**Authors of cited version:** Ronghui Li; YuXiang Zhang; Yachao Zhang; Hongwen Zhang; Jie Guo; Yan Zhang; Yebin Liu; Xiu Li.

**Contribution / composition:** Global diffusion generates characteristic dance primitives; parallel local diffusion expands them into detailed long sequences, with a foot refinement component.

**Scope / curator boundary:** Coarse-to-fine music choreography does not test object-state dependencies or task-completion composition.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2403.10518); checked 2026-11-19.

<a id="edge"></a>
## EDGE: Editable Dance Generation From Music

**edge · 2022 · Audio, dance & gesture composition · abstract**

[Primary source](https://arxiv.org/abs/2211.10658) · [Evidence](https://arxiv.org/abs/2211.10658) · Citekey: `edge2022`

**Authors of cited version:** Jonathan Tseng; Rodrigo Castellon; C. Karen Liu.

**Contribution / composition:** Music-conditioned diffusion supports joint-wise constraints and temporal in-betweening, connecting body-part control with long dance editing.

**Scope / curator boundary:** Music-conditioned dance editing is adjacent to skill composition; its physical-plausibility metric is not full interaction-dynamics certification.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2211.10658); checked 2026-11-19.

<a id="finedance"></a>
## FineDance: A Fine-grained Choreography Dataset for 3D Full Body Dance Generation

**finedance · 2022 · Audio, dance & gesture composition · abstract**

[Primary source](https://arxiv.org/abs/2212.03741) · [Evidence](https://arxiv.org/abs/2212.03741) · Citekey: `finedance2023`

**Authors of cited version:** Ronghui Li; Junfan Zhao; Yachao Zhang; Mingyang Su; Zeping Ren; Han Zhang; Yansong Tang; Xiu Li.

**Contribution / composition:** Full-body music-dance dataset with detailed hand motion and dance genres; its retrieval and generation mechanisms provide an adjacent composition setting.

**Scope / curator boundary:** Dance genre and beat metrics do not substitute for action order, contact and object-state correctness.

**Composition axes:** cross-modal.

**Metadata:** official; [source](https://arxiv.org/bibtex/2212.03741); checked 2026-11-19.

<a id="interaction-survey"></a>
## A Survey on Human Interaction Motion Generation

**interaction-survey · 2025 · Surveys & field maps · abstract**

[Primary source](https://arxiv.org/abs/2503.12763) · [Evidence](https://arxiv.org/abs/2503.12763) · Citekey: `interactionsurvey2025`

**Authors of cited version:** Kewei Sui; Anindita Ghosh; Inwoo Hwang; Bing Zhou; Jian Wang; Chuan Guo.

**Contribution / composition:** Organizes human-human, human-object and human-scene generation with datasets and evaluation; useful for backward citation chasing across interaction types.

**Scope / curator boundary:** A survey taxonomy is a discovery aid; individual method capabilities still require checking the cited primary papers.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2503.12763); checked 2026-11-19.

<a id="video-motion-survey"></a>
## Human Motion Video Generation: A Survey

**video-motion-survey · 2025 · Surveys & field maps · abstract**

[Primary source](https://arxiv.org/abs/2509.03883) · [Evidence](https://arxiv.org/abs/2509.03883) · Citekey: `videomotionsurvey2025`

**Authors of cited version:** Haiwei Xue; Xiangyang Luo; Zhanghao Hu; Xin Zhang; Xunzhi Xiang; Yuqin Dai; Jianzhuang Liu; Zhensong Zhang; Minglei Li; Jian Yang; Fei Ma; Zhiyong Wu; Changpeng Yang; Zonghong Dai; Fei Richard Yu.

**Contribution / composition:** Adjacent literature: surveys human-motion video generation, including planning, generation and refinement across visual, text and audio conditions.

**Scope / curator boundary:** Video appearance and motion plausibility do not establish valid 3D contact or executable motion; keep outside 3D-motion numerical rankings.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2509.03883); checked 2026-11-19.

<a id="generative-survey"></a>
## Motion Generation: A Survey of Generative Approaches and Benchmarks

**generative-survey · 2025 · Surveys & field maps · abstract**

[Primary source](https://arxiv.org/abs/2507.05419) · [Evidence](https://arxiv.org/abs/2507.05419) · Citekey: `generativesurvey2025`

**Authors of cited version:** Aliasghar Khani; Arianna Rampini; Bruno Roy; Larasika Nadela; Noa Kaplan; Evan Atherton; Derek Cheung; Jacky Bibliowicz.

**Contribution / composition:** Reviews generative model families, conditioning, datasets and metrics, emphasizing recent motion-generation literature.

**Scope / curator boundary:** Architecture-based grouping does not by itself distinguish semantic composition from sequence concatenation.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2507.05419); checked 2026-11-19.

<a id="text-motion-overview"></a>
## Text-driven Motion Generation: Overview, Challenges and Directions

**text-motion-overview · 2025 · Surveys & field maps · abstract**

[Primary source](https://arxiv.org/abs/2505.09379) · [Evidence](https://arxiv.org/abs/2505.09379) · Citekey: `textmotionoverview2025`

**Authors of cited version:** Ali Rida Sahili; Najett Neji; Hedi Tabia.

**Contribution / composition:** Reviews text-to-motion through architecture and discrete/continuous representation perspectives.

**Scope / curator boundary:** Text-to-motion quality is not automatically evidence of unseen skill-pair or interaction-state generalization.

**Composition axes:** taxonomy.

**Metadata:** official; [source](https://arxiv.org/bibtex/2505.09379); checked 2026-11-19.

<a id="realis-motion"></a>
## RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space

**realis-motion · 2026 · Adjacent: compositional human video · abstract**

[Primary source](https://proceedings.mlr.press/v306/liang26ad.html) · [Evidence](https://proceedings.mlr.press/v306/liang26ad.html) · Citekey: `realismotion2026`

**Authors of cited version:** Jingyun Liang; Jingkai Zhou; Shikai Li; Chenjie Cao; Lei Sun; Yichen Qian; Weihua Chen; Fan Wang.

**Contribution / composition:** Separates subject, background, world-space trajectory and action controls for human video composition.

**Scope / curator boundary:** Adjacent video-generation evidence; does not imply a joint human-object 3D generator or physically executable controller.

**Composition axes:** appearance-motion, cross-modal.

**Metadata:** official; [source](https://proceedings.mlr.press/v306/liang26ad.html); checked 2026-11-19.
