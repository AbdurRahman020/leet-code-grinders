from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initialize the result variable to store the single number
        result = 0
        
        # iterate through each number in the list
        for num in nums:
            # XOR operation (^) with the current number and the result
            # this operation toggles bits such that they become set if 
            # they are different and unset if they are the same
            result ^= num
        
        # after iterating through all numbers, the result will be the single number
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))
    print(s.singleNumber([1]))