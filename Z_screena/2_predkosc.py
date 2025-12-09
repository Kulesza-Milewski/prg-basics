def f(km):

    ms = km / 3.6

    return f"{km} km/h to {ms:.2f} m/s"

if __name__ == "__main__":
    print(f(100))