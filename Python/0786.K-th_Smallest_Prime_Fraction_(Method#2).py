from typing import List
import bisect

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # initialize the search space
        left, right, n = 0, 1, len(arr)
        # binary search loop
        while True:
            # calculate the midpoint of the interval
            mid = (left + right) / 2
            # calculate the border points using binary search
            border = [bisect.bisect(arr, arr[i]/mid) for i in range(n)]
            # count the number of fractions smaller than or equal to mid
            curr = sum(n-j for j in border)
            # adjust the search interval based on the count
            if curr > k:
                right = mid
            elif curr < k:
                left = mid
            # if we've found exactly k fractions
            else:
                # return the fraction with the maximum value, as per the problem statement
                return max(
                    [[arr[i], arr[j]] for i, j in enumerate(border) if j < n],
                    key=lambda x: x[0] / x[1],
                )

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallestPrimeFraction([1,2,3,5], 3))
    print(s.kthSmallestPrimeFraction([1,7], 1))