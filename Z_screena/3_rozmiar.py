def f(r1,r2):
    hierarchia = ["S", "M", "L"]
    if r1 not in hierarchia or r2 not in hierarchia:
        return "Błąd rozmiaru"
    
    ind1 = hierarchia.index(r1)
    ind2 = hierarchia.index(r2)

    if ind1 > ind2:
        return r1
    else:
        return r2
       
if __name__ == "__main__":
    print(f("M", "S"))