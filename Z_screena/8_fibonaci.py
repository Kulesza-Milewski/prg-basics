def f(liczba):
    a, b = 0, 1
    while a < liczba:
        a, b = b, a + b
    return a == liczba

if __name__ == "__main__":
    print(f(1423))