import math
str1 = input()
str1 = str1[math.ceil(len(str1)/2):] + str1[math.floor(len(str1)/2):math.ceil(len(str1)/2)] + str1[:math.floor(len(str1)/2)]
print(str1)