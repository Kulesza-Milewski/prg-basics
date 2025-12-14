arr = [15, 8, 31, 47, 2, 19]

def f(array):
    all = 0
    x = 0
    while x < len(array):
        all += array[x]
        x += 1
        result = all/len(array)
    return array, result

print(f(arr))