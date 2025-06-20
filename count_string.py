# Count all letters, digits, and special symbols from a given string
string = "bi4u27yn3*&%%^Qefni"
chars = 0
symbols = 0
digits = 0

for i in string:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        chars += 1
    else:
        symbols += 1

print(f"characters: {chars}, symbols: {symbols}, Digits: {digits}")
