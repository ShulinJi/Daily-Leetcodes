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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) and O(1) solution

        # reverse the linked list
        def reverse_link(self, head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # find the end of the first half of the linked list
        def find_the_first_half(self, head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        
        # find first half 
        first_half = find_the_first_half(self, head)
        # reverse the second half
        second_half = reverse_link(self, first_half.next)
        
        # compare the first half and second half
        # if odd numbers [1, 2, 3, 4, 5] first half would be: [1, 2, 3], second half would be: [4, 5]
        result = True
        begin = head
        second_begin = second_half
        while result and second_begin is not None:
            if begin.val != second_begin.val:
                result = False
            begin = begin.next
            second_begin = second_begin.next
        return result