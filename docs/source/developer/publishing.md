# Publishing

`celltraj` owns its documentation source and Sphinx build, then copies the
generated static HTML into the public CancerDynamics.org Astro repo.

Published path:

```text
cancerdynamics-website/public/docs/celltraj/
```

Published URL after the website repo is deployed:

```text
https://cancerdynamics.org/docs/celltraj/
```

## Build Locally

Install docs dependencies:

```bash
python -m pip install -r docs/requirements.txt
```

Build docs:

```bash
bash docs/make_docs.sh
```

Open:

```text
docs/build/html/index.html
```

## Copy Into CancerDynamics.org

Build and copy in one command:

```bash
python docs/publish_to_cancerdynamics.py --build --strict
```

If the website repo is somewhere else:

```bash
python docs/publish_to_cancerdynamics.py --build --website /path/to/cancerdynamics-website
```

The script replaces only:

```text
cancerdynamics-website/public/docs/celltraj/
```

It does not commit or push the website repo.
