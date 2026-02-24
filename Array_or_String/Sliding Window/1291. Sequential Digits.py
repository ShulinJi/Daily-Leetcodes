# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        new_string = "123456789"
        ans = []

        # first loop to try all valid length of strings from low to high so that we ensure that final answer is sorted from small to big
        for length in range(len(str(low)), len(str(high)) + 1):
            # then here we try all possible start points for each length in "123456789"
            # and current combination of start + length should stay under 10 bc len(new_string) = 9
            # then len(new_string) = 9, then we use 9 + 1 = 10 then - length to get all valid start point 
            for start in range(len(new_string) - length + 1):
                curr_int = int(new_string[start: start + length])
                if low <= curr_int <= high:
                    ans.append(curr_int)

        return ans