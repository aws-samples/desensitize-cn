import re

from stdnum import luhn

from .base import RegexDetector
from ..implement import CardImplement
from ..utils import CanonicalStringSet


class CardDetector(RegexDetector):
    """Use part of speech tagging to clean proper nouns out of the dirty dirty
    ``text``. Disallow particular nouns by adding them to the
    ``NameDetector.disallowed_nouns`` set.
    """
    filth_cls = CardImplement

    disallowed_nouns = CanonicalStringSet(["skype"])

    def iter_filth(self, text):

        if not isinstance(self.disallowed_nouns, CanonicalStringSet):
            raise TypeError(
                'NameDetector.disallowed_nouns must be CanonicalStringSet'
            )

        proper_nouns = set()
        regex = re.compile(r'\d{16}|\d{19}')  #card number would be 16 or 19 bytes
        cards_obj = regex.finditer(text)
        for card in cards_obj:
            if luhn.is_valid(card):
                proper_nouns.add(card.group())
            else:
                print("can't match luhn")

        # use a regex to replace the proper nouns by first escaping any
        # lingering punctuation in the regex
        # http://stackoverflow.com/a/4202559/564709
        if proper_nouns:
            re_list = []
            for proper_noun in proper_nouns:
                re_list.append(r'\b' + re.escape(str(proper_noun)) + r'\b')
            self.filth_cls.regex = re.compile('|'.join(re_list))
        else:
            self.filth_cls.regex = None
        return super(CardDetector, self).iter_filth(text)
