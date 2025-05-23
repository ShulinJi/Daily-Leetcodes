# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

# Example 1:

# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

# Example 2:

# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

# Output: [null, 7, 7, 7, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8
 

# Constraints:

# 0 <= nums.length <= 104
# 1 <= k <= nums.length + 1
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add to our min_heap if we haven't processed k elements yet
        # or if val is greater than the top element (the k-th largest)

        # a min-heap that only keeps the top k elements that if the new value is bigger than the first element (k-th largest since smallest on top)
        # we add it and pop the top (k-th element) automatically replaced with k - 1 th element since we added a new bigger element
        if len(self.min_heap) < self.k or val > self.min_heap[0]:
            heapq.heappush(self.min_heap, val)
            # we added a new larger number, now heap[0] is the k+1 th largest, need to pop to maintain
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]



class KthLargest:

    # most basic solution with array 
    # Time Complexity: O(N^2 +N⋅M) since we have n "add" operations
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        # Add val to correct position
        self.stream.insert(index, val)
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            if mid_element == val:
                return mid
            # Go to left half
            elif mid_element > val:
                right = mid - 1
            # Go to right half
            else:
                left = mid + 1
        return left