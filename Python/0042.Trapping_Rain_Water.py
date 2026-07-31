from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
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

    def trap2(self, height: List[int]) -> int:
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

    print(s.trap1([4, 2, 0, 3, 2, 5]))
    print(s.trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    print(s.trap2([4, 2, 0, 3, 2, 5]))
    print(s.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
