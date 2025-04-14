# time complexity: O(n+m)
# space complexity: O(n+m)
# each call adds a new frame to the call stack


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Example 1: both lists have values
node1_1 = ListNode(1)
node1_2 = ListNode(2)
node1_3 = ListNode(4)

node1_1.next = node1_2
node1_2.next = node1_3

node2_1 = ListNode(1)
node2_2 = ListNode(3)
node2_3 = ListNode(4)

node2_1.next = node2_2
node2_2.next = node2_3


merged = Solution().mergeTwoLists(node1_1, node2_1)
# Expected: [1, 2, 3, 4, 5, 6]
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
print("null")