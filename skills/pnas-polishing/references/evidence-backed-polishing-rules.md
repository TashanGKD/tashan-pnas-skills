# Evidence-Backed PNAS Polishing Rules

## Source Reports

These historical report names document provenance; do not attempt to load them
as files from this package. Use the guidance below independently. Author-year
shorthand records historical reading notes, not a verified bibliography. Check
the original article before citing it or treating its details as evidence.

Historical development sources (not bundled and not runtime dependencies):

- `pnas-style-research-project/reports/PNAS_WRITING_STYLE_REPORT.md`
- `pnas-style-research-project/reports/PNAS_REVIEW_RISK_REPORT.md`
- `pnas-style-research-project/reports/PNAS_THEORY_SIM_MECHBIO_PATTERNS.md`
- `pnas-style-research-project/reports/FULL_RESOLUTION_FORMULA_PARAMETER_AUDIT_2026-05-21.md`

## Core Rule

Polishing must not hide weak evidence. First preserve the claim, evidence, boundary, and uncertainty; only then improve rhythm, concision, and English style.

## Paragraph Diagnosis

Before rewriting, decide whether the paragraph is doing one of these jobs:

- `significance`: broad problem, bottleneck, contribution, boundary;
- `abstract`: context, gap, approach, result, implication, scope;
- `introduction`: problem-to-gap argument;
- `results`: claim plus figure/equation/data evidence;
- `methods`: reproducible definition of procedure or model;
- `discussion`: interpretation, limitation, and future test;
- `caption`: panel-specific evidence and metadata.

Do not polish a paragraph into the wrong section job.

## Claim Calibration

Use stronger verbs only when the provided evidence supports them:

- `show` / `demonstrate`: direct evidence in the tested scope.
- `reveal`: clear mechanistic insight, used sparingly.
- `indicate` / `suggest`: partial, indirect, or model-only support.
- `are consistent with`: compatible but not exclusive.
- `may` / `could`: implication, hypothesis, or future test.

Replace broad impact words with the specific consequence. Replace `novel`, `first`, `universal`, or `general` unless evidence and citations verify them.

## Model-To-Biology Boundary

For RDME, landscape/flux, and mechanobiology text:

- keep model results separate from biological claims;
- state parameter regime or assumption when it limits the claim;
- mark representative trajectories as examples, not population behavior;
- avoid treating fitted agreement as predictive validation;
- distinguish condition variables from mechanism variables.

Safer pattern:

`The model shows [mechanistic result] under [defined assumptions], suggesting [biological hypothesis/test] rather than proving [biological fact].`

## Chinese-To-English Repairs

Common repairs for Chinese scientific drafts:

- move the main claim earlier in Results paragraphs;
- split long causal chains into evidence-first English sentences;
- convert implicit caveats into explicit scope;
- reduce dense noun stacks;
- use repeated technical terms consistently when they refer to the same object;
- avoid translating broad Chinese significance language into English hype.

## Required Polishing Output

For nontrivial passages, return:

- polished version;
- key changes;
- claim-strength warnings;
- missing evidence/citation/parameter flags.
