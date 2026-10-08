# Caption And Claim Calibration

## Source Reports

These historical report names document provenance; do not attempt to load them
as files from this package. Use the guidance below independently. Author-year
shorthand records historical reading notes, not a verified bibliography. Check
the original article before citing it or treating its details as evidence.

Historical development sources (not bundled and not runtime dependencies):

- `pnas-style-research-project/reports/PNAS_FIGURE_STYLE_REPORT.md`
- `pnas-style-research-project/reports/PNAS_SI_STRUCTURE_REPORT.md`
- `pnas-style-research-project/reports/FULL_RESOLUTION_FORMULA_PARAMETER_AUDIT_2026-05-21.md`

## Caption Polishing Principle

A PNAS-like caption should let a reviewer understand what the panel shows, what evidence it contributes, and what assumptions or statistics are needed to interpret it. Do not polish away parameters, units, sample sizes, seed counts, or classification rules.

## Caption Skeleton

Use:

`Figure X. [Main claim]. (A) [Panel role and measured/simulated object]. (B) [Panel role]. Parameters: [key values and units]. Statistics: [n/seeds/ensemble, test, error definition]. Source: [data/script/SI section if relevant].`

For compact captions, keep the claim and metadata; move derivation and parameter tables to SI, but point to them.

## Must-Preserve Metadata

When provided, preserve:

- variables and units;
- parameter values or labels;
- seed count or sample size;
- representative-vs-ensemble status;
- perturbation and control definitions;
- classification or transition rule;
- estimator, smoothing, or binning rule;
- uncertainty, error bars, or statistical test;
- SI section, source data, or script reference.

## Claim Calibration By Figure Type

- Representative trajectory: use `illustrates`, not `demonstrates ensemble behavior`.
- Parameter scan: mention scan resolution and classification rule before claiming regimes.
- Phase diagram: avoid precise boundary language unless uncertainty is quantified.
- Landscape/flux: avoid equilibrium wording unless justified; define state space and flux.
- Theory-vs-simulation: distinguish fitted agreement from prediction.
- Mechanobiology image panels: avoid causal language from representative images alone.
- Perturbation panels: state the perturbation and control, then the measured response.

## Reviewer Flags

Flag captions or figure-linked prose if:

- the figure's claim is broader than its panel evidence;
- axes, units, state variables, or conditions are undefined;
- sample size or seed count is missing for statistical claims;
- a single image or trajectory supports a general statement;
- parameter status is hidden;
- SI support is required but not referenced.
