from typing import List

class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
       num = int(''.join(map(str, digits))) + 1
       
       return [int(i) for i in str(num)]
        
if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3]))
    print(s.plusOne([9,9,9]))
    print(s.plusOne([2,9,5,9]))