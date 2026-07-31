from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # initialize i to point to the last element of nums1 (excluding the zeros)
        i = m - 1
        # initialize j to point to the last element of nums2
        j = n - 1
        # initialize k to point to the last position in nums1 where merged elements will go
        k = m + n - 1

        # continue until all elements in nums2 are processed
        while j >= 0:
            # check if the current element in nums1 is greater than the current element in nums2
            if i >= 0 and nums1[i] > nums2[j]:
                # place the larger element at the current position k in nums1
                nums1[k] = nums1[i]
                # move the pointer i left to the next element in nums1
                i -= 1
            # if nums2[j] is greater or if nums1 is exhausted
            else:
                # place the current element from nums2 at position k in nums1
                nums1[k] = nums2[j]
                # move the pointer j left to the next element in nums2
                j -= 1

            # move the pointer k left to the next position for the next insertion
            k -= 1


if __name__ == '__main__':
    s = Solution()
    n1 = [1, 2, 3, 0, 0, 0]
    s.merge(n1, 3, [2, 5, 6], 3)
    print(n1)
