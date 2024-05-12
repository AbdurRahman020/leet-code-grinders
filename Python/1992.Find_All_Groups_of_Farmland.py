from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row_length, col_length = len(land), len(land[0])
        coordinates = []
        visited = set()

        def dfs(r, c):
            if r == row_length or c == col_length or not land[r][c] or (r, c) in visited:
                return [r, c]
            
            visited.add((r, c))

            return [dfs(r+1, c)[0], dfs(r, c+1)[1]]

        for i in range(row_length):
            for j in range(col_length):
                if land[i][j] and (i, j) not in visited:
                    [x, y] = dfs(i, j)
                    coordinates.append([i, j, x-1, y-1])
        
        return coordinates
    
if __name__ == '__main__':
    s = Solution()
    print(s.findFarmland([[1,0,0],[0,1,1],[0,1,1]]))
    print(s.findFarmland([[1,1],[1,1]]))
    print(s.findFarmland([[0]]))