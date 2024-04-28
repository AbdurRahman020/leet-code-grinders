class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s) 
        for i in range(n//2):
            s[i], s[-i-1] = s[-i-1], s[i]

if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
    print(s.reverseString(["H","a","n","n","a","h"]))