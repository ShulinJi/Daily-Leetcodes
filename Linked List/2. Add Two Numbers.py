# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  new linked list for summing result
        # initialize the head, discard this when returning
        sum_list = ListNode(0)
        # record the head for accessing
        head = sum_list
        leading_one = False

        # until both linked lists are exhausted, we keep adding
        while l1 or l2:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            new_val = l1_val + l2_val

            # check if the result is over 10 and if there is leading one for next result
            if leading_one:
                new_val += 1
            if new_val >= 10:
                new_val = new_val % 10
                leading_one = True
            else:
                leading_one = False
            
            # traverse the three linked lists to next one
            sum_list.next = ListNode(new_val)
            sum_list = sum_list.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # if we have a leading one after the last add up, we need to attach the leading one at the end
        if leading_one:
            tmp = head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = ListNode(1)
        return head.next