# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nlogk time and O(N + k)
        num_count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

# same as above but implemented the nlargest in hand
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogk) time and O(N + k)
        num_count = Counter(nums)

        # return heapq.nlargest(k, count.keys(), key=count.get)\
        # same as above
        result = []
        for key, freq in num_count.items():
            if len(result) < k:
                heapq.heappush(result, (freq, key))
            else:
                # if it is bigger than the Kth element since it is min-heap default for python
                if freq > result[0][0]:
                    heapq.heappop(result)
                    heapq.heappush(result, (freq, key))
        
        return [char for _, char in result]
