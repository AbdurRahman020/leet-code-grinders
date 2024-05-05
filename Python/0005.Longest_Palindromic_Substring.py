class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check if the string is already a palindrome
        if s == s[::-1]:
            return s
        
        # initialize the result to store the longest palindrome substring found
        result = []
        # initialize the length of the result substring and the length of the input string
        len_result, n = 0, len(s)
        
        # iterate through the string characters
        for i in range(n):
            # expand around the current character for odd-length palindromes
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len_result:
                    # update the result substring if a longer palindrome is found
                    result = s[left: right + 1]
                    # update the length of the result substring
                    len_result = right - left + 1
                # expand the palindrome window
                left -= 1
                right += 1
            
            # expand around the current and next character for even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len_result:
                    # update the result substring if a longer palindrome is found
                    result = s[left: right + 1]
                    # update the length of the result substring
                    len_result = right - left + 1
                # expand the palindrome window
                left -= 1
                right += 1
        
        # return the longest palindrome substring
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))