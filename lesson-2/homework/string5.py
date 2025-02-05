# Problem 5
s = input("Enter a string: ").lower()
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
v_counts = sum(1 for char in s if char in vowels)
c_counts = sum(1 for char in s if char in consonants)
print(f"Vowels: {v_counts}, Consonants: {c_counts}")