# Objective- Count how many times a substring appears in a given string
# Rule - Don't use the count method
Given_string = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy."
# Substring to count - "happy"
# Give count variable value 0
count = 0
# Iterating till the length of Given_string and adding 1 to count everytime a 5 letter substring is "happy"
len_string = len(Given_string)
for i in range(len_string - 1):
    if Given_string[i : i + 5] == "happy":
        count += 1
    else:
        continue
print(f"The no. of times 'happy' has appeared is {count}")
