from Lecture1 import *

def maxVal(toConsider, avail):
    '''''''''
    toConsider - list of items that haven't taken into consideration
    avail - amount of space still(!) available

    returns tuple of items and weight
    '''''''''
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def maxValwithMemo(toConsider, avail, memo = {}):
    '''''''''
    same method, but using memorization instead

    toConsider - list of items that haven't taken into consideration
    avail - amount of space still(!) available

    returns tuple of items and weight
    '''''''''
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = maxValwithMemo(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxValwithMemo(toConsider[1:], avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxValwithMemo(toConsider[1:], avail, memo)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    memo[(len(toConsider), avail)] = result
    return result


def testMaxValOne(food, maxUnits, printItems = True):
    print("\nUse search/decision tree to allocate", maxUnits, "calories")
    val, taken = maxVal(food, maxUnits)
    print("Total value of items taken is", val)
    if printItems:
        for item in taken:
            print(' ', item)

def testMaxValTwo(food, maxUnits, printItems = True):
    print("\nUse search/decision tree to allocate", maxUnits, "calories")
    val, taken = maxValwithMemo(food, maxUnits, {})
    print("Total value of items taken is", val)
    if printItems:
        for item in taken:
            print(' ', item)

testMaxValOne(food, 750)
testMaxValTwo(food, 750)