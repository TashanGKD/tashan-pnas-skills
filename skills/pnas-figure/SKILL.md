---
name: pnas-figure
description: PNAS-oriented scientific figure design, auditing, and generation for manuscript figures, multi-panel plots, simulations, phase diagrams, kymographs, distributions, trajectories, landscape/flux/dwell analyses, captions, and publication exports. Use when Codex is asked to create, revise, critique, or polish figures for PNAS-like papers, especially Python or R figures for theory-simulation biology and RDME/cell-polarity manuscripts.
---

# PNAS Figure

Use this skill to treat figures as visual evidence for a manuscript claim. Start with logic, then layout, then code, then export QA.

## Figure Contract

Before plotting or editing, establish:

1. Core claim: one sentence the figure must support.
2. Reader path: what the reader must understand first, second, third.
3. Panel roles: model, validation, main result, mechanism, robustness, comparison, or prediction.
4. Data provenance: script, input files, parameters, seeds, ensemble size, and output path.
5. Export needs: editable vector, high-resolution raster, plotted data, and caption.

Use `references/figure-contract.md` for detailed panel planning.

For PNAS-like RDME, mechanobiology, landscape, flux, dwell-time, or theory-simulation figures, also use `references/evidence-backed-figure-audit.md`. For specialized RDME/landscape/cell-mechanics panels, use `references/rdme-landscape-mechanobiology-checklists.md`.

## PNAS Visual Style

- Prefer clean white backgrounds and restrained color.
- Use one visual hierarchy: main panel plus supporting panels when possible.
- Keep axes, labels, and units explicit.
- Prefer direct labels when they reduce legend travel.
- Use color to encode scientific meaning, not decoration.
- Make captions self-contained enough for review.
- Verify current PNAS figure specifications before final submission. Do not hard-code mutable rules.

Use `references/visual-style.md` for plotting defaults.

## Simulation And Theory Figures

For RDME, stochastic polarity, and mechanochemical feedback work, classify panels as:

- kymograph or spacetime pattern
- phase diagram or parameter scan
- trajectory or time-series statistic
- distribution or ensemble histogram
- landscape, flux, dwell-time, or transition plot
- theory-vs-simulation comparison
- schematic or model diagram

Use `references/rdme-figure-types.md` for field-specific checks.

## Output

For figure design tasks, return:

1. Figure claim.
2. Panel map.
3. Data and reproducibility requirements.
4. Layout recommendation.
5. Caption skeleton.
6. Review risks.

For code-generation tasks, also save source data or metadata when practical and report exact output paths.
