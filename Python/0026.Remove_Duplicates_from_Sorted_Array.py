from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i, j = 0, 1

        while i <= j and j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1

            j += 1

        return i + 1


if __name__ == '__main__':
    s = Solution()

    print(s.removeDuplicates([1, 1, 2]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
