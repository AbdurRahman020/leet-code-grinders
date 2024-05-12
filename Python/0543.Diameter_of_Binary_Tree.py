from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter_max = 0
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            self.diameter_max = max(self.diameter_max, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter_max

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2))
    r2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(s.diameterOfBinaryTree(r1))
    print(s.diameterOfBinaryTree(r2))