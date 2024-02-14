# Description: Linear search algorithm to find the first occurrence of a value in an array

names = ['John', 'Jane', 'Jack', 'Jill', 'Jenny', 'Jerry', 'Jill', 'Jenny', 'Jenny']

# Linear search algorithm
def linear_search(arr, value):
    for index, item in enumerate(arr):
        if item == value:
            return index
    return -1

print(f"Result for search: {linear_search(names, 'Jill')}, the linear_search is more efficient that linear_search_2")  # 3
# end of linear search algorithm

# Using enumerate to get the index and value of an array
enum = enumerate(names)
for indice, value in enum:
    print(f"{indice}, {value}, {value == 'Jill'}")

# Get the memory address of the array
print(enum)

# Another way to implement the linear search algorithm
# This implementation using more memory and is less efficient, but it is easier to read
# In this implementaion have a memory leak, because for find the index using the index method, the array is iterated again
def linear_search_2(value):
    for item in names:
        if item == value:
            return names.index(item)
    return -1

print(f"Result for search: {linear_search_2('Jill')}, the linear_search_2 is less efficient that linear_search, because \n for find the index using the index method, the array is iterated again")  # 3

