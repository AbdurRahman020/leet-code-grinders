from collections import Counter

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))
    print(s.isAnagram('car', 'rat'))