def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
        
        return True
    return False
    
print(compare([5,3,1] ,  [5,3,1]))