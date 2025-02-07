from typing import List
from itertools import groupby

class Solution:
    def compress1(self, chars: List[str]) -> int:
        # initialize two pointers i and j
        i, j = 0, 0
        # get the length of the input list chars
        n = len(chars)
        
        # loop through the characters of the input list chars
        while i < n:
            # initialize a count variable to count consecutive occurrences of the current character
            count = 1
            # loop to count consecutive occurrences of the current character
            while i+1 < n and chars[i] == chars[i+1]:
                count += 1
                i += 1
            
            # write the current character to its correct position in the compressed list
            chars[j] = chars[i]
            j += 1
            
            # if the count of consecutive occurrences is greater than 1, write it to the compressed list
            if count > 1:
                # convert the count to a string and iterate over its digits
                for digit in str(count):
                    # write each digit to its correct position in the compressed list
                    chars[j] = digit
                    j += 1
            
            # move to the next character in the input list
            i += 1
        
        # truncate the list to remove the characters beyond the compressed portion
        chars[:] = chars[:j]
        
        # return the length of the compressed list
        return j
    
    def compress2(self, chars: List[str]) -> int:
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
    s.compress1(chars1)
    print(chars1)
    chars2 = ["a"] 
    s.compress1(chars2)
    print(chars2)
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] 
    s.compress1(chars3)
    print(chars3)
    
    chars1 = ["a","a","b","b","c","c","c"] 
    s.compress2(chars1)
    print(chars1)
    chars2 = ["a"] 
    s.compress2(chars2)
    print(chars2)
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] 
    s.compress2(chars3)
    print(chars3)