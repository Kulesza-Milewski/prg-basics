def f(godz):

    czas, pora = godz.split()
    h, m = map(int, czas.split(':'))
    if pora.lower() == 'pm' and h != 12:
        h += 12
    elif pora.lower() == 'am' and h == 12:
        h = 0

    return f"{h:02d}:{m:02d}"

if __name__ == "__main__":
    print(f("02:30 pm"))