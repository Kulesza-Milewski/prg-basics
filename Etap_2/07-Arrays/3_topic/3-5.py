arr = [15, 8, 31, 47, 2, 19]

def f(array):
    all = 0
    for number in array:
        all += number
        result = all/len(array)
    return array, result

print(f(arr))