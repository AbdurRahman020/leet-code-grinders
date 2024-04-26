class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(root, depth):
            # base case: if the root is None, return 0 depth and 0 value
            if not root:
                return 0, 0
            
            # recursive calls to the left children
            left = dfs(root.left, depth + 1)
            # recursive calls to the right children
            right = dfs(root.right, depth + 1)
            
            # determine the leftmost node at the bottom level
            if left[1] == 0 and right[1] == 0:
                return root.val, depth
            if left[1] < right[1]:
                return right
            return left
        
        # start the depth-first search from the root with a depth of 0
        return dfs(root, 0)[0]

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(2, TreeNode(1), TreeNode(3))
    r2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    print(s.findBottomLeftValue(r1))
    print(s.findBottomLeftValue(r2))