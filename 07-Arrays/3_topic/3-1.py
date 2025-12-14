# An array contains integer numbers: 34,7,19,4,21,8. 
# Create a program that calculates and prints the number of even values in the array. 
# Use the ‘while’ loop statement.

arr = [34,7,19,4,21,8]

x = 0
while x < len(arr): 
    if arr[x] % 2 == 0:
        print(arr[x])
    x += 1
