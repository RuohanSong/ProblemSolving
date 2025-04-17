# Definition for a binary tree node.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[Node]):
        if not root:
            return None

        # temporary variables
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        # swap left and right child
        root.left = right
        root.right = left

        return root


# traverse the tree with root in BFS, return a list
def bfs(root: [Node]):
    if not root:
        return None
    result = []
    # deque has to have iterable arguments, so we pass a list with one element
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# build a tree for testing
root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(6)
root.right.right = Node(9)

print(bfs(root))
finaltree = bfs(Solution().invertTree(root))
print(finaltree)

