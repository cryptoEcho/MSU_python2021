from functools import reduce

def mult(x,y):
    return x*y

n = int(input())
lst = list()
for i in range(1, n+1):
    lst.append(i)
print(lst)
result = reduce(mult, lst)