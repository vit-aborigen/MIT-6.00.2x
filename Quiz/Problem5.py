def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    length = len(L)
    sumList = []
    for i in range(length):
        for j in range(i, length):
            sumList.append(sum(L[i:j + 1]))

    return max(sumList)

print(max_contig_sum([3, -3, 4, -1, 5, -4, 9, -8, 8, 1, -2]))