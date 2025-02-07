from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minimumCost1(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # initialize a 26x26 matrix to represent the cost of converting one character to another,
        # use float("inf") to denote initially no path (no direct conversion cost) between characters
        cost_matrix = [[float("inf")] * 26 for _ in range(26)]
        
        # set the cost of converting a character to itself as zero
        for char_index in range(26):
            cost_matrix[char_index][char_index] = 0
        
        # populate the cost matrix with given conversion costs.
        for orig_char, new_char, conversion_cost in zip(original, changed, cost):
            # convert character to its corresponding index (0-25)
            orig_index = ord(orig_char) - ord("a")
            # convert character to its corresponding index (0-25)
            new_index = ord(new_char) - ord("a")
            # update the cost matrix with the minimum cost of conversion from orig_char to new_char
            cost_matrix[orig_index][new_index] = min(cost_matrix[orig_index][new_index], conversion_cost)
        
        # applying the Floyd-Warshall algorithm to find the minimum cost of conversion between all pairs of characters
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    # update cost_matrix[i][j] with the minimum cost found using an intermediate character k
                    cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # initialize total conversion cost.
        total_conversion_cost = 0
        
        # compute the total conversion cost for converting the source string to the target string
        for src_char, tgt_char in zip(source, target):
            # only compute cost if characters are different
            if src_char != tgt_char:
                conversion_cost = cost_matrix[ord(src_char) - ord("a")][ord(tgt_char) - ord("a")]
                
                # if conversion cost is still infinity, it means conversion is impossible
                if conversion_cost == float("inf"):
                    return -1
                
                # accumulate the total cost
                total_conversion_cost += conversion_cost
            
        # return the total conversion cost
        return total_conversion_cost
    
    def minimumCost2(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # create an adjacency list to store the graph
        adjacency_list = defaultdict(list)
        # initialize total cost to 0
        total_cost = 0
        # track if we have processed shortest paths from a given start node
        visited = [False] * 26
        # initialize the shortest path matrix with infinity values
        shortest_paths = [[float('inf') for _ in range(26)] for _ in range(26)]

        # build the graph from the provided conversions
        for from_char, to_char, conversion_cost in zip(original, changed, cost):
            # convert character to index (0-25)
            from_index = ord(from_char) - ord('a')
            to_index = ord(to_char) - ord('a')
            # add the conversion with cost to the adjacency list
            adjacency_list[from_index].append([conversion_cost, to_index])
        
        # function to perform Dijkstra's algorithm from a given start node
        def dijkstra(start_index):
            # priority queue for Dijkstra's algorithm, initialized with the start node
            priority_queue = [(0, start_index)]
            # the cost to reach the start node from itself is 0
            shortest_paths[start_index][start_index] = 0
            
            while priority_queue:
                # extract the node with the minimum cost from the priority queue
                current_cost, current_index = heappop(priority_queue)
                
                # if the current cost is greater than the known shortest path, skip it
                if current_cost > shortest_paths[start_index][current_index]:
                    continue
                
                # explore neighbors of the current node
                for edge_cost, neighbor_index in adjacency_list[current_index]:
                    # calculate the new cost to reach the neighbor
                    new_cost = edge_cost + current_cost
                    
                    # if the new cost is less than the known shortest cost, update and push to the queue
                    if new_cost < shortest_paths[start_index][neighbor_index]:
                        shortest_paths[start_index][neighbor_index] = new_cost
                        heappush(priority_queue, (new_cost, neighbor_index))
        
        # calculate the total cost to convert the source string to the target string
        for src_char, tgt_char in zip(source, target):
            # convert character to its corresponding index (0-25)
            src_index = ord(src_char) - ord('a')
            # convert character to its corresponding index (0-25)
            tgt_index = ord(tgt_char) - ord('a')
            
            # if we haven't processed shortest paths from src_index, run Dijkstra
            if not visited[src_index]:
                dijkstra(src_index)
                visited[src_index] = True
            
            # if no path exists from src_char to tgt_char, return -1
            if shortest_paths[src_index][tgt_index] == float('inf'):
                return -1
            
            # add the shortest path cost to the total cost
            total_cost += shortest_paths[src_index][tgt_index]
        
        # return the total cost to convert the source string to the target string
        return total_cost

if __name__ == '__main__':
    s = Solution()
   
    print(s.minimumCost1("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))
    print(s.minimumCost1("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]))
    print(s.minimumCost1("abcd", "abce", ["a"], ["e"], [10000]))
    
    print(s.minimumCost2("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))
    print(s.minimumCost2("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]))
    print(s.minimumCost2("abcd", "abce", ["a"], ["e"], [10000]))
