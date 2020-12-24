import re

from .base import RegexImplement


class CNIDImplement(RegexImplement):
    type = 'cnid'

    # Chinese ID have two type: 15 digital or 18 digital
    regex = re.compile((
        "([1-9]\d{5}"                              # region
        "(18|19|([23]\d))"                          # first two digital of years, 19
        "\d{2}"                                     # last two digital of years, 89
        "((0[1-9])|(10|11|12))"                     # month
        "(([0-2][1-9])|10|20|30|31)"                # day
        "\d{3}"                                     # first three of personal code 
        "[0-9Xx])"                                 # last one personal code
        "|"                                         ##### 18 codes above & 15 code below ####
        "([1-9]\d{5}"                              # region
        "\d{2}"                                     # last two digital of years
        "((0[1-9])|(10|11|12))"                     # month
        "(([0-2][1-9])|10|20|30|31)"                # day
        "\d{2}"                                     # first two of three-digitals presonal code
        "[0-9Xx])"                                 # last one three-digitals presonal code
    ), re.VERBOSE)

    @property
    def compliance(self):
        #content=self.text.encode("utf-8").decode("utf-8")
        content=self.text
        content_len=len(content)
        marked=content[0:3]+"*"*(content_len-7)+content[-4:]
        return marked