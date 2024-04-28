from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                if root:
                    level.append(root.val)
                    q.append(root.left)
                    q.append(root.right)

            if level:
                result.append(level)
                
        return result

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    r2 = TreeNode(1)
    r3 = None
    print(s.levelOrder(r1))
    print(s.levelOrder(r2))
    print(s.levelOrder(r3))