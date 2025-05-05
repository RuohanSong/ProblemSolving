# Definition for a binary tree node.
from collections import deque
from typing import Optional

# time complexity: O(n log(n))
# space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # a null node has the height of -1
    def height(self, root):
        if not root:
            return -1
        # height of a tree is the larger height of its subtree plus 1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # an empty tree is balanced
        if not root:
            return True

        # to be balanced, a tree must
        return (
                # have height difference of left and right subtrees equal to 1 or 0
                abs(self.height(root.left) - self.height(root.right)) < 2
                # have balanced left and right subtrees
                and self.isBalanced(root.left)
                and self.isBalanced(root.right)
        )


# traverse the tree with root in BFS, return a list
def bfs(root: [TreeNode]):
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
root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(2)

root.left.left = TreeNode(2)
root.left.right = TreeNode(0)

root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(0)

# root.left.left.left.left = TreeNode(0)

root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

root.right.left.left = TreeNode(0)
root.right.left.right = TreeNode(0)

root.right.right.left = TreeNode(0)
root.right.right.right = TreeNode(0)


print(bfs(root))
print(Solution().isBalanced(root))


