class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root:TreeNode, Left:bool) -> int:
            if not root:
                return 0
            if not root.left and not root.right and Left:
                return root.val
            return dfs(root.left, True) + dfs(root.right, False)
        
        return dfs(root, False)

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    r2 = TreeNode(1)
    print(s.sumOfLeftLeaves(r1))
    print(s.sumOfLeftLeaves(r2))