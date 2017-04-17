def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    sum_of_multiplies = 0
    for value in L:
        div, mod = divmod(s, value)
        sum_of_multiplies += div
        s = mod
    return sum_of_multiplies if s == 0 else "no solution"

print(greedySum([4,2],8))
print(greedySum([4,2],9))
print(greedySum([4,2,1],9))


