# Matrix

first_matrix = [
  [3, 12, 21],
  [43, 18, 21],
  [54, 12, 91]
]

# Get matrix items:
print(first_matrix[0])  # Output: [3, 12, 21]
print(first_matrix[2][0])  # Output: 54

second_matrix = [
  [4, 7, 82],
  [5, 81, 23],
  [90, 12, 23]
]

# Define sum:
first_matrix_rows, first_matrix_cols = len(first_matrix), len(first_matrix[0])
second_matrix_rows, second_matrix_cols = len(second_matrix), len(second_matrix[0])

if first_matrix_rows != second_matrix_rows:
  raise ValueError('First matrix rows do not match second matrix rows')

if first_matrix_cols != second_matrix_cols:
  raise ValueError('First matrix cols do not match second matrix cols')

result = [] # Result matrix to save sum of two matrices

for row in range(len(first_matrix)):
  temp_result_row = []
  for col in range(len(second_matrix[row])):
    temp_result_row.append(first_matrix[row][col] + second_matrix[row][col])
  result.append(temp_result_row)

print(result)  # Output: [[7, 19, 103], [48, 99, 44], [144, 24, 114]]
