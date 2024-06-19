from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # helper function to check if given capacity can ship all weights within 'days' days
        def canShipWithinCapacity(capacity: int) -> bool:
            # total days needed to ship all weights
            days_needed = 0
            # current load on the ship
            current_load = 0
            
            for weight in weights:
                # add current weight to the ship's load
                current_load += weight
                
                # if adding this weight exceeds the capacity, ship it separately
                if current_load > capacity:
                    # increment days needed
                    days_needed += 1
                    # reset current load to current weight
                    current_load = weight
            
            # after loop, check if there's any remaining load to ship
            if current_load > 0:
                # increment days for any remaining load
                days_needed += 1
            
            # return whether days needed is within the given 'days'
            return days_needed <= days
        
        # initialize the binary search range for capacity
        # minimum capacity is at least the weight of the heaviest item
        min_capacity = max(weights)
        # maximum capacity is the sum of all weights
        max_capacity = sum(weights)
        
        # binary search to find the minimum capacity that can ship all weights within 'days' days
        while min_capacity < max_capacity:
            # calculate midpoint capacity
            mid_capacity = (min_capacity + max_capacity) // 2  
            
            if canShipWithinCapacity(mid_capacity):
                # if current capacity works, search lower capacities
                max_capacity = mid_capacity
            else:
                # if current capacity doesn't work, search higher capacities
                min_capacity = mid_capacity + 1
        
        # return the minimum capacity found
        return min_capacity  

if __name__ == '__main__':
    s = Solution()
    print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
    print(s.shipWithinDays([3,2,2,4,1,4], 3))
    print(s.shipWithinDays([1,2,3,1,1], 4))  