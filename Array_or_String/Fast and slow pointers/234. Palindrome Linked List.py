# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# O(n) and O(n) solution
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        if not head:
            return False
        
        while head is not None:
            nodes.append(head.val)
            head = head.next
        
        return nodes == nodes[::-1]

        