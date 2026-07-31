from typing import Optional
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if both trees are empty, indicating equality
        if not p and not q:
            return True
        # check if either tree is empty, indicating inequality
        if not p or not q:
            return False
        # check if current nodes have equal values and recursively check left and right subtrees
        return p.val == q.val and self.isSameTree1(
            p.left, q.left) and self.isSameTree1(p.right, q.right)

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            p, q = stack.pop()
            if p or q:
                if not p or not q or p.val != q.val:
                    return False

                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

        return True

    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))

        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True


if __name__ == '__main__':
    s = Solution()

    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))

    print(s.isSameTree1(p1, q1))
    print(s.isSameTree2(p1, q1))
    print(s.isSameTree3(p1, q1))

    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))

    print(s.isSameTree1(p2, q2))
    print(s.isSameTree2(p2, q2))
    print(s.isSameTree3(p2, q2))

    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))

    print(s.isSameTree1(p3, q3))
    print(s.isSameTree2(p3, q3))
    print(s.isSameTree3(p3, q3))
