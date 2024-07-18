class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # initialize pair count to 0
        self.pair_count = 0
        
        # Depth-first search (DFS) function to compute distances from each node
        def dfs(node):
            # base case: if node is None, return an empty list
            if not node:
                return []
            
            # leaf node case: return a list containing 1
            if not node.left and not node.right:
                return [1]
            
            # recursively calculate distances for left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # iterate through all pairs of distances from left and right subtrees
            for l in left_distances:
                for r in right_distances:
                    # if sum of distances is <= given distance, increment pair_count
                    if l + r <= distance:
                        self.pair_count += 1
            
            # return a list of distances incremented by 1, filtering out distances > given distance
            return [
                dist + 1
                for dist in left_distances + right_distances
                if dist + 1 <= distance
                ]

        # initial call to dfs function with the root of the tree
        dfs(root)
        
        # return the total count of valid pairs
        return self.pair_count

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    print(s.countPairs(r1, 3))
    r2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(5), TreeNode(6)))
    print(s.countPairs(r2, 3))
    r3 = TreeNode(7, TreeNode(1, TreeNode(6)), TreeNode(4, TreeNode(5, None, TreeNode(2)), TreeNode(3)))
    print(s.countPairs(r3, 3))