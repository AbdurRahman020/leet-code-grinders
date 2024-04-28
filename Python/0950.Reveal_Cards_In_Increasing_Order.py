from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck_reverse = sorted(deck, reverse=True)
        new_deck = deque()
        
        for card in deck_reverse:
            if len(new_deck) > 1:
                new_deck.rotate(1)
            new_deck.appendleft(card)
        
        return list(new_deck)

if __name__ == '__main__':
    s = Solution()
    print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
    print(s.deckRevealedIncreasing([1,1000]))