message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for chars in message:
    if chars == search:
        result += 1
    
    
print(f"Кількість "r" у рядку: {result}")     