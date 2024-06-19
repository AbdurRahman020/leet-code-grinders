from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # if it's impossible to form m bouquets of size k from the flowers
        # available then return -1
        if m * k > len(bloomDay):
            return -1
        
        # binary search initialization
        left, right = min(bloomDay), max(bloomDay)
        min_days_required = -1
        
        # helper function to calculate the number of bouquets that can be made
        # with flowers blooming on or before the given day `current_day`
        def calculateNumOfBouquets(current_day):
            # initialize to count consecutive bloomed flowers
            consecutive_flowers = 0
            # initialize to count total bouquets formed
            num_of_bouquets = 0
            
            # iterate through each bloom day in bloomDay list
            for d in bloomDay:
                # check if the flower blooms on or before current_day
                if d <= current_day:
                    # tncrement consecutive flowers count
                    consecutive_flowers += 1
                    # if we have enough consecutive flowers to form a bouquet (k flowers),
                    # increment bouquet count and reset consecutive_flowers
                    if consecutive_flowers == k:
                        num_of_bouquets += 1
                        consecutive_flowers = 0
                else:
                    # reset consecutive_flowers if flower blooms after current_day
                    consecutive_flowers = 0
            
            # return the total number of bouquets formed
            return num_of_bouquets
        
        # binary search loop
        while left <= right:
            mid = (left + right ) // 2
            
            # if we can form at least m bouquets with flowers blooming on or before
            # mid days, then it's a valid candidate for minimum days required
            if calculateNumOfBouquets(mid) >= m:
                min_days_required = mid
                # search in the left half for potentially smaller days
                right = mid - 1
            else:
                # search in the right half for potentially larger days
                left = mid + 1
        
        # after binary search completes, min_days_required will hold the minimum
        # number of days required to produce m bouquets of k flowers each
        return min_days_required
    
if __name__ == '__main__':
    s = Solution()
    print(s.minDays([1,10,3,10,2], 3, 1))
    print(s.minDays([1,10,3,10,2], 3, 2))
    print(s.minDays([7,7,7,7,12,7,7], 2, 3))