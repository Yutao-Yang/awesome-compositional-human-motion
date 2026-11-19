# Benchmark protocols and evaluator provenance

Checked against primary sources on 2026-11-19. These are protocol notes, not reproduced scores. `year` in the extra intake means first public preprint year; `venue` records the later proceedings identity.

## MTT and the information supplied to a model

The authoritative MTT (Multi-Track Timelines) release is [nv-tlabs/stmc](https://github.com/nv-tlabs/stmc), alongside the [STMC paper](https://openaccess.thecvf.com/content/CVPR2024W/HuMoGen/papers/Petrovich_Multi-Track_Timeline_Control_for_Text-Driven_3D_Human_Motion_Generation_CVPRW_2024_paper.pdf). The repository supplies `mtt/MTT.txt`, individual timelines, source text/motion lists, baseline conversions and evaluation scripts. Its baseline “One Text” collapses a timeline into prose; “Single track” removes the multiple tracks. These supply different timing/body-part information, so results need a visible input-contract column. MTT is a benchmark artifact of STMC, not a second independent paper.

For each comparison, record whether the model receives explicit start/end intervals and part assignments, multiple texts without intervals, or only a single prose prompt. Report who supplies or predicts timing, total duration, any initial motion/prefix and spatial targets. Equal benchmark names do not guarantee equal conditioning. This comparison rule is our recommendation, motivated by the different released STMC baselines.

[EnergyMoGen](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_EnergyMoGen_Compositional_Human_Motion_Generation_with_Energy-Based_Diffusion_Model_in_CVPR_2025_paper.pdf) evaluates multiple-text composition and single-text multi-concept generation separately on MTT. Preserve that distinction when comparing conjunction/negation systems with timeline-conditioned systems. Do not infer exact interval compliance from a whole-sequence similarity score.

## Evaluators are part of the experiment

[TMR](https://arxiv.org/abs/2305.00976), with [official implementation](https://github.com/Mathux/TMR), learns a text-motion representation through contrastive learning and reconstruction. STMC evaluation explicitly installs pretrained TMR and invokes its MTT evaluation scripts. A score therefore needs the evaluator checkpoint, training corpus, representation conversion and temporal crop protocol. Changing these can change the meaning of FID, retrieval accuracy and text-motion similarity. This is a reproducibility recommendation, not a claim that every surveyed paper used an identical checkpoint.

[What is the Best Automated Metric for Text to Motion Generation?](https://arxiv.org/abs/2309.10248) finds markedly different relationships with human judgment at sample and model-average levels. Consequently, a good average retrieval score should not be treated as proof that each sequence obeys all instructions. Include targeted order/overlap checks and human review; HOI additionally needs object/contact/state checks. The latter checks are survey recommendations beyond that paper's skeleton-motion correlation experiment.

## Complementary benchmarks and their boundaries

| Resource | What it adds | What a comparison must disclose |
| --- | --- | --- |
| [FineMotion](https://arxiv.org/abs/2507.19850) / ICCV 2025 | Detailed part-motion and timing descriptions; generation/editing | Whether edits receive an original motion and exact intervals; snippet versus full-sequence evaluation |
| [MotionMillion-Eval](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_Go_to_Zero_Towards_Zero-shot_Motion_Generation_with_Million-scale_Data_ICCV_2025_paper.html) / ICCV 2025 | Zero-shot, out-of-domain and complex compositional prompts | Source ancestry, prompt split, text processing and training scale; zero-shot relative to which training set |
| [MBench / ViMoGen](https://proceedings.iclr.cc/paper_files/paper/2026/hash/da47bfaf3f3a8d5bbab0d60c5195dc18-Abstract-Conference.html) / ICLR 2026 | Hierarchical motion quality, fidelity and generalization evaluation | Physical/pose versus VLM-based dimensions; model and rendering provenance |

The [official ViMoGen repository](https://github.com/MotrixLab/ViMoGen) separates geometric motion/pose checks from VLM-based consistency/generalization dimensions. A VLM judgment and a geometric measurement are different evidence types; neither alone establishes physically executable loco-manipulation. Its MBench is the motion-generation benchmark, distinct from unrelated video-world-model benchmarks sharing the name.

For synthetic composition, hold out combinations while retaining their components and separately disclose subject, object-instance and source-recording ancestry. COSMI's [published protocol](https://arxiv.org/html/2610.03252v1) holds out five combinations and one chair instance. That tests the declared combinations/object transfer; it should not be relabeled as independent-person or source-recording generalization.
