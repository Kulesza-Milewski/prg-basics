def f(array2D):
    n = len(array2D)
    for nr in range(n):
        row_sum = sum(array2D[nr])
        col_sum = sum(row[nr] for row in array2D)

        if row_sum != col_sum:
            return False
        
    return True



if __name__ == "__main__":


    matrix1 = [[3, 7, 2],[4, 2, 5],[5, 2, 1]]
    print(f(matrix1)) 
    print(len(matrix1))

    matrix2 = [[3, 7, 2],[4, 2, 5],[9, 2, 1]]
    print(f(matrix2))