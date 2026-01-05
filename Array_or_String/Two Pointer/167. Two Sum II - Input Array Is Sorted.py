# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Binary search is not suitable for this problem since it will be O(nlogn) because we are fnding 2 numebrs not just 1, we need a loop outside of the binary search
# SECOND ATTEMPT
# O(n) and O(1) complexity
# avoid integer overflow
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            # if to prevent integer overflow: use the cast long to prevent it
            # ex. long sum = (numbers[left] + numbers[right])
            # but python won't have the overflow problem, if to be sure just int(numbers[left] + numbers[right])
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(N) runtime, O(1) space
        # Two Pointer

        i = 0
        j = len(numbers) - 1
        while i < j:
            # We could cast the sum to be long to avoid overflow!!!
            if numbers[i] + numbers[j] == target:
                # return the index of i and j added by 1
                return [i + 1, j + 1]
            
            # if the sum is bigger than the target
            if numbers[i] + numbers[j] > target:
                j -= 1
            
            # if the sum is smaller than the target
            if numbers[i] + numbers[j] < target:
                i += 1
