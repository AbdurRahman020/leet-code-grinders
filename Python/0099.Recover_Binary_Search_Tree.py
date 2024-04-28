class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []
        def Inorder(root):
            if root != None:
                Inorder(root.left)
                result.append(root)
                Inorder(root.right)
        
        Inorder(root)

        new_result = sorted(result, key = lambda x: x.val)
        
        n = len(result)
        for i in range(n):
            m, n = result[i], new_result[i] 
            if m != n:
                m.val, n.val = n.val, m.val 
                break
        
        return root