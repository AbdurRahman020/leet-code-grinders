from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        # if the tree is empty, it is considered an even-odd tree
        if not root:
            return True
        
        # initialize the level counter
        level = 0
        # initialize a deque to store nodes for BFS
        queue = deque()
        # add the root node to the queue
        queue.append(root)
        
        while queue:
            # initialize a variable to store the value of the previous node
            prev_val = None
            # process nodes at the current level
            for _ in range(len(queue)):
                # dequeue the front node from the queue
                root = queue.popleft()
                
                # check if the current node's value violates the rules of an even-odd tree
                if level %2 == 0: # For even levels
                    if root.val % 2 != 1 or (prev_val is not None and prev_val >= root.val):
                        return False
                else: # For odd levels
                    if root.val % 2 != 0 or (prev_val is not None and prev_val <= root.val):
                        return False
                
                # update the previous value for the next iteration
                prev_val = root.val
                
                # add the children of the current node to the queue for processing in the next level
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            # move to the next level
            level += 1
        
        # if the tree satisfies the conditions at every level, return True
        return True

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(10, TreeNode(3, TreeNode(12), TreeNode(8))), TreeNode(4, TreeNode(7, TreeNode(6)), TreeNode(9, None, TreeNode(2))))
    r2 = TreeNode(5, TreeNode(4, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(7)))
    r3 = TreeNode(5, TreeNode(9, TreeNode(3), TreeNode(5)), TreeNode(1, TreeNode(7)))
    print(s.isEvenOddTree(r1))
    print(s.isEvenOddTree(r2))
    print(s.isEvenOddTree(r3))