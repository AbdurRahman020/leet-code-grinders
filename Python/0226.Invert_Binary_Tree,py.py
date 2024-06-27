from typing import Optional, List
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def serialize(self) -> List[int]:
        """Serialize the tree into a list"""
        result = []
        
        if self is None:
            return result
        
        queue = deque([self])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
                
        # remove trailing None values
        while result and result[-1] is None:
            result.pop()
            
        return result
        
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
    r3 = TreeNode(None)
    print(s.invertTree(r1).serialize())
    print(s.invertTree(r2).serialize())
    print(s.invertTree(r3).serialize())
    