def buildMenu(names, values, calories):
    '''''''''
    Takes 3 lists of food description
    all list must be the same length
    '''''''''
    menu = []
    for idx in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
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


class Food(object):
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
