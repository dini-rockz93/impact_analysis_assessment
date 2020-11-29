from collections import deque

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def deserialize(tree):

        
        if not tree:
            return None
        root = BinaryTree(tree['value'])
        maps = deque([tree])
        nodes = deque([root])
        while nodes:
            frontNode = nodes.popleft()
            frontMap = maps.popleft()
            left, right = frontMap.get('left'), frontMap.get('right')
            if left:
                frontNode.left = BinaryTree(left['value'])
                maps.append(left)
                nodes.append(frontNode.left)
            if right:
                frontNode.right = BinaryTree(right['value'])
                maps.append(right)
                nodes.append(frontNode.right)
        return root
    

def nodeDepth(node=None, depth=0):
    if node is None:
        return 0

    depthlen = depth * (depth + 1) // 2
    return depthlen + nodeDepth(node=node.left, depth= (depth + 1) * 2) + nodeDepth(node=node.right, depth= (depth + 1) * 3)
