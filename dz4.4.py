# Рудзянский Артемий
def revers(n):
    if n == 0:
        return 0
    grade = 1
    tmp = n
    while tmp > 9:
        tmp = tmp // 10
        grade += 1
    x = n % 10
    return x * 10**(grade-1) + revers(n // 10)


n = 54721
result = revers(n)
print(n, result)
