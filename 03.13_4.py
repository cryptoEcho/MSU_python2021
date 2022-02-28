str2 = input()
lst = list(str2)
k = 0
for i in range(0, len(str2), 3):
    print(lst.pop(i-k))
    k += 1
str2 = ''.join(lst)
print(str2)