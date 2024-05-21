from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # base case: if the root is None, return 0
        if root is None:
            return 0
        
        # if the value of the current node is greater than the high value,
        # then recursively search in the left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # if the value of the current node is less than the low value,
        # then recursively search in the right subtree
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # if the value of the current node is within the range [low, high],
        # include its value in the sum, and recursively search in both left
        # and right subtrees
        else:
            return (
                root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
            )

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(s.rangeSumBST(r1, 7, 15))
    r2 = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, None, TreeNode(6))), TreeNode(15,TreeNode(13), TreeNode(18)))
    print(s.rangeSumBST(r2, 6, 10))