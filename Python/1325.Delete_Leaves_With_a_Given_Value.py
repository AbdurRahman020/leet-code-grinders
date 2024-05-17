from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # base case: if root is None, return None
        if root is None:
            return None
        
        # recursively call removeLeafNodes on left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # if current node is leaf and its value matches target, remove it
        if root.left is None and root.right is None and root.val == target:
            return None
        
        # if current node is leaf but its value doesn't match target, keep it
        if not root.left and not root.right and root.val == target:
            return
        
        # return the modified root
        return root

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4)))
    print(s.removeLeafNodes(r1, 2))
    r2 = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3))
    print(s.removeLeafNodes(r2, 3))
    r3 = TreeNode(1, TreeNode(2, TreeNode(2, TreeNode(2))))
    print(s.removeLeafNodes(r3, 2))