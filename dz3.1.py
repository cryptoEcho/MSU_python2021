# Рудзянский Артемий
import math
str1 = input('Введите строку\n')
str1 = str1.replace(' ', '')
b = True
i = 0
for i in range(0, len(str1)//2-1):
    if str1[i] != str1[len(str1)-1-i]:
        b = False
if b:
    print("Введенная строка является палиндромом")
    if len(str1) % 2 == 0:
        str1 = ''
    else:
        str1 = str1[math.ceil(len(str1)//2)]
    # i = 0
    # while i < len(str1):
    #     if str1.count(str1[i]) > 1:
    #         str1 = str1.replace(str1[i], '')
    #         i -= 1
    #     i += 1
    print(str1)
else:
    print("Введенная строка не является палиндромом")
    lst = list(str1)
    lst.reverse()
    print(''.join(lst))


