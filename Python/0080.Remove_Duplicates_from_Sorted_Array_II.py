from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        j = 2
        for i in range(2, n):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
