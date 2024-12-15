import numpy as np


#(Example
import numpy as np

# Create lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Convert lists to NumPy arrays
array1 = np.array(list1)
array2 = np.array(list2)

# Element-wise operations
sum_result = array1 + array2  # Element-wise addition
difference = array1 - array2  # Element-wise subtraction
product = array1 * array2     # Element-wise multiplication
quotient = array1 / array2    # Element-wise division
power = array1 ** 2           # Element-wise power

# Results
print("Addition:", sum_result)
print("Subtraction:", difference)
print("Multiplication:", product)
print("Division:", quotient)
print("Power:", power)
#)

#Echelon form for row equivalence

A = np.array([[0, 1, 2, 3], #R1
              [1, 1, 2, 3], #R2
              [2, 2, 2, 3], #R3
              [3, 3, 3, 3]])#R4

print(A)

#Define each row as an ARRAY NOT A LIST

R1 = np.array([0, 1, 2, 3])
R2 = np.array([1, 1, 2, 3])
R3 = np.array([2, 2, 2, 3])
R4 = np.array([3, 3, 3, 3])

A = np.array([R2 - R1,
              R1,
              R3 - 2*R2,
              R4 - 3*R3])

print(A)



#Inverse (A is non-singular)

