# колво символов, слов, строк в файле (не закончено)
input = open('input.txt', 'r')
# input.read(1)
count_word = 0
count_symbol = 0
count_line = 0
step = input.read(1)
prevstep = ''
# st = set(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z'])
slash = set(['.', ',', '/', ';', ':'])

while step != '':
    b = False
    if step in alphabet:
        count_symbol += 1
    if step == '\n':
        count_line += 1
        if prevstep in alphabet:
            count_word += 1
    while step == ' ' or step in slash:
        step = input.read(1)
        b = True
    if b:
        count_word += 1
        prevstep = step
        continue
    prevstep = step
    step = input.read(1)
if prevstep in alphabet or slash:
    count_line += 1
print('Input file contains: ', count_symbol, ' letters, ', count_word, ' words, ', count_line, 'lines')
input.close()
print('bye')