from typing import List


class Solution:
    def subsetXORSum1(self, nums: List[int]) -> int:
        def backtrack(i, xor_total):
            # base case: when the index reaches the length of nums, return the XOR total
            if i == len(nums):
                return xor_total
            # recursive step: for each element in nums, we have two choices,
            # either include it in the subset or exclude it
            # so, recursively call backtrack with both choices and XOR the result
            return backtrack(i+1, xor_total ^ nums[i]) + backtrack(i+1, xor_total)

        # start the backtracking from the beginning (index 0) with XOR total
        # initialized to 0
        return backtrack(0, 0)

    def subsetXORSum2(self, nums: List[int]) -> int:
        # initialize a variable to store the cumulative XOR sum
        xor_sum = 0
        # iterate through each number in the input list
        for num in nums:
            # perform bitwise OR operation to update the cumulative XOR sum
            xor_sum |= num

        # calculate the final result by left shifting the XOR sum by (len(nums) - 1)
        # positions, this is equivalent to multiplying the XOR sum by 2^(len(nums) - 1)
        # because each element in the subset can either be included or excluded,
        # contributing to 2^(len(nums)) subsets and since we want XOR sum, we need
        # to double the sum (equivalent to left shifting by 1) but since we also want
        # to exclude the empty subset, we left shift by (len(nums) - 1) instead of
        # len(nums) to exclude the contribution of the empty subset
        return xor_sum << (len(nums) - 1)


if __name__ == '__main__':
    s = Solution()

    print(s.subsetXORSum1([1, 3]))
    print(s.subsetXORSum1([5, 1, 6]))
    print(s.subsetXORSum1([3, 4, 5, 6, 7, 8]))

    print(s.subsetXORSum2([1, 3]))
    print(s.subsetXORSum2([5, 1, 6]))
    print(s.subsetXORSum2([3, 4, 5, 6, 7, 8]))
