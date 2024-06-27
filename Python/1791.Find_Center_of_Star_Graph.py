from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # check if the first vertex of the first edge is the same as either vertex of the second edge
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            # if true, return the common vertex (edges[0][0])
            return edges[0][0]
        # if the above condition is false, return the other vertex of the first edge (edges[0][1])
        return edges[0][1]
    
    # method # 2
    # return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

if __name__ == '__main__':
    s = Solution()
    print(s.findCenter([[1,2],[2,3],[4,2]]))
    print(s.findCenter([[1,2],[5,1],[1,3],[1,4]]))
    print(s.findCenter([[10,1],[10,2],[3,10],[10,4],[5,10],[10,6],[10,7],
                        [8,10],[10,9],[10,11],[12,10],[10,13],[14,10]]))