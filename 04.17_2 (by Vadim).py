class Person:
    name=''
    surname=''
    params=''
    my_list=''


    def __init__(self, my_str):
        print(my_str.split())

    def __init__(self, my_str):
        self.my_list=self.parser(my_str)
        #изменить
        self.name = self.parser(my_str)[0]
        self.surname = self.my_list.pop()

    def parser(self,my_str):

        my_list = []
        my_list = my_str.split()
        return my_list

    def print(self):
        print(self.name,self.surname)

    def __str__(self):

        return  p.name +' ' + p.surname

    def __getitem__(self, index):

        return self.my_list[index]

    def __ilshift__(self, other):

        self.surname = other
        return self


p = Person("Johann     Carl Friedrich   Gauß")
print(p)

