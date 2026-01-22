def f(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ['+', '-']:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            
            stack.append(result)
            
    return stack[0]

print(f("2 3 +"))           
print(f("2 6 + 4 5 - +"))   
print(f("11 7 + 15 - 14 +"))