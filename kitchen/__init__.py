# -*- coding: utf-8 -*-
"""
Manipulate counts matrix files and cook scRNA-seq data from command line
"""
from .kitchen import (
    info,
    to_h5ad,
    transpose,
    rename_obs,
    add_label,
    knee_point,
    subset,
    concatenate,
    recipe,
)

__all__ = [
    "info",
    "to_h5ad",
    "transpose",
    "rename_obs",
    "add_label",
    "knee_point",
    "subset",
    "concatenate",
    "recipe",
]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
