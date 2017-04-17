def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not len(L):
        return float('NaN')

    array_of_length = [len(item) for item in L]
    mean = sum(array_of_length)/len(array_of_length)
    squared_sum = 0
    for string_len in array_of_length:
        squared_sum += (mean - string_len)**2
    return (squared_sum/len(array_of_length))**0.5

print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))