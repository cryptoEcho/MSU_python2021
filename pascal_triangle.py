n = 4
m = 7

outer = list()

def array_gen(n, m):
    for i in range(n):
        inner = list()
        for j in range(m):
            if j == 0 or i == 0:
                inner.append(1)
            else:
                inner.append(outer[i-1][j] + inner[j-1])
        outer.append(inner)

array_gen(n, m)

for i in range(n):
    for j in range(m):
        print(outer[i][j], end = '\t')
    print('\n')

print('bye')