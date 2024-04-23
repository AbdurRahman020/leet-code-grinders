class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        def dfs(node):
            node_left, node_right = node.left, node.right
            node.left = None

            if node_left:
                node.right = node_left
                node = dfs(node_left)
            if node_right:
                node.right = node_right
                node = dfs(node_right)
            
            return root
        
        dfs(root)
        return root