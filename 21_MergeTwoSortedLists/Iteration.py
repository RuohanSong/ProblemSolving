# time complexity: O(n+m)
# space complexity: O(1)
# only a few pointers are used constantly

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # start with a dummy node
        dummy = ListNode()
        currentnode = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                currentnode.next = list1
                list1 = list1.next
            else:
                currentnode.next = list2
                list2 = list2.next
            currentnode = currentnode.next

        # at this point, at least one of the two linked lists can still have nodes
        # so connect the non-null list to the end of the merged list
        # if one of them or both of them are empty, it will also run this line
        currentnode.next = list1 if list1 is not None else list2

        return dummy.next


# Example 1: both lists have values
node1_1 = ListNode(3)
# node1_2 = ListNode(2)
# node1_3 = ListNode(4)

# node1_1.next = node1_2
# node1_2.next = node1_3

node2_1 = ListNode(1)
node2_2 = ListNode(5)
node2_3 = ListNode(6)

node2_1.next = node2_2
node2_2.next = node2_3


merged = Solution().mergeTwoLists(node1_1, node2_1)
# Expected: [1, 2, 3, 4, 5, 6]
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
print("null")
