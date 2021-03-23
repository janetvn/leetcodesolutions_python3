# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return

        a_p = headA
        b_p = headB

        while a_p != b_p:
            if a_p is None:
                a_p = headB
            else:
                a_p = a_p.next

            if b_p is None:
                b_p = headA
            else:
                b_p = b_p.next

        return a_p
