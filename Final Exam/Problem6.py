import itertools
import numpy as np

def find_combination(choices, total):
    bins = np.array(list(itertools.product([0, 1], repeat=len(choices))))
    combinations = [b for b in bins if sum(choices * b) == total]
    return (min(combinations, key=sum) if combinations else
            max([b for b in bins if sum(choices * b) < total], key=sum))

print(find_combination([1,2,2,3], 4)