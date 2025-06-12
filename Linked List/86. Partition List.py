# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) and O(1)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        # create 2 lists for before and after (put all nodes that are smaller in before, otheres in after)
        before = ListNode(0)
        after = ListNode(0)
        before_head = before
        after_head = after
            
        curr = head
        # record the tail of before list so that we could attach it to after list
        before_tail = before
        while curr is not None:
            # record the next node b/c we are going to detach current node from linked list to before/after list
            next_node = curr.next
            if curr.val < x:
                # remove node from linked list and add it to before list
                curr.next = None
                before.next = curr
                before = before.next
                before_tail = curr
            else:
                curr.next = None
                after.next = curr
                after = after.next
            curr = next_node

        # if either of the list is None, then we just return the other one
        if before_head.next is None:
            return after_head.next
        if after_head.next is None:
            return before_head.next
        
        # attach the tail of before list to the head of the after list
        before_tail.next = after_head.next
        return before_head.next


            