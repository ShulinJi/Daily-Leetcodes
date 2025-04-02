# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:


# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
#         Let's define a as the length of the path from the start of the list to the entrance of the cycle.
# Let's define b as the length of the path from the cycle's entrance to the meeting point of the hare and the tortoise inside the cycle.
# Let's define c as the total length of the cycle.
# The hare could lap the cycle multiple times before it meets the tortoise, especially if the cycle's size is relatively small compared to the distance from the start to the cycle's entrance, or if the cycle's size is big, and the hare enters it significantly before the tortoise does.

# When the tortoise and the hare meet inside the cycle, the tortoise has walked a+b distance.

# On the other hand, the hare, which moves twice as fast, has covered this distance and maybe a few more laps around the cycle. So, the total distance the hare ran is a+b plus k⋅c, where k is the number of times it lapped the cycle. Because the hare moves twice as fast, this total distance is also equal to 2(a+b).

# If we set these two equal: a+b+k⋅c=2(a+b), we obtain k⋅c=a+b.

# This tells us that the number of times the hare laps the cycle times the length of the cycle equals the distance from the head of the list to the meeting point.

# The question now is where is the entrance to the cycle?

# Here is where the second part of the algorithm comes in: after finding a meeting point inside the cycle, you'll leave the tortoise there and move the hare back to the starting point of the park (or the head of the linked list). Then, have both the hare and the tortoise move at the same pace (one step at a time). When they meet again, that meeting point is the entrance to the cycle.

# You may ask, "Why is this the entrance to the cycle?" Well, let's consider the distances each has traveled.

# The first time that the hare and the tortoise meet within the cycle, we have established that:

# The tortoise has travelled a+b distance.
# The hare has traveled a+b+k⋅c distance, where k represents how many times the hare has lapped the cycle.
# Because the hare moves at twice the speed, a+b+k⋅c=2(a+b), rearrange for k⋅c=a+b.
# If we move the hare back to the start of the straight path and make it move at the same speed as the tortoise, here's what happens:

# The hare has a distance to travel to reach the entrance of the cycle. We can rearrange the above equation to say that the hare will reach the entrance of the cycle in a=k⋅c−b steps.
# Currently, the tortoise is b away from the entrance of the cycle. In k⋅c−b steps, where will the tortoise be? Relative to the entrance of the cycle, the tortoise will be at (k⋅c−b)+b=k⋅c. Because k is an integer, c is defined as the length of the cycle, and this distance is relative to the entrance of the cycle, the tortoise will be at the entrance!
# Because the tortoise and hare are now moving at the same speed, after k⋅c−b steps, they will meet again at the entrance of the cycle. This must be the first time they meet again because the hare has just entered the cycle again for the first time. Therefore, to find the entrance of the cycle, we don't actually need the values of a,b,c,k. We can just return the node at which they meet again.

# Algorithm
# Initialize the tortoise and hare pointers to the head of the linked list.
# Move the tortoise one step and the hare two steps at a time until they meet or either hare or hare.next becomes null.
# If the hare or hare.next pointer is null, it means the hare came to the dead end and we return null as there is no cycle.
# Reset the hare pointer to the head of the linked list.
# Move both pointers one step at a time until they meet again. The meeting point is the node where the cycle begins.
# Return the meeting point node.


 # O(n) time and O(1) space, but complicated proof of Floyd's Tortoise and Hare Algorithm
        if head is None:
            return None
        
        # find first time it either meets or no cycle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # we don't have a cycle
        if not fast or not fast.next:
            return None
        
        # now we know we have a cycle 
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow



        # it works, but take O(n) time and O(n) space complexity
        nodes_seen = set()

        node = head
        while node is not None:
            if node in nodes_seen:
                return node
            else:
                nodes_seen.add(node)
                node = node.next

        # If we reach a null node, there is no cycle
        return None