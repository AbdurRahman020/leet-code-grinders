from typing import List, Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def PostOrder(root):
            if root != None:
                PostOrder(root.left)
                PostOrder(root.right)
                result.append(root.val)
        
        PostOrder(root)
        
        return result

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    r2 = TreeNode(1)
    r3 = None
    print(s.postorderTraversal(r1))
    print(s.postorderTraversal(r2))
    print(s.postorderTraversal(r3))