from typing import List
from collections import deque

class TreeNode:
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # initialize sum as a class variable
        self.sum = 0
        
        def dfs(node):
            # base case: return if node is None
            if not node:
                return
            
            # recursively traverse right subtree
            dfs(node.right)
            # accumulate sum of nodes in reverse inorder
            self.sum += node.val
            # update node value to cumulative sum
            node.val = self.sum
            # recursively traverse left subtree
            dfs(node.left)
        
        # start depth-first traversal from the root
        dfs(root)
        
        # return the modified root node after transformation
        return root

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), 
                  TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
    print(s.bstToGst(r1).serialize())
    r2 = TreeNode(0, None , TreeNode(1))
    print(s.bstToGst(r2).serialize())