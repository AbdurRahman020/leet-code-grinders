from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            if not root:
                return 0
            path = root.val + path*10
            if not root.left and not root.right:
                return path

            return dfs(root.left, path) + dfs(root.right, path)

        return dfs(root, 0)

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2), TreeNode(3))
    r2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    print(s.sumNumbers(r1))
    print(s.sumNumbers(r2))