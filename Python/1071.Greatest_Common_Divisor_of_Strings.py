from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if concatenation of str1 and str2 doesn't match concatenation of 
        # str2 and str1, then there's no common divisor string.
        if str1 + str2 != str2 + str1:
            return ''
        # getting lengths of both strings
        n1, n2 = len(str1), len(str2)
        
        # return the substring of str1 from index 0 to the greatest common divisor
        return str1[:gcd(n1, n2)]

if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))
    print(s.gcdOfStrings("ABABAB", "ABAB"))
    print(s.gcdOfStrings("LEET", "CODE"))