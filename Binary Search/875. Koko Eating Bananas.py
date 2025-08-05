# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

# Binary search solution to find the minimum eating speed k.
# O(n * log(max(piles))) time complexity, where n is the number of piles and max(piles) is the maximum number of bananas in a pile.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min_step = 1
        # max_step = max(piles) to ensure we can eat all bananas in the worst case, there is no point in eating faster than the largest pile.
        min_step = 1
        max_step = max(piles)

        # Binary search to find the minimum eating speed k.
        # use < intead of <=  pattern ensures the loop ends when min_step == max_step, which is the smallest valid k
        while min_step < max_step:
            mid = min_step + (max_step - min_step) // 2
            total_hour = 0
            for bananas in piles:
                total_hour += math.ceil(bananas / mid)
            # If the total hours taken is less than or equal to h, we can try to eat slower (increase k). (try to find minimum k, optimal solution)
            if total_hour <= h:
                # mid is valid, so we can try to find a smaller k, instread of mid + 1
                max_step = mid
            else:
                # mid is too slow(not valid, not satisfy the if condition), we need to increase k, we skip mid and search in the right half, use mid + 1
                min_step = mid + 1

        return max_step

# Brute force solution by adding 1 to the eating rate until the total hours taken is less than or equal to h.
# O(n * h) time complexity, where n is the number of piles.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        eating_rate = 1

        while True:
            total_hour = 0
            for bananas in piles:
                total_hour += math.ceil(bananas / eating_rate)
            
            if total_hour <= h:
                return eating_rate
            else:
                eating_rate += 1