class rectangle:
    default_color = 'green'
    def __init__(self,w,h):
        self._w = w
        self.h = h
        self.__w = w**2
        self.__h = h**2
    def get_w(self):
        return self.w
    def set_w(self,new_w):
        self._w = new_w
    @staticmethod
    def name():
        print('static_method')
    def set_color(str):
        default_color = str
    @classmethod
    def class_m(self):
        # return self.w * self.h
        print('self')
    def sqw(self):
        return self.h * self._w
    @property
    def width_scr(self):
        return self.__w
    # @width_scr.setter
    def width_sqr(self, www):
        if www > 0:
            self.__w = www
        else:
            print('false')

class sqr(rectangle):
    dash = 'yes'
    def __init__(self, w):
        self.h = w
        self.set_w(w)
    def perimetr(self):
        return self.h * 4
#rectangle.default_color


r = rectangle(1,2)
print('bye')