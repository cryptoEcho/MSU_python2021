a = [1, 2, 3, ['hello', 'im in']]
for i in range(len(a)):
    print(a[i])
print('bye')

itr = iter(a)
itr.__next__()
for elem in a:
    print(elem)
   # itr.__next__()
   # print(elem.index())
print('bye')


next(itr)