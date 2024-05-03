from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        # initialize an empty list to store the result
        result = []
        # initialize a deque for breadth-first search
        q = deque()
        # append the root to the deque
        q.append(root)
        
        # perform breadth-first search
        while q:
            # initialize an empty list to store values at the current level
            level = []
            # iterate over the nodes at the current level
            for i in range(len(q)):
                # pop the leftmost node from the deque
                root = q.popleft()
                # if the node exists, append its value to the level list
                if root:
                    # append the left and right children of the current node to the deque
                    level.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
            
            # if the level list is not empty, append it to the result list
            if level:
                result.append(level)
         
        return result

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    r2 = TreeNode(1)
    r3 = None
    print(s.levelOrder(r1))
    print(s.levelOrder(r2))
    print(s.levelOrder(r3))