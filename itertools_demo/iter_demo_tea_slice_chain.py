import itertools as it

def cut(deck, n):
    """Return an iterator over a deck of cards cut at index `n`."""
    deck1, deck2 = it.tee(deck, 2)
    top = it.islice(deck1, n)
    bottom = it.islice(deck2, n, None)
    return it.chain(bottom, top)

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']

cards = it.product(ranks, suits)

cards = cut(cards, 26)

print(list(cards))
