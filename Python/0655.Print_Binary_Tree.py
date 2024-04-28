class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: TreeNode) -> list[list[str]]:
        def dfs(node, count):
            if not node:
                return count
            return max(dfs(node.left, count + 1), dfs(node.right, count + 1))
        
        height = dfs(root, -1)

        row_length, col_length = height + 1, 2 ** (height + 1) - 1
        tree_plot_result = [["" for _ in range(0, col_length)] for _ in range(0, row_length)]

        r, c = 0, (col_length - 1) // 2
        
        def treePlot(node, r, c):
            if not node:
                return

            tree_plot_result[r][c] = str(node.val)
            
            x = 2 ** (height - r - 1)

            if node.left:
                treePlot(node.left, r + 1, c - x)
            if node.right:
                treePlot(node.right, r + 1, c + x)
        
        treePlot(root, r, c)

        return tree_plot_result

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2))
    r2 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    print(s.printTree(r1))
    print(s.printTree(r2))