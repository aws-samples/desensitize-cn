import re

from .base import RegexDetector
from ..implement import EmailImplement


class EmailDetector(RegexDetector):
    """Use regular expression magic to remove email addresses from dirty
    dirty ``text``. This method also catches email addresses like ``john at
    gmail.com``.
    """
    filth_cls = EmailImplement
