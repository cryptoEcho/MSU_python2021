# считать файл, и записать в другой файл считанные строки в обратном порядке
input = open('input.txt', 'r')
rd = input.readlines()
output = open('output.txt', 'w')
rd[len(rd)-1] = rd[len(rd)-1] + '\n'
rd[0].rstrip()
output.writelines(rd[::-1])




input.close()
output.close()
print('\n\nbye')