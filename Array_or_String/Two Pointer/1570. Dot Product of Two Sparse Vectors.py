# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

 

# Example 1:

# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# Example 2:

# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# Example 3:

# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

 

# Example 1:

# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# Example 2:

# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# Example 3:

# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100

# second attempt with follow up answered !
# 3.  2 pointer solution, better
class SparseVector:
    def __init__(self, nums: List[int]):
        # append all the index value pair with non zeros
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append((i, n))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p = 0
        q = 0
        ans = 0

        # follow up: if one of the vector is sparse and the other is not?
        # we will compare the length of each pairs and 
        # loop through the pairs that is shorter in length and do a binary search 
        # in the long pairs to find the index of selected index in shorter one
        
        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                ans += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        
        return ans

# best solution
# O(n) time | O(m + k) space where m and k are the number of non-zero elements in nums1 and nums2 respectively
class SparseVector:
    def __init__(self, nums: List[int]):
        # store only the non-zero elements as (index, value) pairs in order of index
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        # since we stored the pairs in order of index, we can use two pointers to find the common indices
        while p < len(self.pairs) and q < len(vec.pairs):
            # if the indices are the same, we multiply the values and add to the result, this is how dot product is defined
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            # move the pointer with the smaller index forward
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        
        return result


#  1. Brute Force: store as array, self.nums = nums, then just add up by looping all the items in both array

# 2. HashMap solution, O(L + K) for both
However, FB does not accept this solution, because if the vector is too large and spare, the computation time of 
 the hash function would take up bulk of computation time that even the brute force would be better.!!!!!!!
class SparseVector:
    def __init__(self, nums: List[int]):
        # use dictionary to store the non-zero indices and its value
        self.dictionary = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.dictionary[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, n in self.dictionary.items():
            if i in vec.dictionary:
                ans += vec.dictionary[i] * self.dictionary[i]
        
        return ans
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
