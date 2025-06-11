# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        tail = head
        length = 1
        while tail.next is not None:
            length += 1
            tail = tail.next
        # move number of rotation nodes from back to front
        rotation = k % length
        # if rotation == 0, then it means we don't need to rotate and just return the original
        if rotation == 0:
            return head
        # find nth node to start to move to front (nth node + 1 is the one that gets moved)
        nth_node = length - rotation

        # find the nth node
        curr = head
        prev = None
        while nth_node > 0:
            prev = curr
            curr = curr.next
            nth_node -= 1
        
        # if curr is None, it means we only have 1 node
        if curr is None:
            return head
        # new tail
        prev.next = None
        # attach the end to the front, curr becomes the new head
        tail.next = head

        return curr
        


