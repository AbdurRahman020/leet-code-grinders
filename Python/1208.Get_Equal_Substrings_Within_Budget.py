class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # length of the strings
        n = len(s)
        # initialize the start index of the sliding window
        i = 0
        
        # iterate over the characters of the strings
        for j in range(n):
            # calculate the cost of changing the character at index j from s to t,
            # and deduct it from maxCost
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            # if maxCost becomes negative, it means the current substring's cost
            # exceeds the maximum allowed cost
            if maxCost < 0:
                # in such a case, add back the cost of changing the character at
                # index i from s to t, and move the start index of the window forward
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        
        # return the length of the longest valid substring
        return j - i + 1

if __name__ == '__main__':
    s = Solution()
    print(s.equalSubstring("abcd", "bcdf", 3))
    print(s.equalSubstring("abcd", "cdef", 3))
    print(s.equalSubstring("abcd", "acde", 0))