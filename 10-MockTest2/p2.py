def f(arr):
    x = 0
    
    for nr in arr:
        if arr[x] == arr[x+1]:
            nr += 1
        elif arr[x] != arr[x+1]:
            return arr[x+1]

f([7,7,7,7,7,5,7,7])