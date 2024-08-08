import numpy as np
def square_elements(input_array):
    input_array = np.array(input_array)
    squared_array = input_array ** 2
    return squared_array
original_array = np.array([1, 2, 3, 4, 5])
squared_array = square_elements(original_array)
print("Original array:", original_array)
print("Squared array:", squared_array)
