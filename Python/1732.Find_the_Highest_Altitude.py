from typing import List
from itertools import accumulate

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # use itertools' accumulate function to compute the cumulative sum of gain, starting from 
        # an initial altitude of 0 and return the maximum altitude reached during the journey
        return max(accumulate(gain, initial = 0))

if __name__ == '__main__':
    s = Solution()
    print(s.largestAltitude([-5,1,5,0,-7]))
    print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))