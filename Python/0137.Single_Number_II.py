from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initialize two variables to store intermediate results
        a, b = 0, 0
        
        # iterate through each number in the list
        for num in nums:
            # update 'a' by XOR-ing it with the current number and then 
            # masking with the complement of 'b'
            a = (a ^ num) & ~b
            # update 'b' by XOR-ing it with the current number and then 
            # masking with the complement of 'a'
            b = (b ^ num) & ~a
        
        # after iterating through all numbers, 'a' will contain the single number
        return a

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
    print(s.singleNumber([0,1,0,1,0,1,99]))