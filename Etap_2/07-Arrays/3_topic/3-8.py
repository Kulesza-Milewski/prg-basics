arr = [2, 6, 4, 9, 7]

def star(array):
    for n in array:
        stars = '*' * n
        print(f"{n}: {stars}")

print(star(arr))
