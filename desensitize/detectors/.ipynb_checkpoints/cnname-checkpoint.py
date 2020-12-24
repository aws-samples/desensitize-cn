import re

import jieba.posseg

from .base import RegexDetector
from ..implement import CNNameImplement
from ..utils import CanonicalStringSet


class CNNameDetector(RegexDetector):
    """Use part of speech tagging to clean proper nouns out of the dirty dirty
    ``text``. Disallow particular nouns by adding them to the
    ``NameDetector.disallowed_nouns`` set.
    """
    filth_cls = CNNameImplement

    disallowed_nouns = CanonicalStringSet(["skype"])

    def iter_filth(self, text):

        if not isinstance(self.disallowed_nouns, CanonicalStringSet):
            raise TypeError(
                'NameDetector.disallowed_nouns must be CanonicalStringSet'
            )

        # string = "李伟知道伟大的中华人民共和国的创始人是毛泽东，朱德等人"
        proper_nouns = []
        seg = jieba.posseg.cut(text)

        l = []
        index=0
        for i in seg:
            l.append((i.word, i.flag, index, index+len(i.word)))
            index+=len(i.word)
        for element in l:
            if element[1] == "nr":
                proper_nouns.append((element[0],element[2],element[3]))
                print(element[0], element[1], element[2], element[3])

        """# use a regex to replace the proper nouns by first escaping any
        # lingering punctuation in the regex
        # http://stackoverflow.com/a/4202559/564709
        if proper_nouns:
            re_list = []
            for proper_noun in proper_nouns:
                re_list.append(r'\b' + re.escape(str(proper_noun)) + r'\b')
            self.filth_cls.regex = re.compile('|'.join(re_list))
        else:
            self.filth_cls.regex = None
        return super(CNNameDetector, self).iter_filth(text)
        """
        for proper_noun in proper_nouns:
            print("chinese name para:",proper_noun[1]," ",proper_noun[2]," ",proper_noun[0])
            yield CNNameImplement(
                beg=proper_noun[1],
                end=proper_noun[2],
                text=proper_noun[0]
            )