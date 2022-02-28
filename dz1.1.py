# НОД двух целых чисел. Рудзянский Артемий

x = int(input('Введите 1е целое число: '))
y = int(input('Введите 2е целое число: '))
for i in range(1, x):
    if x % i == 0 and y % i == 0:
        NOD = i
print('Наибольший общий делитель ', x, ' и ', y, ': ', NOD)

# алгоритм Евклида
if x > y:
    while x != 0:
        o = x % y
        x = y % o
else:
    while y != 0:
        o = y % x
        y = x % o
print('\nНОД с помощью алгоритма Евклида ', o)