from typing import List
from collections import defaultdict
from graphlib import TopologicalSorter, CycleError

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # function for topological sort
        def topological_sort(edges: List[List[int]]) -> List[int]:
            # create a defaultdict to store predecessors for each node
            pred_map = defaultdict(list)
            
            # populate the predecessor map based on the given edges
            for u, v in edges:
                pred_map[v].append(u)
            
            # initialize a TopologicalSorter with the predecessor map
            sorter = TopologicalSorter(pred_map)
            
            # perform topological sorting and return the result as a list
            try:
                return list(sorter.static_order())
            # handle CycleError if a cycle is detected in the graph
            except CycleError:
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
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        # If either row or column order is empty, return empty matrix
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