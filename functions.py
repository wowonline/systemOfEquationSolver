import numpy as np


def reduction_UT(matrix_A, matrix_B, n):
    """
    Приведение матрицы к верхне-треугольному виду
    и применение тех же преобразований к вектору-
    столбцу. Требования на матрицу A такие же, как 
    требуется в функции gauss_simple.
    """

    matrix_A = np.array(matrix_A, dtype=np.float64)
    matrix_B = np.array(matrix_B, dtype=np.float64)

    if n == 1:
        matrix_B /= matrix_A
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

        for i in range(j, n):
            if matrix_A[j, i] != 0:
                break
        
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


def gauss_simple(matrix_A, matrix_B, n):
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

    matrix_A = np.array(matrix_A, dtype=np.float64)
    matrix_B = np.array(matrix_B, dtype=np.float64)

    matrix_A, matrix_B = reduction_UT(matrix_A, matrix_B, n)

    for j in range(n-1, -1, -1):
        if j == n-1:
            decision_system = np.array([matrix_B[n-1]])
            continue

        tmp = matrix_B[j] - np.sum(matrix_A[j+1:, j] * decision_system)
        decision_system = np.concatenate((decision_system, [tmp]))

    return decision_system[::-1]







