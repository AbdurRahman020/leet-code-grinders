from typing import List
from operator import xor
from functools import reduce

class Solution:
    def minOperations1(self, nums: List[int], k: int) -> int:
        # calculate the XOR of all elements in 'nums'
        # using the reduce function and the xor operator
        # then calculate the XOR between the XOR result and 'k', 
        # after that count the number of set bits (1s) in the result
        # once done, return the calculated minimum number of operations needed
        return (reduce(xor, nums)^k).bit_count()
    
    def minOperations2(self, nums: List[int], k: int) -> int:
        # calculate the XOR of all elements in nums
        xor_result = 0
        for n in nums:
            xor_result ^= n
        
        # calculate the XOR of the result and k
        # and count the number of set bits in the XOR result,
        # which represents the minimum number of operations
        # needed to transform xor_result to k
        return bin(xor_result ^ k).count('1')


if __name__ == '__main__':
    s = Solution()
    
    print(s.minOperations1([2,1,3,4], 1))
    print(s.minOperations1([2,0,2,0], 0))
    
    print(s.minOperations2([2,1,3,4], 1))
    print(s.minOperations2([2,0,2,0], 0))
