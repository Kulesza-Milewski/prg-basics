def f(x, y):
    if x > 0 and y > 0: 
        return "I ćwiartka"
    elif x < 0 and y > 0: 
        return "II ćwiartka"
    elif x < 0 and y < 0: 
        return "III ćwiartka"
    elif x > 0 and y < 0: 
        return "IV ćwiartka"
    elif x == 0 and y == 0: 
        return "Punkt (0,0)"
    else: return "Na osi"

if __name__ == "__main__":
    print(f(15, 42))