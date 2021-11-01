import numpy as np
from numpy.matrixlib import matrix
import functions as func


# c = np.array([[2, 1, 2], [4, 3, 7], [6, 5, 6]],  dtype=np.float64)
# c = np.diag([1] * 3)
# c = np.array([[1, 4], [3, 5]], dtype=np.float64)
# b = func.inverse_matrix(c, 3)

# print(a)
# print()
# print(b)
# print()
# print(func.matrix_multiplication(c, b, 3))
# print(a.T * b.T)
# print(func.matrix_condition_number(c, 3))

# print(func.pivoting_reduction_UT(np.array([[1, 1], [1, 2]]), np.array([3, 4]), 2))

# print(func.inverse_matrix(np.array([[5, 14, 15], [5, 78, 0], [6, 2, 3]]), 3))

# print(func.determinant(np.array([2]), 1))

def matrices_make(size, n=30, m=9):
    matrix_A = np.zeros((size, size))
    matrix_B = np.zeros(size)

    for i in range(size):
        for j in range(size):
            matrix_A[i, j] = (i+j) / (m+n) if i != j else n + m**2 + j/m + i/n

        matrix_B[i] = i**2 - 100

    return (matrix_A, matrix_B)

a, b = matrices_make(5)
print(a, b)
