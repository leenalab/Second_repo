with open("names.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("names.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)
