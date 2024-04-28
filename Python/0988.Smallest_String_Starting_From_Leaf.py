class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        result = []
        def dfs(root, val):
            if not root:
                return False
            
            val += chr(ord('a') + root.val)
            left = dfs(root.left, val)
            right = dfs(root.right, val)

            if not left and not right:
                result.append(val[::-1])
            return True
        
        dfs(root, '')
        result.sort()
        
        return result[0]

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2)))
    r2 = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
    r3 = TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode())), TreeNode(1, TreeNode()))
    print(s.smallestFromLeaf(r1))
    print(s.smallestFromLeaf(r2))
    print(s.smallestFromLeaf(r3))