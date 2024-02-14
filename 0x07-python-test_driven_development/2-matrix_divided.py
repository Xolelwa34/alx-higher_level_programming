#!/usr/bin/python3
"""This defines a division of matrix functionality."""

def matrix_divided(matrix, div):
    """Devides all elements of matrix."""
    list_int = "matrix must be a matrix (list of lists) of integers/floats"
    new_len = "Each row of the matrix must have the same size"
    div_int = "div must be a number"
    div_error = "division by zero"
    get_matrix = []
    old_lists = []
    if not matrix:
        raise TypeError(list_int)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_int)
    if div is 0:
        raise ZeroDivisionError(div_error)
    longitud = len(matrix[0])
    for metrix in matrix:
        if type(metrix) is not list:
            raise TypeError(list_int)
        if len(metrix) != longitud:
            raise TypeError(new_len)
        for item in metrix:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_int)
            numb = item / div
            old_list.append(round(numb, 2))
        get_matrix.append(old_list)
        old_list = []
    return get_matrix
