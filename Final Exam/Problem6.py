import itertools
import numpy as np

def find_combination(choices, total):
    # print(list(itertools.product([0,1],repeat = 4)))
    all_combinations = np.array(list(itertools.product([0, 1], repeat=len(choices))))
    acceptable_combinations = [answer for answer in all_combinations if sum(choices * answer) == total]

    if acceptable_combinations:
        return min(acceptable_combinations, key=sum)
    else:
        acceptable_combinations = [answer for answer in all_combinations if sum(choices * answer) < total]
        return max(acceptable_combinations, key=sum)

print(find_combination([1,2,2,3], 4))