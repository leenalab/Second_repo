fh = open('names.txt', 'w')
fh.write('How are you!')
fh.close()

fh = open('names.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()


