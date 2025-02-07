class Solution:
    def validPalindrome1(self, s: str) -> bool:
        def isPalindrome(s: str):
            return s == s[::-1]
        
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])
            
            l += 1
            r -= 1
        
        return True
    
    def validPalindrome2(self, s: str) -> bool:
        mid = (1 + len(s)) // 2
        
        l, r = s[:mid], s[-mid:][::-1]
        
        if l != r:
            for i in range(mid):
                if l[i] != r[i]:
                    return l[i+1:] == r[i: mid-1] or l[i:mid-1] == r[i+1:]
        
        return True

if __name__ == '__main__':
    s = Solution()
    
    print(s.validPalindrome1("aba"))
    print(s.validPalindrome1("abca"))
    print(s.validPalindrome1("abc"))
    
    print(s.validPalindrome2("aba"))
    print(s.validPalindrome2("abca"))
    print(s.validPalindrome2("abc"))