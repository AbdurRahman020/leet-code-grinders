from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # initialize the maximum diameter to 0
        self.diameter_max = 0
        
        # define a helper function for depth-first search (DFS)
        def dfs(root: Optional[TreeNode]) -> int:
            # if the current node is None (base case), return 0
            if not root:
                return 0
            
            # recursively compute the depth of the left subtree and right subtree
            left, right = dfs(root.left), dfs(root.right)
            
            # update the diameter with the maximum value between the current diameter
            # and the sum of the depths of the left and right subtrees
            self.diameter_max = max(self.diameter_max, left + right)
            
            # Return the depth of the current subtree, depth of the current node is 
            # 1 (for the node itself) + max depth of left/right subtrees
            return 1 + max(left, right)
        
        # call the DFS function starting from the root of the tree
        dfs(root)
        
        # return the maximum diameter found
        return self.diameter_max

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2))
    print(s.diameterOfBinaryTree(r1))
    r2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(s.diameterOfBinaryTree(r2))