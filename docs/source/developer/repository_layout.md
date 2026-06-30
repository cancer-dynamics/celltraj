# Repository Layout

The package now uses a standard `src/` layout:

```text
celltraj/
  pyproject.toml
  README.rst
  src/
    celltraj/
      __init__.py
      trajectory.py
      features.py
      imageprep.py
      model.py
      spatial.py
      translate.py
      utilities.py
  docs/
    source/
    make_docs.sh
    publish_to_cancerdynamics.py
  tests/
  tutorials/
```

Important cleanup decisions:

- Package modules should import siblings through the package namespace or
  relative imports, not by adding `celltraj/celltraj` to `sys.path`.
- Generated docs live in `docs/build/html/` and are ignored by Git in this
  repository.
- Public docs are copied into `cancerdynamics-website/public/docs/celltraj/`.
- Legacy generated HTML and root-level docs artifacts are no longer committed
  to this package repo.
- `sphinx.ext.viewcode` is not enabled for public docs. API pages expose
  docstrings and signatures, not browsable source code.
