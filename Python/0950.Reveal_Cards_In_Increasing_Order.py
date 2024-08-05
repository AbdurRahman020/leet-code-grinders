from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # sort the deck in descending order
        deck_reverse = sorted(deck, reverse=True)
        # create a deque to store the new deck
        new_deck = deque()
        
        # iterate over each card in the reversed deck
        for card in deck_reverse:
            # if the new deck has more than one card, rotate it to the right by 1 position
            if len(new_deck) > 1:
                new_deck.rotate(1)
            
            # add the current card to the left end of the new deck
            new_deck.appendleft(card)
        
        # convert the deque to a list and return the new deck
        return list(new_deck)

if __name__ == '__main__':
    s = Solution()
    print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
    print(s.deckRevealedIncreasing([1,1000]))