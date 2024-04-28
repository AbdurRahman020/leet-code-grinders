class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root, None)

        def dfs(root, lvl):
            if not root:
                return
            lvl -= 1
            if lvl == 1:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
            else:
                dfs(root.left, lvl)
                dfs(root.right, lvl)
        
        dfs(root, depth)
        
        return root
    
if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
    print(s.addOneRow(r1, 1, 2))
    r2 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
    print(s.addOneRow(r2, 1, 3))