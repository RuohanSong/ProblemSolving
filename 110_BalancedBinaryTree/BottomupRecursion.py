# Definition for a binary tree node.
from collections import deque
from typing import Optional

# time complexity: O(n)
# space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(
            leftHeight, rightHeight
        )

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


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

root.left.left.left.left = TreeNode(0)

root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

root.right.left.left = TreeNode(0)
root.right.left.right = TreeNode(0)

root.right.right.left = TreeNode(0)
root.right.right.right = TreeNode(0)


print(bfs(root))
print(Solution().isBalanced(root))