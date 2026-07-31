import re


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        string = filter(str.isalnum, s)
        processed_string = "".join(list(string)).lower()

        l, r = 0, len(processed_string) - 1

        while l < r:
            if processed_string[l] != processed_string[r]:
                return False

            l += 1
            r -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()

    print(s.isPalindrome1("A man, a plan, a canal: Panama"))
    print(s.isPalindrome1("race a car"))
    print(s.isPalindrome1(""))

    print(s.isPalindrome2("A man, a plan, a canal: Panama"))
    print(s.isPalindrome2("race a car"))
    print(s.isPalindrome2(""))
