import numpy as np
def matrix(arr):
    try:
        invers = np.linalg.inv(arr)
        return invers
    except np.linalg.LinAlgError:
        return 'The matrix is singular and cannot be inverted.'
matrixx = np.array([[1,2],[3,4]])
print(f'original matrix is {matrixx}')
print(matrix(matrixx))