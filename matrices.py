#Matrices - Uncle Sam

def create_matrix(order):

    """Returns a square matrix of a given order"""

    size = order**2
    matrix = [0 for i in range(size)]
    c = 0
    for i in range(order):
        for j in range(order):
            index = (i+1, j+1)
            element = int(input(f"Enter element at index {index}: "))
            matrix[c] = (element)
            c += 1
    return matrix

def display_matrix(matrix):

    """Prints a given square matrix"""

    width = 0
    for i in matrix:
        if len(str(i)) > width:
            width = len(str(i))
    size = len(matrix)
    side = int(size ** 0.5)
    if side != size ** 0.5:
        print("Please input a square matrix.")
        return
    start = 0
    end = side
    for i in range(side):
        print("|", end = " ")
        for j in matrix[start:end]:
            print(str(j).zfill(width), end = " ")
        start += side
        end += side
        print("|")

def add_matrices(matrix1, matrix2):

    """Adds two square matrices (of the same order) and returns the resultant matrix"""

    if len(matrix1) != len(matrix2):
        return "Please input two square matrices of the same order"
    else:
        resultant = matrix1[:]
        for i in range(len(matrix2)):
            resultant[i] += matrix2[i]
    return resultant
        
def multiply_matrix_scalar(matrix, scalar):

    """Returns a matrix multiplied by a scalar"""

    return [x * scalar for x in matrix]

def multiply_matrices(matrix1, matrix2):

    """Returns the product of the multiplication of two square matrices (Returns matrix1 X matrix2)"""

    sowry = "Sorry, matrix multiplication is currently only supported for square matrices of the same order"
    if len(matrix1) != len(matrix2):
        return sowry
    size = len(matrix1)
    if size**0.5 != int(size**0.5):
        return sowry
    resultant = [0 for x in range(size)]
    resultant[0] = (matrix1[0] * matrix2[0]) + (matrix1[1] * matrix2[3]) + (matrix1[2] * matrix2[6])
    resultant[1] = (matrix1[0] * matrix2[1]) + (matrix1[1] * matrix2[4]) + (matrix1[2] * matrix2[7])
    resultant[2] = (matrix1[0] * matrix2[2]) + (matrix1[1] * matrix2[5]) + (matrix1[2] * matrix2[8])
    resultant[3] = (matrix1[3] * matrix2[0]) + (matrix1[4] * matrix2[3]) + (matrix1[5] * matrix2[6])
    resultant[4] = (matrix1[3] * matrix2[1]) + (matrix1[4] * matrix2[4]) + (matrix1[5] * matrix2[7])
    resultant[5] = (matrix1[3] * matrix2[2]) + (matrix1[4] * matrix2[5]) + (matrix1[5] * matrix2[8])
    resultant[6] = (matrix1[6] * matrix2[0]) + (matrix1[7] * matrix2[3]) + (matrix1[8] * matrix2[6])
    resultant[7] = (matrix1[6] * matrix2[1]) + (matrix1[7] * matrix2[4]) + (matrix1[8] * matrix2[7])
    resultant[8] = (matrix1[6] * matrix2[2]) + (matrix1[7] * matrix2[5]) + (matrix1[8] * matrix2[8])
    return resultant

a = [x for x in range(9)]
b = [-x for x in range(9)]
display_matrix(a)
display_matrix(b)
display_matrix(multiply_matrices(a, b))
