# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque used to track the max in the current window (dq[0] is max), it is decreasing
        dq = deque()
        res = []

        for i in range(k):
            # if current number is larger than the last of the queue, it means we fonud a number that is larger in index and larger in magnitude
            # then it means that the previous smaller numbers are not in the considerations for the potential max number, we could simply delete it.
            while dq and nums[i] >= nums[dq[-1]]:
                # delete the smaller and older number
                dq.pop()
            dq.append(i)
        # after initial setup of the window, append first answer
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            # starting at new window
            # if current max is out of the window, since i represents the right boundary of the window(current number), i -k + 1represents the left bound
            # then if dq[0] <= i - k, it means it is out of window and should not be considered
            if dq and dq[0] <= i - k:
                dq.popleft()
            # then we do the same stuff for the rest
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            # after everything, we append the current number, and add the max for current window
            res.append(nums[dq[0]])
        
        return res