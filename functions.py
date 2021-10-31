import numpy as np
from numpy.matrixlib import matrix


def determinant(matrix, n, EPS=0.000000001):
    matrix = np.array(matrix, dtype=np.float64)
    det = 1.0
    if n == 1:
        return matrix[0]

    for i in range(n):
        k = i
        
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[k][i]):
                k = j
        
        if abs(matrix[k][i]) < EPS:
            det = 0
            break

        tmp = np.array(matrix[i, :], dtype=np.float64)
        matrix[i, :] = matrix[k, :]
        matrix[k, :] = tmp

        if i != k:
            det = -det

        det *= matrix[i][i]
        try:
            matrix[i, :] /= matrix[i][i]
        except ZeroDivisionError:
            print("Divided by zero\n")

        for j in range(n):
            if j != i and abs(matrix[j][i]) > EPS:
                for k in range(i+1, n):
                    matrix[j][k] -= matrix[i][k] * matrix[j][i]

    return det


def pivoting_reduction_UT(matrix_A, matrix_B, n):
    """
    Приведение матрицы к верхне-треугольному виду
    и применение тех же преобразований к вектору-
    столбцу. Требования на матрицу A такие же, как 
    требуется в функции pivoting_gaussian_elimination.
    """

    matrix_A = np.array(matrix_A, dtype=np.float64)
    matrix_B = np.array(matrix_B, dtype=np.float64)

    if n == 1:
        try:
            matrix_B /= matrix_A
        except ZeroDivisionError:
            print("Divided by zero\n")
        matrix_A[0] = 1
        return (matrix_A, matrix_B)

    for j in range(n):
        if j == n-1:
            try:
                matrix_B[n-1] /= matrix_A[n-1, n-1]
            except ZeroDivisionError:
                print("Divided by zero\n")
            matrix_A[n-1, n-1] = 1
            break

        i = np.argmax(matrix_A[j, j:])
        
        tmp = np.array(matrix_A[:, j], dtype=np.float64)
        matrix_A[:, j] = matrix_A[:, i]
        matrix_A[:, i] = tmp

        tmp = np.array(matrix_B[j], dtype=np.float64)
        matrix_B[j] = matrix_B[i]
        matrix_B[i] = tmp

        pivot = matrix_A[j, i]
        try:
            matrix_A[:, i] /= pivot
            matrix_B[i] /= pivot
        except ZeroDivisionError:
            print("Divided by zero\n")

        for i in range(j+1, n):
            if matrix_A[j, i] != 0:
                factor = matrix_A[j, i]
                matrix_A[:, i] -= factor * matrix_A[:, j]
                matrix_B[i] -= factor * matrix_B[j]

    return (matrix_A, matrix_B)        


def pivoting_gaussian_elimination(matrix_A, matrix_B, n):
    """
    Матрицы n x n, невырожденные.
    Матрица A выглядит таким образом:
                  j
        [[...], [...], ..., [...]]
    i    [...]  [...]       [...]
          ...    ...         ...
         [...]  [...]       [...]
    Матрица B - вектор столбец.
    n - количество строк/столбцов.
    """
    if determinant(matrix_A, n) == 0:
        print("Enter matrix with non-zero determinant")
        return -1

    matrix_A = np.array(matrix_A, dtype=np.float64)
    matrix_B = np.array(matrix_B, dtype=np.float64)

    matrix_A, matrix_B = pivoting_reduction_UT(matrix_A, matrix_B, n)

    for j in range(n-1, -1, -1):
        if j == n-1:
            solution_system = np.array([matrix_B[n-1]])
            continue

        tmp = matrix_B[j] - np.sum(matrix_A[j+1:, j] * solution_system)
        solution_system = np.concatenate((solution_system, [tmp]))

    return solution_system[::-1]







