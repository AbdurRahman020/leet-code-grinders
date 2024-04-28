class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        water_traped, i, j = 0, 0, len(height)-1
        left_max, right_max = height[i], height[j]
        
        while i < j:
            if left_max < right_max:
                water_traped += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                water_traped += right_max - height[j]
                j -= 1
                right_max = max(right_max, height[j])
                
        return water_traped

if __name__ == '__main__':
    s = Solution()
    print(s.trap([4,2,0,3,2,5]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))