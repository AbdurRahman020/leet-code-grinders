from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # length of the input list
        n = len(nums)
        # sorting the input list for easier comparison
        nums.sort()
        # counter for beautiful subsets
        total = 0
        
        def backtrack(index, path):
            # accessing the 'total' variable from the enclosing function
            nonlocal total
            # if the index exceeds the length of the input list, end the recursion
            if index > n:
                return
            
            # if the path is not empty, meaning it's a non-empty subset,
            # increment the total count
            if path:
                total += 1
            
            # iterate over the elements from the current index to the end of the list
            for i in range(index, n):
                # checking if the difference between nums[i] and k is not already in the path
                if nums[i] - k not in path:
                    # recursively call the function with updated index and path
                    backtrack(i+1, path + [nums[i]])
        
        # initial call to the backtrack function with index 0 and an empty path
        backtrack(0, [])
        # return the total count of beautiful subsets
        return total

if __name__ == "__main__":
    s = Solution()
    print(s.beautifulSubsets([2,4,6], 1))
    print(s.beautifulSubsets([1], 1))