class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        def PreOrder(root):
            if root != None:
                result.append(root.val)
                PreOrder(root.left)
                PreOrder(root.right)
        
        PreOrder(root)
        return result

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    r2 = TreeNode(1)
    r3 = None
    print(s.preorderTraversal(r1))
    print(s.preorderTraversal(r2))
    print(s.preorderTraversal(r3))