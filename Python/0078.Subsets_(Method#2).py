from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # get the length of the input list
        n = len(nums)
        # initialize an empty list to store subsets
        result = []
        
        # iterate over all possible subsets using bit manipulation
        # 1<<n calculates 2^n, the number of subsets possible
        for i in range(1<<n):
            # initialize an empty subset
            subset = []
            # iterate over each bit of the current number 'i', each
            # bit represents whether the corresponding element should 
            # be included in the subset
            for j in range(n):
                # check if the j-th bit of i is set
                if i & (1<<j):
                    # if set, include the corresponding element from nums in the subset
                    subset.append(nums[j])
            # add the generated subset to the result list
            result.append(subset)
        
        # return the result list containing all subsets
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([0]))
    print(s.subsets([9,8,7,6,5]))
