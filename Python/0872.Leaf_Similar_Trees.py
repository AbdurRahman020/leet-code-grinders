class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        
        return leaf1 == leaf2

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    r2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    print(s.leafSimilar(r1, r2))
    r3 = TreeNode(1, TreeNode(2), TreeNode(3))
    r4 = TreeNode(1, TreeNode(3), TreeNode(2))
    print(s.leafSimilar(r3, r4))