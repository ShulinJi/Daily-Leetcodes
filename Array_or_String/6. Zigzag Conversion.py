# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

# SECOND ATTEMPT
# O(n) time | O(1) space because the rows array will at most be size of numRows which is capped at 1000
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if we only allow one row, then we don't need the zigzag conversion
        if numRows == 1:
            return s
        # we set up this many number of rows of strings
        rows = [''] * numRows
        # pointer of current row
        current_row = 0
        # direction control, -1 means going down, 1 means going up by 1 row to follow the zigzag pattern
        direction = -1

        # then we traverse through the string
        for char in s:
            # we add the character to the current row
            rows[current_row] += char

            # if we reach either top of bottom, we need to change direction
            if current_row == numRows - 1 or current_row == 0:
                direction *= -1
            
            # move to the next row according to the direction
            current_row += direction
        
        # list of strings, then we just join them together and return
        return "".join(rows)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of empty strings for each row
        # number of rows of string
        # zigzag shape does not matter, just follow the up to down pattern and join all the rows
        rows = [''] * numRows
        current_row = 0
        direction = -1  # To control the movement (up or down)

        # Iterate through each character in the input string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char
            
            # If we are at the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            
            # Move to the next row (up or down depending on direction)
            current_row += direction

        # Join all the rows and return the final string
        return ''.join(rows)
