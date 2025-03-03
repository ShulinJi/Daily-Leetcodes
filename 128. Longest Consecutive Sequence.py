class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) runtime, O(n) space

        # Convert the list to a set(), don't need duplicate
        longest_streak = 0
        num_set = set(nums)

        # wwhenever (num - 1) not in sum_set, it is a beginning of a streak!
        for num in num_set:
            if num - 1 not in num_set:
                # beginning of a streak, starting at 1
                current_num = num
                current_streak = 1

                # the while loop can be run at most n times
                # makes it the same as other linear operations in runtime 
                # (ie. current_streak assigned n times because of for loops)
                # so the total runtime is around O(n + n)

                # and we make a copy of num b/c we are in a loop
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak




        # O(nlogn) runtime, Space Complexity: O(logn) or O(n)
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)



        # Runtime O(N^3), Space complexity : O(1)
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
  
