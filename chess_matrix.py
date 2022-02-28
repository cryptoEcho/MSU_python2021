# 1 0 1 0 1 0
# 0 1 0 1 0 1
# 1 0 1 0 1 0
# 0 1 0 1 0 1
# 1 0 1 0 1 0

def mygenerator(size):
    for i in range(size + 1):
        for j in range(1, size + 1):
            if i % 2 == 0:
                yield i*j % 2
