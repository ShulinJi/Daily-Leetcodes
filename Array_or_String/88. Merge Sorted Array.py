# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ### Approach 2, Time Complexity O(m + n), Space Complexity O(1)
        # This time, we start our pointer at the end of the array, we don't need extra array since we just filling out nums1
        p1 = m - 1
        p2 = n - 1

        # Since nums1 has length of n+m, so there is no way for overtaking happens between p1 and p
        for p in range(n + m - 1, -1, -1):
            # if we run out of p2, then the merge already completes since the rest of nums1 is just staying there
            if p2 < 0:
                break
            # if nums1 is bigger than nums2 and nums1 is inbound
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        


        ### Approach 1

        # Makes an copy of nums1 since nums1 needs to return in-place
        nums1_copy = nums1[:m]
        
        # Two pointers each points at the beginning of each nums array 
        p1 = 0
        p2 = 0

        # Time complexity O(m + n), Space Complexity O(m) since we made copy of nums1
        # We try to fill out nums1 by choosing the bigger one from either nums1_copy or nums2
        for p in range(n + m):
            # we choose from nums1_copy if p2 is out of bound, or p1 is inbound and is the smaller one
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            # otherwise, we choose from nums2
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        
