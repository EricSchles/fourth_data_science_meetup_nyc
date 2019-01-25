import random
import math
import itertools
import collections
import code

# Stolen from here: https://github.com/fluentpython/example-code/blob/master/01-data-model/frenchdeck.py
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
def generate_conditional_deck_joint_probability(deck, n):
    total_cases = [elem for elem in itertools.combinations(deck, 2)] 
    probabilities = {}.fromkeys(total_cases, 0)
    for _ in range(n):
        probabilities[random.choice(total_cases)] += 1
    probabilities = {case:probabilities[case]/n for case in probabilities}
    cases_of_interest = {}
    for case in probabilities:
        first_condition = case[0].suit == "diamonds"
        second_condition = case[0].rank == '3'
        third_condition = case[1].suit == "hearts"
        if first_condition and second_condition and third_condition:
            cases_of_interest.update({case: probabilities[case]})
    return sum(list(cases_of_interest.values()))

   
deck = FrenchDeck()
probabilities = generate_conditional_deck_joint_probability(deck, 999999)
print(probabilities)
