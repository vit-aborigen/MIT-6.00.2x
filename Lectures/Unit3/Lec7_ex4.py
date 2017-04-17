def stdDevOfLengths(L):
    if not len(L):
        return float('NaN')

    array_of_length = L[:]
    mean = sum(array_of_length)/len(array_of_length)
    squared_sum = 0
    for string_len in array_of_length:
        squared_sum += (mean - string_len)**2
    return ((squared_sum/len(array_of_length))**0.5, mean)

mean, dev = stdDevOfLengths([10, 4, 12, 15, 20, 5])
print(round(mean/dev, 3))