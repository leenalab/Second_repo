fh = open('names.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('names.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()


