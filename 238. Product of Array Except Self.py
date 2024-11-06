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
