# Рудзянский Артемий
lst1 = ['Andrey', 'Vitya', 'Yulya', 'Kolya']
lst2 = ['second grader', 'third grader', 'first grader', 'first grader']
dict1 = {}
for i in range(len(lst1)):
    dict1.update({lst1[i]: lst2[i]})
print(dict1)