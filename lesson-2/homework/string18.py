s = input("Enter a sentence: ").split()
start_word = input("Starts with: ")
end_word = input("Ends with: ")
if start_word == s[0] and end_word == s[-1]:
    print("Matches")
else:
    print("Not matches")
