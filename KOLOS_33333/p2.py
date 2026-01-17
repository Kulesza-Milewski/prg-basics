def f(expression):
    stack = []
    # Dzielimy napis na elementy (spacjami)
    tokens = expression.split()
    
    for token in tokens:
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        else:
            # Jeśli nie jest znakiem, to jest liczbą
            stack.append(int(token))
            
    return stack[0]