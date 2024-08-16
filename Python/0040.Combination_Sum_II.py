from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the candidates list to handle duplicates and facilitate the backtracking process
        candidates.sort()
        # initialize an empty list to store the final result (unique combinations)
        sol_set = []
        # store the number of candidates
        n = len(candidates)
        
        # define a helper function backtrack that performs the recursive search
        # 'start' is the index to start checking candidates
        # 'target_sum' is the remaining sum we need to achieve
        # 'path' is the current combination of numbers
        def backtrack(start, target_sum, path):
            
            # if the remaining target_sum is 0, it means we found a valid combination
            if target_sum == 0:
                # add a copy of the current path to the result list
                sol_set.append(path[:])
                # exit the function since we've found a valid combination
                return
            
            # if the remaining target_sum is negative, it means the current path is invalid
            if target_sum < 0:
                # exit the function to backtrack and try other combinations
                return
            
            # loop through the candidates starting from the 'start' index
            for i in range(start, n):
                # check if the current candidate is a duplicate of the previous one
                if i > start and candidates[i] == candidates[i-1]:
                    # skip duplicates to avoid redundant combinations
                    continue
                
                # call backtrack recursively with the next index, reduced target_sum, and updated path
                backtrack(i+1, target_sum - candidates[i], path + [candidates[i]])
        
        # initiate the backtracking process starting from index 0, with the original target and an empty path
        backtrack(0, target, [])
        
        # return the list of unique combinations that sum up to the target
        return sol_set

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))