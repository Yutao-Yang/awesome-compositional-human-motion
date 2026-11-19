# Search, inclusion and evidence protocol

Audit date: **2026-11-19**. This is a living, breadth-first scoping survey. It is not a registered systematic review, a PRISMA completeness claim, or a claim that every included full text has been read.

## Research questions

1. What is composed: clips, body parts, semantic concepts, people, object interactions, scene states, learned distributions, or executable skills?
2. At which level: data construction, representation, inference, planning, or control?
3. What is provided at inference: text, timeline, duration, path, geometry, initial state, goal state, donor motion, actor motion, or future ground truth?
4. What is actually tested: new source pairings, unseen semantic combinations, unseen objects/scenes, dependent task chains, or only average single-clip quality?
5. Does the evidence concern kinematic synthesis, simulated execution, hardware, or downstream learning from manufactured data?

## Search performed

Three parallel literature passes covered temporal/spatial generation and editing; human-object/scene/person interaction; datasets, evaluation, control and humanoid transfer. A consolidation pass added historical foundations, generative backbones, music/gesture composition, surveys and adjacent video composition. An independent cross-lane review checked identity duplication, title/URL matching, year/version ambiguity and evaluation provenance. Newly found gaps were searched again.

Search families (English terms and paper-name variants):

- `compositional human motion`, `motion composition`, `spatial composition`, `temporal composition`, `motion graphs`, `parametric motion graphs`, `motion annotations`.
- `multi-track timeline`, `long text motion`, `streaming motion`, `motion editing`, `in-betweening`, `body part`, `motion decomposition`, `energy composition`.
- `human object interaction generation`, `multi-object interaction`, `articulated object`, `bimanual`, `human scene interaction`, `loco manipulation`.
- `multi human motion`, `reaction synthesis`, `collaborative manipulation`, `number-free motion`.
- `compositional generalization motion`, `motion generation evaluation`, `MTT`, `TMR`, `unseen combinations`, `dataset composition`.
- `physics character control`, `motion imitation`, `skill embedding`, `masked motion control`, `humanoid retargeting`.
- `audio text motion composition`, `dance primitives`, `holistic gesture`, `human interaction survey`.

Discovery used web search, named-paper searches, author/project pages, official repositories, proceedings and existing field surveys. Existing project notes supplied seed names only; this repository does not publish private project paths, assets or results. No commercial citation index export or exhaustive forward-citation graph was collected. A complete per-query hit/rejection log was not retained in this first pass; the query families above document the route without inventing hit counts.

## Inclusion and exclusion

Include papers that explicitly compose motion, enable composition through editable representations or conditions, supply relevant data/evaluation, or demonstrate adjacent execution mechanisms. Foundations and adjacent domains are labelled, not presented as identical competitors. Both historical and recent works are eligible; no fixed start year is imposed. The audit stops at the stated date.

Exclude identity-unverifiable names, duplicate preprint/conference versions, papers only sharing an acronym, and generic rendering/reconstruction work without an explicit relationship to motion/interaction composition. ProciGen is included specifically as procedural interaction-data construction, not as continuous motion generation. Video is an explicitly adjacent branch. This pass does not attempt full coverage of sign-language production, crowd simulation, biomechanics or general robot task-and-motion planning.

## Record and bibliography policy

- Raw lane records: `intake/*.json`; canonical deduplicated records: `papers.json`.
- Identity: arXiv identifier, stable paper identifier/title and reconciled aliases. A shared acronym alone is not identity.
- Bibliography: official arXiv BibTeX or proceedings/author/institution metadata, retained in `sources/metadata.json`. Endpoint errors remain explicit.
- Display year: first preprint year where verified, otherwise the cited source year. The `year` field retains the exact cited bibliography year; `display_year`, `first_preprint_year` and venue/version notes distinguish these identities. Do not silently attach final proceedings authors to an earlier preprint.
- `references.bib` uses stable survey citekeys. Official records are preferred; any minimal curated record is flagged, never padded with guessed authors/pages/DOIs.
- A code link is author-linked, not a claim of complete release, permissive licensing, a working environment or successful reproduction.

## Reading levels

| Level | What was checked | What it does not establish |
|---|---|---|
| `abstract` | Primary-source identity and high-level task/contribution | Exact algorithm, fair replication, all tables or limitations |
| `method` | Targeted method, input conditions and/or evaluation description; source locator when available | Exhaustive full-paper review, implemented baseline or reproduced results |

A detailed author project page can support `method` when explicitly identified as such. Missing details remain pending. `limitations` includes curator comparison boundaries: these are not necessarily author-reported failures. No entry in this release is a reproduction claim.

## Known residual gaps and stopping rule

Breadth is useful only when identities and evidence remain inspectable. This first release prioritizes the above branches and records remaining full-text/protocol work rather than asserting “all papers”. Continue with backward/forward citation chasing from pivotal entries, proceedings sweeps and evaluation-focused reading; preserve the date and reading level of each addition. A future systematic-review release would need frozen search engines/queries, retrieval counts, explicit screening decisions and independent inclusion adjudication.


## Full-text round, 2026-11-19

The second round read the methods and experiments of all 100 previously abstract-only papers, and normalized the original 28 targeted readings to the same structured schema. Nine important omissions were added after full-text reading: OmniControl, GMD, FineMoGen, ReMoDiffuse, DNO, PhysDiff, UniHSI, RG-DNO and InteractAgent. The resulting 137 entries each have mechanism, inference inputs, dataset/split, named metrics, evaluation scope, limitations, section/table locators and a primary full-text identity.

Private retrieval receipts retain the PDFs and decoded text. Public `sources/full_text_inventory.json` exposes source URLs, inspected versions, byte counts and SHA256 without mirroring the papers. Version drift is explicit: the PRISM v4 PDF title differs from the official BibTeX endpoint; `sources/bibliography_discrepancies.json` records the resolution. Supplementary material was consulted where specifically identified, not presumed read for every paper.

Independent cross-lane checks sampled 43 distinct entries. Seven mandatory metadata/protocol/scope corrections were resolved, with further clarifying notes retained for ambiguous source definitions. This is a second check of that sample, not independent double review of every entry. Source omissions remain labelled as unreported or not applicable; no split ratios are inferred from dataset conventions alone. Full-text reading is still distinct from running public code or reproducing a table.

The authoring files and high-resolution renders in `figures/` are the user-authorized exception for publishing the survey diagram. They contain no paper figures, datasets, weights or private project results.
