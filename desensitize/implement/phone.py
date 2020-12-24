from .base import Implement

import hashlib


class PhoneImplement(Implement):
    type = 'phone'

    """
    @property
    def compliance(self):
        content = self.text.decode("utf-8")
        content_len = len(self.text)
        marked=content[0:3]+"*"*(content_len-7)+content[-4:]
        return marked
    """
    
    @property
    def compliance(self):
        content = self.text.encode("utf-8")
        md5 = hashlib.md5(content).hexdigest()
        return md5