import numpy as np
import functions as func


def matrices_make(size, n=30, m=9):
    matrix_A = np.zeros((size, size))
    matrix_B = np.zeros(size)

    for i in range(size):
        for j in range(size):
            matrix_A[i, j] = (i+j) / (m+n) if i != j else n + m**2 + j/m + i/n

        matrix_B[i] = i**2 - 100

    return (matrix_A, matrix_B)


if __name__ == "__main__":
    try:
        size = int(input('Enter matrix size: '))
        response = int(input('\nType "0", in case you want to use premade matrix for specific n. \
                             \nOtherwise type "1" to specify matrix by youself: '))
    except ValueError:
        exit()

    if response == 0:
        a, b = matrices_make(size)
        print("Your matrices a and b:")
        print(a, b)
    elif response == 1:
        print("Specify a matrix(your numbers will be specified as columns):")
        flag = 1
        for i in range(size):
            if flag == 1:
                a = np.array([int(j) for j in input().split()])
                a = a[None, :]
                flag = 0
            else:
                b = np.array([int(j) for j in input().split()])
                b = b[None, :]
                a = np.concatenate((a, b), axis=0)
        print("Now specify B-vector in same manner:")
        b = np.array([int(j) for j in input().split()])
    else:
        print('\nEnter correct number!\n')
        exit()

    try:
        opt = int(input('Now choose a function:\n \
                        0 - solve system of equations\n \
                        1 - find determinant of A\n \
                        2 - find A^-1\n \
                        3 - calculate 1-norm of A\n \
                        4 - calculate condition number of A\n'))
    except ValueError:
        exit()
    
    optiondict = {
        0 : func.pivoting_gaussian_elimination,
        1 : func.determinant,
        2 : func.inverse_matrix,
        3 : func.matrix_norm,
        4 : func.matrix_condition_number
    }
    if opt == 0:
        print(optiondict[opt](a, b, size))
    else:
        print(optiondict[opt](a, size))
    # elif opt == 1:
    #     print(func.determinant(a, size))
    # elif opt == 2:
    #     print(func.inverse_matrix(a, size))
    # elif opt == 3:
    #     print(func.matrix_norm(a, size))
    # elif opt == 4:
    #     print(func.matrix_condition_number(a, size))
    # else:
    #     print("Enter another number!")
    #     exit()