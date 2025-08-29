# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 

# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
we could use a counting array of size 101 to store the frequency of each number. This would allow us to find the median in O(100) = O(1) time.
this serves as a counting sort method by counting total numbers of elements and find the median position
class MedianFinder:
    def __init__(self):
        self.count = [0] * 101   # frequency array for [0..100]
        self.total = 0           # number of elements seen

    def addNum(self, num: int) -> None:
        self.count[num] += 1
        self.total += 1

    def findMedian(self) -> float:
        mid1, mid2 = (self.total + 1) // 2, (self.total + 2) // 2
        cumulative = 0
        median1 = median2 = None

        for i in range(101):
            cumulative += self.count[i]
            if median1 is None and cumulative >= mid1:
                median1 = i
            if median2 is None and cumulative >= mid2:
                median2 = i
                break

        return (median1 + median2) / 2.0

# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


# use two heaps, max heap for the smaller part, min heap for the bigger part
# time complexity: O(logN) for addNum, O(1) for findMedian
class MedianFinder:
    def __init__(self):
        # python default mean heap
        self.max_heap = []
        self.min_heap = []
        # max heap, max on top heap[0], max is used for smaller part
        heapq.heapify(self.max_heap)
        # min heap is sued for the bigger part
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        # always add to max heap first
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -self.max_heap[0])
        heapq.heappop(self.max_heap)

        # balance the size
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) * 0.5

# basic solution, not optimal
# O(nlogn)
class MedianFinder:
    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        if len(self.stream) < 1:
            return 0
        self.stream.sort()
        median = len(self.stream) // 2
        if len(self.stream) % 2 == 0:
            return (self.stream[median] + self.stream[median - 1]) / 2
        else:
            return self.stream[median]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()