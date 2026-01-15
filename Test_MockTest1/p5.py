def f(binary_number):
    n = 0

    while n < len(binary_number):
        if binary_number[n] != '1' and binary_number[n] != '0':
            return False
        else:
            n += 1

    return True

print(f("101101"))


#Błędy:

"""
1. Zapomniałem że elementy są stringami a nie intami i zapisałem 1 zamianst '1'


"""