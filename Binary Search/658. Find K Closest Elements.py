# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

# clever way to compare arr[mid] and arr[mid + k], if arr[mid] is closer to x than arr[mid + k], then we know the answer is on the left side, 
# otherwise, the answer is on the right side, and we can shrink the window by moving left or right pointer
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
# O(log(N)+k) and O(1)
# SECOND ATTEMPT
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        
        # we first find the index that is closest to the number x
        # use the template number 3
        index = None
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                index = mid
                break
            elif arr[mid] < x:
                left = mid
            else:
                right = mid
        
        # need to check left and right since this template left 2 numbers to check
        if index is None:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                index = left
            else:
                index = right
        # after find the index that is closest to the x

        # we need a find the window that is size of k that are closest to x
        # left bound and right bound are not included in the window
        left_bound, right_bound = index - 1, index
        # keep the window size under k + 1, because [1,2,3,4,5], if we want 3,4 our left and right would be 2, 5 and 5-2 = 3, and the size of window is 2, so we need to keep the bound diff under k + 1
        while right_bound - left_bound <= k:
            # if either left or right is out of bound, only move one side
            if left_bound == -1:
                right_bound += 1
            elif right_bound == len(arr):
                left_bound -= 1
            # compare the absolute diff to find the closer one
            elif abs(arr[left_bound] - x) <= abs(arr[right_bound] - x):
                left_bound -= 1
            else:
                right_bound += 1
        
        # use + 1 because rightbound - left_bound == 7
        return arr[left_bound + 1:right_bound]
        
        


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Time complexity: O(log(N)+k).
        # Space complexity: O(1)
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid
        
        # low will be the exact index if it exists 
        # or will be the index that is the first number bigger than x
        

        # not contain the edge of the sliding window
        left, right = low - 1, low
        while right - left - 1 < k:
            # if out of bound, only move right side then
            if left == -1:
                right += 1
                continue
            
            # if right side is out of bound, only move left bound
            if right == len(arr):
                left -= 1
                continue
            
            # compare the abs distance of left and right to x
            if abs(arr[left] - x) > abs(arr[right] - x):
                right += 1
            else:
                left -= 1
            
        # not contain both edge, left + 1 and default right (right is not included)
        return arr[left + 1:right]

