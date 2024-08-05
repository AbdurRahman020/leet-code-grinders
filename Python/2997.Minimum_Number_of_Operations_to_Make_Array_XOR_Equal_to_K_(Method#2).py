from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
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
    print(s.minOperations([2,1,3,4], 1))
    print(s.minOperations([2,0,2,0], 0))