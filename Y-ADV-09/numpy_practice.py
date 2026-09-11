import numpy as np

# 1D Array
numbers = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(numbers)

print("Number of dimensions:")
print(numbers.ndim)

# 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("2D Array:")
print(matrix)

print("Number of dimensions:")
print(matrix.ndim)

print("Shape:")
print(matrix.shape)  

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)

print("Addition:")
print(numbers + 10)

print("Subtraction:")
print(numbers - 5)

print("Multiplication:")
print(numbers * 2)

print("Division:")
print(numbers / 10) 

# Task 5 - Indexing and Slicing

print("First element:")
print(numbers[0])

print("Third element:")
print(numbers[2])

print("Last element:")
print(numbers[-1])

print("Slice 1 to 3:")
print(numbers[1:4])

print("First three:")
print(numbers[:3])

print("From third:")
print(numbers[2:])

# Task 6 - Broadcasting

broadcast_numbers = np.array([10, 20, 30, 40])

print("Broadcasting - Original Array:")
print(broadcast_numbers)

result = broadcast_numbers + 5

print("Broadcasting - After adding 5:")
print(result)