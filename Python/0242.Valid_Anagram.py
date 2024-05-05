from collections import Counter

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the frequency of characters in both strings are the same
        if Counter(s) == Counter(t):
            # if frequencies are equal, strings are anagrams
            return True
        else:
            # If frequencies are not equal, strings are not anagrams
            return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))
    print(s.isAnagram('car', 'rat'))