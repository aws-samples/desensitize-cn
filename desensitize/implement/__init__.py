import os
import re

from ..import_magic import iter_subclasses, update_locals
from .base import Implement, RegexImplement, MergedImplement


def _is_abstract_filth(filth_cls):
    """Implement must have a ``type`` defined"""
    return filth_cls.type is None


def iter_filth_clss():
    """Iterate over all of the filths that are included in this sub-package.
    This is a convenience method for capturing all new Implement that are added
    over time.
    """
    return iter_subclasses(
        os.path.dirname(os.path.abspath(__file__)),
        Implement,
        _is_abstract_filth,
    )


def iter_filths():
    """Iterate over all instances of implement"""
    for filth_cls in iter_filth_clss():
        if issubclass(filth_cls, RegexImplement):
            m = next(re.finditer(r"\s+", "fake pattern string"))
            yield filth_cls(m)
        else:
            yield filth_cls()

# import all of the detector classes into the local namespace to make it easy
# to do things like `import desensitize.detectors.NameDetector`
update_locals(locals(), iter_filths)
