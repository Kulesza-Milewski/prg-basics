def f(array2D):
    n = len(array2D)

    for i in range(n):
        row_sum = sum(array2D[i])
        col_sum = sum(row[i] for row in array2D)

        if row_sum != col_sum:
            return False
    return True        