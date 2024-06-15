from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # create a list of tuples where each tuple represents (capital, profit)
        projects = [(capital[i], profits[i]) for i in range(n)]
        # sort projects based on capital requirement
        projects.sort()
        
        # min-heap to store negative profits for easy retrieval of maximum profit
        min_profit_heap  = []
        # index to iterate through sorted projects list
        current_project = 0
        
        # iterate k times to select up to k projects
        for _ in range(k):
            # add all projects whose capital requirement is less than or equal to current available capital
            while current_project < n and projects[current_project][0] <= w:
                # push negative profit onto min-heap
                heapq.heappush(min_profit_heap , -projects[current_project][1])
                # move to the next project
                current_project += 1
            
            # if no projects can be selected (min_profit_heap is empty), exit the loop
            if not min_profit_heap:
                break
            
            # select the project with the maximum profit from the min-heap
            # add the profit to available capital (subtracting negative profit)
            w -= heapq.heappop(min_profit_heap )
        
        # return the remaining available capital after selecting up to k projects
        return w

if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1,2,3], [0,0,1]))
    print(s.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))