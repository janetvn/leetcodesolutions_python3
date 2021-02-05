# https://www.geeksforgeeks.org/linked-list-set-1-introduction/


# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # initialize next as null


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        l1_current = l1
        l2_current = l2
        new_list = head

        while l1_current and l2_current:

            if l1_current.val < l2_current.val:
                new_list.next = ListNode(l1_current.val)
                new_list = new_list.next
                l1_current = l1_current.next

            elif l1_current.val > l2_current.val:
                new_list.next = ListNode(l2_current.val)
                new_list = new_list.next
                # newList = ListNode(l2Current.val)
                l2_current = l2_current.next

            else:
                new_list.next = ListNode(l1_current.val)
                l1_current = l1_current.next
                new_list = new_list.next
                new_list.next = ListNode(l2_current.val)
                l2_current = l2_current.next
                new_list = new_list.next

        if l1_current:
            new_list.next = l1_current  # append remaining l1 list.

        if l2_current:
            new_list.next = l2_current  # append remaining l2 list.

        return head.next
