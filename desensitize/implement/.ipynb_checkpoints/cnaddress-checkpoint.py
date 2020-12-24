from .base import Implement

from cocoNLP.extractor import extractor

class CNAddressImplement(Implement):
    type = 'cnaddress'

    @property
    def compliance(self):
        content=self.text.decode("utf-8")

        ex = extractor()
        locations = ex.extract_locations(content)
        len_locations= len(locations)

        if len_locations > 1:
            mark_len=len(locations[-1])
            marked=locations[0][0:-mark_len]+"*"*mark_len
        else:
            marked=locations[0]
        return marked