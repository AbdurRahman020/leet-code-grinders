from typing import List, Optional
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # if the root is None, return an empty list because there are no nodes to delete
        if not root:
            return []
        
        # initialize a deque (double-ended queue) to store nodes along with a flag indicating if it's a root
        queue = deque([(root, False)])
        # initialize an empty list to store the resulting forest (list of root nodes of each remaining tree)
        forest = []
        
        # process nodes in the queue until it's empty
        while queue:
            # dequeue a node and its root flag
            node, is_root = queue.popleft()
            
            # if the node is not a root and its value is not in the to_delete list, add it to the forest
            if not is_root and node.val not in to_delete:
                forest.append(node)
            
            # determine if the current node is a root (not in to_delete list)
            is_root = not node.val in to_delete
            
            # process the left child of the current node
            if node.left: 
                # enqueue the left child with the current node's is_root status
                queue.append((node.left, is_root))
                # if the left child's value is in the to_delete list, detach it by setting it to None
                if node.left.val in to_delete:
                    node.left = None
            
            # process the right child of the current node
            if node.right:
                # enqueue the right child with the current node's is_root status
                queue.append((node.right, is_root))
                # if the right child's value is in the to_delete list, detach it by setting it to None
                if node.right.val in to_delete:
                    node.right = None
        
        # return the resulting forest, which contains all valid root nodes after deletion
        return forest

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print([i.serialize() for i in s.delNodes(r1, [3, 5])])
    r2 = TreeNode(1, TreeNode(2), TreeNode(4, TreeNode(3)))
    print([i.serialize() for i in s.delNodes(r2, [3])])