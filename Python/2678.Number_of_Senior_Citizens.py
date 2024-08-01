from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(x[11:13]) > 60 for x in details)

if __name__ == '__main__':
    s = Solution()
    print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
    print(s.countSeniors(["1313579440F2036","2921522980M5644"]))