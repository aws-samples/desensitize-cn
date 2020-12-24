from .base import Implement


class CNNameImplement(Implement):
    type = 'cnname'

    @property
    def compliance(self):
        content = self.text.decode("utf-8")
        content_len = len(self.text)
        marked = content[0:1]+"*"*(content_len-1)
        return marked