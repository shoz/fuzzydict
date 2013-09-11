from fuzzydict import FuzzyDict
import unittest

class FuzzyDictTests(unittest.TestCase):
    def setUp(self):
        pass
    def _set_datasets(self, d):
        d.setdefault('0123456789', 1)
        d.setdefault('X123456789', 2)
        d.setdefault('XX23456789', 3)
        d.setdefault('XXX3456789', 4)
        d.setdefault('XXXX456789', 5)
        d.setdefault('XXXXX56789', 6)
        d.setdefault('XXXXXX6789', 7)
        d.setdefault('XXXXXXX789', 8)
        d.setdefault('XXXXXXXX89', 9)
        d.setdefault('XXXXXXXXX9', 10)
        d.setdefault('XXXXXXXXXX', 11)
        return d
    def test_getitem(self):
        test_sets = [((0.5, '0123456789'), [('0123456789', 1),
                                            ('X123456789', 2),
                                            ('XX23456789', 3),
                                            ('XXX3456789', 4),
                                            ('XXXX456789', 5),
                                            ('XXXXX56789', 6)
                                            ]),
                     ((1.0, '0123456789'), [('0123456789', 1)]),
                     ((0.1, '0123456789'), [('0123456789', 1),
                                            ('X123456789', 2),
                                            ('XX23456789', 3),
                                            ('XXX3456789', 4),
                                            ('XXXX456789', 5),
                                            ('XXXXX56789', 6),
                                            ('XXXXXX6789', 7),
                                            ('XXXXXXX789', 8),
                                            ('XXXXXXXX89', 9),
                                            ('XXXXXXXXX9', 10)
                                            ]),
                     ]
        for params, answer in test_sets:
            threshold = params[0]
            query = params[1]
            fd = self._set_datasets(FuzzyDict(threshold))
            keys, values = fd.fuzzy_items(query)
            assert len(keys) == len(answer)
            assert len(values) == len(answer)
            for k, v in answer:
                assert k in keys
                assert v in values
    def test_setitem(self):
        test_sets = [((0.5, '0123456789'), [('0123456789', 5),
                                            ('X123456789', 5),
                                            ('XX23456789', 5),
                                            ('XXX3456789', 5),
                                            ('XXXX456789', 5),
                                            ('XXXXX56789', 5)
                                            ])]
        for params, answer in test_sets:
            threshold = params[0]
            query = params[1]
            fd = self._set_datasets(FuzzyDict(threshold))
            fd.fuzzy_assign(query, 5)
            for k, v in answer:
                assert fd[k] == v
