s = input("Enter a string: ")
symbol = input("Enter a symbol to replace vowels with: ")

vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, symbol)

print("Modified string:", s)