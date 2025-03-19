# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

# if API returns false, means all previous versions are all good
# if API returns true, it means there is at least one including itself is wrong version, so we are safe to trucate the check for ones after this check

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # version starts at 1
        lo, hi = 1, n

        # cannot use <= since if they equal, mean they have found the earliest version and converged
        # will cause infinite loop b/c hi = lo, mid = (lo + hi) = hi, nothing changed
        while lo < hi:
            mid = (lo + hi) // 2
            # id current version is bad, it means the earliest is still could be before us
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo

