def f(player1, player2):
    teens = ['A', 'K', 'Q', 'J', 'T']

    def scores(hand):
        score = 0
        for card in hand:
            if card in teens:
                score += 10
            else:
                score += int(card)
        return score
    return scores(player1) >= scores(player2)

print(f("9532","K8"))