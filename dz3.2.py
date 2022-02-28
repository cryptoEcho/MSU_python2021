# Рудзянский Артемий
def top3(str1):
    tp3 = list(['', '', ''])
    tp3_value = list([0, 0, 0])
    for i in range(0, len(str1)):
        if str1[i] != ' ' and ''.join(tp3).find(str1[i]) == -1:
            if str1.count(str1[i]) > tp3_value[0]:
                tp3_value[2], tp3_value[1] = tp3_value[1], tp3_value[0]
                tp3[2], tp3[1] = tp3[1], tp3[0]
                tp3_value[0] = str1.count(str1[i])
                tp3[0] = str1[i]
            elif str1.count(str1[i]) > tp3_value[1]:
                tp3_value[2] = tp3_value[1]
                tp3[2] = tp3[1]
                tp3_value[1] = str1.count(str1[i])
                tp3[1] = str1[i]
            elif str1.count(str1[i]) > tp3_value[2]:
                tp3_value[2] = str1.count(str1[i])
                tp3[2] = str1[i]
    lst = list()
    for i in range(3):
        if tp3_value[i] != 0:
            lst.append(tp3[i])
            lst.append(' - ')
            lst.append(tp3_value[i])
            lst.append(', ')
    lst.pop(len(lst)-1)
    print(*lst)


top3('dvadcat chetire              3838888888888ppp')
top3('fsfs')
