class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # get the lengths of the input words
        m, n = len(word1), len(word2)
        
        # initialize a matrix for dynamic programming, dp[i][j] will hold the 
        # minimum edit distance between word1[i:] and word2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # fill the last row of the dp matrix, this represents the distance from 
        # the empty suffix of word1 to word2[j:]
        # dp[m][i] = number of characters left in word2 to delete
        for i in range(n + 1):
            # requires (n-i) deletions
            dp[m][i] = n - i
        
        # fill the last column of the dp matrix, this represents the distance from
        # word1[i:] to the empty suffix of word2
        # dp[j][n] = number of characters left in word1 to delete
        for j in range(m + 1):
            # requires (m - j) insertions
            dp[j][n] = m - j
        
        # fill in the rest of the dp matrix, starting from the bottom-right corner
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # check if the current characters from both words are the same
                if word1[i] == word2[j]:
                    # no operation needed, carry over the count
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # calculate the minimum edit distance considering insertion, deletion, and replacement
                    dp[i][j] = min(
                        dp[i + 1][j],      # deletion: remove word1[i]
                        dp[i][j + 1],      # insertion: add word2[j] to word1
                        dp[i + 1][j + 1]   # replacement: replace word1[i] with word2[j]
                    ) + 1                  # add 1 for the current operation performed
                            
        # the top-left cell of the dp matrix contains the minimum edit distance
        return dp[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))