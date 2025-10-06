def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        total_spaces = length - len(string)
        left_spaces = total_spaces // 2
        right_spaces = total_spaces - left_spaces
        return " " * left_spaces + string + " " * right_spaces
print(format_string("Hi", 4))
