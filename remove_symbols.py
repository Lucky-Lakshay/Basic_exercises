# Remove special symbols / punctuation from a string

import re
import string

str1 = "/*Jon is @developer & musician"
print("Original string is: ", str1)

# Solution 1: Use string functions translate() and maketrans()
new_str = str1.translate(str.maketrans("", "", string.punctuation))
print("New string is: ", new_str)

# Solution 2: Using regex replace pattern in a string
res = re.sub(r"[^\w\s]", "", str1)
print("New string is ", res)
