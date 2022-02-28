# Рудзянский Артемий


def dz41():
    lst = list()
    x = int(input())
    while x != 0:
        lst.append(x)
        x = int(input())
    filtered_lst = list(filter((lambda x: x % 2 == 1), lst))
    print(*filtered_lst)

def summ(x):
    return x + summ()
def dz42():
    sum = 0
    summ = lambda x: sum *= x

    #filter((lambda x: x % 2 == 1), lst)
# dz41()
print('bye')
