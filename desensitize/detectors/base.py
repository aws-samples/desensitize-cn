import re

from .. import exceptions
from ..implement import Implement, RegexImplement


class Detector(object):
    filth_cls = None

    def iter_filth(self, text):
        raise NotImplementedError('must be overridden by base classes')


class RegexDetector(Detector):

    def iter_filth(self, text):
        if not issubclass(self.filth_cls, RegexImplement):
            raise exceptions.UnexpectedImplement(
                'RegexImplement required for RegexDetector'
            )
        if self.filth_cls.regex is None:
            raise StopIteration
        for match in self.filth_cls.regex.finditer(text):
            yield self.filth_cls(match)
