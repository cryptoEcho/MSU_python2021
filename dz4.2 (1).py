# Рудзянский Артемий
def eat(count, summ):
    x = int(input())
    if x == 0:
        if count:
            return summ / count
        else:
            return 'последовательность отсутсвует'
    count += 1
    summ += x
    return eat(count, summ)


count = 0
summ = 0
mean = eat(count, summ)
print(mean)
print('bye')

