from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # initialize a Counter to store the frequency of characters in the first word
        char_freq = Counter(words[0])

        # iterate through each word in the list starting from the second word
        for word in words[1:]:
            # for each word, intersect its character frequencies with the existing frequencies
            char_freq &= Counter(word)
        
        # convert the common characters and their frequencies into a list
        return list(char_freq.elements())

if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["bella","label","roller"]))
    print(s.commonChars(["cool","lock","cook"]))