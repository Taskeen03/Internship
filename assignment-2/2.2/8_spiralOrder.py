def spiralOrder(matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]
    return res

matrix_input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = spiralOrder(matrix_input)
print(result) 