**fuzzydict, an ambiguous dictionary**

.. sourcecode:: python

    >>> from fuzzydict import FuzzyDict
    >>> fdict = FuzzyDict(0.5) # setting a threshold range from 0.0 to 1.0
    >>> # < Assign some values to the 'fdict'>
    >>> fdict
    >>> {'0123456789': 0, 'X123456789': 1, 'XX23456789': 2, 'XXX3456789': 3, 'XXXX456789': 4, 'XXXXX56789': 5, 'XXXXXX6789': 6, 'XXXXXXX789': 7, 'XXXXXXXX89':8, 'XXXXXXXXX9':9, 'XXXXXXXXXX': 10}
    >>> [key for key in fdict.fuzzy_keys('0123456789')]
    ['0123456789', 'X123456789', 'XX23456789', 'XXX3456789', 'XXXX456789', 'XXXXX56789']
    >>> [value for value in fdict.fuzzy_values('0123456789')]
    [0, 1, 2, 3, 4, 5]
    >>> fdict.fuzzy_add('0123456789', 1) # bulk add
    >>> [(k, v) for (k, v) in fdict.fuzzy_items('0123456789')]
    [('0123456789', 1), ('X123456789', 2), ('XX23456789', 3), ('XXX3456789', 4), ('XXXX456789', 5), ('XXXXX56789', 6)] 
    >>> fdict['0123456789'] # You can also access a FuzzyDict as a normal dict
    1

