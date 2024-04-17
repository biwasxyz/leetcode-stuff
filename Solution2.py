# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # type: ignore # Initialize dummy head
        current = dummy  # Initialize current node
        carry = 0  # Initialize carry-over

        # Traverse both input linked lists simultaneously
        while l1 or l2 or carry:
            # Calculate sum of current digits along with carry
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = total // 10  # Update carry
            digit = total % 10  # Calculate digit value

            # Create a new node with the digit value and append it
            current.next = ListNode(digit) # type: ignore
            current = current.next

            # Move to the next nodes in both input lists, if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next