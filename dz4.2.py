def SrZnach(str1, length):
    if len(str1) == 0:
        return
    lst = list(str1)
    x = int(lst[0])
    lst.pop(0)
    return x/length + SrZnach(''.join(lst), length)/length

# x = input('Введите строку чисел ')
x = '1234567890'
SrZnach(x, len(x))
#
# print(result)
