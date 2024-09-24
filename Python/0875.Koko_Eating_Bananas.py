from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define a helper function to check if a given speed is sufficient
        def speedChecker(speed):
            # initialize the total hours needed to zero
            total_hours = 0
            # iterate over each pile of bananas
            for pile in piles:
                # calculate hours needed for this pile at the given speed
                total_hours += ceil(pile / speed)
            
            # return True if total hours is within the limit
            return total_hours <= h
        
        # set the min and max possible speed to 1 banana per hour and largest pile of 
        # bananas respectively 
        min_speed, max_speed  = 1, max(piles)
        
        # perform binary search to find the minimum speed
        # continue while the search range is valid
        while min_speed < max_speed:
            # calculate the midpoint speed
            curr_speed = (min_speed + max_speed) >> 1
            # check if the current speed is sufficient
            if speedChecker(curr_speed):
                # if yes, narrow the search to lower speeds
                max_speed = curr_speed
            else:
                # if no, increase the minimum speed
                min_speed = curr_speed + 1
        
        # return the minimum speed found
        return min_speed

if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))
    print(s.minEatingSpeed([30,11,23,4,20], 5))
    print(s.minEatingSpeed([30,11,23,4,20], 6))