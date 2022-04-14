# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.
import random

def perfect_random(k):
    return random.choice(range(0, k + 1))


def card_shuffle(deck):
    for idx, card in enumerate(deck):
        swap_idx = perfect_random(52)

        deck[idx], deck[swap_idx] = deck[swap_idx], deck[idx]

    return deck
