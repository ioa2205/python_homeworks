# Problem 11
s = input("Enter a string: ")
print("Contains" if any(char.isdigit() for char in s) else "Not digits")