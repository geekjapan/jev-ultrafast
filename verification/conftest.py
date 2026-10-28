"""Load both local forks without replacing their production modules."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BROWSER_USE = Path(os.environ.get("BROWSER_USE_REPO", ROOT.parent / "browser-use")).resolve()
sys.path[:0] = [str(ROOT), str(BROWSER_USE), str(BROWSER_USE / "tests" / "ci")]
