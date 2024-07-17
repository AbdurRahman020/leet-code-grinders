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
        # convert to_delete list to a set for O(1) average time complexity membership check
        nodes_to_delete = set(to_delete)
        # initialize an empty list to store the resulting forest of trees
        forest = []

        # define a function to perform depth-first search (DFS)
        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            # base case: if node is None, return None (no action needed)
            if not node:
                return None
            
            # check if the current node's value is in the nodes_to_delete set
            node_deleted = node.val in nodes_to_delete

            # if the current node is a root (and not to be deleted), add it to the forest
            if is_root and not node_deleted:
                forest.append(node)
            
            # recursively process the left and right children of the current node, pass along
            # whether the current node is deleted to determine the status of its children
            node.left = dfs(node.left, node_deleted)
            node.right = dfs(node.right, node_deleted)
            
            # return None if the current node is deleted; otherwise, return the current node
            return None if node_deleted else node
        
        # start the DFS traversal from the root node with is_root set to True
        dfs(root, True)
        
        # return the resulting forest of trees after deletion operations
        return forest


if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print([i.serialize() for i in s.delNodes(r1, [3, 5])])
    r2 = TreeNode(1, TreeNode(2), TreeNode(4, TreeNode(3)))
    print([i.serialize() for i in s.delNodes(r2, [3])])