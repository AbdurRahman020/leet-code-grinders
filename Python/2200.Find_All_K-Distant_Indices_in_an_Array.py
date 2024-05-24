from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # get the length of the input list
        n = len(nums)
        # initialize two pointers i and j to iterate through the list
        i, j = 0, 0
        # initialize an empty list to store the indices that satisfy the condition
        result = []
        
        # iterate through the list until one of the pointers reaches the end
        while i < n and j < n:
            # if the element at index j is not equal to the key, move the j pointer forward
            if nums[j] != key:
                j += 1
            else:
                # if the element at index j is equal to the key, check the distance between i and j
                if abs(i-j) <= k:
                    # if the distance is less than or equal to k, add the index i to the result list
                    result.append(i)
                
                # move pointers i and j based on the distance condition
                if abs(i-j) > k and i > j:
                    # if the distance is greater than k and i is ahead of j, move j forward
                    j += 1
                else:
                    # otherwise, move i forward
                    i += 1
        
        # return the list of indices that satisfy the condition
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findKDistantIndices([3,4,9,1,3,9,5], 9, 1))
    print(s.findKDistantIndices([2,2,2,2,2], 2, 2))