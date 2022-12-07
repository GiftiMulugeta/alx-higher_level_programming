#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x = matrix[i][j]
            square = x * x
            if j != (len(matrix[i])) - 1:
                print(" ", end="")
                return square
        print("")
