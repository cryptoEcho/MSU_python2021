# Написать класс Stack, у которого есть поле buffer
# ◦	Присваивание этому полю произвольного значения — это операция «положить значение на вершину стека»
# ◦	Чтение значения этого поля — это операция «снять значение с вершины стека»,
# которая возвращает это значение если стек не пуст
# ◦	Если стек пуст, порождается исключение NotImplementedError (внимание: не IndexError)
# ◦	Удаление этого поля — также операция «снять значение с вершины стека»,
# которая ничего не возвращает, и не вызывает исключения на пустом стеке
# ◦	Класс должен поддерживать вывод содержимого стека в любом удобном формате с помощью print()
#
# >>> s=Stack()
#    2 >>> s.buf=100500
#    3 >>> s.buf=100500
#    4 >>> s.buf="ADASDFASD"
#    5 >>> print(s)
#    6 100500 100500 ADASDFASD
#    7 >>> del s.buf
#    8 >>> print(s)
#    9 100500 100500
#   10 100500
#   11 >>> s.buf
#   12 100500
#   13 >>> s.buf
#   14 Traceback (most recent call last):
#   15   File "<stdin>", line 1, in <module>
#   16   File "Stack.py", line 25, in …
#   17     …
#   18 NotImplementedError: Stack is empty
#   19 >>> del(s.buf)
#   20 >>> print(s)
#   21
#   22 >>>
class Stack:
    def __init__(self):
        self.lst = list()

    @property
    def buff(self):
        if len(self.lst) != 0:
            return self.lst.pop()
        else:
            raise NotImplementedError('Stack is empty')

    @buff.setter
    def buff(self, val):
        self.lst.append(val)

    @buff.deleter
    def buff(self):
        self.lst.pop()

    def __str__(self):
        return ' '.join([str(e) for e in list(reversed(self.lst))])

    def __del__(self):
        if len(self.lst) == 0:
            return
        else:
            self.lst.pop()


p = Stack()
p.buff = 2
p.buff = '23'
print(p)
print(p.buff)
print(p)
# del p.buff
# del p.buff

print('bye')
