from functools import reduce


def SrZnach(str1, length):
    # if len(str1) == 0:
    #     return 0
    if str1[0] == '0':
        return 0
    lst = list(str1)
    x = int(lst[0])
    lst.pop(0)
    return x / length + (SrZnach(lst, length))

def sum(x, y):
    return x + y

# x = input('Введите строку чисел ')
# x = '25 2 0'
# x1 = x.split()
x1 =[5, 5, 0]
result = reduce(sum, x1, 0)

print(result)
# result = SrZnach(x1, len(x1)-1)
# print(result)


# print(result)
# result = list(filter(lambda q: int(q) / len(x1) > 1, x1))