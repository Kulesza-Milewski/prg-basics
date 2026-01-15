def f(amount_to_pay):
    amout = 0

    while amount_to_pay > 0:

        if amount_to_pay >= 5:
            amount_to_pay -= 5
            amout += 1
        elif amount_to_pay < 5 and amount_to_pay >= 2:
            amount_to_pay -= 2
            amout += 1
        else:
            amount_to_pay -= 1
            amout += 1

    return amout

print(f(8))

# Błędy: 

"""
1. Zapomniałem o wywołaniu: return
2. Nie wykorzystałem pętli while 
    - if wykonuje się tylko raz
    - while wykonuje się do skutku
"""
