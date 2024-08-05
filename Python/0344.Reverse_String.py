from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # get the length of the list
        n = len(s)
        
        # iterate only up to the middle of the list
        for i in range(n//2):
            # swap the element at index i with the element at index -i-1
            s[i], s[-i-1] = s[-i-1], s[i]

if __name__ == '__main__':
    s = Solution()
    s1 = ["h","e","l","l","o"]
    s.reverseString(s1)
    print(s1)
    s2 = ["H","a","n","n","a","h"]
    s.reverseString(s2)
    print(s2)