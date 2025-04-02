# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iteratively 
        prev = None
        curr = head
        while curr:
            # first record next node since we are going to break the link of current node
            next_node = curr.next
            # break the link and attach it to the previous node
            curr.next = prev
            # update the prev to curr and curr to next node
            prev = curr
            curr = next_node
        
        return prev



# Intuition

# The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed, now how do we reverse the front part? Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

# Assume from node nk+1 to nm had been reversed and we are at node nk.
# n1 → … → nk-1 → nk → nk+1 ← … ← nm

# We want nk+1’s next node to point to nk.
# So,
# nk.next.next = nk;

# Be very careful that n1's next must point to Ø. If you forget about this, your linked list will have a cycle in it. This bug could be caught if you test your code with a linked list of size 2.
        # Recursive method
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p