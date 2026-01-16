def f(array2D):
    n = 0

    while n < len(array2D):
        row = sum(array2D[n])
        col = array2D[0][n] + array2D[1][n] + array2D[2][n]

        if row != col:
            return False
        else:
            n += 1
            continue

    return True

print(f([[3,7,2],[4,2,5],[9,2,1]]))

#Dobrze
