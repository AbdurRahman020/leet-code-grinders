class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a 2D list (matrix) `dp` with dimensions m x n
        # initialize the first row and first column with 1s, since there's 
        # only one way to reach any cell in the first row (only move right)
        # and any cell in the first column (only move down)
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)] 
        
        # loop through the matrix starting from cell (1, 1) to (m-1, n-1)
        for i in range(1, m):
            for j in range(1, n):
                # the number of ways to reach cell (i, j) is the sum of the ways to 
                # reach the cell directly above it (i-1, j) and the cell directly
                # to the left of it (i, j-1)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return the value in the bottom-right cell of the matrix, which contains
        # the total number of unique paths to reach that cell
        return dp[-1][-1]
        
        # one line implementation
        # return math.comb(m+n-2, m-1)

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
    print(s.uniquePaths(3, 2))