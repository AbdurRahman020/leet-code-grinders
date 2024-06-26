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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # check if the root is None
        if not root:
            return None
        
        # perform inorder traversal to get nodes in sorted order
        inorder_nodes = []
        self.inorderTraversal(root, inorder_nodes)
        
        # construct a balanced BST from the sorted nodes
        return self.sortedArrayToBST(inorder_nodes, 0, len(inorder_nodes) - 1)
    
    def inorderTraversal(self, root: Optional[TreeNode], nodes: List) -> None:
        # base case: if root is None, return
        if root is None:
            return
        
        # traverse left subtree recursively
        self.inorderTraversal(root.left, nodes)
        # append current node to the list during inorder traversal
        nodes.append(root)
        # traverse right subtree recursively
        self.inorderTraversal(root.right, nodes)
    
    def sortedArrayToBST(self, nodes: List, start: int, end: int) -> Optional[TreeNode]:
        # base case: if start index is greater than end index, return None
        if start > end:
            return None
        
        # calculate middle index
        mid = (start + end) // 2
        # create a new TreeNode with the middle element as root
        root = nodes[mid]
        # recursively construct left subtree from elements before mid
        root.left = self.sortedArrayToBST(nodes, start, mid - 1)
        # recursively construct right subtree from elements after mid
        root.right = self.sortedArrayToBST(nodes, mid + 1, end)
        
        # return the root of the constructed subtree
        return root

if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(s.balanceBST(r1).serialize())
    r2 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(s.balanceBST(r2).serialize())