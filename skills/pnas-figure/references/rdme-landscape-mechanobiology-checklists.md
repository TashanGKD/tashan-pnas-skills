# RDME, Landscape, And Mechanobiology Figure Checklists

## RDME Or Stochastic Polarity Panels

Require:

- state variables and whether they are counts, densities, probabilities, or labels;
- geometry, boundary conditions, and physical units;
- event types and propensities when the panel depends on model definition;
- total-copy-number or mass-conservation rule if used;
- grid spacing, patch scale, and physical interaction scale;
- diffusion, binding, unbinding, feedback, and saturation parameters;
- seed count, simulation duration, sampling interval, and stationarity or burn-in rule;
- representative-vs-ensemble status;
- mesh/refinement validation when making scale or continuum claims.

PNAS-style rationale: Fange-like RDME evidence makes discretization and mesoscopic-rate mapping part of scientific validity, not a numerical footnote.

## Kymograph Or Trajectory Panels

Require:

- spatial/angular coordinate and time units;
- color-scale variable and normalization;
- parameter set;
- seed ID for representative examples;
- ensemble statistic nearby if the text makes an ensemble claim;
- state-transition rule if polarity switching is discussed.

Risk: a visually convincing trajectory can overstate stochastic reliability.

## Phase Diagram Or Parameter Scan

Require:

- axis definitions, units, and nondimensional groups;
- scan grid and interpolation/smoothing rule;
- classification rule for each region;
- repeats or seeds per point;
- boundary uncertainty;
- representative examples from each key region;
- whether parameters are measured, literature-derived, fitted, estimated, or assumed.

Risk: smooth regions can imply stronger precision than the scan supports.

## Landscape, Flux, Dwell, Or Least-Action Panels

Require:

- state space and coordinates;
- estimator for probability, vector field, potential, and flux;
- smoothing, binning, or regularization;
- noise or diffusion intensity when used;
- definition of potential or landscape;
- definition of flux, curl, or force decomposition;
- transition-state and path/action rule if shown;
- dwell-time or MFPT estimator;
- sampling duration and stationarity check;
- robustness to state variables, binning, and perturbation scale;
- data/code availability for reconstruction.

PNAS-style rationale: Zhu/Wang-like landscape/flux figures are only interpretable when the mathematical objects are defined before interpretation.

## Mechanobiology Condition Matrix

For cell mechanics, migration, or substrate-response figures, require:

- stiffness, viscosity, strain, prestrain, strain energy, confinement, ECM coating, or geometry definitions as applicable;
- perturbation condition such as myosin inhibition, adhesion modulation, or matrix manipulation;
- cell type and culture/imaging conditions;
- measurement object such as morphology, migration speed, focal adhesion, actin, stress fiber, traction, MSD, or radius of gyration;
- sample size per condition and independence definition;
- statistical test and error definition;
- model variable linked to experimental condition.

PNAS-style rationale: Pathak/Kumar, Panzetta/Fusco/Netti, Gong, Bennett, Fischer, and Kim show that mechanobiology claims become reviewable when condition variables and mechanistic variables are kept separate.
