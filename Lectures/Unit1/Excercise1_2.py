import itertools

def powerSet(items, itemsUnique = False):
    #if itemsUnique is True, than all elements will be unique, otherwise
    #   only elements order is important
    if itemsUnique:
        func = itertools.combinations
    else:
        func = itertools.permutations

    for i in range(0, len(items) + 1):
        for subset in func(items, i):
            yield subset
