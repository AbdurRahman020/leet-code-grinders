class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # initialize a list to keep track of the length of the longest ideal substring ending at 
        # each character position
        ideal_sub_string = [0]*26
        # iterate over each character in the input string
        for ch in s:
            # convert the character to its corresponding index in the range 0-25
            i = ord(ch) - ord('a')
            # update the length of the longest ideal substring ending at the current character
            ideal_sub_string[i] = 1 + max(ideal_sub_string[max(0, i - k) : min(26, i + k + 1)])
        # return the maximum value in the list, which represents the length of the longest ideal substring
        return max(ideal_sub_string)

if __name__ == '__main__':
    s = Solution()
    print(s.longestIdealString("acfgbd", 2))
    print(s.longestIdealString("abcd", 3))