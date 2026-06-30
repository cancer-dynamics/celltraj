# Installation

For normal development from a local checkout:

```bash
cd /path/to/celltraj
python -m pip install -e .
```

For documentation-only work, install the lightweight docs requirements:

```bash
python -m pip install -r docs/requirements.txt
```

The docs build mocks heavy scientific dependencies so documentation can be
generated without installing every analysis backend.

For full trajectory-analysis work, use the project environment files as a
starting point and add optional scientific dependencies required by the
specific workflow you are running.
