import numpy as np

#create a matrix
matrix = np.array([
    [12,32,34,54,56],
    [98,87,76,65,54],
    [15,25,35,46,74]
])

#max value from an array
print(np.max(matrix,1))

#min value from an array
print(np.min(matrix,1))