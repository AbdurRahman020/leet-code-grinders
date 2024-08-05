from typing import List, Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        result = []
        def Inorder(root):
            if root != None:
                Inorder(root.left)
                result.append(root.val)
                Inorder(root.right)
        
        Inorder(root)
        return result 
    
if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(s.inorderTraversal(r1))
    r2 = TreeNode(1)
    print(s.inorderTraversal(r2))
    r3 = None
    print(s.inorderTraversal(r3))