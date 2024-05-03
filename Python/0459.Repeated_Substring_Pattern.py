class Solution(object):
    def repeatedSubstringPattern(self, s: str) -> bool:
        # check if the string is present in itself concatenated with itself, 
        # excluding the first and last character
        # if it is, then it means the string can be formed by repeating a substring
        return s in s[1:] + s[:-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('aba'))
    print(s.repeatedSubstringPattern('abab'))
    print(s.repeatedSubstringPattern('abcabcabcabc'))