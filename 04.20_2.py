class Stack:
    def __init__(self):
        self.lst = list()
        self.name = 'buff'

    @property
    def buff(self):
        return self.name

    @buff.setter
    def buff(self, val):
        self.lst.append(val)


p = Stack()
print('bye')