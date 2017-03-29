import itertools

def bruteCowSearch(cow_list):
    for i in range(len(cow_list), -1, -1):
        result = []
        for subset in itertools.combinations(cow_list, i):
            diff = set(cow_list) - set(subset)
            result.append(list(subset))
            result.append(list(diff))
        print(result)
    return result

bruteCowSearch([1,2,3,4,5,6])