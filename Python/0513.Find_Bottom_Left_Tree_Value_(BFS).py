from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
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

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(2, TreeNode(1), TreeNode(3))
    r2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    print(s.findBottomLeftValue(r1))
    print(s.findBottomLeftValue(r2))