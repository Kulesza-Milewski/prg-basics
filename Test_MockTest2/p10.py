def f(array):
    min_val = float('inf')
    min_row = -1
    min_col = -1
    
    rows = len(array)
    cols = len(array[0])
    
    for r in range(rows):
        for c in range(cols):
            if array[r][c] < min_val:
                min_val = array[r][c]
                min_row = r
                min_col = c
                
    return min_row == min_col

print(f([[7,8],[5,3],[9,4]]))     
print(f([[7,8,5,3],[9,4,2,6]]))    