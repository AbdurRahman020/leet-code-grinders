from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # function to check if it's possible to split nums into at most k groups
        # such that each group's sum does not exceed max_sum.
        def can_split_into_k_groups(max_sum):
            # counter for the number of groups formed
            groups_count = 0
            # current sum of elements in the current group
            current_sum = 0
            
            for num in nums:
                # add current number to the current group sum
                current_sum += num
                if current_sum > max_sum:
                    # we exceed max_sum, so start a new group
                    groups_count += 1
                    # reset current sum to the current number
                    current_sum = num
            
            # increment count for the last group formed
            groups_count += 1
            # return True if groups formed <= k
            return groups_count <= k
        
        # initialize the search range for binary search
        # minimum possible maximum sum (at least the largest element)
        min_possible = max(nums)
        # maximum possible maximum sum (sum of all elements)
        max_possible = sum(nums)
        
        # perform binary search to find the minimum possible maximum sum
        while min_possible < max_possible:
            # calculate mid point
            mid = min_possible + (max_possible - min_possible) // 2
            
            # check if it's possible to split into k groups with mid as max_sum
            if can_split_into_k_groups(mid):
                # if yes, adjust the search range to the left
                max_possible = mid
            else:
                # if no, adjust the search range to the right
                min_possible = mid + 1
        
        # at the end of binary search, min_possible will be the minimum possible max_sum
        return min_possible

if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
    print(s.splitArray([1,2,3,4,5], 2))
    print(s.splitArray([2,3,1,1,1,1,1], 5))
    print(s.splitArray([7,6,5,4,3,2,1], 2))