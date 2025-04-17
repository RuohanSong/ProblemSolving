# time complexity: O(n)
# space complexity: best case O(log(n)), worst case O(n)

from typing import Optional

import null


# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# build a tree for testing
root = Node(5)
root.left = Node(12)
root.right = Node(13)

root.left.left = Node(7)
root.left.right = Node(14)

root.right.right = Node(2)

root.left.left.left = Node(17)
root.left.left.right = Node(23)

root.left.right.left = Node(27)
root.left.right.right = Node(3)

root.right.right.left = Node(8)
root.right.right.right = Node(11)

print(Solution().maxDepth(root))