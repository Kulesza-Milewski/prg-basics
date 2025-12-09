def f(kod):
    # kod to np. string "1236"
    if len(kod) != 4: return False
    
    c1 = int(kod[0])
    c2 = int(kod[1])
    c3 = int(kod[2])
    c4 = int(kod[3])
    
    reszta = (c1 + c2 + c3) % 7
    return reszta == c4

if __name__ == "__main__":
    print(f(1423))