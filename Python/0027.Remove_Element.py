from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pointer for the position to place the next non-val element
        insertion_index = 0
        
        # iterate over each element in the list
        for current_index in range(len(nums)):
            # check if the current element is not equal to the value to be removed
            if nums[current_index] != val:
                # place the current element at the insertion_index position
                nums[insertion_index] = nums[current_index]
                # move the insertion_index to the next position
                insertion_index += 1
        
        # return the length of the list after removing all occurrences of the value
        return insertion_index
            
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))
    print(s.removeElement([3,2,2,3], 3))