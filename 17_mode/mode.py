def frequency_counter(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num]+= 1
    
    return freq


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    freq = frequency_counter(nums)
    return freq[max(freq.values())]

print(mode([1, 2, 1]))




