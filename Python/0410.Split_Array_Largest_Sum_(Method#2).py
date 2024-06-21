from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # initialize a 2D list dp with infinity values
        dp = [[float("inf") for _ in range(len(nums))] for _ in range(m)]
        # base case: only one group, sum is just the first element
        dp[0][0] = nums[0]

        # fill the first row of dp: sum of prefix elements
        for c in range(1, len(nums)):
            dp[0][c] = dp[0][c - 1] + nums[c]

        # fill dp table for more than one group
        for r in range(1, m):
            for c in range(r, len(nums)):
                # initialize dp[r][c] as the minimum of all possible maximum sums
                dp[r][c] = min(
                    [
                        max(dp[r - 1][prev_column], dp[0][c] - dp[0][prev_column])
                        for prev_column in range(r - 1, c)
                    ]
                )

        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
    print(s.splitArray([1,2,3,4,5], 2))
    print(s.splitArray([2,3,1,1,1,1,1], 5))
    print(s.splitArray([7,6,5,4,3,2,1], 2))