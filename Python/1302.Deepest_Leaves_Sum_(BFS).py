from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        Calculates the sum of values of the deepest leaves in a binary tree.
        
        :param root: The root of the binary tree.
        :type root: TreeNode
        
        :return: The sum of values of the deepest leaves.
        :rtype: int
        """
        # initialize a deque with the root node
        q = deque([root])
        
        # continue the loop until the deque is empty
        while q:
           # get the current depth by finding the length of the deque
           depth = len(q)
           # initialize depth_sum to store the sum of values at each depth
           depth_sum = 0
           # iterate through all nodes at the current depth
           for _ in range(0, depth):
               # pop the leftmost node from the deque
               node = q.popleft()
               # add the value of the current node to depth_sum
               depth_sum += node.val
               # if the left child of the current node exists, append it to the deque
               if node.left:
                   q.append(node.left)
               # if the right child of the current node exists, append it to the deque
               if node.right:
                   q.append(node.right)
        
        # return the total sum of node values at all depths
        return depth_sum
        
if __name__ == '__main__':
    s = Solution()
    print(s.deepestLeavesSum(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))))
    print(s.deepestLeavesSum(TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))))