---
name: pnas-polishing
description: PNAS-oriented scientific prose polishing, Chinese-to-English rewriting, paragraph restructuring, claim calibration, and style cleanup for manuscript paragraphs, abstracts, Significance Statements, Results, Discussion, figure captions, and cover-letter or response text. Use when Codex is asked to make scientific writing clearer, more concise, more PNAS-like, or more publication-ready without inventing evidence.
---

# PNAS Polishing

Use this skill after the scientific logic is known. Polishing must improve clarity and claim discipline without inventing evidence, citations, novelty, mechanisms, or results.

## First Diagnosis

Before rewriting, classify the main problem:

- argument is unclear
- claim is stronger than evidence
- paragraph lacks a topic sentence
- Chinese structure has not been converted to English scientific logic
- section job is wrong
- wording is verbose or awkward
- terminology is inconsistent
- caption lacks parameters or definitions

If the argument is broken, repair structure before sentence style.

## Polishing Workflow

1. Identify the paragraph job: context, gap, approach, result, mechanism, implication, limitation, or transition.
2. Preserve all factual content and mark missing evidence.
3. Calibrate claim strength.
4. Reduce jargon density for broad PNAS readers.
5. Make sentence subjects concrete.
6. Prefer direct verbs and concise clauses.
7. Keep limitations visible.

Use `references/style-guardrails.md` for wording rules and `references/chinese-to-english.md` for Chinese drafts.

For theory-simulation, RDME, landscape/flux, stochastic polarity, mechanobiology, Significance Statement, Abstract, Results, or Discussion polishing, also use `references/evidence-backed-polishing-rules.md`. For figure captions or claim-heavy sentences tied to plots, use `references/caption-and-claim-calibration.md`.

## Output

Default output:

1. Polished version.
2. What changed.
3. Claim-strength notes.
4. Missing evidence or citation flags.

For Chinese input, provide polished English first, then brief Chinese notes on structural choices.
