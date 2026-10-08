# RDME And Cell-Polarity Figure Types

## Kymograph

Must define:

- angular or spatial coordinate
- time axis and units
- molecule count or density quantity
- color scale and normalization
- seed or ensemble status
- parameter set

Risk: A visually striking single trajectory may not support an ensemble claim.

## Phase Diagram Or Parameter Scan

Must define:

- axes and nondimensional groups
- classification rule
- number of seeds or repeats per point
- boundary uncertainty or interpolation method
- representative examples from key regions

Risk: Smooth boundaries can imply precision not supported by scan resolution.

## Distribution Or Ensemble Statistic

Must define:

- sample size
- seed count
- statistic and binning
- error bars or confidence intervals
- whether data are independent

Risk: Histogram shape can be dominated by bin choice or transient sampling.

## Landscape, Flux, Dwell

Must define:

- state variables
- estimator
- smoothing or regularization
- transition definition
- sampling duration and stationarity check

Risk: Landscape metaphors can imply equilibrium when the system is non-equilibrium.

## Theory-Vs-Simulation

Must define:

- matched parameter definitions
- units and nondimensionalization
- fitting or calibration procedure
- quantity compared
- failure regimes

Risk: Agreement after fitting is not the same as predictive validation.
