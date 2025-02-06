from typing import List

class Solution:
    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        # sort the input list to handle duplicates properly
        nums.sort()
        # get the length of the input list
        n = len(nums)
        
        # define a backtracking function to generate subsets
        def backtrack(i, path):
            # append the current subset to the result
            result.append(path)
            # iterate over remaining elements to generate more subsets
            for j in range(i, n):
                # recursively call backtrack to explore subsets with the current
                # element included
                backtrack(j + 1, path + [nums[j]])
        
        # initialize an empty list to store subsets
        result = []
        # start backtracking from index 0 with an empty subset
        backtrack(0, [])
        
        # convert list of lists to set of tuples to remove duplicates
        result = list(map(list, set(map(tuple, result))))
        
        # return the result list containing all subsets
        return result
    
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        # sort the input list to handle duplicates properly
        nums.sort()
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
        
        # convert list of lists to set of tuples to remove duplicates
        result = list(map(list, set(map(tuple, result))))
        
        # return the result list containing all subsets
        return result
        
if __name__ == '__main__':
    s = Solution()
    
    print(s.subsetsWithDup1([1,2,2]))
    print(s.subsetsWithDup1([0]))
    
    print(s.subsetsWithDup2([1,2,2]))
    print(s.subsetsWithDup2([0]))
