def f(start, stop):
    suma = 0
    for i in range(start, stop + 1):
        if i % 3 == 0:
            suma += i
    return suma

if __name__ == "__main__":
    print(f(1, 10))