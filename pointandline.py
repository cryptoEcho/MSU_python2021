import math


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def module(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class line:
    def __init__(self, p1, p2):
        self.k = (p1.y - p2.y) / (p1.x - p2.x)
        self.b = p1.y - p1.x * (p1.y - p2.y) / (p1.x - p2.x)


print('bye')
