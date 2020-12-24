import re

from cocoNLP.extractor import extractor

from .base import RegexDetector
from ..implement import CNAddressImplement
from ..utils import CanonicalStringSet


class CNAddressDetector(RegexDetector):
    """Use part of speech tagging to clean proper nouns out of the dirty dirty
    ``text``. Disallow particular nouns by adding them to the
    ``NameDetector.disallowed_nouns`` set.
    """
    filth_cls = CNAddressImplement

    disallowed_nouns = CanonicalStringSet(["skype"])

    def iter_filth(self, text):

        if not isinstance(self.disallowed_nouns, CanonicalStringSet):
            raise TypeError(
                'NameDetector.disallowed_nouns must be CanonicalStringSet'
            )

        ex = extractor()
        locations = ex.extract_locations(text)

        # string = '急寻特朗普，男孩，于2018年11月27号11时在陕西省安康市汉滨区走失。后来在深圳市南山区威新软件园发现'
        proper_nouns = []
        old_location = " "
        for location in locations:
            if -1 == old_location.find(location):
                index = text.find(location)
                proper_nouns.append((location,index,index+len(location)))
                old_location = location
        print(proper_nouns)

        # use a regex to replace the proper nouns by first escaping any
        # lingering punctuation in the regex
        # http://stackoverflow.com/a/4202559/564709
        """
        if proper_nouns:
            re_list = []
            for proper_noun in proper_nouns:
                re_list.append(r'\b' + re.escape(str(proper_noun)) + r'\b')
            self.filth_cls.regex = re.compile('|'.join(re_list))
        else:
            self.filth_cls.regex = None
        return super(CNAddressDetector, self).iter_filth(text)
        """
        for proper_noun in proper_nouns:
            print("mobile para:",proper_noun[1]," ",proper_noun[2]," ",proper_noun[0])
            yield CNAddressImplement(
                beg=proper_noun[1],
                end=proper_noun[2],
                text=proper_noun[0],
            )