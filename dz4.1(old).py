def nechet(str1):
    if len(str1) == 0:
        return
    # if str1[0] == '0':
    #     return
    lst = list(str1)
    if int(lst[0]) % 2 != 0:
        print(lst[0])
    lst.pop(0)
    nechet(''.join(lst))

nechet('123456789')