from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # check if the lengths of both words are different
        if len(word1) != len(word2):
            # if lengths differ, they can't be close strings
            return False
        
        # create Counter objects for both words to count character frequencies
        count1, count2 = Counter(word1), Counter(word2)
        
        # check if the sorted list of characters from both counts are the same, this
        # ensures both words use the same set of characters
        if sorted(count1.keys()) == sorted(count2.keys()):
            # check if the sorted list of frequency values from both counts are the same,
            # this ensures both words have the same character frequencies
            return sorted(count1.values()) == sorted(count2.values())
        
        # if either the characters or their frequencies don't match, return False
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.closeStrings("abc", "bca"))
    print(s.closeStrings("a", "aa"))
    print(s.closeStrings("cabbba", "abbccc"))