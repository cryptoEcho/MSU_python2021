class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, num_elems):
        self.n = num_elems
        self.counter = 0

    def __next__(self):
        if self.counter < self.n:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


def simple_generator(val):
    while val > 0:
        val -= 1
        yield val**2
        yield val
    if val == 0:
        return 'final'
iter2 = simple_generator(7)
iter1 = SimpleIterator(7)
for i in iter1:
    print(i)

print('bye')
