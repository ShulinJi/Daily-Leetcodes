class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numOccurrence = {}

        for x in arr:
            if x in numOccurrence:
                numOccurrence[x] += 1
            else:
                numOccurrence[x] = 1
        
        set_of_ocurrence = set(numOccurrence.values())

        # return len(set_of_ocurrence) == len(numOccurrence.values())
        for value in numOccurrence.values():
            if value in set_of_ocurrence:
                return False
            else:
                set_of_ocurrence.add(value)
        
        return True



# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
