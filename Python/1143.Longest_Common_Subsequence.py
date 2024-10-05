class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if both strings are identical, the LCS is the length of either string
        if text1 == text2:
            return len(text1)
        
        # get the lengths of both strings
        m, n = len(text1), len(text2)
        
        # initialize a 2D list (dp) to store the lengths of the LCS for substrings 
        # of text1 and text2
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # fill the dp table using a bottom-up approach
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # if the current characters match, increment the length of the LCS 
                # by 1 from the previous characters match
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    # if they don't match, take the maximum value from either ignoring 
                    # the current character of text1 or text2
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        
        # the bottom-right cell of the dp table contains the length of the LCS for the
        # entire lengths of both strings
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))
    print(s.longestCommonSubsequence("abc", "abc"))
    print(s.longestCommonSubsequence("abc", "def"))