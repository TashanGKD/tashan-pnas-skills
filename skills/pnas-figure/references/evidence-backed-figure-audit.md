# Evidence-Backed PNAS Figure Audit

## Source Reports

These historical report names document provenance; do not attempt to load them
as files from this package. Use the guidance below independently. Author-year
shorthand records historical reading notes, not a verified bibliography. Check
the original article before citing it or treating its details as evidence.

Historical development sources (not bundled and not runtime dependencies):

- `pnas-style-research-project/reports/PNAS_FIGURE_STYLE_REPORT.md`
- `pnas-style-research-project/reports/PNAS_THEORY_SIM_MECHBIO_PATTERNS.md`
- `pnas-style-research-project/reports/FULL_RESOLUTION_FORMULA_PARAMETER_AUDIT_2026-05-21.md`
- `pnas-style-research-project/reports/TARGETED_FIGURE_FORMULA_PARAMETER_AUDIT_2026-05-21.md`
- `pnas-style-research-project/reports/PRELIMINARY_VISUAL_AUDIT_2026-05-21.md`
- `pnas-style-research-project/reports/EVIDENCE_REGISTER.md`

Evidence quality caveat: selected pages in key papers were checked from full-resolution PDF renders; some corpus-wide observations come from MinerU text/caption extraction and contact sheets. Do not quote equations from OCR without checking the rendered PDF page.

## Core Rule

For a research manuscript, a PNAS-like figure is a claim-support instrument, not a polished output dump. Visual polish is secondary to operational clarity: the reviewer must see what is measured or simulated, which variable is being tested, what assumptions or parameters define the panel, and where SI supplies the missing derivation or parameter ledger.

## Evidence-Backed Figure Jobs

Use one primary job per panel:

- `model`: define geometry, state variables, reactions, feedback, or mechanical coupling.
- `validation`: show limiting behavior, reproduction, grid/refinement behavior, or known-regime agreement.
- `main result`: show the central phenomenon.
- `mechanism`: isolate why the phenomenon occurs.
- `robustness`: show parameter, seed, mesh, estimator, or perturbation sensitivity.
- `comparison`: connect model to experiment, prior model, or theory.
- `prediction`: state a testable consequence.

Drop panels that do not add distinct evidence.

## Caption Metadata

Captions should state, when relevant:

- panel condition and perturbation;
- plotted variable definition;
- units or nondimensionalization;
- parameter-set label plus key values;
- sample size, seed count, or ensemble size;
- statistic, error-bar definition, and test;
- representative-vs-ensemble status;
- classification rule for phase or state labels;
- source script/data path when practical.

## Article-Derived Figure Lessons

- Fange 2010: RDME figures should expose microscopic-to-mesoscopic mapping and discretization dependence when grid scale affects behavior.
- Shao 2012 and Gong 2018: compact parameter tables can be essential figure-adjacent evidence.
- Walcott/Sun 2010: dense mechanics needs glossary and derivation figures in SI.
- Pathak/Kumar 2012: stiffness, confinement, perturbation, sample size, and statistic should form a visible condition matrix.
- Panzetta/Fusco/Netti 2019: if claiming `X rather than Y`, figures must separately operationalize and show `X` and `Y`.
- Zhu/Wang 2024: landscape, flux, action, path, transition-state, perturbation, and network figures require mathematical object definitions and data/code availability.

## High-Risk Failure Modes

- A single attractive trajectory is used as ensemble evidence.
- A smooth phase boundary implies precision beyond scan resolution.
- A landscape plot implies equilibrium without defining nonequilibrium flux.
- A schematic hides which variables are state variables, controls, or observables.
- A model comparison calls fitted agreement a prediction.
- A figure depends on assumed or fitted parameters without marking their status.
- A main-text figure makes a claim whose derivation, parameter source, or estimator is not findable in SI.

## Minimum Audit Output

When auditing or designing a figure, return:

- figure claim;
- panel role map;
- evidence and data provenance;
- missing definitions or metadata;
- reviewer-risk notes;
- caption skeleton with parameters/statistics/source-data fields.
