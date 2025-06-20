# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

def balance(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    for i in s1:
        if i not in s2:
            return False
    return True        

print(balance("kg", "joking"))                    