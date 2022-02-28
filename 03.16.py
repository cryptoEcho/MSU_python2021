# функции (именованный фрагмент программного кода)
# лямбда функции, у которых нет имени
a = 15
def f(b):
    return b+a
def f1(a):
    a = 5
    return a
lst = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
def f2(b):
    lst[5] = 50
    return b+a
#print(f(10))
print(f1(a))
print(a)