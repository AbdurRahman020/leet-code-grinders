from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        # generate a list of perfect squares up to the square root of n
        perfect_squares = [x**2 for x in range(1, int(sqrt(n))+1)]
        
        # initialize a dp array with all values set to n (maximum possible steps)
        dp = [n for _ in range(n+1)]
        # base case: 0 steps needed to reach 0
        dp[0] = 0
        
        # iterate through all numbers from 1 to n
        for i in range(1, n+1):
            # iterate through all perfect squares smaller than or equal to i
            for square in perfect_squares:
                # if subtracting a perfect square from i results in a non-negative number
                if i - square >= 0:
                    # update the dp array by taking the minimum of its current value and 1 + dp[i - square]
                    dp[i] = min(dp[i], 1 + dp[i - square])
        
        # return the result for n
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(13)) 