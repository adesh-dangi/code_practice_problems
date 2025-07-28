# https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid_node = head
        end_node = head

        while end_node!=None and end_node.next!=None:
            mid_node = mid_node.next
            end_node = end_node.next.next
        return mid_node

cases = [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 4),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))), 4),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 5),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))))))), 5)
]

for case in cases:
    head, expected = case
    sol = Solution()
    result = sol.middleNode(head)
    assert result.val == expected, f"Expected {expected}, but got {result.val}"
else:
    print("All test cases passed!")