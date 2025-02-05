s = input("Enter anything: ")
s = s.lower().replace(" ", "")
print("palindrome" if s == s[::-1] else "not palindrome")