# Quickstart

Import core modules from the package namespace:

```python
from celltraj.trajectory import Trajectory
from celltraj import features, imageprep, model
```

Run the lightweight CLI smoke command:

```bash
celltraj
```

Most real analyses are currently run from notebooks and scripts that create or
load HDF5 trajectory/model files, extract image and mask features, and run
trajectory or state-modeling routines. The near-term integration work with
`sitelab` will make those entry points more explicit and better documented.
