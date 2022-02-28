# Рудзянский Артемий
def revers(n):
    if n == 0:
        return 0
    x = n % 10
    return x * 10**(len(str(n))-1) + revers(n // 10)


n = 54721
result = revers(n)
print(n, result)
