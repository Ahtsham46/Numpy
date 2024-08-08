import numpy as np
a = np.arange(0,12).reshape(3,4)
sum_row = a.sum(axis=0)
sum_column = a.sum(axis=1)
print(a)
print(f'Sum of each row is: {sum_row}')
print(f"Sum of each column is: {sum_column}")