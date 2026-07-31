from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # get the length of the input list
        n = len(nums)

        # check if the list has only one number
        if n == 1:
            # if so, return 0 as that single number is a peak
            return 0

        # check if the first number is greater than the second
        if nums[0] > nums[1]:
            # if true, the first number is a peak, return its index (0)
            return 0

        # check if the last number is greater than the second last
        if nums[-1] > nums[-2]:
            # if true, the last number is a peak, return its index (n-1)
            return n - 1

        # set the search range, avoiding the first and last numbers
        low, high = 1, n-2
        # continue searching while the range is valid
        while low <= high:
            # calculate the middle index using bitwise right shift
            mid = (low + high) >> 1

            # check if the mid number is greater than its neighbors
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                # if true, return mid index as it is a peak
                return mid

            # if the mid number is greater than the left neighbor
            if nums[mid - 1] < nums[mid]:
                # move the search range to the right side (search for peaks to the right)
                low = mid + 1
            # if the mid number is not greater than the left neighbor
            else:
                # move the search range to the left side (search for peaks to the left)
                high = mid - 1

        # return -1 if no peak is found
        return -1


if __name__ == '__main__':
    s = Solution()

    print(s.findPeakElement([1, 2, 3, 1]))
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
