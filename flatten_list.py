# flatten a nested list using loops
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

def flatten_list(nested_list):
    flattened_list = []
    for items in nested_list:
        if isinstance(items, list):
            for item in items:
                flattened_list.append(item)
        else:
            flattened_list.append(items)
    print(flattened_list)

flatten_list(nested_list)
