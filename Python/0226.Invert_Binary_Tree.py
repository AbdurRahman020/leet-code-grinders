from typing import Optional, List
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self) -> List[int]:
        """Serialize the tree into a list"""
        result = []

        if self is None:
            return result

        queue = deque([self])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Solution(object):
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if the current node is not None
        if root:
            # swap the left and right children of the current node
            root.right, root.left = root.left, root.right
            # recursively invert the left subtree
            self.invertTree1(root.left)
            # recursively invert the right subtree
            self.invertTree1(root.right)

        # return the root of the inverted tree
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(2, TreeNode(1), TreeNode(3))
    r2 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                  TreeNode(7, TreeNode(6), TreeNode(9)))
    r3 = TreeNode(None)

    print(s.invertTree1(r1).serialize())
    print(s.invertTree1(r2).serialize())
    print(s.invertTree1(r3).serialize())

    print(s.invertTree2(r1).serialize())
    print(s.invertTree2(r2).serialize())
    print(s.invertTree2(r3).serialize())
