from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        def dfs(node):
            # store left and right chidren of current node
            node_left, node_right = node.left, node.right
            # clear left child
            node.left = None
            
            # if there is a left child, make it right child of current node
            if node_left:
                node.right = node_left
                # recursively flatten the left subtree and update the current 
                # node to the last node of the flattened left subtree
                node = dfs(node_left)
            # if there is a right child, make it right child of current node
            if node_right:
                node.right = node_right
                # recursively flatten the right subtree and update the current
                # node to the last node of the flattened right subtree
                node = dfs(node_right)
            # return the root of the flattened subtree
            return root
        
        # start the depth-first search from the root node
        dfs(root)
        # return the root of the flattened binary tree
        return root