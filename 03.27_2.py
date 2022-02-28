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


def distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def distance2(p1, p2):
    p3 = point(p2.x - p1.x, p2.y - p1.y)
    return p3.module()

class polygon:
    color ='green'

    @property
    def num_vertices(self):
        return self.num_vertices

    @num_vertices.setter
    def number_of_vertices(self, n):
        self.number_of_vertices = n

    @num_vertices.getter
    def number_vertices(self):
        return self._number_vertices

    def __init__(self, points):
        self.point = points
        self._number_vertices = len(points)



class Triangle(polygon):

    def __init__(self, points, color):
        super().__init__(points)
        self.color = color

    def perimeter(self):
        per = distance(self.points[0], self.points[1]) + distance(self.points[1], self.points[2]) + distance(self.points[2], self.points[0])
        #for i in range(self._number_vertices): можно попробовать реализовать через цикл
        return per

    def sqr_tr(self):
        a = distance(self.points[0], self.points[1])
        b = distance(self.points[1], self.points[2])
        c = distance(self.points[2], self.points[0])
        p = self.perimeter(self)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-b))


def sort(point_list):
    for i in range(len(point_list)):
        for j in range(i, len(point_list)):
            if point_list[i].x > point_list[j].x:
                point_list[i], point_list[j] = point_list[j], point_list[i]

def sort2(point_list):
    my_dict = {}
    for item in point_list:
        my_dict.update({item.x: item.y})
    sorted_list = sorted(my_dict.items(), key = lambda x: x[0])
    print(*sorted_list)

def igrik(point_list, x):
    sort(point_list)
    n = len(point_list) - 1
    if x > point_list[n].x:
        ln1 = line(point_list[n-1], point_list[n])
    elif x < point_list[0].x:
        ln1 = line(point_list[0], point_list[1])
    else:
        i = 0
        while x > point_list[i].x:
            i += 1
        ln1 = line(point_list[i-1], point_list[i])
    return ln1.k*x + ln1.b
my_point_list = list([point(0,0), point(2,1), point(4,0)])
print('bye')
my_tr = Triangle(my_point_list, 'blue')


