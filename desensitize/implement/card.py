from .base import RegexImplement
import hashlib


class CardImplement(RegexImplement):
    type = 'card'

    @property
    def compliance(self):
        content=self.text.encode("utf-8").decode("utf-8")
        content_len=len(content)
        marked="*"*(content_len-4)+content[-4:]
        return marked

    @property
    def hash(self):
        content=self.text.encode("utf-8").decode("utf-8")
        content_len=len(content)
        marked="*"*(content_len-4)+content[-4:]
        return marked