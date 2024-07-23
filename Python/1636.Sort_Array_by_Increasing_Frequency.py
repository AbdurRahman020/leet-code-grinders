from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # count frequencies of each number using Counter from collections
        freq = Counter(nums)
        
        # sort nums based on two criteria:
        #   i. increasing order of frequency (freq[x])
        #  ii. decreasing order of the number itself (-x)
        nums.sort(key = lambda x: (freq[x], -x))
        
        # return the sorted nums list
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort([1,1,2,2,2,3]))
    print(s.frequencySort([2,3,1,3,2]))
    print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1]))