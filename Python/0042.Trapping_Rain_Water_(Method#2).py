from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water_traped = 0

        left_max, right_max = [0] * n, [0] * n 

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            water_traped += min(right_max[i], left_max[i]) - height[i]

        return water_traped

if __name__ == '__main__':
    s = Solution()
    print(s.trap([4,2,0,3,2,5]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))