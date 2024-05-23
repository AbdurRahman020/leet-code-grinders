from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([0]))
    print(s.subsets([9,8,7,6,5]))
