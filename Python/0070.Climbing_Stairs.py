class Solution:
    def climbStairs(self, n: int) -> int:
        # if there are 0 or 1 step, there's only one way to climb, so return 1
        if n == 0 or n == 1:
            return 1
        
        # initialize an array to store the number of ways to climb to each step
        dp = [0] * (n + 1)
        # there is only one way to reach the 0th and 1st step
        dp[0] = dp[1] = 1
        
        # iterate from step 2 to step n
        for i in range(2, n + 1):
            # number of ways to reach the current step is the sum of ways to reach previous two steps
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # return the number of ways to climb to the nth step
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))