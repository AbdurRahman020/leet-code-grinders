from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize two pointers, one at the beginning (i) and one at the end (j) of the height list
        i, j = 0, len(height) - 1
        # initialize max_area to keep track of the maximum area found
        max_area = 0
        
        # loop until the two pointers meet
        while i < j:
            # calculate the current area formed by the lines at the two pointers
            curr_area = (j - i) * min(height[i], height[j])
            # update max_area if the current area is greater than the previous max_area
            max_area = max(max_area, curr_area)

            # move the pointer that points to the shorter line to try and find a potentially larger area
            if height[i] < height[j]:
                # move the left pointer to the right
                i += 1
            else:
                # Move the right pointer to the left
                j -= 1
        
        # return the maximum area found
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([1,1]))