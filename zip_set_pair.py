# create a set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# zip(): Pairs elements from both lists position by position
# set(): removes duplicates and stores items in unordered way
# use list(): if you want it in ordered way

paired = set(zip(first_list, second_list))

print(paired)
