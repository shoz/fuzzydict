from fuzzydict import FuzzyDict
import unittest

class FuzzyDictTests(unittest.TestCase):
    def setUp(self):
        pass
    def tests(self):
        sets = [((0.5, '0123456789'), ['0123456789',
                                       'X123456789',
                                       'XX23456789',
                                       'XXX3456789',
                                       'XXXX456789',
                                       'XXXXX56789',
                                        ]),
                ((1.0, '0123456789'), ['0123456789']),
                ((0.1, '0123456789'), ['0123456789',
                                       'X123456789',
                                       'XX23456789',
                                       'XXX3456789',
                                       'XXXX456789',
                                       'XXXXX56789',
                                       'XXXXXX6789',
                                       'XXXXXXX789',
                                       'XXXXXXXX89',
                                       'XXXXXXXXX9',
                                      ]),
                ]
        for params, answer in sets:
            threshold = params[0]
            query = params[1]
            fd = self._set_datasets(FuzzyDict(threshold))
            ret = fd[query]
            assert len(ret) == len(answer)
            for e in answer:
                assert e in ret
    def _set_datasets(self, d):
        d['0123456789'] = 1
        d['X123456789'] = 2
        d['XX23456789'] = 3
        d['XXX3456789'] = 4
        d['XXXX456789'] = 5
        d['XXXXX56789'] = 6
        d['XXXXXX6789'] = 7
        d['XXXXXXX789'] = 8
        d['XXXXXXXX89'] = 9
        d['XXXXXXXXX9'] = 10
        d['XXXXXXXXXX'] = 11
        return d
