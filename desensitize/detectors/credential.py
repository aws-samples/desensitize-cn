
from .base import RegexDetector
from ..implement import CredentialImplement


class CredentialDetector(RegexDetector):
    """Remove username/password combinations from dirty drity ``text``.
    """
    filth_cls = CredentialImplement
