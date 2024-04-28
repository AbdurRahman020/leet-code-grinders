class Solution(object):
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('aba'))
    print(s.repeatedSubstringPattern('abab'))
    print(s.repeatedSubstringPattern('abcabcabcabc'))