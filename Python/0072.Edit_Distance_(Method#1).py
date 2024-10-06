class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # get the lengths of the input words
        m, n = len(word1), len(word2)
        
        # initialize a matrix for dynamic programming, dp[i][j] will hold the 
        # minimum edit distance between word1[0:i] and word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # fill the first column of the dp matrix, dp[i][0] represents the distance
        # from word1[0:i] to an empty word2
        for i in range(1, m + 1):
            # requires i deletions to convert word1[0:i] to ""
            dp[i][0] = i
        
        # fill the first row of the dp matrix, dp[0][j] represents the distance 
        # from an empty word1 to word2[0:j]
        for j in range(1, n + 1):
            # requires j insertions to convert "" to word2[0:j]
            dp[0][j] = j
        
        # fill in the rest of the dp matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # check if the current characters from both words are the same
                if word1[i - 1] == word2[j - 1]:
                    # no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # calculate the minimum edit distance considering all three operations
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,     # insertion: add word2[j-1] to word1
                        dp[i - 1][j] + 1,     # deletion: remove word1[i-1]
                        dp[i - 1][j - 1] + 1  # replacement: replace word1[i-1] with word2[j-1]
                    )
        
        # the bottom-right cell of the dp matrix contains the minimum edit distance
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))