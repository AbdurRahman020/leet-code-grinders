from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1 
        
if __name__ == '__main__':
    s = Solution()
    r1 = None
    r2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    r3 = TreeNode(1)
    print(s.countNodes(r1))
    print(s.countNodes(r2))
    print(s.countNodes(r3))