def sum_to_one(n):
    if n == 1:
        return n
    print("Recursing with input: {0}".format(n))
    return n + sum_to_one(n - 1)

# define flatten() below...
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
