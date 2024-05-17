class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev_val):
            # base case: if the node is None, return 0
            if not node:
                return 0
            # Check if the value of the current node is greater than or equal 
            # to the previous maximum value
            elif node.val >= prev_val:
                # if yes, increment the count by 1 and recursively traverse the left 
                # and right subtrees
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                # if not, recursively traverse the left and right subtrees with the 
                # same previous maximum value
                return dfs(node.left, prev_val) + dfs(node.right, prev_val)
        
        # start the dfs traversal from the root node with the root node's value as 
        # the initial maximum value
        return dfs(root, root.val)

if __name__ == '__main__':
    s = Solution()
    print(s.goodNodes(TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))))
    print(s.goodNodes(TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))))