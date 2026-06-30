# Overview

`celltraj` contains the trajectory-analysis layer for live-cell imaging data.
The current modules cover:

- image and mask preprocessing,
- per-cell feature extraction,
- HDF5-backed trajectory objects,
- trajectory embedding and state decomposition,
- Markov/Koopman-style dynamical modeling,
- spatial and boundary-aware feature utilities, and
- translation between morphodynamic states and molecular measurements.

The package predates `sitelab`, so some APIs still reflect notebook-era
research workflows. Current modernization work is focused on making these APIs
cleaner, package-relative, testable, and easier for `sitelab` to call.
