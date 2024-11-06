class Solution:
    def productExceptSelf(self, ç: List[int]) -> List[int]:
        totalProductNoZero = 0 # product without considering 0
        productWithZero = 1 # product with zero
        countZero = 0 # count of how many zeros
        for x in ç:
            if x != 0:
                if totalProductNoZero == 0:
                    totalProductNoZero = x
                else:
                    totalProductNoZero = totalProductNoZero * x
            else:
                productWithZero = productWithZero * x
                countZero += 1


        returnList = []
        for x in ç:
            if x != 0:
                # if x is not 0, cannot divide by 0, then if there are more than 1 zero, simply append 0
                # else we just append the division of totalProduct and itself
                if countZero > 0:
                    returnList.append(0)
                else:
                    returnList.append(int(totalProductNoZero / x))
            else:
                # if x is 0, then if it is the only zero, we append the product of the rest
                # else if there's other zeros, we just append 0
                if countZero - 1 < 1:
                    returnList.append(totalProductNoZero)
                else:
                    returnList.append(0)

        return returnList


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# O(1) space O(N) time
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
