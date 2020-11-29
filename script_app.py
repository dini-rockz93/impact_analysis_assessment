class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

def nodeDepth(node=None, depth=0):
    if node is None:
        return 0

    depthlen = depth * (depth + 1) // 2
    return depthlen + nodeDepth(node=node.left, depth= depth + 1) + nodeDepth(node=node.right, depth= depth + 1)
