class MSWord:
    def __init__(self, name):
        self.name = name
        self.a = open(name, 'r')
        self.fulltext = self.a.read()

    @property
    def stat(self):
        count_word = 0
        count_symbol = 0
        count_line = 0
        alphabet = set(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        slash = {'.', ',', '/', ';', ':'}
        prevstep = ''
        for step in input.fulltext:
            if step in alphabet:
                count_symbol += 1
            if step == '\n':
                count_line += 1
            if prevstep in alphabet and step not in alphabet:
                count_word += 1
            prevstep = step
        if prevstep in alphabet or slash:
            count_line += 1
        dict1 = {'count_word': count_word, 'count_symbol': count_symbol, 'count_line': count_line}
        return dict1

    def ShowStat(self):
        print('Input file contains: ', self.stat.get('count_symbol'), ' letters, ', self.stat.get('count_word'),
              ' words, ', self.stat.get('count_line'), ' lines.')


input = MSWord('input.txt')

print('bye')
