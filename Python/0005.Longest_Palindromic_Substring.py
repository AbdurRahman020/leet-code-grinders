class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        result = []
        len_result, n = 0, len(s)

        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len_result:
                    result = s[left: right + 1]
                    len_result = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len_result:
                    result = s[left: right + 1]
                    len_result = right - left + 1
                left -= 1
                right += 1
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))