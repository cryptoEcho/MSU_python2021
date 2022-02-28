def simpl():
    str2 = input()
    first = str2.find('a')

    revers = str2[::-1]
    last = len(str2) - revers.find('a') - 1
    print(first, last)


def another():
    str2 = input()
    first = str2.find('a')
    lst = list(str2)
    lst.reverse()
    revers=''.join(lst)
    last = len(str2)-revers.find('a')-1
    str2 = str2[:first] + str2[last:first:-1] + str2[last:]
    print(str2)
another()

