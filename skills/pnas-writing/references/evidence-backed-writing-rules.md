# Evidence-Backed PNAS Writing Rules

## Source Reports

These historical report names document provenance; do not attempt to load them
as files from this package. Use the guidance below independently. Author-year
shorthand records historical reading notes, not a verified bibliography. Check
the original article before citing it or treating its details as evidence.

Historical development sources (not bundled and not runtime dependencies):

- `pnas-style-research-project/reports/PNAS_WRITING_STYLE_REPORT.md`
- `pnas-style-research-project/reports/PNAS_THEORY_SIM_MECHBIO_PATTERNS.md`
- `pnas-style-research-project/reports/PNAS_REVIEW_RISK_REPORT.md`
- `pnas-style-research-project/reports/FULL_RESOLUTION_FORMULA_PARAMETER_AUDIT_2026-05-21.md`
- `pnas-style-research-project/reports/EXPANDED_DEEP_READING_SYNTHESIS_2026-05-21.md`
- `pnas-style-research-project/reports/EVIDENCE_REGISTER.md`

Evidence quality caveat: these rules are project-derived from local PNAS/PNAS-adjacent papers and parsed corpus evidence. Verify current official PNAS author instructions before encoding submission-format limits.

## Core Writing Model

Use:

`broad question -> unresolved gap -> compact approach -> figure-backed result -> significance -> boundary`

For an RDME manuscript, connect the model to the scientific question it tests. A mechanism claim about stochastic mechanochemical feedback is appropriate only when the supplied evidence supports it; do not impose that claim on an unrelated project.

## Claim-Evidence-Boundary Discipline

For every paragraph-level claim, identify:

- claim: what is being asserted;
- evidence: figure, equation, simulation, experiment, parameter table, or citation;
- boundary: parameter regime, model assumption, data source, or biological scope;
- risk: what a reviewer could challenge.

Do not draft broad mechanism language until the evidence and boundary are explicit.

## Section Moves

### Significance Statement

Move sequence:

`broad problem -> conceptual bottleneck -> what this work resolves -> why it matters beyond the narrow model -> boundary`

Do not repeat the abstract. Avoid unverifiable `first`, `universal`, or field-changing claims unless independently checked.

### Abstract

Move sequence:

`context -> gap -> approach/model/data -> key finding -> implication -> boundary`

For theory-simulation work, name the evidence type: stochastic simulation, analytical reduction, parameter scan, landscape/flux analysis, model-experiment comparison, or perturbation test.

### Introduction

Use an hourglass:

1. broad biological or physical problem;
2. what is known;
3. unresolved mechanism or conceptual gap;
4. why prior approaches are insufficient;
5. this paper's controlled model/data approach;
6. main advance and scope.

Group literature by mechanism or limitation, not by chronology.

### Results

Use an evidence ladder:

1. define model/system only as needed;
2. validate known behavior or limiting cases;
3. show central phenomenon;
4. diagnose mechanism;
5. test robustness across regimes;
6. connect to biological or physical interpretation.

Each Results subsection should open with a testable claim.

### Discussion

Move sequence:

`central advance -> mechanism -> relation to prior work -> limitations -> predictions or future tests`

Separate mathematical/model results, simulation observations, biological interpretations, and experimental predictions.

## Domain-Specific Writing Patterns

- RDME writing must define state variables, conservation laws, event propensities, physical units, parameter regimes, and mesh/physical-scale logic before biological interpretation.
- Landscape/flux writing must define state space, estimator, smoothing/binning, stationarity, noise assumptions, transition criteria, and nonequilibrium interpretation.
- Mechanobiology writing must distinguish condition variables from mechanistic variables: stiffness, viscosity, strain, prestrain, strain energy, confinement, ECM coating, contractility, adhesion, and migration output are not interchangeable.
- Stochastic switching claims require ensemble language: seeds, sampling duration, transition rule, dwell estimator, and uncertainty.

## Verb Calibration

- `show` or `demonstrate`: direct evidence within tested scope.
- `reveal`: only for clear mechanistic insight.
- `indicate` or `suggest`: partial or indirect support.
- `are consistent with`: compatibility, not proof.
- `may` or `could`: hypothesis, implication, or future test.

Model-to-biology rule: `the model demonstrates` can be strong; `cells therefore` requires experimental or literature support.
