
# convenient imports
from .desensitize import Desensitize
from . import implement
from . import detectors

__version__ = VERSION = "1.2.1"


def clean(text, cls=None, **kwargs):
    """Public facing function to clean ``text`` using the scrubber ``cls`` by
    replacing all personal information with ``{{PLACEHOLDERS}}``.
    """
    cls = cls or Desensitize
    scrubber = cls()
    return scrubber.clean(text, **kwargs)
