def buildMenu(names, values, calories):
    '''''''''
    Takes 3 lists of food description
    all list must be the same length
    '''''''''
    menu = []
    for idx in range(len(values)):
        menu.append(Food(names[idx], values[idx], calories[idx]))
    return menu


def greedy(items, max_cost, keyFunction):
    '''''''''
    takes: items - list
           max_cost >= 0
           keyFunction - maps elements of items to numbers
    returns
    '''''''''
    result = []
    total_value, total_cost = 0.0, 0.0
    items_copy = sorted(items, key = keyFunction, reverse = True)

    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].getCost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].getCost()
            total_value += items_copy[i].getValue()

    return (result, total_value)

def testGreedy(items, constrains, keyFunction):
    taken, val = greedy(items, constrains, keyFunction)
    print("Total value of items taken is", val)
    for item in taken:
        print(' ', item)


def testGreedys(foods, maxUnits):
    '''''''''
    This function is defined to test greedy func
    '''''''''
    print("Use greedy by value to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getDensity)


class Food(object):
    '''''''''
    used for describing different kinds of food
    '''''''''
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def getDensity(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ": <" + str(self.getValue()) + ", " + str(self.getCost()) + ">"

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
food = buildMenu(names, values, calories)
testGreedys(food, 800)