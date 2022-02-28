# Написать класс Recurse, которому при создании передаётся функция f
# ◦	Экземпляр класса должен поддерживать операцию индексирования по следующим правилам:
# 1	recurse[x] возвращает бесконечную последовательность f(x), f(f(x)), … , f(…f(f(x))…), …
# 2	recurse[x:n] возвращает бесконечную последовательность f(f(…n_раз…f(x))), f(f(…n+1_раз…f(x))), …,,
# т. е. исходную последовательность, начиная с n-го элемента
# 3	recurse[x:n:k] возвращает конечную последовательность f(f(…n_раз…f(x))),  f(f(…n+1_раз…f(x))),
# … f(f(…k-1_раз…f(x))), т. е. исходную последовательность, начиная с n-го элемента и заканчивая перед k-м
# пример
# from math import sin
#    9 >>> g = Recurse(sin)
#   10 >>> next(g[7:100500])
#   11 0.005463237580162976
#   12 >>> next(g[7:1005000])
#   13 0.001727724719169488
class Recurse:
    __result1__ = None
    __result2__ = None
    __result3__ = None
    count = None

    def __init__(self, f):
        self.f = f

    def func(self, x):
        return eval(self.f)

    def __getitem__(self, x):
        if isinstance(x, slice):
            # x.start(аргумент) x.stop(наш старт) x.step(наш стоп)
            if x.step is None: # recurse[x:n]
                if self.__result2__ is None:
                    for i in range(x.stop):
                        if self.__result2__ is None:
                            tmp = self.func(x.start)
                        else:
                            tmp = self.func(self.__result2__)
                        self.__result2__ = tmp
                    yield tmp
                tmp = self.func(self.__result2__)
                self.__result2__ = tmp
                yield tmp
            else: # recurse[x:n:k]
                if self.__result2__ is None:
                    self.count = x.stop
                    for i in range(x.stop):
                        if self.__result2__ is None:
                            tmp = self.func(x.start)
                        else:
                            tmp = self.func(self.__result2__)
                        self.__result2__ = tmp
                    yield tmp
                self.count += 1
                if self.count == x.step:
                    raise StopIteration
                tmp = self.func(self.__result2__)
                self.__result2__ = tmp
                yield tmp
        else: # recurse[x]
            if self.__result1__ is None:
                tmp = self.func(x)
            else:
                tmp = self.func(self.__result1__)
            self.__result1__ = tmp
            yield tmp

# isinstance(key, slice):


rec = Recurse('x**2')
# next(rec[2])


next(rec[2:2]) # 4 16
next(rec[2:2:4])
print('bye')
 # next(rec[2:2])
# Out[1]: 16
# next(rec[2:2])
# Out[2]: 256
# next(rec[2:2])
# Out[3]: 65536
# next(rec[2:2])
# Out[4]: 4294967296