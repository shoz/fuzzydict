### Fuzzy Dict

Example:

    >>> fdict = FuzzyDict(0.5)
    >>> [key for key in fdict.fuzzy_keys('0123456789')]
    ['0123456789', 'X123456789', 'XX23456789', 'XXX3456789', 'XXXX456789', 'XXXXX56789']
    >>> [value for value in fdict.fuzzy_values('0123456789')]
    [1, 2, 3, 4, 5, 6]
    >>> fdict.fuzzy_add('0123456789', 1) # bulk add
    >>> [key for key in fdict.fuzzy_keys('0123456789')]
    [2, 3, 4, 5, 6, 7]
    >>> fdict['0123456789'] # You can also access a FuzzyDict as a normal dict
    2
