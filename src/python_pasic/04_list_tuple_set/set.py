# Set features:
# - unique items
# - Unordered
# - Can't access to the items via index
unique_groceries = {"Banana", "Apple", "Banana", "Orange"}

print(unique_groceries)  # Output: {'Apple', 'Banana', 'Orange'}
print(len(unique_groceries))  # Output: 3

unique_groceries.add("Milk")  # Output: {'Milk', 'Apple', 'Orange', 'Banana'}
unique_groceries.add("Milk")  # Output: {'Milk', 'Apple', 'Orange', 'Banana'}

second_unique_groceries = {"Banana", "Cucumber"}

# Intersection
second_unique_groceries.intersection(unique_groceries)  # Output: {'Banana'}

# Union
second_unique_groceries.union(unique_groceries)  # Output: {'Milk', 'Cucumber', 'Orange', 'Banana', 'Apple'}

# Difference
unique_groceries.difference(second_unique_groceries)  # Output: {'Apple', 'Milk', 'Orange'}
second_unique_groceries.difference(unique_groceries)  # Output: {'Cucumber'}

# Iterate through the set (Output might be different on each run)
for item in unique_groceries:
  print(item)

# Cast the list to a unique list
groceries_list = ['Banana', 'Apple', 'Apple', 'Banana', 'Orange', 'Milk']
unique_groceries_list = list(set(groceries_list))
print(unique_groceries_list)  # Output: ['Apple', 'Milk', 'Orange', 'Banana'] (Note: This is an Unordered list)
