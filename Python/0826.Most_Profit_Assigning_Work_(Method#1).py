from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # create a list of tuples (difficulty, profit) and sort it by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # create a dictionary to store the maximum profit achievable for each difficulty
        max_profit_map = {}
        max_profit_seen_so_far = 0
        
        # iterate through sorted jobs and update max profit for each difficulty
        for d, p in jobs:
            max_profit_seen_so_far = max(max_profit_seen_so_far, p)
            max_profit_map[d] = max_profit_seen_so_far
        
        total_profit = 0
        
        # calculate total profit for each worker's ability
        for w in worker:
            # find the largest difficulty <= w using binary search
            target_index = self.binary_search(max_profit_map, w)
            if target_index >= 0:
                total_profit += max_profit_map[target_index]
        
        return total_profit
    
    def binary_search(self, max_profit_map: dict, num: int) -> int:
        # helper function to perform binary search on the keys of max_profit_map
        keys = sorted(max_profit_map.keys())
        left, right = 0, len(keys) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if keys[mid] <= num:
                left = mid + 1
            else:
                right = mid - 1
        
        # return the largest key <= num
        if right >= 0:
            return keys[right]
        else:
            # if no valid key found
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))
    print(s.maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]))
    print(s.maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]))