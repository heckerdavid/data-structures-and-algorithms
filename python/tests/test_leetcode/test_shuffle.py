from leet_code.shuffle import card_shuffle

def test_import():
    assert card_shuffle

def test_shuffle():
    unshuffled_deck = [i for i in range(52 + 1)]
    deck = [i for i in range(52 + 1)]

    card_shuffle(deck)

    difference_count = 0
    for i, card in enumerate(deck):
        if unshuffled_deck[i] != card:
            difference_count +=1

    assert difference_count > 25
