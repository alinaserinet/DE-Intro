# Tuple is immutable
tuple_example = (
  3,
  1000,
  "Ali",
  "Python",
  3
)

print(tuple_example)  # Output: (3, 1000, 'Ali', 'Python', 3)

# Get an item from the tuple
print(tuple_example[0]) # Output: 3

# Tuple slicing
print(tuple_example[1:3]) # Output: (1000, 'Ali')

# Count of an item in the tuple
print(tuple_example.count(3)) # Output: 2

# Find the first index of an item
print(tuple_example.index(3)) # Output: 0
