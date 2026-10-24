"""Shared rules for Gr0wthPilot's tool wrappers (bin/gp-*).

The wrappers read the run's config from the environment variable the launcher
sets, GR0WTHPILOT_CONFIG, and refuse to run without it.
"""

from __future__ import annotations

import os
from pathlib import Path

import gp_common as gc


class ToolError(Exception):
    pass


def load_config():
    path = os.environ.get("GR0WTHPILOT_CONFIG")
    if not path or not Path(path).is_file():
        raise ToolError("no Gr0wthPilot run config; these tools run only inside a run started "
                        "with bin/gr0wthpilot <Product>")
    return gc.read_json(Path(path))


def inside(path, root) -> bool:
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
        return True
    except ValueError:
        return False


def require_inside(cfg, path, label, roots=("work", "package")):
    """Resolve a path the wrapper will read or write and require it to lie in
    one of the run's allowed places: its cache folder, its Candidate Package, or
    (for reading) the Product repository."""
    p = Path(path).expanduser()
    if not p.is_absolute():
        p = Path.cwd() / p
    p = p.resolve()
    for name in roots:
        root = cfg.get(name)
        if root and inside(p, root):
            for protected in cfg.get("protected") or []:
                if inside(p, protected):
                    raise ToolError("%s %s is in a protected package" % (label, p))
            return p
    allowed = [cfg.get(name) for name in roots if cfg.get(name)]
    raise ToolError("%s %s must be inside %s" % (label, p, " or ".join(allowed)))
