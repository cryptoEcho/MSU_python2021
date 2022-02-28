# my_list1 = [1,5,6,6,7,29,0,30,29,2,2]
# my_list2 = []
# my_set = set(my_list)
# print(my_set)
# print(len(my_set))

my_list1 = [1, 5, 6, 6, 7, 29, 0, 30, 29, 2, 2]
my_list2 = [1, 1, 4, 4, 7, 29, 0, 30, 29, 2, 2]
my_set1 = set(my_list1)
my_set2 = set(my_list2)
new_set = my_set1 & my_set2
print('bye')

mystr = 'dsfsdfsdfsdfsdf c c c sfd sfd  sfd sfd sfd sfd sfd sfd sfd sfd sfd sfdsfd'
my_dict = {}
a = mystr.split()
my_set3 = set(a)
for item in my_set3:
    my_dict.update({item:a.count(item)})
sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse = True)
print(my_dict)
print(sorted_list[0])
