# Рудзянский Артемий
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
lst_values = list(dict1.values())
product = 1
for item in lst_values:
    product *= item
print(product)
