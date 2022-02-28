a = 'hello'
for i in range(len(a))[::-1]:
    print(a[i])
for i in reversed(range(len(a))):
    print(a[i])

print('bye')