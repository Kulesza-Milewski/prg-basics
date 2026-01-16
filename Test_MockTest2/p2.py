"""def f(arr):
    a = arr[0]
    b = None
    n1 = 1
    n2 = 1
    count_a = 0
    count_b = 0
    
    for liczba in arr:
        if liczba == a:
            continue
        else:
            b += liczba

    while n1 < len(arr)+1:
        if a == arr[n1]:
            count_a += 1
        else:
            continue
        n1 += 1
    
    while n2 < len(arr)+1:
        if b == arr[n2]:
            count_b += 1
        else:
            continue
        n2 += 1

    if count_a > count_b:
        return b
    else:
        return a

print(f([1,7,7,7,7,7,7,7]))"""


# Gemini:

def f(arr):
    unikalna_liczba = set(arr)

    for numer in unikalna_liczba:

        if arr.count(numer) == 1:
            return numer, unikalna_liczba


print(f([1,7,7,7,7,7,7,7]))

#Błędy 

"""
Ogólne zrozumienie zadania i chęć rozpisywania w bardzo długi sposób

"""
