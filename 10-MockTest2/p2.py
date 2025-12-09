def f(arr):
    a, b = set(arr)

    return a if arr.count(a) == 1 else b

if __name__ == "__main__":
    print(f([7, 7, 7, 7, 7, 5, 7, 7]))  
    print(f([1, 1, 2]))