def f(n):
    
    a, b = 0, 1

    if n <= 0:
        return []
    elif n == 1:
        return [a]
    
    else:
        ciąg = [a, b]
        for _ in range(2, n):
            a, b = b, a + b
            ciąg.append(b)
        return ciąg
