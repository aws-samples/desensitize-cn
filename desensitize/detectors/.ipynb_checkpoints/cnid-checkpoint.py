import re

from .base import RegexDetector
from ..implement import CNIDImplement


class CNIDDetector(RegexDetector):
    """Use regular expression magic to remove email addresses from dirty
    dirty ``text``. This method also catches email addresses like ``john at
    gmail.com``.
    """
    filth_cls = CNIDImplement
