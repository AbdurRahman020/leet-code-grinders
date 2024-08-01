class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        # convert the integer to a string representation
        string = str(x)
        # create a reversed version of the string
        rev_string = string[::-1]
        
        # compare the original string with the reversed string
        if string == rev_string:
            # return true if the original and reversed strings are the same
            return True
        else:
            # return False otherwise
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(-10))