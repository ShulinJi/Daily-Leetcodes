# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # maintain an unchanging reference to node ahead of the return node.
        # maintain a stable head to the return list since prev will be traversing through to the end of the list
        prehead = ListNode(-2)
        prev = prehead
        # We basically add one node that is smaller from both links one by time and append the rest at the end.
        # keep the loop if there's still any nodes in both lists (there's still nodes to sort)
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # Append the rest of the list to the end
        prev.next = list1 if list1 is not None else list2

        return prehead.next
