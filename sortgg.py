import math
C = list()
A = [3, 78, 65, 5, 67, 10, 54, 43, 32, 33]
d = len(A)
print(math.ceil(len(A)))
A1 = A[:math.ceil(len(A)/2)]
A2 = A[math.floor(len(A)/2)+1:]
print(A)
print(A1)
print(A2)
A1.sort()
A2.sort()
print(A1)
print(A2)
while d > 0:
    if len(A1) > 0 and len(A2) > 0:
        if A1[-1] > A2[-1]:
            C.append(A1.pop())
        else:
            C.append(A2.pop())
    type(A2)
    if len(A1) == 0:
        C = C + A2.reverse()

    d -= 1
print(C.reverse())