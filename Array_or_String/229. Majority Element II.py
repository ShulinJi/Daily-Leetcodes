# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?


# O(n) time and O(1) space using Boyer-Moore Voting Algorithm, same as 169. Majority Element
# This problem is similar to 169. Majority Element, where we find the element that appears more than n/2 times. for finding elements that appear
#  more than n/3 times, we can at most have two such elements in the array. for more than n/2 times, we can have at most one such element.
# Except that we need to find all elements that appear more than n/3 times, so we need to keep track of two candidates and their counts.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            # If n is equal to candidate1 or candidate2, we increase the count of that candidate
            if candidate1 == n:
                count1 += 1
            # If n is equal to candidate2, we increase the count of that candidate
            elif candidate2 == n:
                count2 += 1
            # If count1 is 0, which means we can assign a new candidate
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            # If count2 is 0, which means we can assign a new candidate
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            # If n is not equal to either candidate, we decrease both counts
            else:
                count1 -= 1
                count2 -= 1
        
        # After the first pass, we have two candidates. We need to verify if they appear more than n/3 times
        ans = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                ans.append(candidate)
        
        return ans

# O(n) time and O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = {}
        ans = []
        # Count the occurrences of each number in the array
        for x in nums:
            hashmap[x] = hashmap.get(x, 0) + 1
        
        # Check if the count of each number is greater than n/3
        for x in hashmap:
            if hashmap[x] > (n // 3):
                ans.append(x)
        
        return ans