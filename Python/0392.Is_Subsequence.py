class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initialize two pointers, i for the string 's' and j for the string 't'
        i, j = 0, 0

        # iterate while we have not exhausted either of the strings
        while i < len(s) and j < len(t):
            # if the current character in 's' matches the current character in 't'
            if s[i] == t[j]:
                # move the pointer 'i' to the next character in 's'
                i += 1

            # always move the pointer 'j' to the next character in 't'
            j += 1

        # if we've gone through all characters in 's', then 's' is a subsequence of 't'
        return i == len(s)


if __name__ == '__main__':
    s = Solution()

    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
