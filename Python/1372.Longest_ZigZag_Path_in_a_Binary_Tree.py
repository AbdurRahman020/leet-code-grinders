from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # initialize the longest path found to 0
        self.long_path = 0
        
        def dfs(root, left, right):
            # update the longest path with the maximum value between the current longest path,
            # the left zigzag length, and the right zigzag length
            self.long_path = max(self.long_path, left, right)
            
            # if there is a left child, continue the zigzag path starting from the left child
            # the direction will switch to right with incremented length
            if root.left:
                dfs(root.left, right + 1, 0)
            
            # if there is a right child, continue the zigzag path starting from the right child
            # the direction will switch to left with incremented length
            if root.right:
                dfs(root.right, 0, left + 1)
        
        # start the depth-first search (DFS) from the root node with initial zigzag lengths set to 0
        dfs(root, 0, 0)
        
        # return the longest zigzag path length found
        return self.long_path

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
    print(s.longestZigZag(r1))
    r2 = TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))
    print(s.longestZigZag(r2))
    print(s.longestZigZag(TreeNode(1)))