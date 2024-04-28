class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        result = []
        
        def dfs(root, path):
            if root == None:
                return []
            if root.left == None and root.right == None:
                return result.append(''.join(path) + str(root.val))
            
            path.append(str(root.val) + '->')
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return result

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    r2 = TreeNode(1)
    r3 = None
    print(s.binaryTreePaths(r1))
    print(s.binaryTreePaths(r2))
    print(s.binaryTreePaths(r3))