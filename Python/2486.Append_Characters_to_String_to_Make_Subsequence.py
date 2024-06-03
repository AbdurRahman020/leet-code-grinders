class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # get the lengths of both strings
        n, m = len(s), len(t)
        # initialize pointers i for s and j for t
        i, j = 0, 0
        
        # iterate through both strings
        while i < n and j < m:
            # if characters at current positions match
            if s[i] == t[j]:
                # move pointer for t
                j += 1
             # move pointer for s
            i += 1
        
        # after the loop, j represents the number of characters in t that were found in s
        # so, the number of characters to append from t to s is the remaining characters in t (m - j)
        return m - j
    
if __name__ == '__main__':
    s = Solution()
    print(s.appendCharacters("coaching", "coding"))
    print(s.appendCharacters("abcde", "a"))
    print(s.appendCharacters("z", "abcde"))