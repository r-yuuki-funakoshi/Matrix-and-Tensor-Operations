import numpy as np

# np.array : creates a matrix
# addition, substraction, elementary multiplication and division : normal
# np.dot : matrix multiplication
# np.transpose : transpose
# np.linalg.inv() : find inverse
# np.linalg.det : find determinant 




# row by column
# 3 by 3 matrix 
array1 = np.array([[1, 2, 3],
                   [0, 0, 0],
                   [3, 2, 1]])
# 2 by 10 matrix using 'func(x) for x in range' loop
array2 = np.array([[x + 1 for x in range(0, 10)],
                   [y == 0 for y in range (0, 10)]])

#Practice
A = ([[1, 0, 1, 0],
      [2, 0, 2, 0],
      [3, 0, 3, 0]])
B = ([[1, 2, 3],
      [1, 2, 3],
      [1, 2, 3],
      [1, 2, 3]])
C = np.matmul(A, B)
D = ([[0, 1, 2, 3],
      [1, 1, 2, 3],
      [2, 2, 2, 3],
      [3, 3, 3, 3]])
E = np.linalg.inv(D)
F = np.dot(E, D)                  
print(array1)
print(array2)
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)

