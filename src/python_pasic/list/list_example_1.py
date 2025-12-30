grocery_list = [
  "Apple",
  "Tomato",
  "Orange",
  "Tomato"
]

# Add an item to the list
grocery_list.append("Carrot")  # Output: ['Apple', 'Tomato', 'Orange', 'Tomato', 'Carrot']

# Remove an item from the list
grocery_list.remove("Tomato")  # Output: ['Apple', 'Orange', 'Tomato', 'Carrot']

# Iterate through the list
for item in grocery_list:
  print(f'- {item}')

# Check if an item is in the list
print("Banana" in grocery_list)  # Output: False
print("Carrot" in grocery_list)  # Output: True

item_name = "Tomato"
if item_name in grocery_list:
  print(f'"{item_name}" is in the list')
else:
  print(f'"{item_name}" is not in the list')

# Get the total number if items in the list
grocery_len = len(grocery_list) # Value is 4
print(f'The length of the list is: {grocery_len}')