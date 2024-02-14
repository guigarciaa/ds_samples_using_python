# Description: Linear search algorithm to find the first occurrence of a value in an array

names = ['John', 'Jane', 'Jack', 'Jill', 'Jenny', 'Jerry', 'Jill', 'Jenny', 'Jenny']

# Linear search algorithm
def linear_search(arr, value):
    for index, item in enumerate(arr):
        if item == value:
            return index
    return -1

print(linear_search(names, 'Jill'))  # 3
# end of linear search algorithm

# Using enumerate to get the index and value of an array
enum = enumerate(names)
for indice, value in enum:
    print(f"{indice}, {value}, {value == 'Jill'}")

# Get the memory address of the array
print(enum)