from collections import deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # create an adjacency list to represent the graph
        adjacency_list = [[] for _ in range(n + 1)]
        
        # populate the adjacency list with the given edges
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        # initialize a queue for BFS, starting from node 1 with a visit count of 1
        queue = deque([(1, 1)])
        
        # list to store the shortest time to reach first node 
        first_min_time = [-1] * (n + 1)
        # list to store the shortest time to reach second node
        second_min_time = [-1] * (n + 1)
        
        # set the time to reach the start node (node 1) as 0
        first_min_time[1] = 0
        
        # perform BFS to explore all possible paths and calculate times
        while queue:
            # dequeue the current node and its visit count (1 or 2)
            curr_node, visit_count = queue.popleft()
            # determine the current time based on whether it's the first or second visit
            curr_time = first_min_time[curr_node] if visit_count == 1 else second_min_time[curr_node]
            
            # calculate the next time after waiting for the traffic light, check if 
            # the current time is during the red light
            if (curr_time // change) % 2:
                # if in red light, wait until the next green light and then add travel time
                curr_time = change * (curr_time // change + 1) + time
            else:
                # if in green light, just add travel time
                curr_time += time
            
            # process all neighbors of the current node
            for neighbor in adjacency_list[curr_node]:
                if first_min_time[neighbor] == -1:
                    # if neighbor has not been visited, mark its first visit time
                    first_min_time[neighbor] = curr_time
                    # add neighbor to queue with first visit
                    queue.append((neighbor, 1))
                elif second_min_time[neighbor] == -1 and first_min_time[neighbor] != curr_time:
                    # if neighbor has not been visited for the second time and the current time is 
                    # different from its first visit
                    if neighbor == n:
                        # if the neighbor is the destination node, return the current time
                        return curr_time
                    # mark the second visit time for the neighbor
                    second_min_time[neighbor] = curr_time
                    # add neighbor to queue with second visit
                    queue.append((neighbor, 2))
        
        # if we finish processing and haven't found the second minimum time to reach node n, return 0
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))
    print(s.secondMinimum(2, [[1,2]], 3, 2))