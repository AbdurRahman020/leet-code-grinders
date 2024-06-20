from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # if there are exactly 2 balls, return the maximum distance between them
        if m == 2:
            return max(position) - min(position)
        
        # sort the positions of the balls
        position.sort()
        
        # function to check if it's possible to place `m` balls with at least
        # `min_distance` distance between any two balls
        def canPlaceBalls(min_distance, num_balls):
            # initialize the position of the last placed ball
            previous_position  = -float('inf')
            for pos in position:
                # check if the current position `pos` can have a ball placed, maintaining
                # at least `min_distance` distance from the previous ball
                if pos - previous_position >= min_distance:
                    # decrement the number of remaining balls to be placed
                    num_balls -= 1
                    # update the position of the last placed ball
                    previous_position = pos
                    # if all balls are placed, return True
                    if num_balls == 0:
                        return True
            
            # if not all balls can be placed with at least `min_distance` distance, return False
            return False
        
        # initialize binary search bounds
        # minimum possible distance between any two balls
        min_distance = 1
        # maximum possible distance between any two balls
        max_distance = position[-1] - position[0]
        
        # binary search to find the maximum possible minimum distance
        while max_distance - min_distance > 1:
            # calculate the midpoint distance
            mid_distance = (min_distance + max_distance) // 2
            # if `m` balls can be placed with `mid_distance` distance, try to increase the distance
            if canPlaceBalls(mid_distance, m):
                min_distance = mid_distance
            # if `m` balls cannot be placed with `mid_distance` distance, decrease the distance
            else:
                max_distance  = mid_distance
        
        # return the maximum possible minimum distance found
        return min_distance

if __name__ == '__main__':
    s = Solution()
    print(s.maxDistance([1,2,3,4,7], 3))
    print(s.maxDistance([5,4,3,2,1,1000000000], 2))