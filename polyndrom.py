a = list(input())
# print(a)
b = True
# print(len(a))
i = 0
while b and i < len(a)//2:
    if a[i] != a[len(a)-i-1]:
        b = False
    i += 1
if b:
    print("Введенная строка является полиндромом")
else:
    print("Введенная строка не является полиндромом")

