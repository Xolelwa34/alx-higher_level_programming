#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    cols = len(matrix[0])
    for i in range(0, n):
        for y in range(0, cols):
            if y == cols - 1:
                print('{}'.format(matrix[i][y]), end='')
            else:
                print('{}'.format(matrix[i][y]), end=' ')
        print()
