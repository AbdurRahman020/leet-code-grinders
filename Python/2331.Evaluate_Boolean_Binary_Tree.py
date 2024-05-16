from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # if value is 0, return False
        if root.val == 0:
            return False
        # if value is 1, return True
        elif root.val == 1:
            return True
        # if value is 2, evaluate left or right subtree
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # if value is 3, evaluate left or right subtree.
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        # default return False if value doesn't match any defined condition
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))))
    print(s.evaluateTree(TreeNode(0)))