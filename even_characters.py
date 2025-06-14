# Printing only characters at even index of a string
# Without using list slicing
Given_word = "sophisticated"
# Calculating length of string
len_word = len(Given_word)
# iterating each character in string at x index
# starting with 0, till string length which is 13 but range stop value is exclusive so it will give 12, 2 to give only even x
print("Characters at even index are:")
for x in range(0, len_word, 2):
    print(Given_word[x], end=" ")
