# выражение for j in итерируемый объект if условие
# [i*j for i in range(5) for j in range(3)]
def list_gen():
    a = list()
    for i in range(5):
        for j in range(3):
            for k in range(2):
                a.append(i * j)


[[i * j for j in range(m)] for i in range(n)]
# 1 0 1 0 1 0
# 0 1 0 1 0 1
# 1 0 1 0 1 0
# 0 1 0 1 0 1
# 1 0 1 0 1 0
m = 8
n = 8
[[(((i % 2) + (j % 2)) + 1) % 2 for j in range(m)] for i in range(n)]


# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8 10
# 0  3  6  9 12 15
# 0  4  8 12 16 20
# 0  5  10 15 20 25
[[i * j for j in range(6)] for i in range(6)]


# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
[[j for j in range(6)] for i in range(6)]


# 1	 1	1	1	1	1	1

# 1	 2	3	4	5	6	7
#
# 1	 3	6	10	15	21	28
#
# 1	 4	10	20	35	56	84
# не решено


[i if i < 3 else -i for i in range(6)]  # *-простой пример с условным оператором


# 0 1 1 1 1 1
# 2 0 1 1 1 1
# 2 2 0 1 1 1
# 2 2 2 0 1 1
# 2 2 2 2 0 1
# 2 2 2 2 2 0
[[1 if j < i else (2 if j > i else (0 if i == j else 0)) for i in range(6)] for j in range(6)]
[[1 if j < i else (2 if j > i else 0) for i in range(6)] for j in range(6)]


# 0  1  2  3  4  5
# 11 10  9  8  7  6
# 12 13 14 15 16 17
# 23 22 21 20 19 18
# 24 25 26 27 28 29
m = 6
n = 5
[[i + j * m if j % 2 == 0 else (j + 1) * m - i - 1 for i in range(m)] for j in range(n)]
