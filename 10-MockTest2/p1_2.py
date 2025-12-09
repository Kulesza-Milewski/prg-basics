def f(player1, player2):

    def calculate_score(hand):
        score = 0
        high_cards = {'A', 'K', 'Q', 'J', 'T'}

        for card in hand:
            if card in high_cards:
                score += 10
            else:
                score += int(card)
        return score
    
    return calculate_score(player1) >= calculate_score(player2)

if __name__ == "__main__":
    print(f("AJ972", "AQT72"))
    print(f("9532", "K8"))