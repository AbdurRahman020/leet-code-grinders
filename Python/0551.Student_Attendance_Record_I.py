class Solution:
    def checkRecord(self, s: str) -> bool:
        # check if the number of 'A's in the string is less than 2and ensure
        # that 'LLL' (three consecutive 'L's) is not present in the string
        # return True if both conditions are met, otherwise return False
        return (s.count('A') < 2) and ('LLL' not in s)

if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord("PPALLP"))
    print(s.checkRecord("PPALLL"))