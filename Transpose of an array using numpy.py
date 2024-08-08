import numpy as np
def transpose(arr):
    transpose_arr = np.transpose(arr)
    return transpose_arr
array = np.array([[1,2,3],[4,5,6]])
print(f'Orignal array \n{array}')
print(f'Transpose of array \n{transpose(array)}')