string = input("Please type a sentence: ")
print(*map(string.lower().count, "aeiou"))
