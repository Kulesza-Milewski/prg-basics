def f(mnumbers):
    dozwolone = ["A", "a", "B", "b", "C", "c", "D", "d"]

    for i in range (1, 8):
        dozwolone.append(str(i))

    pierwszy = ["+", "-"] + dozwolone
    results = []
    count = 0

    for i in range(len(mnumbers)):
        numb = mnumbers[i][::-1]
        for j in range(len(numb)):
            if j == len(numb)-1:
                if numb[j] not in pierwszy:
                    break
                else:
                    count += 1
                    results.append(numb[::-1])
                    break
            else:
                if numb[j] not in dozwolone:
                    break
                else:
                    continue
    
    return len(results)


print(f(["A15","-31","7abC","+D1","-g4"])) #returns 4
print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"])) #returns 2 