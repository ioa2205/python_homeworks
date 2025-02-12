# Problem 3
txt = input("Enter a string: ")
new_txt = []
for i, char in enumerate(txt):
    if i == 3:
        new_txt.append('_')
    new_txt.append(char)
print(''.join(new_txt))