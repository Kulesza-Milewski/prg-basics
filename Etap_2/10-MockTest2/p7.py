def f(array):
    for password in array:
        count = 0
        if 4 < len(password) < 12:
            for sumbol in range(len(password)):
                corect = ['_', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                if sumbol != sumbol.lower() or sumbol is not corect:
                    return False
            count += 1 
            return count
        
print()