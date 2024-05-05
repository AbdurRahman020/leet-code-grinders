from collections import Counter

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams of each other.
        
        An anagram is a word or phrase formed by rearranging the letters of a 
        different word or phrase, typically using all the original letters exactly once.
        
        :param s: The first string.
        :type s: str
        :param t: The second string.
        :type t: str
        
        :return: True if s and t are anagrams, False otherwise.
        :rtype: bool
        """
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