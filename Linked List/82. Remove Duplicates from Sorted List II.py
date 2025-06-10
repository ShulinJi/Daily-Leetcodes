# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# O(n) and O(1) complexity
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = None
        curr = head
        while curr is not None:
            # if we found a duplicate, we skip the duplicates
            dup = False
            while curr.next is not None and curr.val == curr.next.val:
                curr = curr.next
                dup = True
            
            # if duplicate, prev is the one before duplicate node
            if dup:
                # if it includes the head, then we set the head to the next new non-dup node
                if prev is None:
                    head = curr.next
                # if it is in middle, then just attach prev to the next non-dup node
                else:
                    prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return head


# more clear approach by adding a fake head
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node
        # before the sublist of duplicates
        pred = sentinel

        while head:
            # If it's the beginning of a duplicates sublist
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next

                # Skip all duplicates
                pred.next = head.next

            # Otherwise, move predecessor
            else:
                pred = pred.next

            # move forward
            head = head.next

        return sentinel.next
