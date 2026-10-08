# Figure Contract

## Core Question

Every figure should answer one manuscript-level question. Write it before making panels.

Examples:

- Does stochastic positive feedback generate persistent polarity?
- Which parameter regime separates transient clustering from stable polarization?
- Does the reduced theory reproduce RDME simulation outcomes?
- Which mechanism controls dwell times between polarity states?

## Panel Role Map

Use one role per panel:

- `model`: define system, variables, reactions, or geometry.
- `validation`: show known limiting behavior or reproduction of prior result.
- `main result`: show the primary observation.
- `mechanism`: explain why the result occurs.
- `robustness`: parameter scan, sensitivity, seed ensemble, or boundary test.
- `comparison`: theory vs simulation, model vs experiment, or prior model.
- `prediction`: testable consequence.

Drop panels that do not carry unique evidence.

## Caption Skeleton

Use:

`Figure X. [Main claim]. (A) [Panel role and what is shown]. (B) [Panel role]. ... Parameters: [key values and units]. Statistics: [n, seeds, ensemble, error definition]. Source: [simulation/data/script if relevant].`

Do not hide model assumptions only in the main text if they are needed to interpret the figure.
