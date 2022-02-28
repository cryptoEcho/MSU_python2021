# Написать генератор-функцию zigzag(), принимающую на вход последовательность подпоследовательностей
# (например, список строк или итератор по кортежам).
# o	Итератор, возвращаемый этой функцией, должен проходить элементы подпоследовательностей,
# находящихся на чётных местах, в прямом порядке, а на нечётных — в обратном
# o	Если одна из подпоследовательностей пуста, итератор завершает работу
# o	Если очередной элемент не является подпоследовательностью, должно вызываться исключение IndexError (а не Type Error)
# o	Пример:
# Переключить отображение номеров строк
#    1 >>> list(zigzag(["QE", "123", "ZXCVB"]))
#    2 ['Q', 'E', '3', '2', '1', 'Z', 'X', 'C', 'V', 'B']
#    3 >>> for z in zigzag(([1,2], "AB", [], [3,4,5,6])):
#    4 ...     print(z)
#    5 ...
#    6 1
#    7 2
#    8 B
#    9 A
#   10 >>> for z in zigzag([range(3), 1.1, "QWE"]):
#   11 ...     print(z)
#   12 ...
#   13 0
#   14 1
#   15 2
#   16 Traceback (most recent call last):
#   17   File "<stdin>", line 1, in <module>
#   18
#   19     …
#   20 IndexError: 1.1 must be iterable
# 2.
#
def zigzag(lst):
    for i in range(len(lst)):
        if lst[i] == '':
            break
        if type(lst[i]) != str:
            raise IndexError('list index out of range')
        if i % 2 == 0:
            for j in range(len(lst[i])):
                yield lst[i][j]
        else:
            for j in reversed(range(len(lst[i]))):
                yield lst[i][j]


a = zigzag(["QE", "123", 2, "ZXCVB"])
for x in a:
    print(x)
print(a)
print('bye')