# Рудзянский Артемий
import functools
def dz41():
    lst = list()
    x = int(input())
    while x != 0:
        lst.append(x)
        x = int(input())
    filtered_lst = list(filter((lambda x: x % 2 == 1), lst))
    print(*filtered_lst)

def dz42():
    lst = list()
    x = int(input())
    while x != 0:
        lst.append(x)
        x = int(input())
    summ = functools.reduce(lambda sum, x: sum + x, lst)
    print(summ/len(lst))
   # summ()
    #filter((lambda x: x % 2 == 1), lst)
dz41()
dz42()
print('bye')
