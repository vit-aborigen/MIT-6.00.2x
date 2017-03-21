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

def testMaxVal(food, maxUnits, printItems = True):
    print("\nUse search/decision tree to allocate", maxUnits, "calories")
    val, taken = maxVal(food, maxUnits)
    print("Total value of items taken is", val)
    if printItems:
        for item in taken:
            print(' ', item)

testMaxVal(food, 750)
