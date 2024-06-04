from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
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