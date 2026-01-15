def f(arr):
    a, b = set(arr)

    return a if arr.count(a) == 1 else b

print(f([7,7,7,7,7,10,7,7]))