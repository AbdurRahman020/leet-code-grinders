from collections import defaultdict

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
        # initialize a dictionary to store the sum of node values at each depth
        leaves_sum = defaultdict(int)
        
        def dfs(node, depth):
            # if the current node is None, return to exit the current call
            if not node:
                return
            
            # add the value of the current node to the sum at the current depth
            leaves_sum[depth] += node.val
            # recursively call the function for the left child with increased depth
            dfs(node.left, depth + 1)
            # recursively call the function for the right child with increased depth
            dfs(node.right, depth + 1)
        
        # start depth-first search from the root node with depth 0
        dfs(root, 0)
        # find the maximum depth in the leaves_sum dictionary
        max_depth = max(leaves_sum)
        
        # return the sum of node values at the deepest level
        return leaves_sum[max_depth]

if __name__ == '__main__':
    s = Solution()
    print(s.deepestLeavesSum(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))))
    print(s.deepestLeavesSum(TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))))