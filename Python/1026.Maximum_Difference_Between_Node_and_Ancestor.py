from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, min_val, max_val):
            if not root:
                return max_val - min_val
            
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)

            left = dfs(root.left, min_val, max_val)
            right = dfs(root.right, min_val, max_val)

            return max(left, right)
        
        return dfs(root, root.val, root.val)

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
    r2 = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
    print(s.maxAncestorDiff(r1))
    print(s.maxAncestorDiff(r2))