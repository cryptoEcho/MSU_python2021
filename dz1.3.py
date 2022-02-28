# Нахождение корня натурального числа. Рудзянский Артемий
# def my_sqrt(number, acc):

n = int(input('Введите число, корень которого требуется найти '))
e = float(input('И точность, с которой необходимо вычислить корень '))
# нахождение корня с помощью формулы Ньютона x(i+1) = {x(i)+[n/x(i)]}/2
xn = 1 # начальное значение
while abs(xn*xn - n) > e:
    xn = (xn + n / xn) / 2
print(float('{:3f}'.format(xn)))






# i = 2
# x = 1
# for i in range(1, n):
#     if n-i*i < 2:
#         x = i
#         break
# print(i)
# step = 0.1
# while step != e:
#     i = i + step
#     # if n - i*i < step:
#     #     step *= 0.1
# print(i)