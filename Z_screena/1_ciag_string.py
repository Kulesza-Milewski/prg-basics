def f(n):
    wynik = ""
    for i in range(1, n+1):
        wynik += str(i)
    return wynik

if __name__ == "__main__":
    print(f(7))