from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # initialize variables to store XOR result and unique numbers
        xor_result = first_unique = second_unique = 0
        
        # calculate XOR of all numbers
        for num in nums:
            xor_result ^= num
        
        # find the rightmost set bit in the XOR result
        rightmost_bit = xor_result & -xor_result
        
        # split numbers into two groups based on the rightmost set bit
        for num in nums:
            if num & rightmost_bit:
                # numbers with the rightmost set bit
                second_unique ^= num
            else:
                # numbers without the rightmost set bit
                first_unique ^= num
        
        # return the two unique numbers
        return [first_unique, second_unique] 

if __name__ == '__main__':
    s =  Solution()
    print(s.singleNumber([1,2,1,3,2,5]))
    print(s.singleNumber([-1,0]))
    print(s.singleNumber([0,1]))