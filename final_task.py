# Рудзянский Артемийо 27.04.2021
# Реализовать класс Tlist.
# 1. операторы  << и >> осуществляют циклический сдвиг массива влево и вправо соответсвенно.
# 2.конструктор класса принимая  на вход строку str и число p,  создаёт лист символов по следующему закону:
# первые p символов строки записываются в алфавитном порядке, затем следующие p в обратном алфавитном,
# потом следующие p  в алфавитном и т.д. длина входной строки может не быть кратной р,
# в таком случае оставшиеся символы записываются в порядке, как они были в исходной строке.
# пример tl=tlist('batyfghpoiuy',3)
# ['a',b,'t','y','g','h','h','o','p','y','u','i']
# tl>>
# ['i','a',b,'t','y','g','h','h','o','p','y','u']
# tl<<
# ['b','t','y','g','h','h','o','p','y','u','i','a']
# 3. добавить метод ispol()
# возвращает True, если полиндром и False, если нет.
class Tlist:
    def __init__(self, str1, p, b):  # b - вариант реализации сортировки (они почти одинаковые)
        if b:
            self.lst = list(str1)
            for i in range(0, len(self.lst) // p * p, p):
                if i / p % 2 == 0:
                    sorted_piece = sorted(self.lst[i:i + p])
                else:
                    sorted_piece = sorted(self.lst[i:i + p], reverse=True)
                for j in range(p):
                    self.lst.pop(i + j)
                    self.lst.insert(i + j, sorted_piece[j])
                    # self.lst[i+j] = sorted_piece[j]
        else:
            self.lst = list(str1)
            for i in range(0, len(self.lst) // p * p, p):
                for j in range(p - 1):
                    if i / p % 2 == 0:
                        if self.lst[i + j] > self.lst[i + j + 1]:
                            self.lst[i + j], self.lst[i + j + 1] = self.lst[i + j + 1], self.lst[i + j]
                    else:
                        if self.lst[i + j] < self.lst[i + j + 1]:
                            self.lst[i + j], self.lst[i + j + 1] = self.lst[i + j + 1], self.lst[i + j]

    def __lshift__(self, times):
        for k in range(times):
            for i in range(len(self.lst) - 1):
                self.lst[i], self.lst[i + 1] = self.lst[i + 1], self.lst[i]

    def __rshift__(self, times):
        for k in range(times):
            for i in range(len(self.lst) - 1, -1, -1):
                self.lst[i], self.lst[i - 1] = self.lst[i - 1], self.lst[i]

    def ispol(self):
        b = True
        for i in range(len(self.lst) // 2):
            if self.lst[i] != self.lst[len(self.lst) - 1 - i]:
                b = False
        if b:
            return True
        else:
            return False


st1 = Tlist('ehhelj', 3, 1)
st2 = Tlist('bcaghfba', 3, 1)
st3 = Tlist('abcba', 1, 1)
st4 = Tlist('ynmaaaamny', 2, 1)
st5 = Tlist('ynmaaaamny', 2, 0)
# st4.lst == st5.lst >>> True

print('bye')
