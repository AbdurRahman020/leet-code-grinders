from itertools import combinations
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # create a list of numbers from 1 to 9
        nums = [i for i in range(1, 10)]
        
        # generate all possible combinations of k numbers from the nums list
        combo = combinations(nums, k)
        
        # filter combinations to keep only those whose sum equals n
        return [c for c in combo if sum(c) == n]

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(4, 1))