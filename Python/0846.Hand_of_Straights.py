from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # count occurrences of each card
        card_count = Counter(hand)
        # sort the cards
        keys = sorted(card_count)
        
        # iterate over each card
        for key in keys:
            # if there are remaining cards of this type
            if card_count[key] > 0:
                # try to form a group of size groupSize starting from this card
                for i in range(groupSize-1, -1, -1):
                    # if the next card in the group is not available, return False
                    if key + i not in card_count:
                        return False
                    
                    # reduce the count of the next card in the group
                    card_count[key + i] -= card_count[key]
                    
                    # if we have used more cards than available, return False
                    if card_count[key + i] < 0:
                        return False
        
        # if we successfully formed all groups, return True
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 5))
    print(s.isNStraightHand([1,2,3,4,5], 4))
    print(s.isNStraightHand([8,8,9,7,7,7,6,7,10,6], 2))