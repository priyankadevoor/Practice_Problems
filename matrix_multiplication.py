def multiply(A, B):
    
    rows_a = len(A)
    rows_b = len(B)
    col_a = len(A[0])
    col_b = len(B[0])

    if col_a != rows_b:
        raise ValueError('Dimension not proper to multiply!')
    
    res = [[0] * col_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(col_b):
            for k in range(col_a):
                res[i][j] += A[i][k] * B[k][j]

    print(res)

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

multiply(A, B)