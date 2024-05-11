class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        # initialize an empty list to store serialized node values
        result = []
        
        # define a Depth-First Search (DFS) function to serialize the tree
        def dfs(root):
            # if the current node is None
            if not root:
                # append 'None' to represent an empty node
                result.append('None')
                return
            # append the string representation of the node's value
            result.append(str(root.val))
            # recursively serialize the left and right subtrees
            dfs(root.left)
            dfs(root.right)
        
        # start the DFS serialization process
        dfs(root)
        
        # join the serialized node values with commas and return the result as a string
        return ','.join(result)
    
    def deserialize(self, data: str) -> TreeNode:
        # split the serialized string by commas to get a list of node values
        lst = data.split(',')
        self.index = 0
        
        # define a DFS function to deserialize the tree
        def dfs():
            # if the current value is 'None'
            if lst[self.index] == 'None':
                # move to the next index
                self.index += 1
                # return None to represent an empty node
                return None
            # create a new TreeNode with the integer value of the current string
            _root = TreeNode(int(lst[self.index]))
            # move to the next index
            self.index += 1
            # recursively deserialize the left and right subtrees
            _root.left = dfs()
            _root.right = dfs()
            # return the current node
            return _root
        
        # start the DFS deserialization process and return the root of the deserialized tree
        return dfs()
        
if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    
    r1 = TreeNode(1)
    r1.left = TreeNode(2)
    r1.right = TreeNode(3)
    r1.right.left = TreeNode(4)
    r1.right.right = TreeNode(5)
    print(deser.deserialize(ser.serialize(r1)))
    
    r2 = TreeNode(None)
    print(deser.deserialize(ser.serialize(r2)))