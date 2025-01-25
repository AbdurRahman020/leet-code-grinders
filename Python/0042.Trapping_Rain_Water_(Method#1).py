from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        
        water_traped = 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_traped += (left_max - height[left])
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_traped += (right_max - height[right])
                right -= 1
            
        return water_traped

if __name__ == '__main__':
    s = Solution()
    print(s.trap([4,2,0,3,2,5]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))