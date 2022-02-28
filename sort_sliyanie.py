a1 = list()
i = 0
for i in range(1, 10):
    a1.append(i*3)
print(a1)

a2 = list()
i = 0
for i in range(1, 10):
    a2.append(i*2)
print(a2)
c = list()
for i in range(1, len(a1)+len(a2)):
    if a1[i] < a2[i]:
        c.append(a2[i])
        c.append(a1[i])
    else:
        c.append(a1[i])
        c.append(a2[i])
print(c)
