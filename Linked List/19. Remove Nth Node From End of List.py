# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find the total nnumber of nodes in linked list
        number_of_nodes = 0
        temp_head = head
        while temp_head is not None:
            number_of_nodes += 1
            temp_head = temp_head.next
        
        # find the nodes that needs to be removed
        node_to_remove = number_of_nodes - n
        # record prev(nodes before the removed one) and curr(nodes to be removed)
        curr = head
        prev = None
        while node_to_remove > 0:
            prev = curr
            curr = curr.next
            node_to_remove -= 1
        
        # skip the curr node to delete it. If it is the head (prev == None) then simply skip the head
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        
        return head