# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5

def my_genrows(size):
    for i in range(size):
        yield i

def gen_matrix(rows, cols):
    w = next(kj)
    while w < rows:
        for j in range(cols):
            yield j
        w = next(kj)



cols = 6
rows = 5
# my_genrows(rows)
kj = my_genrows(rows)
a = gen_matrix(rows, cols)
for i in range(rows):
    for j in range(cols):
        print(next(a), end = '\t')
    print('\n')

print('bye')


