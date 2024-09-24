from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort the potions list to enable binary search
        potions.sort()
        # get the number of potions
        potion_count = len(potions)
        # initialize a list to hold the counts of successful pairs
        successful_pairs_count = []
        
        # iterate over each spell to find successful pairs
        for spell in spells:
            # initialize the binary search range
            low, high = 0, potion_count - 1
            
            # perform binary search to find the number of successful pairs,
            # continue while the search range is valid
            while low <= high: 
                # calculate the midpoint index
                mid = (low + high) >> 1
                # check if the current potion and spell meet the success criteria
                if potions[mid] * spell >= success:
                    # if yes, search in the left half (potentially more successful pairs)
                    high = mid - 1
                else:
                    # if no, search in the right half (higher potions needed)
                    low = mid + 1
            
            # append the count of successful pairs for the current spell,
            # all potions from index 'low' to the end are successful
            successful_pairs_count.append(potion_count - low)  
        
        # return the list of successful pairs count for each spell
        return successful_pairs_count

if __name__ == '__main__':
    s = Solution()
    print(s.successfulPairs([5,1,3], [1,2,3,4,5], 7))
    print(s.successfulPairs([3,1,2], [8,5,8], 16))