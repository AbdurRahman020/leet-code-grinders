from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # check if the input list is empty. If so, return 0 since no water can be trapped
        if not height:
            return 0
        
        # initialize the amount of water trapped to 0
        water_traped = 0
        
        # initialize two pointers: one at the start of the list and one at the end
        i, j = 0, len(height) - 1
        
        # initialize the maximum heights encountered from the left and the right
        left_max, right_max = height[i], height[j]
        
        # process elements while the two pointers do not cross each other
        while i < j:
            # if the left maximum height is less than the right maximum height:
            if left_max < right_max:
                # add the difference between the current left maximum height and the height 
                # at the current left pointer to the total amount of water trapped, this is
                # because water can be trapped above the current height up to the level 
                # of the left maximum height
                water_traped += left_max - height[i]
                # move the left pointer one step to the right
                i += 1
                # update the left maximum height if the new height is greater than the previous
                # left maximum height
                left_max = max(left_max, height[i])
            # if the right maximum height is less than or equal to the left maximum height:
            else:    
                # add the difference between the current right maximum height and the height 
                # at the current right pointer to the total amount of water trapped, this is
                # because water can be trapped above the current height up to the level of 
                # the right maximum height
                water_traped += right_max - height[j]
                # move the right pointer one step to the left.
                j -= 1
                # update the right maximum height if the new height is greater than the 
                # previous right maximum height
                right_max = max(right_max, height[j])
        
        # return the total amount of water trapped after processing all elements
        return water_traped

if __name__ == '__main__':
    s = Solution()
    print(s.trap([4,2,0,3,2,5]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))