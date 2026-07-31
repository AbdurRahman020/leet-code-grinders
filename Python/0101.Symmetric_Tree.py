from typing import Optional
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        # define a helper function to check whether two subtrees are mirror images
        def isMirror(l, r):
            # if both nodes are empty, they are symmetric
            if not l and not r:
                return True
            
            # if one node is missing or the values differ, the tree is not symmetric
            if not l or not r or l.val != r.val:
                return False
            
            # recursively compare the outer and inner pairs of child nodes
            return isMirror(l.left, r.right) and isMirror(l.right, r.left)

        # check whether the left and right subtrees are mirror images
        return isMirror(root.left, root.right)

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        # if the tree is empty, it is symmetric
        if not root:
            return True

        # initialize a stack with the left and right children of the root
        stack = [(root.left, root.right)]

        # process node pairs until the stack becomes empty
        while stack:
            # remove the top pair of nodes from the stack
            l, r = stack.pop()

            # if both nodes are empty, continue with the next pair
            if not l and not r:
                continue
            
            # if one node is missing or the values differ, return False
            if not l or not r or l.val != r.val:
                return False

            # push the outer pair of child nodes onto the stack
            stack.append((l.left, r.right))
            
            # push the inner pair of child nodes onto the stack
            stack.append((l.right, r.left))

        # if all node pairs match, return True
        return True

    def isSymmetric3(self, root: Optional[TreeNode]) -> bool:
        # if the tree is empty, it is symmetric
        if not root:
            return True

        # initialize a queue with the left and right children of the root
        queue = deque()
        queue.append((root.left, root.right))

        # process node pairs until the queue becomes empty
        while queue:
            # remove the front pair of nodes from the queue
            l, r = queue.popleft()

            # if both nodes are empty, continue with the next pair
            if not l and not r:
                continue
            
            # if one node is missing or the values differ, return False
            if not l or not r or l.val != r.val:
                return False

            # add the outer pair of child nodes to the queue
            queue.append((l.left, r.right))
            
            # add the inner pair of child nodes to the queue
            queue.append((l.right, r.left))

        # if all node pairs match, return True
        return True


if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                  TreeNode(2, TreeNode(4), TreeNode(3)))
    r2 = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                  TreeNode(2, None, TreeNode(3)))

    print(s.isSymmetric1(r1))
    print(s.isSymmetric1(r2))

    print(s.isSymmetric2(r1))
    print(s.isSymmetric2(r2))

    print(s.isSymmetric3(r1))
    print(s.isSymmetric3(r2))
