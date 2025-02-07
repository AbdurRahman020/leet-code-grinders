from typing import Optional
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        # check if the root is empty
        if not root:
            return True
        
        # initialize a deque with the root node
        q = deque([root])
        
        # loop until the deque is empty
        while q:
            # get the number of nodes at the current level
            n = len(q)
            left = 0
            # iterate over all nodes at the current level
            for _ in range(n):
                # pop the leftmost node from the deque
                curr = q.popleft()
                # if it's the first node in the level, update the leftmost value
                if not left:
                    left = curr.val
                 # add the left child of the current node to the deque
                if curr.left:
                    q.append(curr.left)
                 # add the right child of the current node to the deque
                if curr.right:
                    q.append(curr.right)
        
        # return the value of the leftmost node at the bottom level
        return left
    
    def findBottomLeftValue2(self, root: Optional[TreeNode]) -> int:
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
    
    print(s.findBottomLeftValue1(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(s.findBottomLeftValue1(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))))
    
    print(s.findBottomLeftValue2(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(s.findBottomLeftValue2(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))))
