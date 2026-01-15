arr = [-15, 8, -31, 47, -2, 19]

def f(array):
    max = array[0]
    min = array[0]

    for i in array:
        if i > max:
            max = i

        if i < min:
            min = i
            
    return max, min

print(f(arr))