# Remove special symbols / punctuation from a string

import re

str1 = "/*Jon is @developer & musician"
print("Original string is: ", str1)

# Solution: Using regex replace pattern in a string
# ^ negates, anything inside [] is what ur matching in string: w words, s spaces, d digits
# if u remove ^ everything u r matching will be removed

res = re.sub(r"[^\w\s]", "", str1)
print("New string is ", res)
