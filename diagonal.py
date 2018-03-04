import numpy as np

matrix = np.array([
    [23,54,87,56],
    [91,43,23,45],
    [89,69,29,79]
])

#find diagonal
print(matrix.diagonal())

#getting sum of diagonal result

print(matrix.diagonal().sum())

#getting sum of a complete matrix
print(matrix.sum())
