# Рудзянский Артемий
def eat(lst):
    x = int(input())
    if x == 0:
        return lst
    elif x % 2 == 1:
        lst.append(x)
    return eat(lst)


lst = list()
result = eat(list())
print(*result)
print('bye')