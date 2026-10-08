# SI, Parameter, And Reproducibility Evidence Rules

## Source Reports

These historical report names document provenance; do not attempt to load them
as files from this package. Use the guidance below independently. Author-year
shorthand records historical reading notes, not a verified bibliography. Check
the original article before citing it or treating its details as evidence.

Historical development sources (not bundled and not runtime dependencies):

- `pnas-style-research-project/reports/PNAS_SI_STRUCTURE_REPORT.md`
- `pnas-style-research-project/reports/PNAS_THEORY_SIM_MECHBIO_PATTERNS.md`
- `pnas-style-research-project/reports/FULL_RESOLUTION_FORMULA_PARAMETER_AUDIT_2026-05-21.md`
- `pnas-style-research-project/reports/PNAS_FIGURE_STYLE_REPORT.md`
- `pnas-style-research-project/reports/PNAS_REVIEW_RISK_REPORT.md`

## Core Rule

For PNAS-like theory, simulation, and mechanobiology papers, SI is the audit trail. It is not a dumping ground. It should make the main-text claims reviewable, reproducible, and bounded.

## Main Text vs SI Division

Main text should carry:

- central question;
- model concept or experimental system;
- decisive figures;
- mechanism;
- broad significance;
- essential assumptions needed to understand claims.

SI should carry:

- complete derivations;
- full model definitions;
- parameter ledger;
- algorithm and numerical method;
- grid/time-step/mesh checks;
- seed/ensemble protocol;
- estimator definitions;
- robustness and sensitivity checks;
- code/data/software availability.

## Parameter Ledger Requirements

For each parameter, include:

- symbol;
- meaning;
- value or range;
- unit;
- source;
- status: measured, literature-derived, fitted, estimated, or assumed;
- sensitivity or robustness locator;
- figure/equation where it matters.

Article-derived precedent:

- Shao 2012 and Gong 2018 show parameter tables as core computational evidence.
- Walcott/Sun 2010 shows order-of-magnitude estimates and section-local symbol discipline.
- Pathak/Kumar 2012 and Panzetta/Fusco/Netti 2019 show that mechanical condition variables must not be collapsed into one generic "mechanics" parameter.

## Glossary And Equation Requirements

Use section-local glossaries when:

- symbols are reused across model layers;
- equations combine mechanics, stochastic dynamics, or biochemical state variables;
- SI includes separate derivation blocks;
- variables change between dimensional and nondimensional forms.

For RDME or stochastic models, define:

- state space;
- conservation laws;
- event list;
- propensities;
- units;
- boundary conditions;
- numerical method;
- random seeds and ensemble design.

## Landscape, Flux, And Dwell SI Requirements

Define:

- state coordinates;
- probability or density estimator;
- vector-field estimator;
- smoothing/binning/regularization;
- potential or landscape formula;
- flux or force decomposition;
- transition definition;
- dwell-time or MFPT estimator;
- stationarity or sampling checks;
- perturbation size and interpretation;
- code/data path.

## Reviewer-Risk Checks

Flag the manuscript if:

- a main-text claim has no SI support map;
- a parameter lacks unit or source;
- fitted and assumed parameters are not marked;
- a landscape/flux figure lacks estimator definitions;
- mesh or physical-scale claims lack validation;
- statistical/sample-size information appears only in code or not at all;
- code/data availability is described vaguely.
