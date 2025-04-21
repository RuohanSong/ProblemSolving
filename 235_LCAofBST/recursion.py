from collections import deque

# time complexity: O(n) worst case
# space complexity: O(n) for worst case with skewed BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# bfs function for testing
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
root = TreeNode(6)
node1 = root.left = TreeNode(2)
node2 = root.right = TreeNode(8)

node3 = node1.left = TreeNode(0)
node4 = node1.right = TreeNode(4)

node5 = node2.left = TreeNode(7)
node6 = node2.right = TreeNode(9)

node7 = node4.left = TreeNode(3)
node8 = node4.right = TreeNode(5)

print(bfs(root))
print(Solution().lowestCommonAncestor(root, node1, node4).val)
print(Solution().lowestCommonAncestor(root, node1, node2).val)


