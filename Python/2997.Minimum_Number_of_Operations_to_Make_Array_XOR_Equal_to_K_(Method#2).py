class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations needed to transform the XOR result of the elements in nums to k.

        :param nums: The list of integers.
        :type nums: list[int]
        :param k: The target XOR value.
        :type k: int
        
        :return: The minimum number of operations.
        :rtype: int
        """
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