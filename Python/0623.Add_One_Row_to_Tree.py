from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # if the depth is 1, insert a new node with the given value as the root
        if depth == 1:
            return TreeNode(val, root, None)
        
        # define a depth-first search function to traverse the tree
        def dfs(root, lvl):
            # if the root is None, return
            if not root:
                return
            # decrement the depth level
            lvl -= 1
            # if the depth level is 1, insert new nodes with the given value
            if lvl == 1:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
            # otherwise, continue traversing the tree recursively
            else:
                dfs(root.left, lvl)
                dfs(root.right, lvl)
        
        # start the depth-first search from the root node with the specified depth
        dfs(root, depth)
        
        # return the modified root node
        return root
    
if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
    print(s.addOneRow(r1, 1, 2))
    r2 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
    print(s.addOneRow(r2, 1, 3))