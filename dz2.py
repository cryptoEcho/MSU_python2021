def dz21():
    # Рудзянсикй Артемий
    dict1 = {'a': 300, 'b': 400}
    dict2 = {'c': 500, 'd': 600}
    sum_dict = dict(list(dict1.items()) + list(dict2.items()))
    print(sum_dict)
    # Python 3.9
    # sum_dict = dict1 | dict2
    # print(sum_dict)


def dz22():
    # Рудзянский Артемий
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    lst_values = list(dict1.values())
    product = 1
    for item in lst_values:
        product *= item
    print(product)


def dz23():
    # Рудзянский Артемий
    lst = [1, 2, 3, 4, 5]
    dict1 = {}
    # dict1 = {1: str(int(1**3))}
    for i in range(1, 11):
        dict1.update({i: str(int(i ** 3))})
    print(dict1)
    print('bye')


def dz24():
    # Рудзянский Артемий
    lst1 = ['Andrey', 'Vitya', 'Yulya', 'Kolya']
    lst2 = ['second grader', 'third grader', 'first grader', 'first grader']
    dict1 = {}
    for i in range(len(lst1)):
        dict1.update({lst1[i]: lst2[i]})
    print(dict1)

dz21()
dz22()
dz23()
dz24()

print('bye')