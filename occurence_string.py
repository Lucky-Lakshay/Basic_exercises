# Write a program to count occurrences of all characters within a string

str1 = "Pineapple"
str1 = str1.lower()
characters = {}

for i in str1:
    count = str1.count(i)
    characters.update({i: count})

print(characters)
