#Objective- Capitalize first letter of all words in a statement
statement = "courage is not the absence of fear but the strength to overcome it."
words = statement.split()
cap_words = [word.capitalize() for word in words]
print(" ".join(cap_words))