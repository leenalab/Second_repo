fh = open("names.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("names.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()

