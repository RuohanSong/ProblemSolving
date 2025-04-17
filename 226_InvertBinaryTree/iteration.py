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

        # to show the result for testing
        finaltree = []
        queue = deque([root])
        while queue:
            current = queue.popleft()
            finaltree.append(current.val)
            # swap
            current.left, current.right = current.right, current.left
            # if this current node has no children, it goes to the next loop
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return finaltree


# build a tree for testing
root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(6)
root.right.right = Node(9)

print(Solution().invertTree(root))



