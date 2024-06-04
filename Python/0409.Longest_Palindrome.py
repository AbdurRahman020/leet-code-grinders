from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count the occurrences of each character in the string
        char_count = Counter(s)
        # initialize the variable to store the length of the longest palindrome
        max_palindrome_length = 0
        
        # iterate through the counts of characters
        for count in char_count.values():
            # add the maximum number of characters that can form pairs to the max_palindrome_length
            max_palindrome_length += int(count/2) * 2
            
            # if the current count is odd and the current max_palindrome_length is even,
            # add one more character to the palindrome length as a center character
            if max_palindrome_length % 2 == 0 and count % 2 == 1:
                max_palindrome_length += 1
        
        # return the length of the longest palindrome
        return max_palindrome_length 

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))