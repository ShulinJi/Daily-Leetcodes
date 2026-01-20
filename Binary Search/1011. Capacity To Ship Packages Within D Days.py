# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# Example 2:

# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# Example 3:

# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
 

# Constraints:

# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500

# SECOND ATTEMPT
# O(nlogn) because O(n) to compute days and logn for binary search
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min should be at least be able to ship all the weight
        # max should be able to ship all weights at once
        left = max(weights)
        right = sum(weights)

        # we try different capacity and calcualte the needed days for current capacity
        # if current_capacity needs less days, then we can try a bigger capacity, vice versa
        while left < right:
            mid = (left + right) // 2
            curr_days = 0
            curr_weights = 0
            for i in range(len(weights)):
                if curr_weights + weights[i] > mid:
                    curr_days += 1
                    curr_weights = weights[i]
                else:
                    curr_weights += weights[i]

            if curr_weights != 0:
                curr_days += 1

            print(mid)
            print(curr_days)
            # if we need less than days, we can still try a smaller capacity
            if curr_days <= days:
                right = mid
            else:
                # we try larger capacity
                left = mid + 1
        
        return left


# O(n log(sum(weights))) time complexity solution using binary search. O(1) space complexity.
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # left is the maximum weight of a single package (we need to ensure that the ship can carry all possible packages), right is the sum of all weights
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            # count how many days it takes to ship with the current mid capacity
            count = 0
            temp_sum = 0
            for i in range(len(weights)):
                if temp_sum + weights[i] > mid:
                    count += 1
                    temp_sum = weights[i]
                else:
                    temp_sum += weights[i]
            if temp_sum != 0:
                count += 1

            # if the count of days exceeds the limit, we need to increase the capacity
            if count > days:
                left = mid + 1
            # if the count of days is within the limit, we can try to reduce the capacity
            else:
                right = mid
        
        return right
