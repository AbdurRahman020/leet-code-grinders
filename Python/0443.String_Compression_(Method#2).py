from typing import List
from itertools import groupby

class Solution:
    def compress(self, chars: List[str]) -> int:
        # initialize an empty list to store the compressed characters
        compressed_chars = []
        
        # iterate through each character and its consecutive occurrences using groupby
        for key, group in groupby(chars):
            # calculate the count of consecutive occurrences
            count = len(list(group))
            # append the current character to the compressed list
            compressed_chars.append(key)
            # if the count of consecutive occurrences is greater than 1, append its 
            # count to the compressed list
            if count > 1:
                compressed_chars.extend(list(str(count)))
        
        # replace the original list with the compressed list
        chars[:] = compressed_chars

if __name__ == '__main__':
    s = Solution()
    chars1 = ["a","a","b","b","c","c","c"] 
    s.compress(chars1)
    print(chars1)
    chars2 = ["a"] 
    s.compress(chars2)
    print(chars2)
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] 
    s.compress(chars3)
    print(chars3)