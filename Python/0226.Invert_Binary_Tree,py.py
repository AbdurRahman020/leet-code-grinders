from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertTreeLevel(root):
            if root != None:
                root.right, root.left = root.left, root.right
                invertTreeLevel(root.left)
                invertTreeLevel(root.right)
        
        invertTreeLevel(root)
        return root

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(2, TreeNode(1), TreeNode(3))
    r2 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    r3 = None
    print(s.invertTree(r1))
    print(s.invertTree(r2))
    print(s.invertTree(r3))
    