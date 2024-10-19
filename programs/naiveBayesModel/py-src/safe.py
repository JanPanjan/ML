data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# list comprehension
# new_list = [expression for item in iterable if condition]

# first two rows
print(data[:2])

# first two columns
print([row[:2] for row in data])

# 2x2 matrix, top left corner
print([row[:2] for row in data[:2]])

# flattened list
print([item for row in data for item in row])

# basic cases
print([x for x in range(0, 5)])
print([x ** 2 for x in range(0, 5)])
print([x for x in range(0, 5) if x > 3])
print([x for x in [1, 2, 3, 4, 5] if x % 2 == 0])

# strings
print([char for char in "jan"])
print([char for char in "jan" if char.isupper()])
print([char for char in "jan" if char.islower()])
