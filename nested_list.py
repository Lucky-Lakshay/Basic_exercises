# print the element '55'
nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print(nested_list[1][1])

# flatten the list(list comprehension)
flatten_list = [item for sublist in nested_list for item in sublist]
print(flatten_list)