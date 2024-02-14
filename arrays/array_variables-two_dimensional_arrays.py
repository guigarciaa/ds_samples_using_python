names = [
    ['John', 'Jane', 'Jack', 'Jill', 'Jenny', 'Jerry'],
    ['Blue', 'Black', 'Cat', 'Marik', 'Joel', 'Doe']
]

# Linear search algorithm
def linear_search(arr, value):
    for index, item in enumerate(arr):
        if item == value:
            return index
        for i, row in enumerate(item):
            if row == value:
                return (index, i)
    return -1

print(f"Result for search: {linear_search(names, 'Jill')}")  #(0, 3)

# enum = enumerate(names)
# for indice, col in enum:
#     if col == 'Jill':
#         print(indice)
#     for i, row in enumerate(col):
#         if row == 'Jill':
#             print((indice,i))
