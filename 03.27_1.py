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


def distance(p1,p2):
    return math.sqrt((p2.x-p1.x)**2 +(p2.y-p1.y)**2)

def distance2(p1,p2):
    p3=point((p2.x-p1.x),(p2.y-p1.y))
    return p3.module()

class Figure:
    color ='green'

    @property
    def number_vertices(self):
        return self._number_vertices

    @number_vertices.setter
    def number_vertices(self,n):
        self._number_vertices=n

    @number_vertices.getter
    def number_vertices(self):
        return self._number_vertices

    def __init__(self, points):
        self.points = points
        self._number_vertices=len(points)

class Triangle(Figure):

    def __init__(self, points,color):
       super().__init__(points)
       self.color=color


    def perimeter(self):
        per=distance(self.points[0],self.points[1]) +  distance(self.points[1],self.points[2]) + distance(self.points[2],self.points[0])
        return per

    def sqr_tr(self):
        a=distance(self.points[0], self.points[1])
        b=distance(self.points[1], self.points[2])
        c=distance(self.points[2],self.points[0])
        p=self.perimeter()/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))


my_point_list=[point(0,0),point(1,1),point(2,0)]

my_tr=Triangle(my_point_list,'blue')
print('fdf')
