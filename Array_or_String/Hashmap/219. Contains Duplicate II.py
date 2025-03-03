# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # we create a hashmap to store num: index pairs
        hashmap = {}
        for x in range(len(nums)):
            # if we haven't seen the number before
            if nums[x] not in hashmap:
                hashmap[nums[x]] = x
            else:
                # we have seen the number before, we check if it satisfies the condition index(current) - index(before) <= k
                # if satify, then return True
                if x - hashmap[nums[x]] <= k:
                    return True
                # if not satisfied, we update the most recent index of this number for the use of checking of next time
                else:
                    hashmap[nums[x]] = x
        return False