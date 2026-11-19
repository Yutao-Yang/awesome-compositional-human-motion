# Maintaining the survey

The canonical editable research inputs are `intake/*.json`; official bibliographic receipts are `sources/metadata.json`. Generated `papers.json`, `README.md`, `notes/papers.md`, `references.bib`, `audit.json` and `docs/papers.js` should be rebuilt together.

1. Search for an existing arXiv ID, title and alias before adding a record. Preprint revisions and conference versions normally remain one paper; preserve version-specific metadata.
2. Add a focused intake record using the existing schema: `id`, `title`, `year`, `category`, `url`, `summary`, `limitations`, `evidence_level`, `evidence_url`, `checked`. Prefer HTTPS primary sources. Authors and official code are optional until verified.
3. For deeper reading add `method`, `conditions`, `evaluation` and `evidence_locator`. Distinguish initial state, goal, predicted plan, donor references and real future ground truth. Do not upgrade the reading level based on another survey's prose.
4. Add the stable ID to the controlled category map in `scripts/build.py`; preserve independent tags. Search for revised titles and changes in authors or release status.
5. Run `python scripts/enrich.py` with network access to obtain small official bibliography records. Do not download PDFs, datasets, weights or credentials into the public repository. Metadata failures remain explicit; a minimal record must never invent missing authors.
6. Run `python scripts/build.py` then `python scripts/validate.py`. Review `audit.json`, bibliography status and title mismatches manually. Check any nonzero mismatch rather than blindly accepting an automatic title change.
7. Preview with `python -m http.server 8765 --directory docs`. Test search, categories, reading filters, expansion and citation copying. All README links must still work without JavaScript.
8. Review the full diff and ignore rules before committing. Publish only this survey directory, never its parent project, data or private context. Synchronization must refuse dirty remote checkouts and never force-push or delete unrelated files.

A source returning 403/429 is unresolved access, not proof that the paper or repository does not exist. Recheck using another official author/institution/proceedings entry. Release availability and scientific reproducibility are separate fields.

## Extending coverage

Prioritize missing mechanisms and evaluation contracts over raw paper count. Keep foundational, direct-composition and adjacent application branches explicit. Start with `notes/reading-guide.zh.md` and `notes/benchmarks.md`; additional topics can be added without renaming existing paper IDs or citekeys.

No scheduled background maintenance is configured. Updates are made when requested or when adding research evidence during active work.
