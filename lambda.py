# lambda inside map, sorted and filter functions:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The even numbers in the list are: {even_numbers}")

print("-" * 120)

doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"The doubled numbers are: {doubled_numbers}")

print("-" * 120)

data = [("apple", 5), ("banana", 2), ("cherry", 8), ("date", 1)]
sorted_data = sorted(data, key=lambda item: item[1])
print(f"The sorted list of tuples based on the second element is: {sorted_data}")

print("-" * 120)

unsorted_num = [6, 3, 8, 9, 1, 5, 2, 0, 7, 4]
sorted_numbers = sorted(unsorted_num, key=lambda x: x)
print(sorted_numbers)

print("-" * 120)
