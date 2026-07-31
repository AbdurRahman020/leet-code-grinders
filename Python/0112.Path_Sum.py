from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if the root is None, return False
        if not root:
            return False

        # initialize a queue for level-order traversal, each element contains (node, sum)
        queue = deque()
        queue.append((root, root.val))

        # iterate through the queue until it's empty
        while queue:
            # dequeue the current node and its accumulated sum
            node, val = queue.popleft()

            # check if the current node is a leaf node and if its accumulated sum equals the target sum
            if not node.left and not node.right:
                if val == targetSum:
                    return True

            # enqueue the left child if it exists, updating the accumulated sum
            if node.left:
                queue.append((node.left, val + node.left.val))

            # enqueue the right child if it exists, updating the accumulated sum
            if node.right:
                queue.append((node.right, val + node.right.val))

        # if no path with the target sum is found, return False
        return False

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            # base case: if the node is None, return False
            if not node:
                return False

            # update current sum by adding the value of the current node
            curr_sum += node.val

            # if the current node is a leaf node, check if the current sum equals the target sum
            if not node.left and not node.right:
                return curr_sum == targetSum

            # recursively call dfs for left and right children
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

        # base case: (an empty tree) if root is None, return None
        if not root:
            return None

        # start the depth-first search from the root with initial sum 0
        return dfs(root, 0)

    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case: if the node is None, return False
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum - root.val == 0

        targetSum -= root.val

        return self.hasPathSum3(root.left, targetSum) or self.hasPathSum3(root.right, targetSum)


if __name__ == '__main__':
    s = Solution()

    print(s.hasPathSum1(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(
        2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))
    print(s.hasPathSum1(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.hasPathSum1(TreeNode(), 0))

    print(s.hasPathSum2(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(
        2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))
    print(s.hasPathSum2(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.hasPathSum2(TreeNode(), 0))

    print(s.hasPathSum3(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(
        2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))
    print(s.hasPathSum3(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.hasPathSum3(TreeNode(), 0))
