# Visual Style And Export

## Python Defaults

Use these as a starting point, then adapt to the manuscript.

```python
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7,
    "axes.linewidth": 0.7,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "legend.frameon": False,
})
```

## Color

- Use neutral gray/black for context.
- Use one main signal color family for the key result.
- Use one contrasting accent for comparison or perturbation.
- Use perceptually ordered colormaps for scalar fields.
- Avoid rainbow colormaps unless reproducing a field convention.
- Make phase diagrams colorblind-aware and label regions directly when possible.

## Export

For code-generated final figures, prefer:

- SVG or PDF with editable text.
- PNG or TIFF at high resolution for raster preview or journal upload.
- CSV/NPZ/JSON source data for plotted values when practical.
- Metadata file with script path, command, parameters, seed, input, and output.

Verify current PNAS file-format and resolution requirements before submission.
