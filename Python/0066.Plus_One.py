from typing import List

class Solution():
    def plusOne1(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOne2(digits[:-1] + [0])
        else:
            digits[-1] += 1
        
        return digits
    
    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            
            if i == 0:
                return digits + [1]
            
        
if __name__ == '__main__':
    s = Solution()
    
    print(s.plusOne1([1,2,3]))
    print(s.plusOne1([9,9,9]))
    print(s.plusOne1([2,9,5,9]))
    
    print(s.plusOne2([1,2,3]))
    print(s.plusOne2([9,9,9]))
    print(s.plusOne2([2,9,5,9]))
