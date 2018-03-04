from scipy import sparse
import numpy as np

matrix = np.array([
    [12,43,32],
    [64,32,98],
    [84,81,61]
])

sparse_matrix = sparse.csr_matrix(matrix)
sparse_matrix2 = sparse.coo_matrix(matrix)
print(sparse_matrix)
print('2nd method')
print(sparse_matrix2)