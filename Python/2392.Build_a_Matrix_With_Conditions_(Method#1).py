from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # function for topological sort
        def topological_sort(edges: List[List[int]], k: int) -> List[int]:
            # initialize predecessor map to store predecessors
            pred_map = defaultdict(list)
            # initialize in-degree array to store in-degree of each node
            in_degree = [0] * (k+1)
            
            # build the predecessor map and in-degree array
            for u, v in edges:
                pred_map[u].append(v)
                in_degree[v] += 1
            
            # initialize queue with nodes having zero in-degree
            queue = deque([i for i in range(1, k+1) if in_degree[i] == 0])
            # list to store the topological order
            topological_order = []
            
            # Pperform topological sorting using Kahn's algorithm
            while queue:
                # extract node from queue
                node = queue.popleft()
                # add node to the topological order
                topological_order.append(node)
                
                # decrease in-degree of neighbors and enqueue if in-degree becomes zero
                for neighbor in pred_map[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            # if the order contains all nodes (k nodes), return the order
            if len(topological_order) == k:
                return topological_order
            else:
                # return empty list if not all nodes are included
                return []
        
        # function to fix positions based on topological order
        def fix_position(topological_order: List[int]) -> dict:
            # map node to its position in order
            pos_map  = {x: i for i, x in enumerate(topological_order)}
            # next available position
            next_pos = len(topological_order)
            
            # fill positions for nodes not present in the order
            for node in range(1, k + 1):
                if node not in pos_map:
                    pos_map [node] = next_pos
                    next_pos += 1
            
            # return a dictionary mapping each node to its position in the topological order
            return pos_map
        
        # perform topological sorting on row and column conditions
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        # if either row or column order is empty, return empty matrix
        if not row_order or not col_order:
            return []
        
        # fix positions for rows and columns
        row_positions = fix_position(row_order)
        col_positions = fix_position(col_order)
        
        # initialize matrix with zeros
        matrix = [[0]*k for _ in range(k)]
        # fill matrix based on fixed row and column positions
        for node in range(1, k + 1):
            matrix[row_positions[node]][col_positions[node]] = node
        
        # return the constructed matrix
        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))
    print(s.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]))