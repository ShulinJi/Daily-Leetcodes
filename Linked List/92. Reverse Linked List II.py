# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr = head
        prev = None

        # locate curr to the first node that needs to be reversed, prev is the node before the recersed list
        # use > 1, not 0 because we start at the first node, which is already 1
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        
        # Reason to record: record the current head(curr), that will become tail after reverse, and con needs to attach to the new head 
        # after the reverse 
        tail = curr
        con = prev

        while right > 0:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            right -= 1
        # after reverse, the curr would become the first node after the reversed list, prev is the last node of reversed list
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        
        return head
# how to reverse a linked list
# Before looking at the algorithm, it's important to understand how the link reversal will work and what set of pointers will be required for the same. Let's say we have a linked list consisting of three different nodes, A → B → C and we want to reverse the links between the nodes and obtain A ← B ← C.

# Suppose we have at our disposal, two pointers. One of them points to the node A and the other one points to the node B. Let's call these pointers prev and cur respectively. We can simply use these two pointers to reverse the link between A and B.

# cur.next = prev
# The only problem with this is, we don't have a way of progressing further i.e. once we do this, we can't reach the node C. That's why we need a third pointer that will help us continue the link reversal process. So, we do the following instead.

# third = cur.next
# cur.next = prev
# prev = cur
# cur = third

