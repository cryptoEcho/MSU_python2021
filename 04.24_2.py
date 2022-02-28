# Написать класс Vect, унаследованный от list, со следующими изменениями:
# ◦	При создании экземпляра должно проверяться, что
# 1	Все элементы последовательности одного типа
# 2	Этот тип поддерживает сложение и умножение на число
# ◦	В противном случае возникает исключение Type Error
# ◦	Класс поддерживает поэлементное умножение на число: vect @ 5
# ◦	Класс поддерживает поэлементное сложение (вместо конкатенации): vect1 + vect2
# ◦	Класс поддерживает запись в файл vect.write("файл") и чтение из файла vect.read("файл") (имя файла любое)
# ◦	Пример:
#
#    1 >>> v, w = Vect(range(9)), Vect(range(10,16))
#    2 >>> v, w
#    3 ([0, 1, 2, 3, 4, 5, 6, 7, 8], [10, 11, 12, 13, 14, 15])
#    4 >>> v+w
#    5 [10, 12, 14, 16, 18, 20]
#    6 >>> v@3
#    7 [0, 3, 6, 9, 12, 15, 18, 21, 24]
#    8 >>> s = Vect("QWER")
#    9 >>> s
#   10 ['Q', 'W', 'E', 'R']
#   11 >>> s+"ASDFG"
#   12 ['QA', 'WS', 'ED', 'RF']
#   13 >>> s@4
#   14 ['QQQQ', 'WWWW', 'EEEE', 'RRRR']
#   15 >>> l = Vect(i*2+1 for i in range(6))
#   16 >>> l
#   17 [1, 3, 5, 7, 9, 11]
#   18 >>> e = Vect((1,2,3,4.4,5,6))

class Vect(list):
    def __add__(self, other):
        sum = Vect()
        size = min(len(self), len(other))
        for i in range(size):
            sum.append(other[i] + self[i])
        return sum

    def __mul__(self, other):
        for i in range(len(self)):
            self[i] *= other
        return self

    def write(self, path):
        output = open(path, 'w')
        output.write(str(self))

    def read(self, path):
        input = open(path, 'r')
        str = input.read()
        lst = list(eval(str))
        self.clear()
        for i in range(len(lst)):
            self.append(lst[i])
v = Vect(range(9))
# v.write('output1.txt')
v.read('output1.txt')
print('bye')





