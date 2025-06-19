def calculation(a, b):
    # return multiple values separated by comma
    return a + b, a - b


# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)
