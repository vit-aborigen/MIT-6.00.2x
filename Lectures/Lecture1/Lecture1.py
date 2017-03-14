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
