import numpy as np

#creating a matrix
matrix = np.array([[10,20,30],
                   [40,50,60],
                   [71,82,93]])
#print(matrix[1,2])

#creating a tensor

tensor = np.array([
    [[[13,23],[11,31]],[[23,14],[34,43]]],
    [[[22,23],[36,35]],[[44,34],[52,55]]]
])

#print(tensor)
#select element from a tensor
print(tensor[1,0,1])

