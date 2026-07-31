from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = Solution()
    n1 = [1, 2, 3, 4, 5, 6, 7]
    s.rotate1(n1, 3)
    print(n1)

    n2 = [-1, -100, 3, 99]
    s.rotate2(n2, 2)
    print(n2)
