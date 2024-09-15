class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case: if the current root is None, or matches one of the target nodes 
        # (p or q), return root
        if not root or root == p or root == q:
            return root
        
        # recursively search for the lowest common ancestor in the left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
        # recursively search for the lowest common ancestor in the right subtree
        r = self.lowestCommonAncestor(root.right, p, q)
        
        # if both left and right recursive calls return non-None values, it means p and q
        # are found in different subtrees
        # therefore, the current root is their lowest common ancestor
        if l and r:
            return root
        
        # if one of the recursive calls returns a non-None value, return that value
        # this means either p or q was found in one of the subtrees, and the other was 
        # found in the subtree where the current root is not
        return l or r