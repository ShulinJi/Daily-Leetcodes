# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(m + n) bc we make 2 counters, O(min(n, m)) bc we choose the smaller one in size
        # we choose the one that is smaller in size to optimize the space complexity
        if len(nums1) > len(nums2):
            # we switch the order bc we always make nums1 to counters, if we switch nums2 will be counter
            return intersect(num2, nums1)

        counter_nums1 = Counter(nums1)
        ans = []

        # we traverse nums2, and whenver we see a common value, we add it to the answer
        for num in nums2:
            if num in counter_nums1:
                ans.append(num)
                counter_nums1[num] -= 1
                if counter_nums1[num] == 0:
                    del counter_nums1[num]
        
        return ans

### Answers for the follow up questions: ###


# followups 1: What if the given array is already sorted? How would you optimize your algorithm?
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0, j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return ans

# followup 2: What if nums1's size is small compared to nums2's size? Which algorithm is better?
#  Then we simply use the hashmap approach since we use it for the smaller one, better space complexity


# followup 3: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# If nums1 fits into the memory, we can use Approach 1 to collect counts for nums1 into a hash map. Then, we can sequentially load and process nums2.

# If neither of the arrays fit into the memory, we can apply some partial processing strategies:
# Split the numeric range into subranges that fits into the memory. Modify Approach 1 to collect counts only within a given subrange, and call the method multiple times (for each subrange).

# Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.