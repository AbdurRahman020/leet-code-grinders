from typing import List

class Solution(object):
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get the dimensions of the board
        row_length, col_length = len(board), len(board[0])
        
        def dfs(r, c, current):
            # if the current index equals the length of the word, we've found the word
            if current == len(word):
                return True
            # if the current position is out of bounds or doesn't match the current character,
            # or if the cell has been visited already, return False
            if (
                r < 0
                or c < 0
                or r >= row_length
                or c >= col_length
                or board[r][c] == ''
                or word[current] != board[r][c]
            ):
                return False
            
            # cache the current cell value, mark it as visited
            cache = board[r][c]
            board[r][c] = ''
            
            # recursively check neighboring cells in all four directions
            if (
                dfs(r+1, c, current + 1)
                or dfs(r-1, c, current + 1)
                or dfs(r, c+1, current + 1)
                or dfs(r, c-1, current + 1)
            ):
                return True
            
            # if the word is not found, backtrack by restoring the original value of the cell
            board[r][c] = cache
            return False
        
        # iterate over each cell in the board and start DFS from there to find the word
        return any(dfs(i, j, 0) for i in range(row_length) for j in range(col_length))

if __name__ == '__main__':
    s = Solution()
    b = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(s.exist(b, 'ABCCED'))
    b = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(s.exist(b, 'ABCB'))
    b = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(s.exist(b, 'SEE'))