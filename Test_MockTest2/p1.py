def f(player1, player2):

    def calculate_points(hand):
        total = 0
        for card in hand:
            if card in "AKQJT":
                total += 10 
            else:
                total += int(card)
        return total
    
    sum1 = calculate_points(player1)
    sum2 = calculate_points(player2)
    
    return sum1 >= sum2

print(f("AJ972", "AQT72"))
print(f("9532", "K8"))

"""
Gdy mamy do obliczenia dwa wyniki w jednej funkcji to opłaca się
zdefiniować funkcję liczącą o dowolnej nazwie, aby użyć wartości
wystarczy dodać wartości jak tu czyli zdefiniować atrybut sum1 i sum2
i porównać je do napisanej funkcji

"""