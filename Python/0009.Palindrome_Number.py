class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        r_string = string[::-1]
        if string == r_string:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(-10))