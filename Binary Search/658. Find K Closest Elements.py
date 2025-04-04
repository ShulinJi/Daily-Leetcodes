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

