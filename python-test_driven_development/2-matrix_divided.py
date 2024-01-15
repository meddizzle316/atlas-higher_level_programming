#!/usr/bin/python3
"""
part of a module to help us learn doctesting
"""
def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix """

    # rows are same length check
    for row in matrix:
        if not len(row) == len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    # is float or int check
    for i in range(len(matrix)):
        for x in range(len(matrix[0])):
            if not isinstance(matrix[i][x], (int, float)):
                raise TypeError('matrix must be a matrix' 
                    '(list of lists) of integers/floats')

    # checks if div is a int or float
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number') 
  
    # checks if div is zero
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # dividing operation
    new_matrix = [[round(j / div, 2) for j in row] for row in matrix]
    return new_matrix
