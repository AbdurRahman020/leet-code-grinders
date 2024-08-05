from typing import List, Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # helper function to perform depth-first search (DFS) and collect leaf node values
        def dfs(root: Optional[TreeNode], leaf: List[int]) -> None:
            # base case: # if the current node is None, return
            if not root:
                return
            
            # if the current node is a leaf node (no left and right children), add 
            # its value to the leaf list
            if not root.left and not root.right:
                leaf.append(root.val)
            
            # recursively perform DFS on the left subtree
            dfs(root.left, leaf)
            # recursively perform DFS on the right subtree
            dfs(root.right, leaf)
        
        # lists to store the leaf values of the two trees
        leaf1, leaf2 = [], []
        
        # perform DFS on the first tree and collect its leaf values
        dfs(root1, leaf1)
        # perform DFS on the second tree and collect its leaf values
        dfs(root2, leaf2)
        
        # compare the leaf sequences of the two trees
        return leaf1 == leaf2

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    r2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    print(s.leafSimilar(r1, r2))
    r3 = TreeNode(1, TreeNode(2), TreeNode(3))
    r4 = TreeNode(1, TreeNode(3), TreeNode(2))
    print(s.leafSimilar(r3, r4))