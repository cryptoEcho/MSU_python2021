# в файле два числа (каждое на своей строке) и пробелы. Найти их сумму.
input = open('input.txt', 'r')
rd = input.read()
splt = rd.split()
sum = 0
for i in range(len(splt)):
    sum += int(splt[i])
print(sum)

print('\n\nbye')