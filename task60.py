def find_determinant(matrix):
    if len(matrix[0]) != len(matrix):
        raise ValueError("Matrix is not a square one")
    process_gaussian_elimination(matrix)
    return multiply_main_diagonal(matrix)


def process_gaussian_elimination(matrix):
    for k in range(0, len(matrix)):
        for i, line in enumerate(matrix[k + 1:len(matrix)]):
            coef = determine_coef(matrix[k][k], line[k])
            for j, elem in enumerate(line):
                line[j] += coef * matrix[k][j]


def multiply_main_diagonal(matrix):
    result = matrix[0][0]
    for i in range(1, len(matrix)):
        result *= matrix[i][i]
    return result


def determine_coef(a0, ax):
    return (-1) * ax / a0


def print_matrix(matrix):
    for line in matrix:
        for elem in line:
            print(elem, end=" ")
        print()


if __name__ == '__main__':
    matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    matrix2 = [[3, 1, -2, 7], [-3, 5, 1, 9], [12, 2, 3, -2], [-6, 3, -2, 1]]
    # print(len(matrix))
    # print(len(matrix[0]))
    print(find_determinant(matrix))
    print(find_determinant(matrix2))
