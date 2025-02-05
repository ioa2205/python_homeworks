sentence = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in sentence.split())
print(acronym)