def sum_to_one(n):
    if n == 1:
        return n
    print("Recursing with input: {0}".format(n))
    return n + sum_to_one(n - 1)

def flatten(my_list):
    result = []
    for item in my_list:
        if isinstance(item, list):
            print("List found!")
            flat_list = flatten(item)
            result.extend(flat_list)
    else:
        result.append(item)
    
    return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

#fibonacci sequence with recursion
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

# build a binary earch tree with recursion from a sorted list
def build_bst(my_list):
    if my_list == []:
        return "No Child"
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    print(f"Middle index: {middle_idx}")
    print(f"Middle value: {middle_value}")
    tree_node = {"data": middle_value}
    tree_node["left_child"] = build_bst(my_list[:middle_idx])
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])
    return tree_node