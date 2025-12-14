arr =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

for i in range(0, len(arr)):
    arr[i][i] = 1

for row in arr:
    for number in row:
        print(number, end=" ")
    print()