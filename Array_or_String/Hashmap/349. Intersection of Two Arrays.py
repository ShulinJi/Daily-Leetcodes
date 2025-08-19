# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# O(n) time | O(n) space but better space complexity than using a set since we are using only one hashmap to track counts
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        ans = []
        # Count occurrences of each number in nums1 with only 1 occurrence since we want unique elements
        for x in nums1:
            dict1[x] = 1

        # Check if numbers in nums2 are in dict1 and have a count of 1
        for x in nums2:
            if x in dict1 and dict1[x] == 1:
                # If found, append to result and set count to 0 to avoid duplicates
                ans.append(x)
                dict1[x] = 0
        
        return ans

# O(n) time | O(n) space
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        intersect = list()
        for num in set2:
            if num in set1:
                intersect.append(num)
        
        return intersect