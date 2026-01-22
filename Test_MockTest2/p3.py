def f(array2D):
    rows = len(array2D)
    cols = len(array2D[0])
    
    for i in range(rows):
        row_sum = sum(array2D[i])
        col_sum = sum(row[i] for row in array2D)
        
        if row_sum != col_sum:
            return False
            
    return True

print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))