from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version as package_version
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

project = "celltraj"
author = "Jeremy Copperman"
copyright = "2026, Jeremy Copperman"

try:
    release = package_version("celltraj")
except PackageNotFoundError:
    init_file = SRC / "celltraj" / "__init__.py"
    namespace: dict[str, str] = {}
    exec(init_file.read_text(encoding="utf-8"), namespace)
    release = namespace.get("__version__", "0.1.86")
version = release

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["docutils"]

html_theme = "sphinx_rtd_theme"
html_title = "celltraj documentation"
html_baseurl = "https://cancerdynamics.org/docs/celltraj/"
html_extra_path = ["_extra"]
html_copy_source = False

autosummary_generate = True
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
autodoc_typehints = "description"

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_preprocess_types = True
napoleon_include_init_with_doc = True

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

autodoc_mock_imports = [
    "adjustText",
    "btrack",
    "csaps",
    "dask",
    "fipy",
    "h5py",
    "click",
    "mahotas",
    "matplotlib",
    "multipoles",
    "nanomesh",
    "numpy",
    "ot",
    "pandas",
    "pcdiff",
    "pyemma",
    "pygpcca",
    "pyntcloud",
    "pystackreg",
    "scipy",
    "skimage",
    "sklearn",
    "torch",
    "umap",
]
