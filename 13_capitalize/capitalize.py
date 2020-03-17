def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    true_ele = []
    for element in lst:
        if element:
            true_ele.append(element)

    return true_ele


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))