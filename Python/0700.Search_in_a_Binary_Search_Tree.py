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

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case: if the root is None or we've reached a leaf node
        if root is None:
            return None
        
        # if the value we're searching for is greater than the current node's value
        if val > root.val:
            # recur on the right subtree
            return self.searchBST(root.right, val)
        # if the value we're searching for is less than the current node's value
        elif val < root.val:
            # recur on the left subtree
            return self.searchBST(root.left, val)
        # if the value matches the current node's value
        else:
            # return the current node
            return root

if __name__ == '__main__':
    s = Solution()
    r = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    print(s.searchBST(r, 2).serialize())
    print(s.searchBST(r, 5))