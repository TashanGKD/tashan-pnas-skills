<!-- Tashan logo -->
<p align="center">
  <a href="https://tashan.ac.cn" target="_blank" rel="noopener noreferrer">
    <img src="docs/assets/tashan.svg" alt="Tashan Logo" width="280" />
  </a>
</p>

<p align="center">
  <strong>Tashan PNAS Skills</strong><br>
  <em>Manuscript Writing, Scientific Figure Design &amp; Evidence-Preserving Polishing</em>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#choose-a-skill">Skills</a> •
  <a href="#installation">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#before-and-after">Before &amp; after</a> •
  <a href="#ecosystem">Ecosystem</a> •
  <a href="README.md">中文</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 3](https://img.shields.io/badge/Skills-3-2E74B5.svg)](skills/)

> Turn research evidence into manuscript arguments, scientific figures, and precise prose.

---

## Overview

These Agent Skills form part of the research methods and scientific communication layer of Tashan's human–agent digital world. They capture recurring decisions in manuscript work: establish the question, evidence, and scope; organize the text and figures; then refine the language. Researchers provide the evidence and retain responsibility for scientific judgment.

Developed in Tashan research projects, the suite targets theoretical and computational biology, biophysics, and systems biology. Specialized references cover reaction–diffusion master equations (RDME), stochastic cell polarity, mechanochemical feedback, and landscape/flux analysis. Other fields can use the workflows with appropriate domain adjustments.

- **Organize around evidence:** connect major claims to figures, equations, data, or verified literature and state their scope.
- **Treat figures as arguments:** define panel roles, observables, statistical meaning, and provenance.
- **Preserve scientific meaning:** distinguish model results, biological interpretations, and predictions while retaining parameters and uncertainty.

Use the skills for first drafts, Results restructuring, multi-panel figures, Chinese-to-English rewriting, or reviewer-response text. They contain instructions and references, not a model, literature database, plotting engine, or document compiler. File generation uses the tools available in the host Agent.

PNAS denotes a communication orientation. This project is independently maintained by Tashan and is not affiliated with or endorsed by PNAS. It does not guarantee publication or a measured quality improvement. Verify current journal requirements before submission.

---

## Choose a skill

| Skill | Use when | Input | Deliverables |
| --- | --- | --- | --- |
| [`pnas-writing`](skills/pnas-writing/SKILL.md) | Drafting or restructuring an argument | Question, model/methods, figures, results, evidence gaps | Draft/outline, claim–evidence map, structure notes, overclaims and gaps |
| [`pnas-figure`](skills/pnas-figure/SKILL.md) | Planning, auditing, or revising figures | Figure question, data/scripts, variables, parameters, statistics | Claim, panel map, layout, caption, reproducibility needs; figure files when tools and data permit |
| [`pnas-polishing`](skills/pnas-polishing/SKILL.md) | Scientific logic is known and wording needs work | Original text, section, terminology, facts and boundaries | Revised text, changes, claim-strength notes, missing evidence flags |

Each skill is independently installable. A typical manuscript workflow starts with writing, checks the figure argument, and then polishes prose. If the figure audit exposes missing evidence, revisit the argument and research before refining the language.

---

## Installation

### 1. Get the repository

The installer needs Git and Python 3.9+ and uses only the standard library. The skills themselves do not require Python; plotting and document dependencies depend on the task. Alternatively, download and extract **Code → Download ZIP** and run the installer from the extracted directory.

```bash
git clone https://github.com/TashanGKD/tashan-pnas-skills.git
cd tashan-pnas-skills
```

### 2. Install for Codex

Windows PowerShell:

```powershell
# Preview without changing files
python .\scripts\install.py --dry-run
# Install all three skills to ~/.agents/skills
python .\scripts\install.py
# Alternatively, install just one
python .\scripts\install.py --skill pnas-writing
```

macOS / Linux:

```bash
python3 scripts/install.py --dry-run
python3 scripts/install.py
# Alternatively, install only the figure skill
python3 scripts/install.py --skill pnas-figure
```

Current [OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) lists `~/.agents/skills` for personal skills and `<project>/.agents/skills` for project skills. Use `--dest` for an explicitly configured alternative. Avoid duplicate names across scanned directories.

```powershell
# Replace this example with your project path
python .\scripts\install.py --dest 'D:\my-paper\.agents\skills'
# For an existing environment using ~/.codex/skills
python .\scripts\install.py --dest "$env:USERPROFILE\.codex\skills"
```

Manual installation also works: copy the complete desired folders under `skills/` to the host's skills directory, including `references/` and `agents/`. Other `SKILL.md`-compatible agents can reuse the content, but discovery paths and invocation syntax depend on the product; cross-product behavior has not been individually tested.

### 3. Confirm discovery

In a new Codex conversation, try:

```text
Use $pnas-writing to read the research material I provide.
First produce a claim–evidence–scope table, then a Results outline.
Flag missing evidence instead of inventing findings or citations.
```

If the skill is missing, restart Codex and check that `~/.agents/skills/pnas-writing/SKILL.md` exists.

### Updating and removing

If any requested destination already exists, the installer stops before copying. To update, run `git pull --ff-only`, back up the old skill directories **outside scanned skill locations**, then run the installer. You can also install into a separate staging directory to inspect changes first. To uninstall, remove only the installed skill folders. The installer does not edit Agent settings, read credentials, or use the network.

---

## Usage

### pnas-writing: organize research into a manuscript

Provide the question, key results, figures/equations, model assumptions, parameter regimes, validation, and target section. Incomplete materials are acceptable if gaps remain explicit.

```text
Use $pnas-writing to draft a manuscript from my notes, figures, and methods.
Topic: state switching in a stochastic cell-polarity model.
Map what each figure does and does not support, then outline Significance,
Abstract, Introduction, Results, Discussion, and Methods.
Separate simulation observations, mechanistic interpretations, and experimental
predictions. Leave explicit placeholders for missing controls and parameter sources.
```

Expect a draft or outline, evidence map, structural notes, overclaim and citation flags, and next revision actions. A title, abstract, Significance Statement, introduction, or single Results subsection can be requested on its own. Check that the prose matches the inputs, Methods describes actual procedures, and unfinished validation remains marked.

### pnas-figure: plan and audit scientific figures

Provide the scientific question, panels, data and plotting scripts, variables/units, parameters, seeds, and statistical definitions. Without data, request a plan; do not present invented plots as experimental or simulation results.

```text
Use $pnas-figure to assess whether these three trajectories support the claim
that feedback affects switching dynamics. Define the figure claim and panel roles.
Check variables, units, seeds, observation duration, and transition definitions.
Separate representative observations from conclusions requiring ensembles or controls.
Propose a layout and caption. If the data suffice, revise the plotting script and
export SVG/PDF, a PNG preview, and a record of parameters and data provenance.
```

Expect a claim, panel map, layout/color guidance, caption, reproducibility requirements, and review risks. With data and execution tools, the Agent can also create code and figures. Check ensemble definitions, phase classification/interpolation, error bars, fitted versus predictive comparisons, and readability at the intended size.

### pnas-polishing: refine wording without changing evidence

Provide the original paragraph, section, terminology, fixed numbers/conditions, and supporting evidence. Chinese input defaults to polished English followed by brief Chinese notes; explicitly request another language if preferred.

```text
Use $pnas-polishing to revise this Results paragraph in scientific English.
Preserve all numbers, parameters, figure references, and qualifications.
Do not add mechanisms or citations. Explain the key changes and separately
identify claims that exceed the evidence and the validation they need.
Original: [paste paragraph]
Evidence and scope: [describe data, model, and completed validation]
```

Expect revised prose, change notes, claim-strength checks, and missing-information flags. If the argument is unsound, the skill should identify the structural issue before making sentences more fluent.

---

## Before and after

These are **authored teaching examples**, not model A/B tests, real research findings, or performance guarantees. See [the example set](examples/before-after.md) for shared inputs, target responses, and review criteria.

| Skill | Before: input or approach | After: illustrative application |
| --- | --- | --- |
| `pnas-writing` | A chronological “built model → plotted → saw switching” report ending in a universal biological claim | Results organized around model definition, available validation, observed switching, untested mechanism, and scope; missing controls remain explicit |
| `pnas-figure` | Three attractive trajectories with a caption saying only “polarity over time” | Representative status, variables, units, and parameters are explicit; proposed ensemble/control panels are marked as awaiting data |
| `pnas-polishing` | “We reveal the universal mechanism of cell-polarity switching for the first time.” | “In the simulated trajectory, polarity switched between states under the tested parameter conditions. Establishing a causal role for feedback requires a matched perturbation control.” |

The intended differences are argument structure, inspectability, and calibrated language. A skill cannot turn a single simulation into ensemble evidence or missing experiments into a validated mechanism.

---

## Repository structure and documentation

```text
tashan-pnas-skills/
├── README.md / README.en.md       # Bilingual setup and usage
├── skills/
│   ├── pnas-writing/              # Argument and manuscript workflow
│   ├── pnas-figure/               # Figure logic and reproducibility
│   └── pnas-polishing/            # Prose and claim calibration
├── examples/before-after.md       # Teaching examples and review criteria
├── scripts/install.py            # Standard-library, no-overwrite installer
├── tests/test_install.py          # Installation and conflict checks
├── docs/PROVENANCE.md             # Development history and attribution
├── docs/assets/tashan.svg         # Tashan logo
├── licenses/nature-skills-MIT.txt # External design-reference license
├── CONTRIBUTING.md / CHANGELOG.md
└── LICENSE                       # MIT
```

Each skill includes `SKILL.md`, `references/`, and `agents/`. Historical report names document provenance; those reports are not shipped and are not runtime dependencies. The original research project and paper PDFs are unnecessary for installation. Raw research data, unpublished manuscripts, personal conversations, and credentials are outside this package.

---

## Origins and validation scope

The suite originated in Tashan research work in May 2026 and was expanded from local PNAS and related-paper reading notes. `Yuan1z0825/nature-skills` informed modular architecture and workflow design; the manuscript instructions and specialized checks were developed for PNAS-oriented theory and simulation work. See [PROVENANCE](docs/PROVENANCE.md) for attribution and scope.

This release checks skill structure, internal references, installation behavior, and package contents. The examples have not undergone independent model-controlled evaluation. Historical article observations are not mandatory journal rules or a substitute for current author instructions.

---

## Ecosystem

```text
Tashan digital world
├── General Agent workflows and collaboration
├── Research methods and scientific communication
│   ├── tashan-research-skills     # Broad research tasks
│   ├── tashan-pnas-skills         # This repository
│   └── tashan-ppt-skills          # Presentations and pitch decks
└── Research projects and applications
```

| Related repository | Relationship |
| --- | --- |
| [tashan-research-skills](https://github.com/TashanGKD/tashan-research-skills) | Complementary general research workflows; no installation dependency |
| [tashan-ppt-skills](https://github.com/TashanGKD/tashan-ppt-skills) | Presentation workflows; no installation dependency |
| [tashan-world](https://github.com/TashanGKD/tashan-world) | Digital-world application; no runtime dependency |

---

## Contributing

Contribute cases with inspectable inputs, a clear problem, and an evidence-preserving improvement. Do not submit unauthorized manuscripts, datasets, or full-text papers. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

---

## License

[MIT License](LICENSE). See the [third-party notice](licenses/nature-skills-MIT.txt) for the external design reference. The Tashan name and logo identify the project; the software license does not grant rights to impersonate the organization or claim its endorsement.
