class Person:
    name = ''
    surname = ''
    params = ''
    my_list= ''
    def __init__(self, my_str):
        self.my_list = self.parser(my_str)
        lst = my_str.split()
        self.parser(my_str)
        self.name = self.my_list[0]
        self.surname = self.my_list[-1]
    def parser(self, my_str):
        my_list = my_str.split()
        return my_list

    def __str__(self):
        return self.name + ' ' + self.surname

    def __getitem__(self, key):
        return self.my_list[key]

    def __ilshift__(self, other):
        self.surname = other
        return self
    # self.name = name



p = Person("Johann     Carl Friedrich   Gauß")

print('bye')
