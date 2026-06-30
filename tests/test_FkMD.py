"""Legacy Koopman/FkMD regression fixture.

The original test executed a MATLAB-reference comparison at import time and
patched ``sys.path`` to a workstation-specific path. Keep the fixture data in
the repository for now, but do not run this as part of the normal test suite
until it is rewritten as a fast, isolated pytest test.
"""

from pathlib import Path

import pytest


pytestmark = pytest.mark.skip(
    reason="legacy numerical regression needs a modern, isolated pytest rewrite"
)


def test_legacy_fkmd_fixture_files_exist():
    fixture_dir = Path(__file__).parent / "FkMD_test"
    assert (fixture_dir / "noisy_lorenz_data.mat").exists()
