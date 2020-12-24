import operator
import sys

from . import exceptions
from . import detectors
from .implement import Implement


class Desensitize(object):

    def __init__(self, *args, **kwargs):
        super(Desensitize, self).__init__(*args, **kwargs)

        # instantiate all of the detectors which, by default, uses all of the
        # detectors that are in the detectors.types dictionary
        self._detectors = {}
        for detector_cls in detectors.iter_detector_clss():
            print(detector_cls.filth_cls.type)
            self.add_detector(detector_cls)

    def add_detector(self, detector_cls):
        """Add a ``Detector`` to desensitize"""
        name = detector_cls.filth_cls.type
        if name in self._detectors:
            raise KeyError((
                'can not add Detector "%(name)s"---it already exists. '
                'Try removing it first.'
            ) % locals())
        self._detectors[name] = detector_cls()

    def remove_detector(self, name):
        """Remove a ``Detector`` from desensitize"""
        self._detectors.pop(name)

    def clean(self, text, **kwargs):
        if sys.version_info < (3, 0):
            # Only in Python 2. In 3 every string is a Python 2 unicode
            if not isinstance(text, unicode):
                raise exceptions.UnicodeRequired

        clean_chunks = []
        filth = Implement()
        for next_filth in self.iter_filth(text):
            clean_chunks.append(text[filth.end:next_filth.beg])
            clean_chunks.append(next_filth.replace_with(**kwargs))
            filth = next_filth
        clean_chunks.append(text[filth.end:])
        print(clean_chunks)
        return u''.join(clean_chunks)

    def iter_filth(self, text):
        """Iterate over the different types of implement that can exist.
        """
        all_filths = []
        for detector in self._detectors.values():
            for filth in detector.iter_filth(text):
                if not isinstance(filth, Implement):
                    raise TypeError('iter_filth must always yield Implement')
                all_filths.append(filth)

        # Sort by start position. If two filths start in the same place then
        # return the longer one first
        all_filths.sort(key=lambda f: (f.beg, -f.end))

        # this is where the Desensitize does its hard work and merges any
        # overlapping filths.
        if not all_filths:
            raise StopIteration
        filth = all_filths[0]
        for next_filth in all_filths[1:]:
            if filth.end < next_filth.beg:
                yield filth
                filth = next_filth
            else:
                filth = filth.merge(next_filth)
        yield filth
