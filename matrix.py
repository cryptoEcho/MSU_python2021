# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8 10
# 0  3  6  9 12 15
# 0  4  8 12 16 20
# 0  5  10 15 20 25

def mygenerator1(size):
    for i in range(size):
        yield i


def mygenerator2(start, size):
    i = next(iter1)
    for i in range(size):
        for j in range(size):
            yield i*j
    # while i < size:
    #     for j in range(size):
    #         yield j+i
    #         i = next(iter1)


iter1 = mygenerator1(6)
a = mygenerator2(0, 6)
for i in range(6):
    for j in range(6):
        print(next(a), end= '\t')
    print('\n')
# def mygenerator2(start, size):
#     iter1 = mygenerator1(size)
#     strn = iter1.__next__()
#     for i in range(size):
#         for j in range(size):
#             yield strn
#     strn = iter1.__next__()

# def mygenerator(start, size):
#     step = 1
#     plus = 0
#     while step % size != 0:

print('bye')