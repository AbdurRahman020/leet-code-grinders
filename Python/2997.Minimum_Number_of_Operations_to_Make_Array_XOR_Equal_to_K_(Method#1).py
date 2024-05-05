from operator import xor
from functools import reduce

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        # calculate the XOR of all elements in 'nums'
        # using the reduce function and the xor operator
        # then calculate the XOR between the XOR result and 'k', 
        # after that count the number of set bits (1s) in the result
        # once done, return the calculated minimum number of operations needed
        return (reduce(xor, nums)^k).bit_count()

if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([2,1,3,4], 1))
    print(s.minOperations([2,0,2,0], 0))